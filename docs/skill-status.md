# 发布、安装与验证状态

发布日期版本与本地安装是两件事。v0.4.0 已提供八款独立 ZIP；v0.5.0 提供十一款，v0.6.0 提供十三款。个人技能列表只显示已安装且被当前环境发现的项目，不显示整个 GitHub 仓库。

本项目的状态使用 **已发布 / 样例已测**，不把少量漂亮样例称作普遍稳定性证明。全部款式已有 Codex 内置 image_gen 样例；豆包仅测试了建筑版画的正文粘贴生图，详见 [豆包记录](doubao.md)。其他款在豆包中的表现、人脸身份保真尚未验证。所有 Skill 使用独立规则和版本，可单独更新。

下表统计不同来源照片，不把多次修订当作多个独立测试；源码和版本见 skills-catalog.json。补测由同一主会话执行，不是独立盲测。

| 玩法 | 规则版本 | 不同来源 | 结果记录（含修订） | 审图 |
|---|---|---:|---:|---|
| 没什么大事日报 | 0.1.0 | 5 | 7 | [记录](../evals/round-2-review.md) |
| 私人生活博物馆 | 0.2.1 | 4 | 5 | [记录](../evals/private-life-museum/quality-review.md) |
| 像素生活存档 | 0.3.1 | 3 | 4 | [记录](../evals/pixel-life-save/quality-review.md) |
| 大航海悬赏令 | 0.1.2 | 3 | 5 | [记录](../evals/pirate-bounty-poster/quality-review.md) |
| 日常电影剧照 | 0.1.1 | 4 | 5 | [记录](../evals/everyday-film-still/quality-review.md) |
| 微型纸雕 | 0.1.1 | 3 | 3 | [记录](../evals/paper-scene-diorama/quality-review.md) |
| 照片记忆册 | 0.1.1 | 3 | 3 | [记录](../evals/photo-memory-book/quality-review.md) |
| 日常说明书 | 0.1.1 | 3 | 3 | [记录](../evals/everyday-user-manual/quality-review.md) |
| 拼豆纪念画 | 0.1.0 | 2 | 2 | [记录](../evals/bead-memory-tile/quality-review.md) |
| 单双色网点海报 | 0.1.0 | 2 | 2 | [记录](../evals/spot-ink-editorial/quality-review.md) |
| 摄影与微小诗意 | 0.1.0 | 2 | 3 | [记录](../evals/photo-poetry-diptych/quality-review.md) |
| 实景渐绘拼贴 | 0.1.0 | 2 | 2 | [记录](../evals/scene-sketch-collage/quality-review.md) |
| 建筑版画海报 | 0.1.0 | 1 | 1 | [记录](../evals/architectural-relief-poster/quality-review.md) |

## 尚未覆盖的能力

- 拼豆仅为视觉效果图，未输出真实逐格图纸、品牌色号或采购数量。
- 网点海报未生成可制版的专色分色文件；本轮新增样例是英文大字。
- 摄影双联的长椅修订样例仍约 57/43 分割，不能承诺严格五五或原片无损。
- 电影衣架为空镜，叙事感弱于宠物场景；新增像素黑白狗偏写实。
- 记忆册为图片效果，未做翻页程序、印刷 PDF 或多张不同照片的编排验证。
- 悬赏令日文小字、人像以及多人复杂场景尚未覆盖。

安装完整同名目录后再调用。已装旧版时先备份自己的修改，按版本更新对应一款即可；不需要覆盖其他款。
