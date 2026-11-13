---
title: 字体与性能审计
category: Organization
status: draft
owner: SSIR
last_reviewed: YYYY-MM-DD
---

# 字体与性能审计

本文记录 Stage 4C 的字体授权调查、Variable Font 原型和脚本加载基线。MiSans 原型仅通过字体提供方的官方 CSS/CDN 临时加载；本仓库不包含 MiSans 字体文件，生产网站暂不启用该字体。

## 字体授权与技术能力

### MiSans Variable

官方 [MiSans 字体页面](https://hyperos.mi.com/font/en/) 将 MiSans 列为免费商用字体，并列出简体中文 MiSans 共 29,608 个字形、10 个字重及 Variable Font。官方 [下载与许可页面](https://hyperos.mi.com/font/en/download/) 的许可协议授予非转让、非独占、免版税、可撤销的全球使用许可，并要求在软件中注明使用 MiSans。

协议同时明确禁止单独转让、再许可、借出或进一步分发字体组件，也禁止重新分发或销售字体软件及其副本。因此不得将 MiSans 字体文件提交到公开仓库。官方 [MiSans VF CSS 服务](https://cdn-font.hyperos.mi.com/font/css?family=MiSans_VF:VF:Chinese_Simplify,Latin&display=swap) 可提供网页字体样式：检查到的 `font-weight` 轴为 `1 999`，`font-display` 为 `swap`，并提供 WOFF2、WOFF、TTF 和 EOT 格式。

官方 CSS 服务证明存在网页字体交付方式，但许可协议没有明确说明第三方网站使用该 CDN 的具体条件。为避免将这一点当作已确认的法律授权，MiSans 仅用于本阶段的临时 A/B 原型；取得明确确认前不在生产站加载，也不托管字体文件。

### 可变字体备选：Noto Sans SC

Google Fonts 官方仓库的 [Noto Sans SC 元数据](https://github.com/google/fonts/blob/main/ofl/notosanssc/METADATA.pb) 标注 SIL Open Font License，并声明 `wght` 轴范围为 100–900。仓库中的 [OFL 许可文本](https://github.com/google/fonts/blob/main/ofl/notosanssc/OFL.txt) 允许嵌入、打包和再分发，但要求保留许可和版权声明。通过现代浏览器请求 Google Fonts 官方 CSS 时确认了 `font-weight: 100 900` 的 WOFF2 子集。

该备选在许可和字重轴方面更明确，但完整变量 TTF 为约 17.8 MB；对同一首页内容进行完整字形加载测试时，Google Fonts 提供的 17 个子集共计约 868 KB。它比 MiSans 原型低约 22%，但仍会产生明显的第三方字体下载量，且依赖外部 CDN。当前不选用；未来如有需要，应先测试经过许可的按需子集方案。

## A/B 原型的资源测量

测量环境：集成 Chromium 浏览器、桌面默认网络和 CPU 配置、无显式网络/CPU 限速；页面由本地 MkDocs 预览服务提供，字体文件从各字体官方 CDN 请求。字体字节数为 HTTP `Content-Length` 之和，不等同于压缩后的线路流量。

| 方案 | CSS | 首页完整文本实际触发的字体子集 | 字体字节数 | 许可结论 |
|---|---:|---:|---:|---|
| MiSans Variable | 102,585 B；56 条 WOFF2 字体规则 | 18 个 WOFF2 子集 | 1,113,728 B | 不得向仓库再分发；第三方 CDN 嵌入条款待明确 |
| Noto Sans SC Variable | Google Fonts CSS | 17 个 WOFF2 子集 | 868,128 B | OFL 允许嵌入/再分发，需保留许可和声明 |

子集按页面所需字符加载，完整中文页面仍会请求多个文件。根据授权和实测加载量，Stage 4C 不将 MiSans 或 Noto Sans SC 全站上线；继续使用 Material 当前字体栈，并通过字体回退和字重 token 保持一致的设计接口。

## 字重 Tokens

统一 token 定义于 [`static/stylesheets/typography.css`](../static/stylesheets/typography.css)，并由首页和普通文档样式复用：

| 用途 | Token | 当前值 |
|---|---|---:|
| 正文 | `--handbook-weight-body` | 400 |
| 导航 | `--handbook-weight-navigation` | 500 |
| 标签 | `--handbook-weight-label` | 600 |
| 元数据 | `--handbook-weight-metadata` | 500 |
| 按钮和主要操作 | `--handbook-weight-control` | 600 |
| 文档 H1 | `--handbook-weight-heading-1` | 700 |
| 分类标题 | `--handbook-weight-category` | 800 |
| H2 | `--handbook-weight-heading-2` | 600 |
| H3 | `--handbook-weight-heading-3` | 600 |
| 首页 Hero | `--handbook-weight-hero` | 800 |
| 表格表头与强调文字 | `--handbook-weight-strong` | 700 |

当前 Material 字体栈不保证在所有设备上使用可变字重轴；这些 token 统一现有排版并为未来经批准、经过性能验证的可变字体提供单一调整点。不对正文段落添加动态字重效果。

## 脚本加载基线与按需策略

改动前，首页即加载 MathJax 3 和 Mermaid 11，即使页面没有公式或图表。浏览器 Resource Timing 报告的脚本体积分别为 MathJax 204,607 B、Mermaid 745,043 B；对应资源仅在含公式或 Mermaid 图表的页面需要。

Stage 4C 将两者改为按需加载：

- 只有页面中包含 `.arithmatex` 时才加载 MathJax。
- 只有页面中包含 `.mermaid` 时才加载 Mermaid。
- 加载或渲染失败会输出控制台错误，不静默降级。
- 文档内容和 MkDocs 的 MathJax/Mermaid Markdown 语法保持不变。

## 实测结果

### 构建与页面功能

使用 MkDocs 1.6.1、Material for MkDocs 9.8.1、Python 3.14 执行：

```text
& 'D:\SSER\SSIR_Engineering_Handbook\.venv\Scripts\python.exe' -m mkdocs build --strict -f 'D:\SSER\SSIR_Engineering_Handbook_Stage4C\mkdocs.yml'
```

结果：退出码 0，严格构建通过。构建仅报告两个 `_nav.md` 文件不在 `nav` 中的信息提示；这是目录插件使用的辅助文件，不是构建警告或错误。

本次使用的 Material for MkDocs 版本为 9.8.1；构建还输出了上游关于 2027-05-05 终止 Material 维护并建议评估 Zensical 的提示。Stage 4C 不进行主题迁移，后续应单独评估迁移兼容性。

页面级浏览器检查结果：

- 首页、PETG、Bambu Lab A1 和 PLA 在 1920 × 1080、1366 × 768、390 × 844 下，分别检查浅色和深色模式，共 24 个页面/视口/配色状态；当前字体栈和 MiSans 原型各验证一次，合计 48 次渲染，均有 H1 且没有横向溢出。
- 搜索 `PETG` 返回相关条目；Bambu Lab A1 页面目录的 12 个锚点均有对应目标，左侧当前页面导航高亮正常。
- 编辑入口指向对应文档的 GitHub 编辑 URL；问题反馈入口指向仓库的有效 Issue 模板 URL。
- Mermaid 页面实际加载 Mermaid 并生成 1 个 SVG。用临时浏览器测试页验证 MathJax 仅在出现 `.arithmatex` 时依次加载配置与引擎，并成功生成 `mjx-container`。
- 首页及 PETG 普通页面没有请求 MathJax 或 Mermaid 的第三方引擎。

### 字体 A/B 与交互

A 为当前 Material 字体栈，B 为通过 MiSans 官方 CSS/CDN 临时加载的 MiSans Variable。B 的字体面在浏览器中确认已加载，计算后的字体族为 `MiSans VF`。首页、PETG、Bambu Lab A1、PLA 的浅/深色及上述三个视口均已分别捕获 A/B 截图，共 48 张；截图保存在本次会话产物中，不加入仓库。

MiSans 官方 CSS 为 102,585 B；首页实际触发 18 个 WOFF2 子集，共 1,113,728 B。字体与 CSS 合计约 1.16 MiB，且许可仍未明确允许第三方网站嵌入；因此 B 仅作原型，不进入生产配置，也没有字体文件提交到仓库。

在原型中对首页知识卡片标题和主要操作按钮测试了 600 → 750、150 ms 的字重变化。1366 px 桌面样本中，卡片及按钮的边界框尺寸不变；这只是 MiSans 原型结果，生产站不启用该效果，以免当前字体栈无法保证连续字重轴。窄屏仍有完整的静态操作文字，不依赖悬停。

### 性能对比与限制

以本地预览首页的唯一资源 URL 和 `transferSize`/`encodedBodySize` 汇总 CSS、JavaScript：

| 指标 | 基线（PR #12 合并后的 `main`） | Stage 4C 当前 | 变化 |
|---|---:|---:|---:|
| CSS | 170,083 B | 172,418 B | +2,335 B |
| 首页 JavaScript | 1,103,494 B | 155,209 B | −948,285 B，约 −86% |
| 首页 MathJax / Mermaid 引擎 | 204,607 B + 745,043 B | 0 B + 0 B | 改为按需加载 |

CSS 增量包含新增的 758 B 字体 token 文件及相关局部样式。首页 JavaScript 当前总量包含 Material 主 bundle、搜索 bundle 和两个轻量按需加载器；MathJax 配置文件与两个图表引擎仅在对应内容需要时加载。上述资源字节基于本地预览，不代表公网压缩传输量。

性能目标为 LCP ≤ 2.5 s、INP ≤ 200 ms、CLS ≤ 0.1。本次集成浏览器报告 `document.visibilityState = hidden`，没有提供 LCP 条目或可用的事件计时条目；因此不能有效报告本轮 LCP/INP，也不把浏览器中观察到的 CLS 0 声明为 Core Web Vitals 达标。改动前已有一次无节流、1024 × 768 本地样本：LCP 228 ms、CLS 0；本轮无法获得同条件有效的 LCP 复测，不能据此作前后性能结论。当前单次导航 `loadEventEnd` 为 193 ms，它不是 LCP 的替代指标。

字体授权、MiSans/Noto Sans SC 字体量和性能目标的限制仍按上述结论处理：不全站启用中文网页字体，等待清晰的嵌入授权和可接受的实际用户设备测量后再决定。
