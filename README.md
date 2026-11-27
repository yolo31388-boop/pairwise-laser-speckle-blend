# pairwise-laser-speckle-blend

## 领域

游戏、图形与多媒体

## 主题

激光投影散斑抑制与多机重叠

## 说明

多波长散斑去相关、扰动序列时域连续、重叠区亮度自适应。

初始状态下 `graphics/laser_speckle.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
