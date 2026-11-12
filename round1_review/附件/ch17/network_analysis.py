#!/usr/bin/env python3
"""New teaching implementation. NOT_RUN at delivery; no external dependencies.

python network_analysis.py --data . --out run_new
Python 3.10+. Output must be a new directory. Inputs are never modified.
The calculations describe an explicitly defined synthetic graph, not historical power.
"""
import argparse
import csv
import hashlib
import html
import itertools
import json
import platform
import sys
from collections import defaultdict, deque
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def unique(rows, key):
    result = {}
    for row in rows:
        if not row[key] or row[key] in result:
            raise ValueError(f"empty or duplicate {key}: {row[key]!r}")
        result[row[key]] = row
    return result


def jwrite(path, value):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def cwrite(path, fields, rows):
    with path.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def qtext(value):
    return None if value is None else str(value)


def adjacency(nodes, edges, directed=False):
    graph = {node: set() for node in nodes}
    for a,b in edges:
        if a not in graph or b not in graph or a == b:
            raise ValueError("graph contains absent endpoint or self-loop")
        graph[a].add(b)
        if not directed:
            graph[b].add(a)
    return graph


def reachable(graph, start):
    seen = {start}
    todo = [start]
    for node in todo:
        for other in sorted(graph[node]):
            if other not in seen:
                seen.add(other)
                todo.append(other)
    return seen


def components(graph):
    remaining = set(graph)
    result = []
    while remaining:
        group = reachable(graph, min(remaining))
        result.append(sorted(group))
        remaining -= group
    return sorted(result, key=lambda group: (-len(group), group))


def strongly_connected(graph):
    reverse = {node: set() for node in graph}
    for a, targets in graph.items():
        for b in targets:
            reverse[b].add(a)
    remaining, result = set(graph), []
    while remaining:
        node = min(remaining)
        group = reachable(graph, node) & reachable(reverse, node)
        result.append(sorted(group))
        remaining -= group
    return sorted(result, key=lambda group: (-len(group), group))


