# photo-poetry-diptych · v0.5.0 补测记录

使用内置 image_gen，由当前会话读取该 Skill 规则并编译提示词；不是独立代理盲测，也没有跨模型验证。保留所有生成结果与修订提示词。

## bench

首稿插画偏大且上半约占 57%；修订缩小插画改善留白，分割线仍约 57/43，未达到精确五五。

[最终图](../../examples/results/photo-poetry-diptych/bench-q2.png) · [实际提示词](../../evals/photo-poetry-diptych/bench-q2-prompt.txt)

## cat

猫咪姿态及电脑/书/鼠标关系一致，上下约各半，插画较小；细节仍偏精细干笔，未保证原片像素不变。

[最终图](../../examples/results/photo-poetry-diptych/cat-q1.png) · [实际提示词](../../evals/photo-poetry-diptych/cat-q1-prompt.txt)

本轮样例通过基础可用性检查或附带明确保留意见；样本不足以估计成功率、分享意愿或任意照片稳定性。
