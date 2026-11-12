---
title: 文档贡献指南
category: Organization
status: draft
owner: SSIR
last_reviewed: YYYY-MM-DD
---

# 文档贡献指南

普通成员可使用 GitHub 网页或 VS Code 贡献，不需要直接修改 `main`。逐步操作请见[文档编辑与贡献指南](document-editing-guide.md)。

## 简要流程

1. 阅读仓库根目录的 `CONTRIBUTING.md`。
2. 选择[对应的文档模板](../templates/index.md)。
3. 核实事实、来源和公开授权；不确定的信息应留空或标注待确认。
4. 检查文档中没有个人信息、凭据、内部资产明细、采购记录或其他敏感内容。
5. 新增页面时更新必要的导航；本地编辑者运行 `mkdocs build --strict`。
6. 从功能分支提交 Pull Request，描述变更目的、内容范围和验证结果。

## Pull Request

在 PR 的 Checks 页签查看自动构建结果；如失败，修复后再次提交。对需要负责人审核的信息明确标注，不要把草稿描述为已批准的流程。等待管理员或指定维护者审核、合并后，文档才会进入正式网站。