def density(n, m, directed=False):
    if n < 2:
        return None  # explicitly not applicable, not a fake zero
    return Fraction(m, n * (n-1) if directed else n*(n-1)//2)


def graph_metrics(nodes, edges):
    edges = {tuple(sorted(edge)) for edge in edges}
    graph = adjacency(nodes, edges)
    n, m = len(graph), len(edges)
    groups = components(graph)
    raw = {node: Fraction(0) for node in graph}
    distances = {}
    # Unweighted Brandes accumulation, exact path fractions, no endpoints.
    for source in sorted(graph):
        stack = []
        predecessors = {node: [] for node in graph}
        sigma = {node: 0 for node in graph}
        distance = {source: 0}
        sigma[source] = 1
        queue = deque([source])
        while queue:
            v = queue.popleft()
            stack.append(v)
            for w in sorted(graph[v]):
                if w not in distance:
                    distance[w] = distance[v] + 1
                    queue.append(w)
                if distance[w] == distance[v] + 1:
                    sigma[w] += sigma[v]
                    predecessors[w].append(v)
        distances[source] = distance
        dependency = {node: Fraction(0) for node in graph}
        while stack:
            w = stack.pop()
            for v in predecessors[w]:
                dependency[v] += Fraction(sigma[v], sigma[w]) * (1 + dependency[w])
            if w != source:
                raw[w] += dependency[w]
    for node in raw:
        raw[node] /= 2  # undirected paths were counted from both sources
    centralities = []
    for node in sorted(graph):
        r = len(distances[node]) - 1
        total_distance = sum(distances[node].values())
        norm_denominator = (n-1)*(n-2)//2
        normalized = raw[node] / norm_denominator if n > 2 else Fraction(0)
        closeness = Fraction(r, n-1) * Fraction(r, total_distance) if n > 1 and total_distance else Fraction(0)
        dc = Fraction(len(graph[node]), n-1) if n > 1 else Fraction(0)
        centralities.append({"node_id": node, "degree": len(graph[node]), "degree_centrality_fraction": str(dc),
            "degree_centrality_decimal": float(dc), "raw_betweenness_fraction": str(raw[node]),
            "normalized_betweenness_fraction": str(normalized), "normalized_betweenness_decimal": float(normalized),
            "reachable_other_nodes": r, "distance_sum": total_distance,
            "corrected_closeness_fraction": str(closeness), "corrected_closeness_decimal": float(closeness)})
    base_components = len(groups)
    bridges = []
    for edge in sorted(edges):
        if len(components(adjacency(nodes, edges - {edge}))) > base_components:
            bridges.append(list(edge))
    articulations = []
    for node in sorted(nodes):
        reduced = set(nodes) - {node}
        kept = {edge for edge in edges if node not in edge}
        if len(components(adjacency(reduced, kept))) > base_components:
            articulations.append(node)
    d = density(n, m)
    summary = {"model": "simple_undirected_unweighted_existence", "N": n, "M": m,
        "possible_pairs": n*(n-1)//2, "density_fraction": qtext(d), "density_decimal": float(d) if d is not None else None,
        "component_sizes": [len(x) for x in groups], "components": groups,
        "isolates": [node for node in sorted(graph) if not graph[node]],
        "largest_component_share": str(Fraction(len(groups[0]), n)) if n else None,
        "degree_sum": sum(len(x) for x in graph.values()), "degree_sum_reference_2M": 2*m}
    return {"summary": summary, "centralities": centralities, "bridges": bridges, "articulation_points": articulations}


def partitions(items):
    """Each unordered set partition exactly once; canonical restricted growth."""
    blocks = []
    def visit(index):
        if index == len(items):
            yield tuple(tuple(block) for block in blocks)
            return
        for block in blocks:
            block.append(items[index])
            yield from visit(index+1)
            block.pop()
        blocks.append([items[index]])
        yield from visit(index+1)
        blocks.pop()
    yield from visit(0)


def modularity(partition, edges, degrees, gamma):
    m = len(edges)
    if not m:
        return None
    score = Fraction(0)
    for block in partition:
        members = set(block)
        internal = sum(a in members and b in members for a,b in edges)
        degree_sum = sum(degrees[node] for node in block)
        score += Fraction(internal, m) - gamma * Fraction(degree_sum, 2*m)**2
    return score


def community_analysis(nodes, edges, gammas, limit):
    graph = adjacency(nodes, edges)
    active = sorted(node for node in graph if graph[node])
    isolates = sorted(set(nodes) - set(active))
    if len(active) > limit:
        raise ValueError(f"exhaustive communities require <= {limit} non-isolated nodes; got {len(active)}. No heuristic fallback is silently substituted.")
    degrees = {node: len(graph[node]) for node in graph}
    best = {gamma: {"score": None, "partitions": []} for gamma in gammas}
    partition_count = 0
    for partition in partitions(active):
        partition_count += 1
        for gamma in gammas:
            value = modularity(partition, edges, degrees, gamma)
            rec = best[gamma]
            if not rec["partitions"] or (value is not None and value > rec["score"]):
                rec["score"], rec["partitions"] = value, [partition]
            elif value == rec["score"]:
                rec["partitions"].append(partition)
    rows, stability = [], []
    for gamma, rec in best.items():
        for index, partition in enumerate(rec["partitions"], 1):
            rows.append({"gamma": str(gamma), "optimum_id": index, "Q_fraction": qtext(rec["score"]),
                "Q_decimal": float(rec["score"]) if rec["score"] is not None else None,
                "active_partition": ";".join(",".join(block) for block in partition),
                "isolates_display_separately": ";".join(isolates), "candidate_partition_count": partition_count,
                "meaning": "objective_optimum_not_historical_group"})
        for a,b in itertools.combinations(active, 2):
            count = sum(any(a in block and b in block for block in partition) for partition in rec["partitions"])
            stability.append({"gamma": str(gamma), "node_a": a, "node_b": b,
                "coassigned_optima": count, "all_optima": len(rec["partitions"]),
                "coassignment_status": "all" if count == len(rec["partitions"]) else ("some" if count else "none"),
                "warning": "not_a_probability_of_historical_affiliation"})
    return rows, stability


def read_inputs(data):
    nodes = unique(read_csv(data / "nodes.csv"), "node_id")
    sources = unique(read_json(data / "sources.json"), "source_id")
    events = read_csv(data / "events.csv")
    unique(events, "event_id")
    spec = read_json(data / "model_spec.json")
    if spec["interval"] != "closed_integer_year":
        raise ValueError("unsupported interval convention")
    if not nodes:
        raise ValueError("empty roster")
    for node in nodes.values():
        sid, loc = node["roster_source"], node["roster_locator"]
        if sid not in sources or loc not in sources[sid]["locations"]:
            raise ValueError("roster source location missing")
        if node["identity_status"] != "confirmed":
            raise ValueError("fixed roster requires explicitly confirmed identities")
    for event in events:
        if event["sender"] not in nodes or event["recipient"] not in nodes or event["sender"] == event["recipient"]:
            raise ValueError("invalid event endpoint")
        sid, loc = event["source_id"], event["locator"]
        if sid not in sources or loc not in sources[sid]["locations"] or not sources[sid]["locations"][loc]:
            raise ValueError("event source excerpt missing")
        event["event_year"] = int(event["event_year"])
        if event["identity_status"] not in {"confirmed", "pending"} or event["event_status"] not in {"accepted", "pending", "rejected"}:
            raise ValueError("unknown evidence status")
    return nodes, sources, events, spec


def derive_events(events, start, end):
    included, audit = [], []
    for event in events:
        reasons = []
        if event["identity_status"] != "confirmed":
            reasons.append("identity_pending")
        if event["event_status"] != "accepted":
            reasons.append("event_" + event["event_status"])
        if not start <= event["event_year"] <= end:
            reasons.append("outside_window")
        audit.append({**event, "included": not reasons, "all_reasons": reasons})
        if not reasons:
            included.append(event)
    return included, audit


def edge_lineage(events):
    grouped = defaultdict(list)
    for event in events:
        grouped[tuple(sorted([event["sender"], event["recipient"]]))].append(event)
    rows = []
    for (a,b), records in sorted(grouped.items()):
        rows.append({"node_a": a, "node_b": b, "event_count": len(records),
            "event_ids": ";".join(row["event_id"] for row in records),
            "source_locations": ";".join(row["source_id"]+"/"+row["locator"] for row in records),
            "status": "derived_from_given_synthetic_events"})
    return rows


def svg_network(nodes, edges):
    # Fixed teaching positions are not geographic or centrality measurements.
    fixed = {"A": (80,80), "B": (80,250), "C": (230,165), "D": (430,165),
             "E": (580,80), "F": (580,250), "G": (750,250), "H": (750,80)}
    coords = {node: fixed.get(node, (80+100*i,340)) for i,node in enumerate(sorted(nodes))}
    body = []
    for a,b in sorted(edges):
        x1,y1 = coords[a]; x2,y2 = coords[b]
        body.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#555" stroke-width="2"/>')
    for node, (x,y) in coords.items():
        body.append(f'<circle cx="{x}" cy="{y}" r="20" fill="white" stroke="#222"/><text x="{x}" y="{y+5}" text-anchor="middle">{html.escape(node)}</text>')
    return '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="420"><style>text{font:16px sans-serif}</style><text x="20" y="25">Reader-generated existence graph. Layout is not geography or power.</text>'+"".join(body)+'</svg>'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path("."))
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--start-year", type=int)
    parser.add_argument("--end-year", type=int)
    parser.add_argument("--gamma", action="append", help="Repeat to set exact rational/decimal resolution values")
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Output exists; choose a new --out directory. No overwrite is supported.")
    data = args.data.resolve()
    nodes, sources, events, spec = read_inputs(data)
    start = args.start_year if args.start_year is not None else spec["start_year"]
    end = args.end_year if args.end_year is not None else spec["end_year"]
    if start > end:
        raise ValueError("reversed research window")
    gammas = list(dict.fromkeys(Fraction(gamma) for gamma in (args.gamma or spec["gamma"])))
    if any(gamma <= 0 for gamma in gammas):
        raise ValueError("this teaching exercise uses positive gamma")
    selected, event_audit = derive_events(events, start, end)
    lineage = edge_lineage(selected)
    node_set = set(nodes)
    edges = {(row["node_a"],row["node_b"]) for row in lineage}
    directed_edges = {(row["sender"],row["recipient"]) for row in selected}
    result = graph_metrics(node_set, edges)
    directed_graph = adjacency(node_set, directed_edges, directed=True)
    directed_density = density(len(nodes),len(directed_edges),directed=True)
    directed_summary = {"model": "simple_directed_existence", "N": len(nodes), "M": len(directed_edges),
        "possible_ordered_pairs": len(nodes)*(len(nodes)-1), "density_fraction": qtext(directed_density),
        "density_decimal": float(directed_density) if directed_density is not None else None,
        "weak_components": components(adjacency(node_set, directed_edges)), "strong_components": strongly_connected(directed_graph)}
    communities, stability = community_analysis(node_set, edges, gammas, spec["exhaustive_nonisolated_limit"])
    sensitivity = {"base": {**result, "change": "none", "hypothetical_edges": []}}
    scenarios = [("omit_CD", node_set, edges-{("C","D")}, "暂不纳入CD，原始事件不删除", []),
        ("assume_BE", node_set, edges|{("B","E")}, "假设新增一条无来源BE；非新发现", [["B","E"]]),
        ("omit_H_boundary", node_set-{"H"}, {e for e in edges if "H" not in e}, "只改变观察边界，不解释为H不存在", []),
        ("omit_D_records", node_set-{"D"}, {e for e in edges if "D" not in e}, "缺D及其全部邻边；不是死亡因果实验", [])]
    for sid in sorted({row["source_id"] for row in selected}):
        subset = [row for row in selected if row["source_id"] != sid]
        subset_edges = {(row["node_a"],row["node_b"]) for row in edge_lineage(subset)}
        scenarios.append(("omit_source_"+sid,node_set,subset_edges,"整组来源缺失情境；保留固定名册",[]))
    for a,b in sorted(edges):
        scenarios.append(("omit_edge_"+a+"_"+b,node_set,edges-{(a,b)},"逐边缺失情境；不是档案缺失概率",[]))
    for name, snodes, sedges, change, hypothetical in scenarios:
        # The built-in scenarios target the fixed A-H exercise; all graph inputs still validate.
        metrics = graph_metrics(snodes, sedges)
        metrics.update({"change": change, "hypothetical_edges": hypothetical,
                        "kept_nodes": sorted(snodes), "kept_edges": [list(e) for e in sorted(sedges)],
                        "omitted_original_edges": [list(e) for e in sorted(edges-sedges)],
                        "evidence_reference": "derived_edges.csv for recorded edges; hypothetical additions have no source"})
        sensitivity[name] = metrics
    comparisons = []
    for a,b in [(1700,1702),(1703,1705)]:
        period_events,_ = derive_events(events,a,b)
        period_edges = {(row["node_a"],row["node_b"]) for row in edge_lineage(period_events)}
        summary = graph_metrics(node_set,period_edges)["summary"]
        comparisons.append({"window_start": a,"window_end": b,"roster": "fixed_X0",
            "N": summary["N"],"M": summary["M"],"density_fraction": summary["density_fraction"],
            "component_sizes": ";".join(map(str,summary["component_sizes"])),
            "event_ids": ";".join(row["event_id"] for row in period_events),
            "warning": "equal_window_length_does_not_establish_equal_source_coverage"})
    # No output directory is created until input and calculations finish.
    args.out.mkdir(parents=False,exist_ok=False)
    jwrite(args.out/"network_summary.json",{"window": [start,end],"interval": "closed_integer_year",
        "undirected": result["summary"],"directed": directed_summary})
    cwrite(args.out/"centralities.csv",list(result["centralities"][0]),result["centralities"])
    cwrite(args.out/"derived_edges.csv",["node_a","node_b","event_count","event_ids","source_locations","status"],lineage)
    cwrite(args.out/"components.csv",["view","component_id","nodes","size"],
        [{"view": view,"component_id": i,"nodes": ";".join(group),"size": len(group)}
         for view,groups in [("undirected",result["summary"]["components"]),("directed_weak",directed_summary["weak_components"]),("directed_strong",directed_summary["strong_components"])]
         for i,group in enumerate(groups,1)])
    jwrite(args.out/"bridges_and_articulations.json",{"bridges": result["bridges"],"articulation_points": result["articulation_points"],"meaning": "structural_removal_not_historical_intervention"})
    cwrite(args.out/"communities.csv",["gamma","optimum_id","Q_fraction","Q_decimal","active_partition","isolates_display_separately","candidate_partition_count","meaning"],communities)
    cwrite(args.out/"co_membership.csv",["gamma","node_a","node_b","coassigned_optima","all_optima","coassignment_status","warning"],stability)
    cwrite(args.out/"comparisons.csv",list(comparisons[0]),comparisons)
    jwrite(args.out/"sensitivity.json",sensitivity)
    jwrite(args.out/"event_audit.json",event_audit)
    with (args.out/"network.svg").open("x",encoding="utf-8") as handle:
        handle.write(svg_network(node_set,edges))
    inputs = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(data.iterdir()) if path.is_file()}
    jwrite(args.out/"provenance.json",{"implementation": "new_teaching_not_original_script_recovery",
        "run_status": "READER_EXECUTED_NOT_HISTORICALLY_VERIFIED","created_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),"argv": sys.argv,"input_sha256": inputs,"model_spec": spec,
        "actual_window": [start,end],"actual_gamma": [str(x) for x in gammas],
        "node_roster_lineage": list(nodes.values()),"event_lineage": [{**event,"excerpt": sources[event["source_id"]]["locations"][event["locator"]]} for event in events],
        "derived_edge_lineage": lineage,"source_catalog": list(sources.values()),
        "transformations": ["validate_all_inputs_before_window_filter","select_events_by_occurrence_year","preserve_fixed_roster_isolates","collapse_events_by_ordered_pair_for_directed_view","collapse_both_directions_for_undirected_existence","exact_unweighted_shortest_path_fractions","enumerate_nonisolated_set_partitions","derived_only_missingness_scenarios"],
        "limitations": ["No original-script recovery","No historical truth or source independence validation","No temporal propagation inference","No LLM or model evaluation","No causal identification from structural removal"]})
    print(f"New teaching results written to {args.out}. Historical interpretation remains unverified.")


if __name__ == "__main__":
    main()
