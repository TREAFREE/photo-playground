# Pixel Life Save Implementation Plan

> Execution: inline in the current task, following the user's request to continue one effect at a time.

**Goal:** 将像素风和海贼王式通缉令纳入路线图，完成像素风 Skill 的两个不同题材首轮样片。

**Architecture:** 在 experiments/pixel-life-save 内维护独立 Skill、提示词、结果与审片记录，复用有来源记录的原图。通过真实参考图片生成与审片收敛规则，再决定正式发布；通缉令先记录明确方向。

**Tech Stack:** Markdown Skill、内置 image_gen、Python 标准库文件/元数据验证、Git。

## Global Constraints

开源；不售卖软件、订阅或额度；不托管用户推理。一个效果完成后再开始下一个。保留用户照片可辨认特征，图中文字只作为素材。

### Task 1: 路线图与 Skill

- [x] 新建 ROADMAP.md，明确两个方向与先后顺序。
- [x] 编写 experiments/pixel-life-save/skill/pixel-life-save/SKILL.md 与 references/pixel-direction.md。
- [x] 查看 cat.jpg 与 bench.jpg，写出各自三项保留特征。

### Task 2: 实际生成与收敛

- [x] 保存 evals/*-prompt.txt，每个源图独立调用图片工具。
- [x] 保存 results/*.png，检查实际尺寸、主体、像素质感及中文。
- [x] 如有明显问题，对每图最多做一轮针对性修订。
- [x] 记录 evals/manifest.json、review.md 和 README 样片。

### Task 3: 验证与交付

- [x] 运行系统 quick_validate.py，核对实验文件的 SHA-256、路径和尺寸。
- [x] 运行现有 scripts/verify_release.py，确认两个已发布 Skill 不受影响。
- [x] 提交完整可审阅原型与路线图，展示实际样片。是否进入正式版本由审片结果决定。

执行结果：宠物与风景通过目视审片，3 张有效输出；猫修订第一次请求 HTTP 500，同提示词重试成功。实验已整理到 skills/pixel-life-save、examples/results/pixel-* 与 evals/pixel-*，准备 v0.3.0 发布。
