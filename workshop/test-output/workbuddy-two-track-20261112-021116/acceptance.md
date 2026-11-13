# 最终双轨验收报告 — workbuddy-two-track-20261112-021116

生成时间：2026-11-12（本地 +0800）；输出目录标签 `20261112-021116`
仓库：`\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis`

## 0. 范围与边界

- 统一查询：主题 `automated written corrective feedback`，2024 年至今（`from_publication_date:2024-01-01`，未设上界），**默认相关性排序（两次请求 URL 均不含 `sort`）**，最多 5 条（`per-page=5`）。
- 沿用已验证的 Windows Python + WSL UNC 环境；允许查询 OpenAlex、执行代码、创建独立验收产物。
- 未安装依赖、未修改项目源码、未提交推送、未操作 Zotero；两次请求均未发送邮箱、`mailto`、`api_key` 或任何凭据，也未使用离线 fixture 冒充联网结果。
- 目录：`workshop/test-output/workbuddy-two-track-20261112-021116/`，下分 `track-a/`、`track-b/`；历史材料未覆盖。
- **执行顺序**：Track A 全部产物保存完成（02:14–02:15）之后，才读取并解释 `workshop/fetch_literature.py`（02:16），随后才执行 Track B。Track A 未读取、导入、运行或复制该脚本，也未使用旧响应或 `sample-data`。

已读材料：`docs/workbuddy-two-track-acceptance.md`、`docs/review-followup.md`（含 01:55 最新第 7 节修改记录）、`workshop/test-output/workbuddy-example-20261112-005622/acceptance.md`。

## 1. 环境与解释器

| 项 | 实际观察 |
|---|---|
| 执行 shell | Windows NT 上的 MINGW64/Git Bash，经 `\\wsl.localhost\Ubuntu\...` 访问 WSL2 文件系统 |
| 解释器 | `C:\Users\andy\.workbuddy-ai\binaries\python\versions\3.13.12\python.exe`（bash 形式 `/c/Users/andy/.workbuddy-ai/binaries/python/versions/3.13.12/python.exe`） |
| 版本 | `Python 3.13.14` |
| 调用约定 | `MSYS2_ARG_CONV_EXCL='*'`；所有 Python 调用带 `-B`；路径为 Windows UNC |

## 2. Track A（独立实现，一次真实请求）

在 `track-a/track_a_run.py` 内**自行编写**标准库实现（不引用项目脚本）。按文档自然语言提示：Step A1 三点计划记录于 `planning_notes.md`（用户本轮已统一授权执行，未模拟交互式暂停，也未声称有聊天记录）；Step A2 输出 Markdown 表格 `results_table.md`；Step A3 生成 `found.csv` / `found.bib` / `found.ris` 与 `run_log.txt`（记录精确 API URL 和时间戳）。

命令（完整版见 `command.txt`）：

```
MSYS2_ARG_CONV_EXCL='*' '/c/Users/andy/.workbuddy-ai/binaries/python/versions/3.13.12/python.exe' -B '\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-two-track-20261112-021116\track-a\track_a_run.py'
```

| 项 | 实际值 |
|---|---|
| 请求 | `GET https://api.openalex.org/works?search=automated+written+corrective+feedback&filter=from_publication_date%3A2024-01-01&per-page=5` |
| 参数 | `search / filter / per-page`；`query_contains_sort=false`、`mailto=false`、`api_key=false` |
| 请求头 | `User-agent: PromptPraxisWorkshop/1.0`；timeout 30s |
| 请求时间 | `2026-11-11T18:14:40.471651Z`；响应头 `Date: Wed, 11 Nov 2026 18:14:41 GMT` |
| 运行区间 | 开始 `02:14:23 +0800` / `18:14:34Z`，结束 `02:14:59` / `18:15:10Z` |
| 结果 | `HTTP 200`、`TRACK_A_EXIT=0`、无 stderr 错误；`raw_response.json` 83958 字节 |
| 响应元数据 | `meta.count=11915`、`x_query.order="best matches first"`、`order_default=true` |

导出规则（本次自写）：CSV 九列 `OpenAlex_ID,Title,Authors,Year,Citations,DOI,Journal,Reading_Status,Notes`（`Reading_Status=Unread`、`Notes` 空）；**无作者时 CSV `Authors` 写空字符串、BibTeX 省略整个 `author` 行、RIS 不产生 `AU` 行**；citekey 用 `Ref` 作无作者占位，不编造元数据。所有导出行均从本次保存的 `raw_response.json` 重新读取生成。

## 3. Track B（现成脚本，一次真实请求）

