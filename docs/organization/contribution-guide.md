---
title: 文档贡献指南
category: Organization
status: draft
owner: SSIR
last_reviewed: YYYY-MM-DD
---

# 文档贡献指南

普通成员可使用 GitHub 网页或 VS Code 贡献，不需要直接修改 `main`。第一次使用请从[网站使用指南](website-guide.md)开始；逐步操作请见[文档编辑与贡献指南](document-editing-guide.md)。

## 简要流程

1. 阅读仓库根目录的 `CONTRIBUTING.md`。
2. 选择[对应的文档模板](../templates/index.md)。
3. 核实事实、来源和公开授权；不确定的信息应留空或标注待确认。
4. 检查文档中没有个人信息、凭据、内部资产明细、采购记录或其他敏感内容。
5. 新增页面时更新必要的导航；本地编辑者运行 `mkdocs build --strict`。
6. 从功能分支或 Fork 提交 Pull Request，目标分支为 `main`，描述变更目的、内容范围和验证结果。

## Pull Request

在 PR 的 Checks 页签查看 `Documentation build` 自动构建结果；如失败，先修复再请求合并。当前 Ruleset 已对 `main` 强制要求 PR 和至少一项有效审批，并在新提交后清除过期审批。Ruleset 尚未将 `Documentation build` 设为必需状态检查，因此失败状态目前不一定会被 GitHub 阻止合并；贡献者和维护者仍应以检查通过为合并前提。

对需要负责人确认的信息明确标注，不要把草稿描述为已批准的流程。获批 PR 合并后，main 上的部署工作流会构建并更新网站；请确认 Actions 部署成功后再检查网页。提交 Issue 仅用于反馈，不会直接修改正式文档。

## 维护者审核

1. 打开仓库的 Pull requests 页面并选择待审 PR。
2. 在 Files changed 中核对改动范围、技术依据及公开安全性。
3. 确认 `Documentation build` 检查成功；若失败，要求贡献者先修复，即使当前 Ruleset 未将该检查设为合并必需项。
4. 按审核结果选择 Approve 或 Request changes。新提交会清除先前审批，届时需重新审核。
5. 确认至少一项有效审批及其他合并条件满足后，再合并 PR。
6. 在 Actions 确认 main 的部署工作流成功，并打开正式网站核对更新。
