# 贡献指南

欢迎协助完善工程知识文档。提交内容前请阅读[文档贡献指南](docs/organization/contribution-guide.md)及[文档规范](docs/organization/document-standards.md)。

## 工作流程

1. 确认新增或修改内容适合公开发布，不包含内部资产资料、个人信息、采购记录、凭据或其他敏感信息。
2. 使用对应的[文档模板](docs/templates/)创建 Markdown 文件，并填写元数据。
3. 更新 `mkdocs.yml` 导航，确保导航链接指向存在的 Markdown 文件。
4. 在独立 Python 虚拟环境中安装 `requirements.txt` 并运行 `mkdocs build --strict`。
5. 提交 Pull Request，说明变更目的、影响范围及验证结果；需要组织或技术负责人确认的内容应明确标注。

## 内容原则

- 使用清晰、可复现且与具体网站主题解耦的 Markdown。
- 不猜测组织信息、人员、设备型号、项目数据或安全规范。
- 对尚未核实的事实使用待确认标记，不以示例冒充真实记录。
- 不在提交中包含访问令牌、密钥或其他凭据。
## PR 检查与审核

- Pull Request 创建或更新后，GitHub Actions 会运行 `Documentation build`，执行 `mkdocs build --strict`。请在 PR 的“Checks”页签查看结果；若失败，先修复再请求审核。
- 文档须由管理员或指定维护者审核并合并后才会进入 `main`。合并后，main 上的部署工作流会构建并更新网站；请在 Actions 确认部署成功后再检查网页。
- 当前 `main` Ruleset 强制要求通过 PR 并获得至少一项有效审批；新提交会清除先前的审批。`Documentation build` 会自动运行，但尚未配置为必需状态检查，因此失败时 GitHub 目前不一定阻止合并；仍应先修复失败再请求合并。
- 公开仓库禁止提交成员个人信息、内部资产资料、采购记录、凭据、密钥或其他未经授权的信息。拿不准时先咨询管理员。
