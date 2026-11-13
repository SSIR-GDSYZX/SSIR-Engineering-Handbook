---
title: 第一次社课：Boids 群体行为模拟
category: Academy
status: draft
owner: SSIR
last_reviewed: YYYY-MM-DD
---

# 第一次社课：Boids 群体行为模拟

用 80 个三角形个体在窗口里运动，靠三条**局部**规则涌现出鱼群、鸟群那样的群体行为。整个过程没有"总指挥"：每只 boid 只看得见半径 50 像素内的邻居。

## 三条规则

| 规则 | 个体在做什么 | 对应参数 |
| --- | --- | --- |
| 分离 Separation | 离得太近就往外让一点，避免撞在一起 | `SEPARATION_WEIGHT`、`SEPARATION_DISTANCE` |
| 对齐 Alignment | 尽量和邻居们朝同一个方向飞 | `ALIGNMENT_WEIGHT` |
| 凝聚 Cohesion | 稍微往邻居的中心靠一靠，别掉队 | `COHESION_WEIGHT` |

三者按权重加权求和，再加上一点"惯性"（保留 80% 当前速度），最后把速度限制在 `[MIN_SPEED, MAX_SPEED]` 之间，就是下一帧的速度：

```python
new_velocity = (
    self.velocity[0] * 0.8 +
    separation[0] * SEPARATION_WEIGHT +
    alignment[0] * ALIGNMENT_WEIGHT +
    cohesion[0] * COHESION_WEIGHT +
    edge_avoidance[0],
    ...
)
self.velocity = limit_vector(new_velocity, MAX_SPEED, MIN_SPEED)
```

## 参数速查（`config.py`）

| 参数 | 默认值 | 作用 |
| --- | --- | --- |
| `WINDOW_WIDTH` / `WINDOW_HEIGHT` | 1200 / 900 | 窗口尺寸 |
| `BOID_COUNT` | 80 | 个体数量 |
| `PERCEPTION_RADIUS` | 50 | 感知半径，决定"邻居"的范围 |
| `MAX_SPEED` / `MIN_SPEED` | 20.5 / 1.0 | 速度上下限 |
| `SEPARATION_WEIGHT` | 2.0 | 分离权重，调大更"散" |
| `ALIGNMENT_WEIGHT` | 10.5 | 对齐权重，调大更容易成群同向 |
| `COHESION_WEIGHT` | 0.8 | 凝聚权重，调大更"抱团" |
| `FPS` | 60 | 帧率 |

调参是这节课的重点：把 `ALIGNMENT_WEIGHT` 调到 0，群会立刻散掉；把 `SEPARATION_WEIGHT` 调到 0，个体又会挤成一团。

## 运行方法

需要 Python 3.8+ 和 Pygame：

```powershell
pip install pygame
python main.py            # 正常模式
python main.py --debug    # 调试模式，每 10 帧打印位置、速度、邻居数
```

按 `ESC` 或点窗口关闭按钮退出。

## 文件结构

| 文件 | 内容 |
| --- | --- |
| `main.py` | 主入口：初始化窗口、事件循环、逐帧更新与绘制 |
| `boids.py` | `Boid` 类与三条规则、边缘转向、位置更新 |
| `config.py` | 所有可调参数集中在这里 |
| `utils.py` | 向量运算、绘制等工具函数 |
| `README.md` | 原始项目说明 |

## 下载

- [第一次社课代码包（ZIP，约 5 KiB）](../../assets/files/boids-demo.zip)

解压后进入目录执行 `python main.py` 即可，无需安装其他依赖（除 Pygame）。
