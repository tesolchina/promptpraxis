# 最小离线验收报告 — workbuddy-offline-20261111-234550

生成时间：2026-11-11 23:45:55 +0800（目录时间戳 `20261111-234550`）
仓库：`\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis`

## 0. 范围声明

- **本次三组运行全部使用离线 fixture（`--fixture` 读取本地 JSON），没有访问 OpenAlex，没有发出任何网络请求。**
- 未安装软件或依赖，未修改源代码，未提交或推送，未配置账号或连接器。
- 所有输出仅写入本目录 `workshop\test-output\workbuddy-offline-20261111-234550\`。

## 1. 环境与解释器

| 项 | 实际观察 |
|---|---|
| 执行 shell | Windows NT 上的 MINGW64/Git Bash（`uname -a`: `MINGW64_NT-10.0-26300 ZA-G17 3.6.9-... x86_64 Msys`），**不是** WSL 发行版内部 shell |
| 当前目录 (bash cwd) | `//wsl.localhost/Ubuntu/home/andy/projects/promptpraxis` |
| 解释器（Windows 路径） | `C:\Users\andy\.workbuddy-ai\binaries\python\versions\3.13.12\python.exe` |
| 解释器（bash 调用形式，同一文件） | `/c/Users/andy/.workbuddy-ai/binaries/python/versions/3.13.12/python.exe` |
| 版本 | `Python 3.13.14`（`--version` 实测；目录名 `3.13.12` 与自报版本不一致，如实记录，未做任何处理） |
| 路径形式 | 脚本、fixture、输出均使用 Windows UNC 绝对路径 `\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\...` |
| 参数保护 | 每次调用前置 `MSYS2_ARG_CONV_EXCL='*'`，避免 MSYS 改写 UNC 参数 |
| 字节码 | 所有 Python 调用均带 `-B` |

未切换到 WSL 内 Linux Python。

## 2. 参数确认依据（读源码，未猜参数）

- `fetch_literature.py` → `query_openalex(..., fixture_path=None)`：当 `fixture_path` 为真时执行 `open(fixture_path, "r", encoding="utf-8")` + `json.load(f)` 并立即返回，**不构造 URL、不调用 `urllib.request.urlopen`**。
- `fetch_literature.py` → `argparse` 定义：`--topic`、`--year`、`--sort`、`--limit`、`--email`、`--output-csv`、`--output-bib`、`--output-ris`、`--fixture`。本次只显式传 `--fixture` 与三个 `--output-*`，其余使用脚本默认值（离线分支下不产生网络请求）。
- `verify_zotero_import.py` → `argparse` 定义：`--bib`、`--ris`；脚本只读文件、不写文件、不联网。

## 3. 输出目录

```
workshop/test-output/workbuddy-offline-20261111-234550/
├── acceptance.md            （本文件）
├── normal/                  （openalex_normal.json）
├── empty/                   （openalex_empty.json）
└── missing_metadata/        （openalex_missing_metadata.json）
```

创建前 `workshop/test-output` 不存在（`ls` 报 `No such file or directory`），本次新建，未覆盖 `sample-data/` 或任何既有输出。每组输出位于独立子目录。

## 4. 实际执行的命令

公共形式（下列三组只有 `--fixture` 文件名与输出子目录不同；`normal` 组以字面量路径执行，`empty`/`missing_metadata` 组由 shell 变量展开为同样的路径）：

```
MSYS2_ARG_CONV_EXCL='*' '/c/Users/andy/.workbuddy-ai/binaries/python/versions/3.13.12/python.exe' -B \
  '\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\fetch_literature.py' \
  --fixture '<FIXTURE>' \
  --output-csv '<GROUP_DIR>\found.csv' \
  --output-bib '<GROUP_DIR>\found.bib' \
  --output-ris '<GROUP_DIR>\found.ris'
```

三组具体值（其余参数全部一致）：

| 组 | `<FIXTURE>` | `<GROUP_DIR>` |
|---|---|---|
| normal | `\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\tests\fixtures\openalex_normal.json` | `\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-offline-20261111-234550\normal` |
| empty | `\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\tests\fixtures\openalex_empty.json` | `...\workshop\test-output\workbuddy-offline-20261111-234550\empty` |
| missing_metadata | `\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\tests\fixtures\openalex_missing_metadata.json` | `...\workshop\test-output\workbuddy-offline-20261111-234550\missing_metadata` |

格式校验命令（三组各一次，指向本组的 `found.bib` / `found.ris`）：

