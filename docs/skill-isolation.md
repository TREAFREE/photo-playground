# Skill 独立维护约定

每个 Skill 是独立可复制的目录。运行时只需要自己的 SKILL.md、自己的 references/ 与所需图片工具；不依赖本仓库的其他 Skill，也不共用一份可变视觉配置。

## 修改与打包

1. 只修改目标 skills/<name>/ 内的规则与资源。测试照片可以共享来源目录，但提示词和审片记录按 Skill 保存，新款采用 evals/<name>/results-manifest.json；比例要求也随样例记录，不强迫所有效果使用同一纸张尺寸。不要覆盖其他效果的结果。
2. 执行 `python3 scripts/pack_skill.py <name>`，只重建目标 ZIP；其他 ZIP 的字节保持不变，SHA256SUMS 只更新校验索引。
3. 执行 `python3 -m unittest discover -s tests` 与 `python3 scripts/verify_release.py`。打包检查拒绝越出自身目录的 Markdown 本地引用和符号链接；源码/规则仍需要正常审查，不能把静态检查当成所有代码行为的证明。
4. 独立发布可以使用 `<name>-vX.Y.Z` 标签，只上传该 ZIP。若使用这种发布方式，应把 README 下载入口指向各自固定 release，不能再依赖整个仓库的 latest 链接。当前 v0.3.0 的下载方式保持兼容。

## 使用时的范围

明确指定目标 Skill，如 `$pirate-bounty-poster`，只加载它的视觉规范。需要比较两种效果时分别生成。长对话中的先前风格描述仍可能影响模型；要求严格隔离的测试应在新对话中只指定一个 Skill。文件与打包隔离不意味着生成模型每次都确定性输出。

## 本次版本处理

GitHub v0.3.0 的像素版继续保留。用户选定的另一张猫图与相关修订保存在 fix/pixel-art-direction 分支，没有混入大航海悬赏令开发分支。
