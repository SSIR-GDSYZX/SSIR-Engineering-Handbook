# SSIR Engineering Handbook

Robotics and Engineering Knowledge Base

这是 SSIR 工程技术文档平台的基础框架。文档以 Markdown 为主，网站由 MkDocs 和 Material for MkDocs 构建。项目尚处于基础设施搭建阶段，组织信息、设备资料和项目内容均由授权维护者后续确认并补充。

## 本地预览

需要 Python 3.12 或更新版本，以及 [uv](https://docs.astral.sh/uv/)。

```powershell
uv venv .venv
uv pip install --python .venv\Scripts\python.exe -r requirements.txt
.\.venv\Scripts\Activate.ps1
mkdocs serve --dev-addr 127.0.0.1:8000
```

在浏览器打开 `http://127.0.0.1:8000/`。退出预览可按 `Ctrl+C`，退出虚拟环境可运行 `deactivate`。

## 构建与检查

```powershell
mkdocs build --strict
```

静态网站输出到 `site/`，该目录不会提交到 Git。

## 内容与公开范围

- 从首页进入学院、项目、工坊、资产、技术、研究、安全和组织八个板块。
- 新贡献者请先阅读[贡献指南](docs/organization/contribution-guide.md)和[文档规范](docs/organization/document-standards.md)。
- 新文档应从[标准模板](docs/templates/index.md)开始。
- 发布前确认内容已获公开授权。不要提交内部资产明细、成员个人信息、采购记录、凭据或其他敏感资料。
- GitHub 仓库地址已确认为 `https://github.com/SSIR-GDSYZX/SSIR-Engineering-Handbook`。正式 Pages URL、许可证及公开范围仍待 SSIR 管理人员确认；工作流不会自动启用 GitHub Pages。
- MkDocs 中的 GitHub 编辑入口已指向上述仓库的 `main/docs/`；正式 Pages URL 尚未设置。

## 远端初始 README 说明

为保留原始仓库说明，以下文字来自远端初始提交 `247962154f9804704bad41dd24e90621ccfe01b8`：

> This the public repository for Guangdongshiyan SSIR. It is aiming to provide effective dirction for members.