A 产物保存完成后读取 `workshop/fetch_literature.py`（mtime 2026-11-12 01:55:23，12247 字节，本轮未修改）。面向初学者的解释见 `track-b/script_explanation.md`，要点：脚本用标准库查询 OpenAlex Works 并导出 CSV/BibTeX/RIS，支持 `--fixture` 离线模式；参数含 `--topic/--year/--sort/--limit/--email/--output-*/--fixture`；缺失字段保持为空。

**`--sort relevance` 实现确认**（第 88–96 行）：`params` 初始为 `search / filter / per-page`，仅当 `if sort and sort != "relevance"` 时才写入 `sort`；因此传 `relevance` **不发送 sort 参数**。`mailto` 仅在 `--email` 非空时加入，`--email=` 使 URL 与请求头都不带邮箱/凭据（第 95–96、101 行）。空作者处理：`write_csv` 写 `""`（185 行）、`write_bibtex` 省略 `author` 行（208–210 行）、`write_ris` 不写 `AU` 行。

命令（完整版见 `command.txt`）：

```
MSYS2_ARG_CONV_EXCL='*' '/c/Users/andy/.workbuddy-ai/binaries/python/versions/3.13.12/python.exe' -B '\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-two-track-20261112-021116\track-b\audit_run.py' --topic 'automated written corrective feedback' --year 2024 --sort relevance --limit 5 --email= --output-csv '<...>\track-b\found.csv' --output-bib '<...>\track-b\found.bib' --output-ris '<...>\track-b\found.ris'
```

`track-b/audit_run.py` 仅 tee 本次响应并转发参数给 `runpy.run_path(项目脚本, run_name="__main__")`，不改源码、不改请求或解析行为。

| 项 | 实际值 |
|---|---|
| 请求 | `GET https://api.openalex.org/works?search=automated+written+corrective+feedback&filter=from_publication_date%3A2024-01-01&per-page=5` |
| 参数 | 与 A 完全一致；`query_contains_sort=false`、`mailto=false`、`api_key=false` |
| 请求头 | `User-agent: PromptPraxisWorkshop/1.0`；timeout 30s |
| 请求时间 | `2026-11-11T18:17:17.495306Z`；响应头 `Date: Wed, 11 Nov 2026 18:17:18 GMT` |
| 运行区间 | 开始 `02:17:00 +0800` / `18:17:11Z`，结束 `02:17:35` / `18:17:46Z` |
| 结果 | `HTTP 200`、`TRACK_B_EXIT=0`、`Mode: Live OpenAlex API ()`（email 为空）、`Sort: relevance`、`Parsed 5 publications.`；`raw_response.json` 83958 字节 |
| 响应元数据 | `meta.count=11915`、`x_query.order="best matches first"`、`order_default=true` |

## 4. 验收逐项结果（证据：`cross_check.txt`、`response_diff.txt`、`run_summary.txt`、各轨 `verify.log`）

**① 两轨输出 vs 各自原始响应：均通过。** A、B 各为 `results=5 / CSV 5 行 / BibTeX 5 条 / RIS 5 条`；逐条比较 `OpenAlex_ID / Title / Authors / Year / Citations / DOI / Journal` 共 7 字段 × 5 条 × 2 轨，全部 `match=True`（`CSV field-by-field ALL MATCH: True`）。

**② 两次实际请求均未发送 sort，查询条件一致：通过。** 两份 `request_meta.json` 的 URL **完全相同**、query_params 完全相同、请求头完全相同；`query_contains_sort/mailto/api_key` 六项全为 `false`；两者 `HTTP 200`，响应 `x_query.order="best matches first"`、`order_default=true`。两次各只发一次请求，无重试、无第二次补请求。

**③ A/B 书目比较：完全一致（无需调和）。** 响应 ID 序列相同，5 条记录的 OpenAlex ID、标题、作者、年份、DOI（以及引用数、期刊、Reading_Status、Notes）零差异；`found.csv` 与 `found.ris` **逐字节相同**。

- `found.bib` 不逐字节相同（A 2005 B / B 2006 B），差异仅在两处非书目内容：文件首行注释（A 为 `% Track A generated...`，B 为 `% Generated by Prompt & Praxis literature pipeline`），以及第 2 条无作者记录的 citekey（A `Ref2024Automated` vs B `Unknown2024Automated`）。字段内容一致，文档亦说明不要求逐字节相同。
- **两份 `raw_response.json` 并非字节相同，已按要求先调查**：解析后仅 2 个叶节点不同 —— `/meta/db_response_time_ms`（A 390 / B 203）与 `/results/3/relevance_score`（A 233.04147 / B 233.67732）。二者都是服务端动态性能/评分值，请求条件完全一致，书目字段无变化；属数据/服务端波动，**未强行改成一致**，也未改任何输出去迎合。

