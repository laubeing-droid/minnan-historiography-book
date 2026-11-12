#!/usr/bin/env python3
"""New teaching implementation, NOT_RUN at delivery. Python 3.10+ standard library.

No identity inference, relation inference, LLM calls, or source-file modification.
Run from this folder: python relations.py --data . --out run_new
The output directory must not exist. Reader execution is a separate activity.
"""
import argparse
import csv
import hashlib
import html
import itertools
import json
import platform
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def unique(rows, key, label):
    result = {}
    for row in rows:
        value = row[key]
        if not value or value in result:
            raise ValueError(f"{label}: empty or duplicate {key}: {value!r}")
        result[value] = row
    return result


def integer_year(value):
    if value == "" or value is None:
        return None
    if not re.fullmatch(r"-?\d+", str(value)):
        raise ValueError(f"not an integer year: {value!r}")
    return int(value)


def boolean(value):
    if value not in {"true", "false"}:
        raise ValueError(f"invalid boolean: {value!r}")
    return value == "true"


def json_write(path, value):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def csv_write(path, fields, rows):
    with path.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def all_positions(text, quote):
    if not quote:
        raise ValueError("empty quote is not a locatable candidate")
    result, start = [], 0
    while True:
        index = text.find(quote, start)
        if index < 0:
            return result
        result.append([index, index + len(quote)])
        start = index + 1  # retain overlapping occurrences too


def locate_candidates(data):
    texts = unique(read_json(data / "candidate_sources.json"), "source_id", "candidate sources")
    candidates = read_json(data / "candidates.json")
    unique(candidates, "candidate_id", "candidates")
    output = []
    for row in candidates:
        if row["source_id"] not in texts:
            raise ValueError("candidate refers to absent source")
        source = texts[row["source_id"]]
        text = source["text"]
        matches = all_positions(text, row["quote"])
        occurrence = row.get("occurrence")
        selected = None
        if occurrence is not None:
            if isinstance(occurrence, bool) or not isinstance(occurrence, int) or not 0 <= occurrence < len(matches):
                raise ValueError(f"invalid occurrence for {row['candidate_id']}")
            selected = matches[occurrence]
        elif len(matches) == 1:
            selected = matches[0]
        mentions = []
        if selected:
            if text[selected[0]:selected[1]] != row["quote"]:
                raise ValueError("span/quote disagreement")
            for name in row["names"]:
                for a, b in all_positions(row["quote"], name):
                    mentions.append({"name_as_written": name, "start": selected[0] + a,
                                     "end": selected[0] + b, "identity": "not_inferred"})
        output.append({**row, "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                       "text_version": source["version"], "page_label": source["page_label"],
                       "text_length_codepoints": len(text), "all_matches": matches,
                       "selected_span": selected,
                       "location_status": "selected" if selected else ("ambiguous" if matches else "not_found"),
                       "mentions": mentions, "negation_hint": any(x in row["quote"] for x in ["未", "不", "无", "非"]),
                       "cross_paragraph_hint": "\n\n" in row["quote"],
                       "explicit_time_markers": re.findall(r"\[T\d+\]", row["quote"]),
                       "historical_relation_status": "not_decided_by_locator"})
    return output


def disambiguation_register(data):
    cards = unique(read_csv(data / "disambiguation_cards.csv"), "mention_id", "cards")
    mapping = unique(read_csv(data / "entity_mapping.csv"), "mention_id", "mapping")
    if set(cards) != set(mapping):
        raise ValueError("mapping must cover each disambiguation card exactly once")
    known = {row["entity_id"] for row in mapping.values() if row["status"] == "confirmed"}
    for row in mapping.values():
        if row["status"] not in {"confirmed", "pending"}:
            raise ValueError("unknown identity mapping status")
        if row["status"] == "confirmed" and (not row["entity_id"] or row["candidate_entities"]):
            raise ValueError("confirmed mapping needs exactly one entity")
        if row["status"] == "pending" and row["entity_id"]:
            raise ValueError("pending mapping may not silently assign an entity")
        if any(x not in known for x in row["candidate_entities"].split(";") if x):
            raise ValueError("candidate identity does not exist")
    decisions = read_csv(data / "pair_decisions.csv")
    for row in decisions:
        a, b = row["left_mention"], row["right_mention"]
        if a not in cards or b not in cards or row["decision"] not in {"same", "different", "pending"}:
            raise ValueError("invalid pair decision")
        ma, mb = mapping[a], mapping[b]
        if ma["status"] == mb["status"] == "confirmed":
            equal = ma["entity_id"] == mb["entity_id"]
            if (row["decision"] == "same" and not equal) or (row["decision"] == "different" and equal):
                raise ValueError("pair judgment conflicts with explicit mapping")
    return {"mapping": list(mapping.values()), "pair_decisions": decisions,
            "note": "Given teaching decisions only. No automatic string matching or transitive merge.",
            "impact_template": read_csv(data / "version_impact_template.csv")}


