# 最小真实 OpenAlex 联网验收 — workbuddy-live-20261112-001414

报告生成：2026-11-12（本地 +0800）；输出目录标签 `20261112-001414`
仓库：`\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis`

## 0. 范围声明

- 本次执行**一次真实 OpenAlex 联网查询**（`--fixture` 未使用），HTTP 200，无重试、无第二次请求、未切换到离线 fixture。
- **email 显式置空**（`--email=`）：未发送默认 `andyzheng0715@example.com`，也未发送任何虚构邮箱或真实凭据；请求 URL 中无 `mailto`，请求头中无 `Authorization` / API key。
- 未安装依赖、未修改项目源码、未迁移仓库、未改 Git 配置、未提交或推送。所有产物只写本目录；离线验收目录与 `sample-data/` 未被改动。
- 沿用离线验收已验证的 Windows Python、UNC 路径、`MSYS2_ARG_CONV_EXCL='*'` 与 `-B`。

## 1. 环境与解释器

| 项 | 实际观察 |
|---|---|
| 执行 shell | Windows NT 上的 MINGW64/Git Bash（沿用上一轮环境），非 WSL 内部 shell |
| 解释器 | `C:\Users\andy\.workbuddy-ai\binaries\python\versions\3.13.12\python.exe`（bash 形式 `/c/Users/andy/.workbuddy-ai/binaries/python/versions/3.13.12/python.exe`） |
| 版本 | `Python 3.13.14`（`--version` 实测） |
| 路径 | 脚本/输出均用 Windows UNC `\\wsl.localhost\Ubuntu\...`；`MSYS2_ARG_CONV_EXCL='*'`；每次 Python 调用带 `-B` |

## 2. 联网参数只读核对（步骤 2，执行前完成）

读取 `workshop/fetch_literature.py` 第 81–117 行与 249–284 行，确认：

- `query_openalex()` 联网分支构造 `params = {search, filter=from_publication_date:{year}-01-01, sort, per-page=min(limit,50)}`；`mailto` **仅在 `email` 非空时**加入；URL 为 `https://api.openalex.org/works?...`。
- 请求头只有 `User-Agent`（email 为空时为 `PromptPraxisWorkshop/1.0`）；`urllib.request.Request(url, headers=headers)`；`urlopen(req, timeout=30)`。**没有 API key 参数、没有 Authorization 头、没有环境变量/凭据读取**。
- `--email` 是 `type=str` 且带默认值，可用 `--email=` 显式置空；脚本参数层面**不要求**真实邮箱或 API key，因此未触发"停止并报告"条件，继续执行。
- 实际请求证据（`request_meta.json`）证实：URL 无 `mailto`，请求头 `{"User-agent": "PromptPraxisWorkshop/1.0"}`，stdout 中 `Mode: Live OpenAlex API ()` 也显示 email 为空。

## 3. 实际请求参数与证据

来自本次请求的 `request_meta.json`（单次 call，`error_entries: {}`）：

| 项 | 值 |
|---|---|
| 请求时间 (UTC) | `2026-11-11T16:17:33.850392+00:00` |
| 方法 | GET |
| URL | `https://api.openalex.org/works?search=applied+linguistics+AI&filter=from_publication_date%3A2024-01-01&sort=cited_by_count%3Adesc&per-page=3` |
| query 参数 | `search=["applied linguistics AI"]`、`filter=["from_publication_date:2024-01-01"]`、`sort=["cited_by_count:desc"]`、`per-page=["3"]`（无 `mailto`） |
| 请求头 | `User-agent: PromptPraxisWorkshop/1.0` |
| timeout | 30 秒 |
| HTTP 状态 | **200** |
| 响应头要点 | `Content-Type: application/json`；`Date: Wed, 11 Nov 2026 16:17:34 GMT`；`X-RateLimit-Remaining: 910`；`Server: cloudflare` |
| 原始响应体 | `raw_response.json`，**184544 字节**（与 `response_body_bytes` 及磁盘文件大小一致） |

**证据获取方式与限制**：在输出目录内用小型标准库包装器 `audit_run.py` 拦截 `urllib.request.urlopen`，仅将**本次**响应体 tee 到磁盘并记录请求/响应元数据；随后以 `runpy.run_path(<项目 fetch_literature.py>, run_name="__main__")` 执行未修改的项目脚本。包装器不修改 URL、查询参数、Request 对象、请求头、超时或解析逻辑，也不重试。核对严格基于这同一份 `raw_response.json`，**没有另发一次请求来补证据**。限制：保存的是 urlopen 层的响应体与元数据，不是网络层抓包；TLS/DNS/代理细节未记录；OpenAlex 的引用数与作者列表随时间变化，本报告结论只对这份保存文件成立。

## 4. 命令、时间、退出码

完整命令见同目录 `command.txt`。主命令（只执行一次）：

```
MSYS2_ARG_CONV_EXCL='*' '/c/Users/andy/.workbuddy-ai/binaries/python/versions/3.13.12/python.exe' -B \
  '\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-live-20261112-001414\audit_run.py' \
  --topic 'applied linguistics AI' --year 2024 --sort 'cited_by_count:desc' --limit 3 --email= \
  --output-csv '\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-live-20261112-001414\found.csv' \
  --output-bib '\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-live-20261112-001414\found.bib' \
  --output-ris '\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-live-20261112-001414\found.ris'
```

格式检查命令（项目自带 `verify_zotero_import.py --bib ... --ris ...`，见 `command.txt`）。

