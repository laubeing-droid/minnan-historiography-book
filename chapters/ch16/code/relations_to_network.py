#!/usr/bin/env python3
"""第16→17章合成教学桥接。Python 3.10+，无第三方依赖。

仅转通信事件，不把全部关系改名为网络边。不运行第17章内置 A–H 情景。
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


REL = load('ch16_relations', ROOT / 'manuscript/附件/ch16/relations.py')
NET = load('ch17_network', ROOT / 'manuscript/附件/ch17/network_analysis.py')


def bridge(data, start=1700, end=1710):
    if start > end:
        raise ValueError('起年不得晚于终年')
    nodes, types, sources, grouped, _ = REL.validate_relations(data)
    if any(s.get('material_kind') != 'new_synthetic_reconstruction' for s in sources.values()):
        raise ValueError('此入口只处理已标明的合成教学材料；真实史料需另行研究设计和核验')
    typ = types.get('send_letter', {})
    if not (typ.get('subject_type') == typ.get('object_type') == 'person'
            and typ.get('directed') == 'true' and typ.get('event_required') == 'true'):
        raise ValueError('send_letter 必须是有明确事件的有向人物通信关系')
    roster = {k for k, v in nodes.items() if v['entity_type'] == 'person' and v['identity_status'] == 'confirmed'}
    if not roster:
        raise ValueError('无明确身份的人物名册')
    events, audit, lineage = [], [], []
    seen_events = set()
    for rid, rows in sorted(grouped.items()):
        r = rows[0]
        reasons = []
        if r['relation_type'] != 'send_letter': reasons.append('not_send_letter')
        if r['subject'] not in roster or r['object'] not in roster: reasons.append('not_confirmed_person_pair')
        if r['layer'] != 'statement': reasons.append('hypothesis_not_event')
        if r['judgment'] != 'accepted': reasons.append('judgment_' + r['judgment'])
        if r['temporal_kind'] != 'event_year' or r['start_year'] is None: reasons.append('not_exact_event_year')
        elif not start <= r['start_year'] <= end: reasons.append('outside_window')
        audit.append({'instance_id': rid, 'included': not reasons, 'reasons': reasons})
        evidence = [{'assertion_id': x['assertion_id'], 'source_id': x['source_id'], 'locator': x['locator'],
                     'independent_group': sources[x['source_id']]['independent_group'],
                     'excerpt': sources[x['source_id']]['locations'][x['locator']]} for x in rows]
        lineage.append({'instance_id': rid, 'event_id': r['event_id'], 'included': not reasons, 'evidence': evidence})
        if reasons: continue
        if r['event_id'] in seen_events:
            raise ValueError('一个事件分配给多个通信实例，须先核对，不能自动重复计数')
        seen_events.add(r['event_id'])
        events.append({'event_id': r['event_id'], 'instance_id': rid, 'sender': r['subject'],
                       'recipient': r['object'], 'event_year': r['start_year'], 'identity_status': 'confirmed',
                       'event_status': 'accepted', 'source_id': r['source_id'], 'locator': r['locator']})
    edges = NET.edge_lineage(events)
    pairs = {(r['node_a'], r['node_b']) for r in edges}
    metrics = NET.graph_metrics(roster, pairs)
    return {'status': 'EXECUTED_SYNTHETIC_TEACHING_NOT_HISTORICAL_REVIEW',
            'window': [start, end], 'roster': sorted(roster), 'events': events,
            'audit': audit, 'lineage': lineage, 'edges': edges, 'metrics': metrics,
            'limitations': ['固定名册来自教学 entities.csv，不是完整历史人口',
                            '方向在事件中保留；此处指标针对无向简单存在图',
                            '同一实例的多条出处保留，但不按出处数增加事件数',
                            '未使用 A–H 敏感性情景，未推断历史社群、权力或因果关系']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=ROOT / 'manuscript/附件/ch16')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--start-year', type=int, default=1700)
    parser.add_argument('--end-year', type=int, default=1710)
    args = parser.parse_args()
    if args.out.exists(): raise FileExistsError('输出已存在，请选新目录')
    result = bridge(args.data, args.start_year, args.end_year)
    result['input_sha256'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in sorted(args.data.iterdir()) if p.is_file()}
    result['implementation_sha256'] = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in [Path(__file__), ROOT/'manuscript/附件/ch16/relations.py', ROOT/'manuscript/附件/ch17/network_analysis.py']}
    args.out.mkdir(parents=True, exist_ok=False)
    (args.out/'bridge_report.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    REL.csv_write(args.out/'events.csv', ['event_id','instance_id','sender','recipient','event_year','identity_status','event_status','source_id','locator'], result['events'])
    print(json.dumps({'roster': result['roster'], 'events': len(result['events']), 'graph': result['metrics']['summary']}, ensure_ascii=False))


if __name__ == '__main__': main()