```
MSYS2_ARG_CONV_EXCL='*' '/c/Users/andy/.workbuddy-ai/binaries/python/versions/3.13.12/python.exe' -B \
  '\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\verify_zotero_import.py' \
  --bib '<GROUP_DIR>\found.bib' --ris '<GROUP_DIR>\found.ris'
```

每组 `fetch.log` / `verify.log` 保存了该次运行的完整 stdout+stderr。

## 5. 退出码

| 组 | fetch_literature.py | verify_zotero_import.py |
|---|---|---|
| normal | 0 | 0 |
| empty | 0 | 0 |
| missing_metadata | 0 | 0 |

## 6. 实际输出逐项核对（打开文件读取内容，不是只看退出码或文件存在）

### 6.1 normal（fixture `meta.count=3`，`results` 3 条）

CSV 数据行 3 行、BibTeX `@article` 3 条、RIS `TY/ER` 记录 3 条，三者记录数一致。逐条与 fixture 对照：

| # | OpenAlex ID | 标题 | 作者 | 年份 | DOI（fixture 值） | 三份输出核对 |
|---|---|---|---|---|---|---|
| 1 | W4414939355 | Qwen3 Technical Report | An Yang; Baosong Yang | 2025 | `https://doi.org/10.48550/arxiv.2505.09388` | 一致 |
| 2 | W4414281281 | DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning | Daya Guo; Dejian Yang | 2025 | `https://doi.org/10.1038/s41586-025-09422-z` | 一致 |
| 3 | W4362515116 | A Survey of Large Language Models | Wayne Xin Zhao; Kun Zhou | 2026 | `https://doi.org/10.1007/s11704-026-60308-3` | 一致 |

细节：CSV 的 DOI 保留完整 `https://doi.org/...`，作者以 `; ` 连接，Year/Citations/Journal 与 fixture 一致（17561/16737/8505；arXiv (Cornell University) / Nature / Frontiers of Computer Science），`Reading_Status=Unread`、`Notes` 空。BibTeX 的 citekey 为 `Yang2025Qwen3`、`Guo2025Deepseekr1`、`Zhao2026A`；`doi` 为去掉 `https://doi.org/` 前缀的标识符，`url` 保留原值，`note` 保留 OpenAlex ID。RIS 的 `DO` 为去前缀标识符、`UR` 为原值、`N1` 为 OpenAlex ID。**结论：3/3 条，标题、作者、年份、DOI 与 fixture 逐项一致。**

### 6.2 empty（fixture `meta.count=0`，`results=[]`）

- 脚本 stdout：`OpenAlex reports 0 matching records in database.` / `Notice: Query returned 0 records. Generating empty output templates.`
- `found.csv`：仅 1 行表头（75 bytes），**无数据行**。
- `found.bib`：仅注释行 `% Generated by Prompt & Praxis literature pipeline` 与空行（54 bytes），**无 `@article` 条目**。
- `found.ris`：**0 字节空文件**（读取工具返回空内容提示）。
- 格式校验：BibTeX PASS 0 records、RIS PASS 0 records，退出码 0。

**结论：空结果生成空模板而非报错，三份文件均为 0 条记录。**

### 6.3 missing_metadata（fixture `meta.count=2`）

记录 1 `W9999999991`（fixture：doi `null`、year `null`、cited `null`、`primary_location` `null`、`oa_url` `null`、`authorships` `[]`、title `Early Working Paper on Syntax`）：

- CSV：`Authors=Unknown` —— **这是脚本写入的字面量占位符，不是"原字段保持空白"**；`Year`、`Citations`、`DOI`、`Journal` 为空字段；`Reading_Status=Unread`。
- BibTeX：citekey `UnknownndEarly`（由 `Unknown` + `nd` + 标题首词拼成），`author = {Unknown}` —— **同样是占位符**；没有 `year`、`doi`、`url`、`journal` 行；保留 `note = {OpenAlex: ...}`。
- RIS：只有 `TI`、`N1`、`ER`；没有 `AU`、`PY`、`DO`、`UR`、`JO` 行。
- 终端摘要打印 `Authors: Unknown | Citations: None | DOI: None`（`None` 是 Python 值在 stdout 的字符串化，不是文件内容）。

记录 2 `W9999999992`（fixture：year 2023、cited 0、doi `https://doi.org/10.1234/test.5678`、作者 Jane Doe、`primary_location.source` 为 `null` 即期刊缺失）：

