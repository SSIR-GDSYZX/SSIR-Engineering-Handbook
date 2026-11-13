---
title: 普通文档页面视觉与图片规范
category: Organization
status: draft
owner: SSIR
last_reviewed: YYYY-MM-DD
---

# 普通文档页面视觉与图片规范

本规范将手册现有的 Industrial Editorial 视觉语言延伸到知识页面。工程内容优先；装饰不得影响阅读、导航或交互。

## 视觉规则

- **颜色**：沿用现有黑、白、灰与信号黄。黄色用于少量行动或状态强调，不作为大面积底色或浅底文字色。
- **文字**：复用 Material 当前字体栈，并通过 `static/stylesheets/typography.css` 统一字体回退和字重 token。分类标题采用 750–800 字重；文档 H1 为 30–36 px、700 字重；H2 为 23–27 px、600 字重；H3 为 18–21 px、600 字重；正文 15–17 px、行高 1.65–1.8；技术标签 11–12 px 等宽字体；表格 13–14 px。MiSans Variable 已完成授权与加载性能审计，暂不启用；详见[字体与性能审计](typography-and-performance.md)。
- **页面头部**：显示面包屑、分类标签、文档标题、状态及可用的编辑入口。标题不做高幅 Banner；如需副标题，在 Markdown 标题后以正文段落表达。编辑入口使用 MkDocs 生成的 GitHub 编辑地址。
- **层级**：保留 Markdown 标题及其自动锚点。使用字号、字重和间距区分 H1/H2/H3，右侧目录继续由 Material 按原文档标题生成。
- **导航**：当前页通过字重和中性色竖条标示；Material 原生多级目录、缩进和当前目录跟踪逻辑保持不变。
- **响应式**：正文图片最大宽度为容器宽度并保持原比例；表格在窄屏可横向滚动；照片组在窄屏改为单列。装饰层不参与内容布局。
- **交互与无障碍**：编辑及反馈链接使用真实地址并可键盘聚焦；页面支持浅色、深色、高对比和减少动态效果设置。等高线只作装饰，不能传递信息。

上面的字号范围是本项目的实施目标（并与 Stage 4B 需求一致），不是对参考网站的实测声明。参考文档将部分颜色和尺寸标为实测，将字号、组件间距、断点及等高线强度中的若干建议标为推断或建议；两者不可混为一谈。

## 参考依据

- [设计总纲与六条原则](https://icaruszezen.github.io/endfield-ui/design/overview/)：中性色为主体、信号色克制、内容偏心、纹理有预算。
- [官网表面规范](https://icaruszezen.github.io/endfield-ui/design/surfaces/website/)：官网语气以纸白、墨色、少量黄色、直角和大留白为主。来源标记为实测。
- [色彩规范](https://icaruszezen.github.io/endfield-ui/design/foundations/color/)：`#FFFA00` 为参考中的信号黄实测值；其浅底对比度不足，不作为白底正文色。
- [字体规范](https://icaruszezen.github.io/endfield-ui/design/foundations/typography/)：中文负责阅读、英文技术标签负责结构；正文 16 px 和行高 1.6 是参考文档给出的建议，不是官网实测字号。
- [布局与空间](https://icaruszezen.github.io/endfield-ui/design/foundations/layout/)：使用固定字号与断点、长文本布局加入 `min-width: 0` 等建议标记为推断。
- [形状规范](https://icaruszezen.github.io/endfield-ui/design/foundations/shape/)：默认直角，细线和局部强调优先于大量圆角卡片。
- [按钮规范](https://icaruszezen.github.io/endfield-ui/design/components/button/)：参考行动按钮高度建议为 40 px；本项目编辑按钮采用约 38 px 高度，属于本项目实现值。
- [导航规范](https://icaruszezen.github.io/endfield-ui/design/components/navigation/)：当前项应清晰可辨，当前状态不只依赖颜色。
- [卡片规范](https://icaruszezen.github.io/endfield-ui/design/components/card/)：卡片克制使用，靠底色与分隔线组织内容。
- [纹理规范](https://icaruszezen.github.io/endfield-ui/design/foundations/texture/) 与 [网格、等高线、点阵](https://icaruszezen.github.io/endfield-ui/design/elements/grid-contour-dots/)：纹理应弱于文字、不可拦截交互，并在高对比或打印时隐藏；参考中的等高线强度属于建议/推断，不是本项目测量值。

本项目的等高线 SVG 是原创曲线，不描摹游戏截图、地图、标志或其他现成资产。它仅出现在分类索引页头部；长篇正文不铺设背景纹理。

## 文档图片管理

### 素材边界

- 优先使用经授权、可公开的 SSIR 实拍，并由贡献者确认照片中没有个人信息、内部记录或不应公开的内容。
- 不得把网络图片描述为 SSIR 设备或库存现状；不得用 AI 生成图冒充真实设备、储存环境、材料或打印样件。
- 当前没有提交实拍素材。缺少照片时页面保持完整，不放破损链接、假缩略图或装饰性占位图。
- 所有图片必须有准确的替代文本（Alt Text）和说明文字；纯装饰图的替代文本留空并明确标为装饰。

### 建议目录与命名

3D 打印照片建议存放在 `docs/assets/images/3d-printing/`。文件名使用小写英文和连字符，并描述内容；以下名称仅为未来命名建议，不代表这些照片已经存在：

| 类别 | 未来文件名示例 |
|---|---|
| 设备 | `bambu-a1-overview.webp` |
| 储存 | `filament-dry-storage.webp`、`filament-dryer.webp` |
| 材料 | `pla-spools.webp`、`petg-spools.webp` |
| 技术样件 | 用材料、样件或缺陷名称命名，例如 `petg-stringing-sample.webp` |

优先采用经过适度压缩的 WebP；保留原始比例，避免不必要的大图和重复副本。只有获得实际照片后才在页面中加入对应链接。

### Markdown 与说明文字

普通 Markdown 图片语法继续有效，容器会限制图片最大宽度且不拉伸：

```markdown
![Bambu Lab A1 正面实拍，展示打印机外观](../images/3d-printing/bambu-a1-overview.webp)

*Bambu Lab A1 正面实拍。*
```

多张同类照片需要并排展示时，可用 `.handbook-photo-grid` 和 `.handbook-photo` 包裹真实图片；缺少素材时不要创建空白图片组件：

```html
<div class="handbook-photo-grid">
  <figure class="handbook-photo">
    <img src="../images/3d-printing/filament-dryer.webp"
         alt="耗材烘干机实拍，设备型号待核实"
         loading="lazy">
    <figcaption>实际设备照片；型号与使用条件以核实后的说明为准。</figcaption>
  </figure>
</div>
```

移动端自动单列。不得为照片样式改变 Markdown 图片链接、裁切原图来隐藏重要信息，或省略图片说明。