时间（`run_times.txt`）：开始 `2026-11-12 00:17:16 +0800` / `2026-11-11T16:17:27Z`；结束 `2026-11-12 00:17:52 +0800` / `2026-11-11T16:18:03Z`。

| 运行 | 退出码 | 日志 |
|---|---|---|
| 联网抓取 | `FETCH_EXIT=0` | `stdout_stderr.log`（完整 stdout+stderr，`exit_code.txt`） |
| 结构化核对 | `COMPARE_EXIT=0` | `comparison.txt` |
| 格式检查 | `VERIFY_EXIT=0` | `verify.log`（`verify_exit.txt`） |

stdout/stderr：无错误输出；关键行 `Mode: Live OpenAlex API ()`、`OpenAlex reports 139196 matching records in database.`、`Parsed 3 publications.`。**未遇到 401/403/429、网络或认证错误，未重试，未绕过任何限制。**

## 5. 输出与保存响应的逐项核对（步骤 5）

记录数：`meta.count=139196`（命中总数），本次响应 `results` 3 条；`found.csv` 3 行数据、`found.bib` 3 个 `@article`、`found.ris` 3 个 `TY/ER` 记录 —— 四者一致（`comparison.txt` 中 `RECORD COUNTS EQUAL: True`）。

CSV 按字段与 `raw_response.json` 逐项比较（`CSV FIELD-BY-FIELD ALL MATCH: True`）：

| # | OpenAlex ID | 标题 | 年份 | 引用数 | DOI | 期刊 | 字段核对 |
|---|---|---|---|---|---|---|---|
| 1 | W4414939355 | Qwen3 Technical Report | 2025 | 17653 | `https://doi.org/10.48550/arxiv.2505.09388` | arXiv (Cornell University) | ID/标题/作者/年份/引用/DOI/期刊 全部 match=True |
| 2 | W4414281281 | DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning | 2025 | 16779 | `https://doi.org/10.1038/s41586-025-09422-z` | Nature | 全部 match=True |
| 3 | W4404330874 | GPT-4o System Card | 2024 | 8851 | `https://doi.org/10.48550/arxiv.2410.21276` | arXiv (Cornell University) | 全部 match=True |

- 作者字段：CSV 以 `; ` 连接、BibTeX 以 ` and ` 连接、RIS 为多个 `AU` 行；三条作者字符串长度 707 / 1209 / 1512 字符，与响应 `authorships` 完全一致（格式检查器计为 60 / 100 / 100 位作者）。响应本身返回的作者列表即如此，脚本未截断。
- **缺失字段：本次 3 条记录在响应中均无缺失**（`missing/empty fields in raw response: none`），因此未出现 `Unknown` 占位或空字段。如实记录一处原始数据异常：第 3 条作者列表含显示名 `:`（`OpenAI; :; Hurst, Aaron; ...`），脚本按响应原样写出，未改写、未清洗。
- BibTeX / RIS 的标题、年份、去前缀 DOI 均能在对应文件中找到（`escaped_title_present / title_present / year_present / doi_present` 全为 True）。
- **格式检查**：`verify_zotero_import.py` 返回 `[PASS] BibTeX 3 records`、`[PASS] RIS 3 records`，退出码 0。**这仍是项目自带的正则/结构格式检查，不是 Zotero 客户端导入测试，未启动 Zotero、未调用其 import translator。**

## 6. 检索成功与主题相关性（分开报告）

**检索成功：是。** 单次 GET 返回 HTTP 200、3 条记录、字段与保存响应逐项一致、退出码 0，无 401/403/429、无网络或认证错误，未重试、未切 fixture。

**主题相关性：低，不适合作为"应用语言学 AI"教学示例。** 返回的 3 篇均为通用大模型技术报告/系统卡：Qwen3 Technical Report、DeepSeek-R1（LLM 强化学习）、GPT-4o System Card；标题与研究主题都不涉及应用语言学、语言教学、二语习得、语料库或话语分析。原因是使用全文 `search` 配合 `sort=cited_by_count:desc`（按引用量降序），高引用的通用 AI 论文被排到最前；`meta.count=139196` 也说明检索式很宽。这批结果适合演示"检索 → CSV/BibTeX/RIS 导出"的流程，**不适合**当作应用语言学课程的文献样例。

按要求**不为了匹配主题而改写结果**：未更换检索词、未调整排序、未补发第二次请求、未把结果替换成更贴题的论文；上述三篇即为本次响应的原始结果。

## 7. 错误、限制与未验证环节

- 本次无错误；`request_meta.json` 的 `error_entries` 为空，`stdout_stderr.log` 无 stderr 内容。因未遇到错误，未触发"保存原始错误并停止"的分支。
- 未验证：`mailto` / polite pool 行为与 429 限流（本次 email 为空、未限流）、401/403 认证分支、真实 Zotero 导入、`tests/test_workshop.py` 测试套件、其他 topic/sort/分页参数、非 ASCII 与超长字段的边界行为、OpenAlex 数据时效性。
- 写入范围核查：`find -newermt '2026-11-12 00:14:00'` 列出的文件全部位于本目录内；`workbuddy-offline-20261111-234550/acceptance.md`（mtime 23:54:11）与 `sample-data/sample-found.csv`（mtime 22:33:02）未变；`workshop` 下仅存在既有的 `cpython-314.pyc`（22:32 / 22:34），本次 `-B` 未生成新字节码。

## 8. 文件清单

```
acceptance.md（本文件）  command.txt  audit_run.py
stdout_stderr.log  exit_code.txt  run_times.txt
request_meta.json  raw_response.json
found.csv  found.bib  found.ris
verify.log  verify_exit.txt  comparison.txt
```
