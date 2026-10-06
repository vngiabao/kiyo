"""Editorial allocations for the next social situations; no curriculum publication."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
path=ROOT/'prompts/research/c2-allocation-staged.json'
data=json.loads(path.read_text('utf-8'))
rows={
's2-u09':'层 封 放下 条 位 份 套 纸 笔 笔记 笔记本 交 交给 送给 送到 接 接到 接受 感谢 感动 感到 照顾'.split(),
's2-u10':'周 上周 下周 学期 周年 不久 就要 快要 以后 以前 刚 刚才 刚刚 这时 停 灯 节目 后来 不一会儿 半夜 夜里 早晨'.split(),
's2-u11':'多么 更 十分 挺 有空儿 有一点儿 一点点 不太 不够 不如 不行 大声 小声 难听 好 好多 好久 亮 满 超过 响 温度'.split(),
's2-u12':'只 只能 所有 全体 全家 大部分 大多数 多数 少数 其他 其中 一部分 两 蛋 鸡 鱼 油 饱 完全 公平 请客 人数'.split(),
}
for uid, words in rows.items():
    assert len(words)==22 and len(set(words))==22
    data['vocabulary'][uid]=words
data['note']='Editorial allocation only; source rows/senses and pronunciation are checked when each batch is serialized. Repeated forms are not independent extra entries.'
path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n','utf-8')
print('Staged s2-u09–s2-u12; no packs published.')