**④ 格式检查器：两轨均通过，但不代表 Zotero 导入通过。** `verify_zotero_import.py` 对 A/B 各运行一次，`VERIFY_track-a_EXIT=0`、`VERIFY_track-b_EXIT=0`，均返回 `[PASS] BibTeX 5 records` / `[PASS] RIS 5 records`；第 2 条（无作者）显示 `Author=False` / `Authors=0` 但仍 PASS。**这仅是项目自带的正则/结构语法检查，未启动 Zotero、未调用其 import translator、未做桌面导入。**

**⑤ 缺失作者未变成名为 Unknown 的作者：导出文件中通过，但有两处字样残留需如实说明。**

| 检查 | A | B |
|---|---|---|
| CSV `Authors` 含 `Unknown` | 否（空字符串） | 否（空字符串） |
| BibTeX 含 `author = {Unknown}` | 否（省略该行） | 否（省略该行） |
| RIS 含 `AU  - Unknown` | 否（无 AU 行） | 否（无 AU 行） |
| 含 `Unknown` 的 citekey | 无（`Ref2024Automated`） | **有：`Unknown2024Automated`** |
| 终端日志含 `Authors: Unknown` | 否 | **有（脚本第 320 行打印文本）** |

B 轨这两处 "Unknown" 分别是 `generate_citekey()` 的技术占位符（脚本第 55 行）与控制台摘要字符串，**不是导出文件里的作者字段**；本轮未修改源码，故原样保留、如实记录。若要求连 citekey/终端都不出现该字样，需要改源码，属本轮边界之外。

**失败信息**：两次请求 `error entries` 均为空，无 401/403/429、网络或认证错误，无 stderr 异常，退出码全为 0；未触发"保留现场并停止"的失败分支，未用 fixture 替代联网结果。

## 5. 给 Winnie 的六个导出文件（准确绝对路径）

```
\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-two-track-20261112-021116\track-a\found.csv
\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-two-track-20261112-021116\track-a\found.bib
\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-two-track-20261112-021116\track-a\found.ris
\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-two-track-20261112-021116\track-b\found.csv
\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-two-track-20261112-021116\track-b\found.bib
\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-two-track-20261112-021116\track-b\found.ris
```

六个文件均实际存在（1238 / 2005 / 1686 / 1238 / 2006 / 1686 字节），且各自通过格式检查。**Winnie 的导出材料齐备**（就六个文件而言）。

## 6. 剩余阻塞与未验证环节

- **桌面 Zotero 实际导入未做**（本轮禁止操作 Zotero）；格式检查仅是语法层面，不能当作导入通过。
- 未打开任何 DOI / OA / PDF 链接，全文可下载性与付费墙仍未验证。
- Track A Step A1 的"三点计划后暂停等待确认"未在真实 GUI 对话中执行（本轮由用户统一指令直接授权，以 `planning_notes.md` 记录）；文档要求的聊天记录、点击 DOI 的浏览器验证、7 张桌面 UI 截图仍缺。
- B 轨 citekey 与终端摘要仍含 "Unknown" 字样（非作者字段，见 ⑤），消除需改源码，本轮未改。
- 两份原始响应存在 2 处非书目差异（已归因，非阻塞）；OpenAlex 数据随时间可能变化，本报告结论只对 18:14:41 / 18:17:18 GMT 两份响应成立。
- `docs/review-followup.md` 第 6 节的其他事项（真实 WorkBuddy GUI 双轨、文章裁剪至 ≤1550 词、协作者权限）不属于本轮范围，仍未完成。

## 7. 写入范围核查

`find -newermt '2026-11-12 02:11:00'` 列出的文件**全部**位于本次 `workbuddy-two-track-20261112-021116/` 目录内。`workshop/fetch_literature.py`（01:55:23）、`workshop/verify_zotero_import.py`（前日 20:31）、`docs/workbuddy-two-track-acceptance.md`（01:57:04）、`docs/review-followup.md`（01:58:35）、`workshop/sample-data/sample-found.csv`（前日 22:33）mtime 均未变。`workshop` 下 `cpython-314.pyc` 时间戳为前日 22:32/22:34 与今日 01:56/01:58（均早于本轮 02:11，非本次产生）；本轮所有 Python 调用带 `-B`，未生成新字节码。

## 8. 文件清单

```
acceptance.md（本文件）  command.txt  cross_check.txt  response_diff.txt  run_summary.txt  verify_exits.txt
track-a/  track_a_run.py  planning_notes.md  results_table.md  run_log.txt  run_times.txt
          request_meta.json  raw_response.json  stdout_stderr.log  exit_code.txt  verify.log
          found.csv  found.bib  found.ris
track-b/  audit_run.py  script_explanation.md  run_times.txt
          request_meta.json  raw_response.json  stdout_stderr.log  exit_code.txt  verify.log
          found.csv  found.bib  found.ris
```
