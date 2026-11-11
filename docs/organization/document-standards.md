---
title: 文档规范
category: Organization
status: draft
owner: SSIR
last_reviewed: YYYY-MM-DD
---

# 文档规范

## 元数据

每篇文档应在文件开头使用以下 YAML 元数据。`last_reviewed` 使用 ISO 日期格式；尚未审核时保留 `YYYY-MM-DD` 占位符，并保持 `status: draft`。

```yaml
---
title: Document Title
category: General
status: draft
owner: SSIR
last_reviewed: YYYY-MM-DD
---
```

状态只能使用：

- `draft`：草稿，尚未完成审核。
- `review`：正在审核。
- `approved`：已由适当负责人审核批准。

模板示例中的字段值和方括号内容均需按实际情况替换；示例不代表真实组织资料。

## 写作与发布

- 使用清晰、可移植的 Markdown，避免把正文绑定到特定主题的短代码。
- 说明版本、单位、适用条件、复现步骤及可核实的资料来源。
- 不编造组织信息、设备型号、人员或项目数据。
- 发布前确认公开范围；不提交个人资料、内部资产清单、采购信息、访问凭据或未获授权的数据。
- 安全及操作类内容在获得审核前不得标记为 `approved`。
- 如适用，记录复核日期；内容发生重大变化时重新审核。
