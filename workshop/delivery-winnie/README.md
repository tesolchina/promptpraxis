# Prompt & Praxis Entry 2 — Zotero 文献导入验收说明

亲爱的 Winnie：

这是为 Prompt & Praxis Entry 2（智能体文献检索工作坊）准备的 Zotero 实操验收材料包。数据源自腾讯 WorkBuddy 在 Windows 环境下对 OpenAlex 进行的真实联网检索（主题：*Automated Written Corrective Feedback*，2024 年至今，默认相关性排序）。

---

## 1. 目录结构与文件说明

材料包包含两条路线（Track A 与 Track B）各自生成的文献文件：

```text
delivery-winnie/
├── README.md               # 本说明文档
├── FEEDBACK_TEMPLATE.md    # 验收回填模板（填好后发回）
├── track-a/                # 路线 A：由 AI 依据自然语言提示从零编写代码生成的检索结果
│   ├── found.csv           # 【人工对照用】表格文件（用 Excel / Numbers / 纯文本打开）
│   ├── found.bib           # 【Zotero 导入用】标准 BibTeX 格式书目
│   └── found.ris           # 【Zotero 导入用】标准 RIS 格式书目
└── track-b/                # 路线 B：由 AI 驱动项目现成脚本 (fetch_literature.py) 生成的检索结果
    ├── found.csv           # 【人工对照用】表格文件
    ├── found.bib           # 【Zotero 导入用】标准 BibTeX 格式书目
    └── found.ris           # 【Zotero 导入用】标准 RIS 格式书目
```

### 关键区别：
- **`found.csv` 仅供人工核对对照**：请在 Excel、Numbers 或文本编辑器中打开，用来核对 Zotero 导入的字段是否准确完整。**请勿将 CSV 文件导入 Zotero**。
- **`found.bib` 与 `found.ris` 用于导入 Zotero**：这是两类标准学术引文交换格式。

---

## 2. 导入操作指引（保护个人文库）

为避免测试数据污染你现有的个人研究文献库，也为了清晰核验每种格式的导入条数（避免多格式混入同一分类造成重复计数）：

1. 打开桌面端 **Zotero Standalone**。
2. 在左侧文库树中，新建 **独立的测试分类（Collection）**：
   - 例如：`__Test_TrackA_Bib`、`__Test_TrackA_RIS`、`__Test_TrackB_Bib`、`__Test_TrackB_RIS`
3. 分别执行导入：
   - 菜单栏选择 **File（文件） → Import...（导入...）**。
   - 选择对应文件（如 `track-a/found.bib`）。
   - 弹窗中选择 **"Place items into a new collection"（放置到新建分类）** 或直接导入到刚刚建好的空分类中。
4. 确认条数：每个文件导入后应恰好显示 **5 条文献**。

---

## 3. 字段核对要点（对照 CSV）

请在 Zotero 中逐条检查 5 篇文献的右侧详情窗格，并与 `found.csv` 对照：

1. **标题（Title）**：标题文本是否完整清洁，无异常乱码或多余的转义符号（如双层花括号 `{{...}}`）。
2. **作者（Authors）**：作者姓名是否被正确切分（姓和名是否分别填入对应方框，未颠倒）。
3. **年份（Year）**：是否正确显示 2024、2025 或 2026 年。
4. **DOI**：是否显示标准 DOI 链接（如 `10.1057/s41599-024-03543-y`），且可点击访问。
5. **缺失作者记录的真实性**：
   - 第 2 条文献（BRILL 出版的书本章节：*Automated Written Corrective Feedback (AWCF)*）在 OpenAlex 原始数据库中就没有作者和摘要。
   - **正确表现**：导入 Zotero 后，该条目的**作者栏应保持完全留空**。
   - **错误表现**：若作者栏出现名为“Unknown”或“None”的虚构作者，则判定为格式缺陷。
6. **重要区别：关于 citekey 中的 Unknown**：
   - 在 Track B 的 `found.bib` 中，引用标识键（citekey）形如 `@article{Unknown2024Automated, ...}`。
   - **请注意：citekey 中的 `Unknown` 仅是 BibTeX 内部引用的键名占位符，不是文献的作者字段**。
   - 只要 Zotero 右侧面板里的“作者 / Creator”栏是干净的空白，就属于完全正常且正确，**切勿将 citekey 中的技术占位当作作者姓名错误**。
7. **关于全文 PDF 的提醒**：
   - 本次导入的是**书目引文元数据（Citation Metadata）**，**不代表已自动下载全文 PDF**。
   - 不需要测试付费墙下载，无需尝试点击下载 PDF。

---

## 4. 最小截图要求（用于交付验收证明）

测试过程中请保留 **3 张清晰截图**：

1. **CAP-01（导入步骤）**：导入文件选择对话框或导入确认弹窗截图。
2. **CAP-02（导入后的列表）**：Zotero 中间栏显示 5 条导入条目的列表视图（包含 Title、Creator、Year 等列）。
3. **CAP-03（缺失作者记录详情）**：选中第 2 条无作者文献（*Automated Written Corrective Feedback (AWCF)*），展示右侧详细元数据面板的完整截图（重点展示作者栏为空，未显示 Unknown）。

> **隐私保护提示**：截图时请裁切或打码个人 Zotero 账号邮箱以及个人私有分类名称。

---

## 5. 验收反馈模板

请将核对结果填写到本包内的 `FEEDBACK_TEMPLATE.md`（或直接复制下方模板回复）：

```markdown
### Winnie Zotero Desktop 验收反馈表

- **测试人员**：Winnie Bo
- **测试日期**：[YYYY-MM-DD]
- **Zotero 版本**：[例如 Zotero 7.0.11 / Zotero 6.x]
- **操作系统**：[macOS Sequoia / Windows 11 / 其他]

#### 1. Track A 测试结果
- **found.bib**：
  - 导入数量：[ 5 / 5 ]
  - 字段状态：[ PASS / FAIL ]
  - 缺失作者处理：[ 作者栏为空(正常) / 出现Unknown(异常) ]
  - 观察记录：
- **found.ris**：
  - 导入数量：[ 5 / 5 ]
  - 字段状态：[ PASS / FAIL ]
  - 缺失作者处理：[ 作者栏为空(正常) / 出现Unknown(异常) ]
  - 观察记录：

#### 2. Track B 测试结果
- **found.bib**：
  - 导入数量：[ 5 / 5 ]
  - 字段状态：[ PASS / FAIL ]
  - 缺失作者处理：[ 作者栏为空(正常) / 出现Unknown(异常) ]
  - 观察记录：
- **found.ris**：
  - 导入数量：[ 5 / 5 ]
  - 字段状态：[ PASS / FAIL ]
  - 缺失作者处理：[ 作者栏为空(正常) / 出现Unknown(异常) ]
  - 观察记录：

#### 3. 截图凭据保存路径
- CAP-01 导入步骤截图：`[路径或文件名]`
- CAP-02 导入列表截图：`[路径或文件名]`
- CAP-03 缺失作者详情截图：`[路径或文件名]`

#### 4. 总体结论与摩擦点记录
- **总体结论**：[ PASS / FAIL ]
- **任何异常提示或体验问题**：
```
