"""Allocate source entries for arrival, messages, clarification and light teasing."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
path=ROOT/'prompts/research/c2-allocation-staged.json'
data=json.loads(path.read_text('utf-8'))
rows={
's2-u13':'忽然 一直 已经 急 交通 公共汽车 公交车 司机 车辆 出发 等到 经过 离 离开 路边 停车 停车场 近 手表 信号 快点儿 一定'.split(),
's2-u14':'重新 经常 老 老是 又 然后 接着 接下来 出门 关机 开机 随时 通 通过 进入 走进 走开 走过 出口 入口 找出 拿出'.split(),
's2-u15':'正是 正确 准确 真正 直接 意思 重点 主要 观点 角度 方面 提 提出 提到 讨论 问题 道理 实际 实在 对 同样 相同'.split(),
's2-u16':'故意 好像 以为 感觉 难看 可怕 笑话 笑话儿 哭 喊 眼 眼睛 脸 嘴 头发 点头 小心 假 好人 坏人 好事 气'.split(),
}
baseline=json.loads((ROOT/'prompts/research/c1-coverage-baseline.json').read_text('utf-8'))
official={w for e in baseline['levels'][1]['words']['remainingEntries'] for w in e['forms']}
for uid,words in rows.items():
    assert len(words)==len(set(words))==22
    assert set(words)<=official
    prior={w for k,ws in data['vocabulary'].items() if k.startswith('s2-') and k!=uid for w in ws}
    assert not prior&set(words), (uid,prior&set(words))
    data['vocabulary'][uid]=words
path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n','utf-8')
print('Staged s2-u13–s2-u16; no packs published. 老/实在/对 retain source-specific senses.')
