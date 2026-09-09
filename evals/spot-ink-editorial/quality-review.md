# spot-ink-editorial · v0.5.0 补测记录

使用内置 image_gen，由当前会话读取该 Skill 规则并编译提示词；不是独立代理盲测，也没有跨模型验证。保留所有生成结果与修订提示词。

## dog

单色视觉成立，OFF DUTY. 与副句准确，眼睛口鼻未被裁掉；是网点效果，未做印刷分色检测。

[最终图](../../examples/results/spot-ink-editorial/dog-q1.png) · [实际提示词](../../evals/spot-ink-editorial/dog-q1-prompt.txt)

## croissant

蓝色主墨、红色草莓重点成立，SLOW MORNING. 与副句准确；可颂形状可辨，未验证中文大字版本。

[最终图](../../examples/results/spot-ink-editorial/croissant-q1.png) · [实际提示词](../../evals/spot-ink-editorial/croissant-q1-prompt.txt)

本轮样例通过基础可用性检查或附带明确保留意见；样本不足以估计成功率、分享意愿或任意照片稳定性。