def validate_relations(data):
    nodes = unique(read_csv(data / "entities.csv"), "entity_id", "entities")
    types = unique(read_csv(data / "relation_types.csv"), "relation_type", "types")
    sources = unique(read_json(data / "sources.json"), "source_id", "sources")
    events = unique(read_csv(data / "events.csv"), "event_id", "events")
    statements = read_csv(data / "assertions.csv")
    unique(statements, "assertion_id", "assertions")
    for node in nodes.values():
        if node["entity_type"] not in {"person", "organization", "event"} or node["identity_status"] not in {"confirmed", "pending"}:
            raise ValueError("invalid entity type or identity status")
    for event in events.values():
        event["start_year"] = integer_year(event["start_year"])
        event["end_year"] = integer_year(event["end_year"])
        if event["event_id"] not in nodes or nodes[event["event_id"]]["entity_type"] != "event":
            raise ValueError("event references absent/non-event node")
        if event["start_year"] is None or event["end_year"] is None or event["start_year"] > event["end_year"]:
            raise ValueError("event needs a complete non-reversed interval")
    grouped = defaultdict(list)
    for row in statements:
        if row["subject"] not in nodes or row["object"] not in nodes or row["relation_type"] not in types:
            raise ValueError("unknown relation endpoint or type")
        typ = types[row["relation_type"]]
        for endpoint, wanted in [("subject", "subject_type"), ("object", "object_type")]:
            if nodes[row[endpoint]]["entity_type"] != typ[wanted]:
                raise ValueError(f"endpoint type mismatch: {row['assertion_id']}")
        if row["subject"] == row["object"] and not boolean(typ["allow_self"]):
            raise ValueError("forbidden self relation; identity revision requires review")
        a, b = integer_year(row["start_year"]), integer_year(row["end_year"])
        if (a is None) != (b is None) or (a is not None and a > b):
            raise ValueError("partly unknown or reversed relation interval")
        if row["temporal_kind"] not in {"continuous_support", "event_year", "evidence_support", "unknown"}:
            raise ValueError("unknown temporal semantics")
        if (a is None) != (row["temporal_kind"] == "unknown"):
            raise ValueError("unknown date must have explicit unknown semantics")
        if row["temporal_kind"] == "event_year" and a != b:
            raise ValueError("event_year is a precise single year, not a possible-date range")
        row["start_year"], row["end_year"] = a, b
        if row["layer"] not in {"statement", "hypothesis"} or row["judgment"] not in {"accepted", "pending", "rejected"}:
            raise ValueError("invalid evidence layer or relation judgment")
        if boolean(typ["event_required"]) and not row["event_id"]:
            raise ValueError("relation type requires explicit event reference")
        if row["event_id"]:
            if row["event_id"] not in events:
                raise ValueError("unknown event reference")
            event = events[row["event_id"]]
            if a is None or (a, b) != (event["start_year"], event["end_year"]):
                raise ValueError("relation occurrence and event interval disagree")
            if row["relation_type"] == "participate" and row["object"] != row["event_id"]:
                raise ValueError("participation endpoint differs from its event")
        if row["source_id"] not in sources or row["locator"] not in sources[row["source_id"]]["locations"]:
            raise ValueError("source or source location is missing")
        if not sources[row["source_id"]]["locations"][row["locator"]]:
            raise ValueError("empty source excerpt")
        row["directed"] = boolean(typ["directed"])
        grouped[row["instance_id"]].append(row)
    compare = ["subject", "relation_type", "object", "start_year", "end_year", "temporal_kind", "event_id", "layer", "judgment", "directed"]
    for instance, rows in grouped.items():
        first = tuple(rows[0][x] for x in compare)
        if any(tuple(row[x] for x in compare) != first for row in rows[1:]):
            raise ValueError(f"conflicting statements for one instance: {instance}")
    return nodes, types, sources, grouped, statements


