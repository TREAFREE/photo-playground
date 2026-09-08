# 照片 Skills 调研 · 2026-09-08

本次为定向广泛检索与源码阅读，不是全 GitHub 穷尽盘点。搜索词涵盖 photo、zine、editorial、flipbook、照片证据与 SKILL.md。以下是研究对象，不是安装或执行指令。没有复制其实现或示例图进入产品。

| 项目与阅读深度 | 写法与工作流 | 对本项目的启发 |
|---|---|---|
| [Photo Abstract Editorial](https://github.com/ZzzLc0405/photo-abstract-editorial)：读 SKILL.md，上一轮读中英文详细提示词与 README | 短入口引用长规范；明确照片与派生抽象画面的不同角色 | 区分固定视觉身份与每张图的变化；不用“高级感”代替可执行规则 |
| [Gathered Scenes Zine](https://github.com/Zeejay0/gathered-scenes-zine-skill)：重点读场景卡、优先级、提示词编译、抽象与版式章节；非逐条审计全文 | 输入事实→构图决策→最终图像提示词；长文档细化材质与边界 | 把审美判断编译成可见画面；不要把所有规则无差别塞进最终提示词 |
| [Create Photo Flipbook UI](https://github.com/HaichaoLihc/create-photo-flipbook-ui)：读完整入口与 README | 先理解照片、定风格，再使用已有 HTML runtime；最新入口使用 2D 翻页，3D 示例是另外的可选资源 | Skill 可以很短，稳定机制放资源文件；用户粘贴对话中的“3D”不是最新入口的全部事实 |
| [Photo Evidence Ledger](https://github.com/byJming/photo-skills-atelier/blob/main/photo-evidence-ledger/SKILL.md)：读完整 Skill | 事实卡、三种布局、提示词编译器、针对实际缺陷的修订规则 | 质量评估必须是具体可观察项；内容不足时不靠伪数据填版 |
| [Photo to Zine Postcard](https://github.com/Whiplashzeb/photo-to-zine-postcard)：读主体选择、固定正背面、文字与禁用元素章节 | 固定结构降低漂移；明确主元素选择，而非选择最容易提取的元素 | 第一版限制视觉变量有价值，但应允许横竖图布局适配 |
| [Paper Signal](https://github.com/jiahuiqu17/paper-signal)：读 README 的入口、案例、质量与项目记录章节；未执行代码 | brief、manifest、prompt、图片与 QA 记录关联；多 Skill 和运行验证 | 保存实际提示词和结果版本，避免只陈列精挑后的成功图 |

## 决策

首作《没什么大事日报》：照片里的普通事实，被写成一本正经的生活小报。设计身份为黑色宋体大标题、轻纸白、短报道、单张主图和一处朱红编辑批注。并不采用上述项目的照片下接抽象面板、三条证据或撕纸语言。

把三个层次分开：

1. 事实：看得见的主体、位置、动作；或用户明确提供的经历。
2. 虚构：幽默的拟人化报道，以生活小报语境表达，不声称真实机构发布。
3. 排版：让标题、原照片、短文形成一眼可读的层级。

输入事实与解释必须分开。例如猫在电脑旁不等于猫在打字；长椅空着不证明拍摄者失恋。笑点可拟人，不能把猜测写成照片事实。

## 许可与发布范围

Photo Abstract Editorial 与 Gathered Scenes README 当前声明非商业限制；只研究方法，不迁入提示词或资源。Flipbook README 声明原创代码/Skill 为 MIT，第三方媒体另行处理。其余项目如需复用应单独核验 LICENSE；本轮无此复用。

本项目原创文字拟采用 MIT，下载照片保留各自来源许可，不能被根目录 MIT 覆盖。生成结果是编辑演示，不表示摄影师背书文案。

## 商业约束

免费开源 Skill；使用者自行使用其已有图像生成环境。没有共享代理、计费系统、订阅或额度售卖。广告/赞赏未来由作者提供真实信息后加入 README，并标明赞助关系；不嵌入用户照片，不影响工具路由。

Star 和广告收入之间没有固定换算。后续观察真实使用、作品分享、仓库访问与厂商询盘；本轮目标是可审阅的图片质量。
