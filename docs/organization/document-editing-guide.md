---
title: 文档编辑与贡献指南
category: Organization
status: draft
owner: SSIR
last_reviewed: YYYY-MM-DD
---

# 文档编辑与贡献指南

网站编辑按钮只用于创建变更提案，不会直接发布到 `main`。所有文档修改都应通过 Pull Request（PR）提交；至少一项有效审批后方可合并。没有 Git 使用经验的成员可以只用浏览器完成贡献。

## GitHub 基础概念

| 英文 | 中文 | 简单解释 |
| --- | --- | --- |
| Repository | 仓库 | 存放网站和文档的地方 |
| Branch | 分支 | 独立保存修改，不影响正式网站 |
| Commit | 提交 | 保存一次修改记录 |
| Pull Request（PR） | 拉取请求 / 修改申请 | 请求维护者检查并合并修改 |
| Merge | 合并 | 将获批修改加入正式版本 |

创建新分支是正常操作。没有仓库写入权限的贡献者可以通过 Fork（在自己账号下创建的仓库副本）提交 PR；有写入权限的成员则可在原仓库创建功能分支。两种方式都不会绕过 `main` 的 PR 和审批规则。

## 方式一：在 GitHub 网页编辑

适合修改少量文字或修正链接，不需要安装 Git。

1. 登录 GitHub，打开[SSIR Engineering Handbook 网站](https://ssir-gdsyzx.github.io/SSIR-Engineering-Handbook/)并进入要修改的页面。
2. 点击页面上的“编辑此页”图标。它会打开仓库中对应的 Markdown 源文件；若页面没有编辑按钮，可在仓库的 `docs/` 目录中找到相应 `.md` 文件。
3. 在 GitHub 编辑器中修改 Markdown。可先使用预览检查标题、列表和链接；不要把敏感资料复制到编辑器。
4. 保存修改时选择创建新分支；有仓库写入权限时可在组织仓库创建分支。若无写入权限，GitHub 会提示通过自己的 Fork 提出修改。不要选择直接提交到 `main`。
5. 点击 GitHub 提供的“Propose changes”或“Compare & pull request”入口创建 PR，目标分支选择组织仓库的 `main`。在 PR 描述中说明修改内容和验证情况。
6. 打开 PR 的“Checks”页签查看 `Documentation build`。该检查运行 `mkdocs build --strict`；通过表示严格构建成功，失败时查看日志并更新同一 PR。
7. 按需请求维护者审核，并根据反馈修改 PR。当前 Ruleset 要求至少一项有效审批后才能合并；如继续推送新提交，已有审批可能被清除，需要重新审批。
8. PR 合并后打开 Actions，确认 main 上的 “Build and deploy handbook” 工作流成功，再刷新[网站](https://ssir-gdsyzx.github.io/SSIR-Engineering-Handbook/)确认更新。

当前 Ruleset 尚未把 `Documentation build` 配置为必需状态检查。因此，CI 会自动运行并显示结果，但 GitHub 目前不保证仅因该检查失败就阻止合并；仍应先修复失败再请求合并。

PR 页面常见状态：

| 状态 | 含义 |
| --- | --- |
| `Checks passed` | 自动构建检查通过 |
| `Review required` | 仍需满足审批规则 |
| `Changes requested` | 按审核意见修改后更新同一个 PR |
| `Approved` | 已获得审批；仍需满足其他合并条件 |
| `Merged` | 修改已合并；再确认网站部署完成 |

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

## 常见问题

**我不会 Git，可以贡献吗？** 可以，使用浏览器编辑即可。

**为什么 GitHub 提示创建分支或 Fork？** 修改必须先独立保存。组织仓库成员可新建分支；没有写入权限时使用 Fork 是正常流程。

**提交 PR 后网站为什么没变化？** PR 只是修改申请；只有获批、合并并完成部署后，正式网站才会更新。

**没有 GitHub 账号怎么办？** 可以阅读网站；提交 Issue 或 PR 需要登录 GitHub。网页评论用于交流，不会直接修改正式文档；评论功能是否可用，以网站实际部署情况为准。

## 提交前安全检查

此仓库是公开仓库。不得提交成员个人信息、内部资产清单或标识、存放位置、采购或财务记录、访问凭据、密钥、未授权实验数据及其他内部资料。不确定能否公开时，先询问管理员，不要提交试探版本。