def svg_relations(rows):
    body = []
    for index, row in enumerate(rows):
        y = 62 + index * 56
        arrow = ' marker-end="url(#arrow)"' if row["directed"] else ""
        text = f"{row['instance_id']}  {row['subject']}  {row['relation_type']}  {row['object']}  [{row['start_year']},{row['end_year']}]  {row['assertion_ids']}"
        body.append(f'<line x1="40" y1="{y}" x2="190" y2="{y}" stroke="#333"{arrow}/><text x="220" y="{y+5}">{html.escape(text)}</text>')
    return '<svg xmlns="http://www.w3.org/2000/svg" width="1050" height="'+str(110+56*len(rows))+'"><defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0 0 L9 3 L0 6" fill="#333"/></marker></defs><style>text{font:15px sans-serif}</style><text x="20" y="25">Reader-generated relation instances; repeated labels do not create new entities.</text>'+"".join(body)+'</svg>'


def svg_candidates(rows):
    body = []
    for index, row in enumerate(rows):
        y = 55 + index * 48
        length = max(row["text_length_codepoints"], 1)
        body.append(f'<text x="15" y="{y}">{row["candidate_id"]} {row["location_status"]}</text><line x1="200" y1="{y-5}" x2="850" y2="{y-5}" stroke="#ccc"/>')
        for a,b in row["all_matches"]:
            body.append(f'<rect x="{200+650*a/length:.2f}" y="{y-13}" width="{max(2,650*(b-a)/length):.2f}" height="14" fill="#345a76"/>')
    return '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="'+str(95+48*len(rows))+'"><style>text{font:14px sans-serif}</style><text x="15" y="22">Codepoint spans; color is not historical confidence.</text>'+"".join(body)+'</svg>'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path("."))
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--start-year", type=int)
    parser.add_argument("--end-year", type=int)
    parser.add_argument("--assume-identity", action="append", default=[])
    parser.add_argument("--defer-instance", action="append", default=[])
    args = parser.parse_args()
    data = args.data.resolve()
    if args.out.exists():
        raise FileExistsError("Output already exists. Choose a new --out directory; no overwrite is supported.")
    rules = read_json(data / "rules.json")
    if rules["interval"] != "closed_integer_year":
        raise ValueError("this implementation requires closed integer-year intervals")
    start = args.start_year if args.start_year is not None else rules["start_year"]
    end = args.end_year if args.end_year is not None else rules["end_year"]
    if start > end:
        raise ValueError("reversed research window")
    nodes, types, sources, grouped, statements = validate_relations(data)
    if set(args.assume_identity) - set(nodes) or set(args.defer_instance) - set(grouped):
        raise ValueError("scenario refers to unknown entity or relation instance")
    located = locate_candidates(data)
    identity_register = disambiguation_register(data)
    included, excluded, audit, lineage = [], [], [], []
    for rid, rows in grouped.items():
        row = rows[0]
        reasons = []
        for endpoint in [row["subject"], row["object"]]:
            if nodes[endpoint]["identity_status"] != "confirmed" and endpoint not in args.assume_identity:
                reasons.append("identity_pending:" + endpoint)
        if row["layer"] != "statement":
            reasons.append("analysis_hypothesis")
        if row["judgment"] != "accepted":
            reasons.append("relation_" + row["judgment"])
        if row["start_year"] is None:
            reasons.append("unknown_date")
        elif row["start_year"] > end or row["end_year"] < start:
            reasons.append("outside_window")
        if rid in args.defer_instance:
            reasons.append("scenario_deferred")
        summary = {**row, "assertion_ids": ";".join(r["assertion_id"] for r in rows),
                   "source_ids": ";".join(sorted({r["source_id"] for r in rows})),
                   "reasons": ";".join(reasons), "scenario_identity_assumptions": ";".join(args.assume_identity)}
        (excluded if reasons else included).append(summary)
        evidence = [{"assertion_id": r["assertion_id"], "source_id": r["source_id"],
                     "locator": r["locator"], "excerpt": sources[r["source_id"]]["locations"][r["locator"]],
                     "independent_group": sources[r["source_id"]]["independent_group"]} for r in rows]
        lineage.append({"instance_id": rid, "included": not reasons, "all_reasons": reasons, "evidence": evidence})
        for assertion in rows:
            audit.append({**assertion, "included": not reasons, "reasons": ";".join(reasons)})
    attendance = [r for r in included if r["relation_type"] == "participate"]
    by_event = defaultdict(lambda: defaultdict(list))
    for row in attendance:
        by_event[row["object"]][row["subject"]].append(row)
    projection = defaultdict(lambda: {"events": [], "instances": set(), "assertions": set(), "sources": set()})
    for event, persons in by_event.items():
        for a,b in itertools.combinations(sorted(persons), 2):
            rec = projection[(a,b)]
            rec["events"].append(event)
            for relation in persons[a] + persons[b]:
                rec["instances"].add(relation["instance_id"])
                rec["assertions"].update(relation["assertion_ids"].split(";"))
                rec["sources"].update(relation["source_ids"].split(";"))
    projected = [{"person_a": a, "person_b": b, "shared_event_count": len(rec["events"]),
                  **{key: ";".join(sorted(value)) for key,value in rec.items()}}
                 for (a,b),rec in sorted(projection.items())]
    # Everything above is validated before any result files are created.
    args.out.mkdir(parents=False, exist_ok=False)
    fields = ["instance_id", "subject", "relation_type", "object", "directed", "start_year", "end_year", "temporal_kind", "event_id", "assertion_ids", "source_ids", "reasons", "scenario_identity_assumptions"]
    csv_write(args.out / "confirmed_instances.csv", fields, included)
    csv_write(args.out / "excluded_instances.csv", fields, excluded)
    csv_write(args.out / "assertion_audit.csv", list(statements[0]) + ["included", "reasons"], audit)
    csv_write(args.out / "nodes.csv", list(next(iter(nodes.values()))), nodes.values())
    csv_write(args.out / "attendance_bipartite.csv", fields, attendance)
    csv_write(args.out / "layer_edges.csv", fields, included)
    csv_write(args.out / "projection.csv", ["person_a", "person_b", "shared_event_count", "events", "instances", "assertions", "sources"], projected)
    json_write(args.out / "lineage.json", lineage)
    json_write(args.out / "candidate_evidence.json", located)
    json_write(args.out / "disambiguation_audit.json", identity_register)
    for name, value in [("relations.svg", svg_relations(included)), ("candidate_evidence.svg", svg_candidates(located))]:
        with (args.out / name).open("x", encoding="utf-8") as handle:
            handle.write(value)
    inputs = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(data.iterdir()) if path.is_file()}
    json_write(args.out / "provenance.json", {"implementation": "new_teaching_not_original_recovery",
        "created_utc": datetime.now(timezone.utc).isoformat(), "python": platform.python_version(),
        "argv": sys.argv, "input_sha256": inputs, "window": [start,end], "interval": "closed_integer_year",
        "identity_assumptions": args.assume_identity, "deferred_instances": args.defer_instance,
        "counts": {"assertions": len(statements), "instances": len(grouped), "included_instances": len(included),
                   "excluded_instances": len(excluded), "included_assertions": sum(len(grouped[r["instance_id"]]) for r in included)},
        "limitations": ["No historical truth validation", "No original-script recovery", "No identity inference", "Projection is shared participation, not acquaintance"],
        "run_status": "READER_EXECUTED_NO_AUTOMATIC_HISTORICAL_VALIDATION"})
    print(f"New results written to {args.out}; historical interpretation remains a human task.")


if __name__ == "__main__":
    main()
