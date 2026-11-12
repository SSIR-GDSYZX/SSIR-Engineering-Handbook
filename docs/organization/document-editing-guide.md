---
title: 文档编辑与贡献指南
category: Organization
status: draft
owner: SSIR
last_reviewed: YYYY-MM-DD
---

# 文档编辑与贡献指南

网站编辑按钮只用于创建变更提案，不会直接发布到 `main`。所有贡献都应通过 Pull Request（PR）提交，并等待管理员或指定维护者审核。

## 方式一：在 GitHub 网页编辑

适合修改少量文字或修正链接，不需要安装 Git。

1. 登录 GitHub，打开[SSIR Engineering Handbook 网站](https://ssir-gdsyzx.github.io/SSIR-Engineering-Handbook/)并进入要修改的页面。
2. 点击页面上的“编辑此页”图标。它会打开仓库中对应的 Markdown 源文件；若页面没有编辑按钮，可在仓库的 `docs/` 目录中找到相应 `.md` 文件。
3. 在 GitHub 编辑器中修改 Markdown。可先使用预览检查标题、列表和链接；不要把敏感资料复制到编辑器。
4. 选择创建新分支来保存变更。如果没有该仓库的写入权限，GitHub 会引导你在自己的 Fork 中提出变更；请使用 GitHub 提供的分支/Fork 流程，不要尝试直接修改 `main`。
5. 按 GitHub 页面提示提交变更，然后选择“Compare & pull request”创建 PR，目标分支选 `main`。在描述中说明修改内容与验证情况。
6. 打开 PR 的“Checks”页签查看自动构建状态。检查通过表示严格构建成功；失败时查看日志、修改后再次提交。
7. 在 PR 对话中请求管理员或指定维护者审核。根据反馈更新 PR，并等待维护者批准、合并；提交 PR 不等于已经发布。
8. PR 合并后打开 Actions，确认 main 上的 “Build and deploy handbook” 工作流成功，再刷新[网站](https://ssir-gdsyzx.github.io/SSIR-Engineering-Handbook/)确认更新。

## 方式二：使用 VS Code

适合多文件修改、预览或需要本地检查的贡献。

1. 安装 Git、VS Code 和 Python；克隆[正式仓库](https://github.com/SSIR-GDSYZX/SSIR-Engineering-Handbook)，并在 VS Code 中打开目录：

   ```powershell
   git clone https://github.com/SSIR-GDSYZX/SSIR-Engineering-Handbook.git
   cd SSIR-Engineering-Handbook
   ```

2. 从最新 `main` 创建自己的功能分支：

   ```powershell
   git switch -c docs/简短主题名称
   ```

   分支名称建议使用简短英文和连字符，例如 `docs/update-install-guide`。

3. 在 `docs/` 下编辑或新增 Markdown。新目录页面通常使用 `index.md`；完成后按[文档规范](document-standards.md)检查。
4. 在仓库根目录创建独立环境并安装依赖。Windows PowerShell 示例：

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   .\.venv\Scripts\python.exe -m mkdocs serve --dev-addr 127.0.0.1:8000
   ```

   打开终端显示的本地地址预览网站。按 `Ctrl+C` 停止预览，再运行以下命令检查严格构建：

   ```powershell
   .\.venv\Scripts\python.exe -m mkdocs build --strict
   ```

5. 只暂存本次修改的文档和相关导航，再提交并推送功能分支：

   ```powershell
   git add docs/你的文档路径.md mkdocs.yml
   git commit -m "docs: describe your change"
   git push -u origin docs/简短主题名称
   ```

   若只修改现有文档且未改导航，`git add` 只需包含相应文档路径。

6. 打开 GitHub 仓库，点击新分支提示中的 “Compare & pull request”，创建目标为 `main` 的 PR。没有仓库写入权限时，请先 Fork，再从 Fork 分支创建 PR。
7. 在 PR 的“Checks”页签查看 `Documentation build`。如失败，打开日志修正问题并再次推送同一功能分支。
8. 在 PR 请求管理员或指定维护者审核。按反馈修改并等待审核、合并；合并后检查 main 部署工作流及网站更新。

## 提交前安全检查

此仓库是公开仓库。不得提交成员个人信息、内部资产清单或标识、存放位置、采购或财务记录、访问凭据、密钥、未授权实验数据及其他内部资料。不确定能否公开时，先询问管理员，不要提交试探版本。

## 审核规则说明

当前仓库规则要求通过 PR，但尚未强制至少一项审批。请按协作流程等待管理员或指定维护者审核后再合并；本轮不修改 Ruleset。若需由 GitHub 阻止未审批 PR 合并，需由管理员另行设置必需审批数。
