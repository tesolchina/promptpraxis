# Winnie Zotero Desktop 验收反馈表

请在此模板中填写 Zotero 实操验收结果，完成后连同截图返回给 Andy。

---

## 基本信息

- **测试人员**：Winnie Bo
- **测试日期**：[ 例如：2026-11-12 ]
- **Zotero 版本**：[ 例如：Zotero 7.0.11 / Zotero 6.0.37 ]
- **操作系统**：[ 例如：macOS 15.1 / Windows 11 23H2 ]

---

## 1. Track A 测试结果（自然语言从零生成）

### A. `track-a/found.bib` (BibTeX)
- **导入数量**：[  / 5 ]
- **字段核对（Title/Year/DOI）**：[ PASS / FAIL ]
- **作者姓名切分（姓/名）**：[ 正确 / 颠倒 / 异常 ]
- **第 2 条缺失作者处理**：[ 作者栏完全留空 (PASS) / 出现 Unknown 姓名 (FAIL) ]
- **问题与备注**：

### B. `track-a/found.ris` (RIS)
- **导入数量**：[  / 5 ]
- **字段核对（Title/Year/DOI）**：[ PASS / FAIL ]
- **作者姓名切分（姓/名）**：[ 正确 / 颠倒 / 异常 ]
- **第 2 条缺失作者处理**：[ 作者栏完全留空 (PASS) / 出现 Unknown 姓名 (FAIL) ]
- **问题与备注**：

---

## 2. Track B 测试结果（现成脚本运行）

### A. `track-b/found.bib` (BibTeX)
- **导入数量**：[  / 5 ]
- **字段核对（Title/Year/DOI）**：[ PASS / FAIL ]
- **作者姓名切分（姓/名）**：[ 正确 / 颠倒 / 异常 ]
- **第 2 条缺失作者处理**：[ 作者栏完全留空 (PASS) / 出现 Unknown 姓名 (FAIL) ]
- **关于 citekey 说明**：citekey 形如 `@article{Unknown2024Automated, ...}` 属于技术键名占位符，右侧作者栏为空即为正常。
- **问题与备注**：

### B. `track-b/found.ris` (RIS)
- **导入数量**：[  / 5 ]
- **字段核对（Title/Year/DOI）**：[ PASS / FAIL ]
- **作者姓名切分（姓/名）**：[ 正确 / 颠倒 / 异常 ]
- **第 2 条缺失作者处理**：[ 作者栏完全留空 (PASS) / 出现 Unknown 姓名 (FAIL) ]
- **问题与备注**：

---

## 3. 验收截图凭据

请在此附上或注明保存的 3 张截图路径：

1. **CAP-01 导入步骤截图**（导入文件选择或选项弹窗）：
   - 文件路径/名称：`screenshots/cap-01-import-dialog.png`
2. **CAP-02 导入后的列表截图**（显示 5 条记录列表）：
   - 文件路径/名称：`screenshots/cap-02-collection-view.png`
3. **CAP-03 缺失作者条目详情截图**（第 2 条无作者文献的右侧详情窗格）：
   - 文件路径/名称：`screenshots/cap-03-missing-author-detail.png`

---

## 4. 总体结论

- **验收结论**：[ PASS / FAIL ]
- **体验与摩擦点记录**（如有任何导入报错弹窗、警告或显示异常，请在此粘贴说明）：
