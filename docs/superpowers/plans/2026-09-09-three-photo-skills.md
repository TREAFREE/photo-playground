# Three Photo Skills Implementation Plan

**Goal:** 完成用户确认的微型纸雕、照片记忆册、日常说明书，每款两个题材，交付统一检查页。

**Architecture:** 三个自包含 Skill，不依赖或修改已发布五款。每款独立提示词、结果清单、审图记录和 ZIP。统一预览页仅展示结果。

**Tech Stack:** Markdown、内置 image_gen、Python 标准库打包校验、静态 HTML 预览。

## Global Constraints

开源，不托管推理或售卖额度。既有五款目录与 ZIP 必须逐字节不变。保留照片来源许可。样例是创意生成，不承诺照片无损。用户统一审美检查后再决定正式发布。

## Tasks

- [x] 创建 skills/paper-scene-diorama/SKILL.md 与 LICENSE；测试 cat 和 bench；记录 evals/paper-scene-diorama；独立打包。
- [x] 创建 skills/photo-memory-book/SKILL.md 与 LICENSE；测试 cat 和 croissant；记录 evals/photo-memory-book；独立打包。
- [x] 创建 skills/everyday-user-manual/SKILL.md 与 LICENSE；测试 cat 和 bench；记录 evals/everyday-user-manual；独立打包。
- [x] 在 examples/review-2026-09-09/index.html 展示六张成品、原图、下载链接。补充 Markdown 检查入口与路线图状态。
- [x] 运行 quick_validate、verify_release.py、已有隔离单元测试；比较既有五款 SHA256；检查全部样例和预览资源。