- CSV：`Authors=Jane Doe`、`Year=2023`、`Citations=0`（原值 0 按原值写出）、`DOI` 完整 URL、`Journal` 空字段。
- BibTeX：citekey `Doe2023Incomplete`，有 `year {2023}`、`doi {10.1234/test.5678}`、`url` 原值；无 `journal` 行。
- RIS：有 `TY/TI/AU/PY/DO/UR/N1/ER`；无 `JO` 行。

**结论：缺失字段并非统一"保持空白"——作者缺失被替换为 `Unknown` 占位符（CSV 与 BibTeX 均是），citekey 中出现 `Unknown`/`nd`；年份、引用数、DOI、期刊在 CSV 里是空字段，在 BibTeX/RIS 里是直接省略整行；`0` 引用数按原值写出。**

## 7. 格式校验的性质（步骤 5）

对三组输出分别运行了项目现有的 `verify_zotero_import.py`，结果：normal PASS 3/3、empty PASS 0/0、missing_metadata PASS 2/2，退出码均为 0。

**明确说明：这只是项目自带的正则/结构格式检查（UTF-8、括号平衡、记录边界、作者分隔、字段存在性、citekey 唯一性），不是真实 Zotero 导入，未启动 Zotero、未调用其 import translator。** 在 missing_metadata 组，脚本打印第 1 条 `Year=False`、RIS `Authors=0, Year=None, DOI=None`，仍返回 PASS —— 说明该自写校验不会因字段缺失而判失败。

## 8. UNC 读写与失败信息

- **UNC 读写成功**：`mkdir -p` 创建 4 个目录；Windows 原生 Python 3.13.14 经 `\\wsl.localhost\Ubuntu\...` 成功读取 `fetch_literature.py`、`verify_zotero_import.py` 与 3 个 fixture，成功写出 9 个输出文件。**未出现任何 UNC 路径错误、PermissionError 或 FileNotFoundError，原始报错为空。** 未为绕过问题而迁移仓库、改源码或安装任何东西。
- 只读探测 `git status --porcelain` 时遇到既有 git 安全策略报错，原样保留（未添加 `safe.directory`、未修改 git 配置、未提交或推送）：

```
fatal: detected dubious ownership in repository at '//wsl.localhost/Ubuntu/home/andy/projects/promptpraxis'
'//wsl.localhost/Ubuntu/home/andy/projects/promptpraxis' may refer to a non-local directory
To add an exception for this directory, call:

	git config --global --add safe.directory '%(prefix)///wsl.localhost/Ubuntu/home/andy/projects/promptpraxis'
```

- 既存字节码（**非本次生成**）：`workshop/__pycache__/fetch_literature.cpython-314.pyc`、`verify_zotero_import.cpython-314.pyc`（mtime 22:32:12）、`workshop/zotero-spike/__pycache__/zotero_formatter.cpython-314.pyc`（mtime 22:34:51）；均为 cpython-314，早于本次运行（23:45 之后），本次 `-B` 未生成新 pyc。
- 写入范围核查：`find -newermt '2026-11-11 23:45:00'` 列出的 15 个文件全部位于本输出目录内；`sample-data/` 三个文件 mtime 均为 22:33:02，未被覆盖。

## 9. 尚未验证的环节

- 真实 OpenAlex 联网查询：DNS/代理/连通性、30s 超时、HTTP 429、polite pool 与默认 `--email andyzheng0715@example.com` 是否可用 —— 本次按要求全部离线，未访问 OpenAlex。
- 真实 Zotero 客户端导入及其 import translator —— 未做，只跑了项目自带格式检查。
- `tests/test_workshop.py` 自动化测试套件、`verify_zotero_import.py` 之外的脚本、`zotero-spike/`、`prompts/`、`sample-data/` 内容一致性、README 中列出的其他 Quick Start —— 未执行。
- WSL Ubuntu 内部的 Linux Python 与其他解释器 —— 未使用、未探测。
- 默认相对输出路径（写到仓库根/当前目录）的场景、以及 Windows 侧 Office / 腾讯文档打开这些文件的表现 —— 未测试。
- 编码、换行、超长字段、非 ASCII 作者名等边界情况 —— 未测试。

## 10. 本次输出文件清单

```
normal/fetch.log  normal/verify.log  normal/found.csv  normal/found.bib  normal/found.ris
empty/fetch.log   empty/verify.log   empty/found.csv   empty/found.bib   empty/found.ris
missing_metadata/fetch.log  missing_metadata/verify.log
missing_metadata/found.csv  missing_metadata/found.bib  missing_metadata/found.ris
acceptance.md（本文件）
```
