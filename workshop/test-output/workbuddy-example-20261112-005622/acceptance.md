# 教学示例核验报告 — workbuddy-example-20261112-005622

生成时间：2026-11-12（本地 +0800）；目录标签 `20261112-005622`
仓库：`\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis`
范围：**仅核验教学示例**，未执行完整双轨 Track A/B；未修改源码或已有文档；未安装、未推送；未使用离线 fixture 替代联网结果。

## 0. 已读取材料

- `docs/example-selection.md`（agy 的候选主题评估与推荐）
- `docs/workbuddy-two-track-acceptance.md`（双轨验收协议，本轮只作背景，不执行）
- `workshop/test-output/workbuddy-live-20261112-001414/acceptance.md`（上一轮真实联网验收，确认可复用的联网方式）

## 1. 证据分级：`example-selection.md` 是否附有实际成功请求的原始响应

**结论：正文没有附原始响应。** 第 34–42 行只在 "Raw Response Storage" 里列出 4 个文件路径，没有内嵌响应体、HTTP 状态或响应头。

被引用的文件确实存在（只读核查，mtime 均为 2026-11-12 00:44 +0800）：

| 文件 | 字节 | 实际结构（只读解析，见 `evidence_inspection.txt`） |
|---|---|---|
| `docs/candidate-queries/candidate1_awcf.json` | 139190 | 顶层 `candidate_id / candidate_name / request_url / request_params / timestamp_utc / response`；`response` 内才是 OpenAlex `meta`+`results`（5 条，含 `x_query`、`cost_usd`、`notice`、`abstract_inverted_index`） |
| `candidate2_genai_l2_writing.json` | 140444 | 同上结构 |
| `candidate3_chatbots_lang_learning.json` | 145636 | 同上结构 |
| `summary.json` | 11360 | 3 个候选的**派生摘要**（`candidate/url/count/items` + `abstract_preview`），不是 API 响应 |

四类证据区分如下：

| 类别 | 具体内容 | 判定依据 |
|---|---|---|
| **真实证据（本环境可复核）** | 上一轮 `workbuddy-live-20261112-001414/raw_response.json` + `request_meta.json`（HTTP 200、响应头、单次请求）；**本轮** `raw_response.json` + `request_meta.json`（HTTP 200、响应头、单次请求） | 由本机 Windows Python 实际发出，保存逐字节响应体与请求/响应元数据 |
| **包装过的响应副本（声称）** | `docs/candidate-queries/candidate*.json` | 内嵌的 `response` 看起来是真实 OpenAlex 响应（含服务端生成的 `meta.x_query`、`cost_usd`、`notice`），但文件被**重新包装/重新序列化**：顶层多了自定义字段，**没有** `http_status` / `response_headers`，文件中也不含 "HTTP/2 200"、"BypassSandbox"、"PromptPraxisResearch" 字样。不是逐字节原始响应，也无法据此复核请求是否真的成功 |
| **离线 fixture** | `workshop/tests/fixtures/openalex_normal.json` (2373 B)、`openalex_empty.json` (87 B)、`openalex_missing_metadata.json` (970 B) | 构造的小样本 `meta`+`results`（count 3/0/2），仅用于离线测试，非真实请求 |
| **推测 / 未验证断言** | 文档中的 "沙箱 403 → BypassSandbox: true → HTTP/2 200 OK"、"User-Agent: PromptPraxisResearch/1.0"；"Book chapter behind publisher paywall"、"Full-text PDF freely accessible"、"Direct Cambridge Core PDF link"、"top-tier peer-reviewed journal"、"100% Applied Linguistics"、教学最优结论 | 引用文件内无对应证据；链接未打开验证；属于评价性判断 |

附带观察：文档正文写 Candidate 1 时间戳 `2026-11-11T16:44:05Z`，而 `candidate1_awcf.json` 自述 `timestamp_utc: 2026-11-11T16:44:14.367728+00:00`，两者相差约 9 秒，不完全一致（如实记录，不影响书目字段对照）。

## 2. 本轮真实查询（一次，无重试）

沿用上一轮成功的环境：Windows Python `C:\Users\andy\.workbuddy-ai\binaries\python\versions\3.13.12\python.exe`（`Python 3.13.14`）、Windows UNC 路径、`MSYS2_ARG_CONV_EXCL='*'`、每次 Python 调用带 `-B`。

**为何不调用 `workshop/fetch_literature.py`**：读源码第 88–93 行可见其 `query_openalex()` 无条件把 `sort` 写进 URL，默认值就是 `cited_by_count:desc`；这与"使用 API 默认搜索排序、不另设引用数排序"冲突。本轮**不修改源码**，改为在输出目录内用标准库 `example_query.py` 发一次最小请求（见 `command.txt`）。

请求（`request_meta.json` 记录，`query_contains_sort / mailto / api_key` 均为 `false`）：

```
GET https://api.openalex.org/works?search=automated+written+corrective+feedback&filter=from_publication_date%3A2024-01-01&per-page=5
User-agent: PromptPraxisWorkshop/1.0      # 无邮箱、无凭据、无 Authorization
timeout: 30s
```

- `search = automated written corrective feedback`；`filter = from_publication_date:2024-01-01`（2024 年至今，**未设上界**，与 agy 的 URL 一致；响应含 2026 年记录）；`per-page = 5`（最多 5 条）；**URL 中无 `sort`**。
- 时间（`run_times.txt`）：开始 `2026-11-12 01:00:15 +0800` / `2026-11-11T17:00:26Z`；请求 `17:00:32.545411Z`；响应头 `Date: Wed, 11 Nov 2026 17:00:33 GMT`；结束 `01:00:51` / `17:01:02Z`。
- 结果：`http_status 200`、`QUERY_EXIT=0`、无 stderr 错误、原始响应体 **83957 字节**（`raw_response.json`）。未遇 401/403/429、网络或认证错误，未触发"停止"分支；未重试、未发第二次请求、未打开任何 DOI/OA/PDF 链接。
- `meta.count=11915`、`page=1 / per_page=5`、`meta.x_query.order = "best matches first"`、`order_default = true` —— **证实未设 sort 且实际采用 OpenAlex 默认相关性排序**。
- `meta.notice` 说明本次无 API key、共用免费每日额度；未使用任何凭据。

## 3. 逐条主题相关性判断（依据实际标题与可重建摘要）

摘要由响应中的 `abstract_inverted_index` 按词位置重建（见 `response_extract.txt`）；词序还原可能丢失大小写/标点细节。

| # | 标题（年份） | 与二语写作反馈的相关性 | 判断依据 | 信息充足度 |
|---|---|---|---|---|
| 1 | *Automated Written Corrective Feedback in EFL context* (2026) | **高度相关** | 摘要明确 "Chinese English as a Foreign Language (EFL) university students engage with automated written corrective feedback (AWCF) provided by Pigai"，是 EFL 大学生使用自动写作反馈平台 | 充足（摘要 335 字符） |
| 2 | *Automated Written Corrective Feedback (AWCF)* (2024) | **仅标题命中，无法确认** | 响应中 `abstract_inverted_index` 缺失、`authorships` 为 0、venue `BRILL eBooks`；只有标题含主题词，**没有摘要或作者信息**判断是否为二语写作语境 | **信息不足，标明** |
| 3 | *Effectiveness of Generative AI in Automated Written Corrective Feedback With Prompting* (2025) | **高度相关** | 摘要：AWCF tools "supporting English writing instruction"，评估 GPT-4 与提示策略的纠错表现，并有教师/学生实证研究；英语写作教学 + AWCF + 提示工程（未直接写 "second language"） | 充足（1520 字符） |
| 4 | *L2 writer engagement with automated written corrective feedback provided by ChatGPT: A mixed-method multiple case study* (2024) | **最相关** | 摘要明确 "second language (L2) writing classrooms"、"L2 writers"、"ChatGPT as an AWCF provider"、学生修订与反馈投入 | 充足（1576 字符） |
| 5 | *Impact of prompt sophistication on ChatGPT's output for automated written corrective feedback* (2025) | **高度相关** | 摘要明确 "feedback in second language writing, particularly automated written corrective feedback (AWCF)"，比较不同提示设计与 Grammarly 的纠错表现 | 充足（1703 字符，报告内截取前 1600 字符） |

**整体判断**：5 条中 4 条有摘要直接支持"二语/英语写作反馈 + AI/ChatGPT/提示设计"，1 条仅标题匹配且信息不足。相比上一轮 `applied linguistics AI` 返回的 Qwen3 / DeepSeek-R1 / GPT-4o 等通用大模型技术报告，本主题检索结果**主题聚焦度明显更高**。未为贴合主题改写、替换或补发任何结果。

## 4. API 返回的 OA/PDF 链接 vs 实际验证可访问的全文

下表**全部只是 API 响应里的字段值**（`open_access` / `primary_location` / `best_oa_location`），不是访问结果：

| # | `is_oa` | `oa_status` | `oa_url`（API 字段） | `pdf_url`（API 字段） | `any_repository_has_fulltext` |
|---|---|---|---|---|---|
| 1 | true | green | `https://doi.org/10.48321/d13320141e` | null | true |
| 2 | false | closed | null | null | false |
| 3 | false | closed | null | null | false |
| 4 | true | gold | `https://doi.org/10.1057/s41599-024-03543-y` | null | false |
| 5 | true | hybrid | Cambridge Core PDF URL（`.../S095834402510044Xa.pdf/...`） | 同一 Cambridge Core PDF URL | false |

**本轮没有打开、点击或下载任何 URL，没有发起额外网络请求。** 因此：

- **不声称**任何一条"全文/PDF 可下载""免费可访问"；第 5 条虽有 `pdf_url` 字段，也未验证其可访问性。
- **不声称**任何一条"存在付费墙""需机构订阅"；`is_oa=false` / `oa_status=closed` 只表示 OpenAlex 元数据未标记开放获取，不等同于已验证的付费墙。
- agy 文档里的 "Full-text PDF freely accessible"、"Direct Cambridge Core PDF link"、"behind publisher paywall" 都属于**未打开验证的断言**，需另行人工打开链接才能成立。

## 5. 与 agy 推荐逐项对照（见 `agy_comparison.txt`）

**得到本轮真实响应支持：**

- 推荐查询 URL 与参数完全一致（`search / filter=from_publication_date:2024-01-01 / per-page=5`，无 `sort`），且 `meta.x_query.order = best matches first`、`order_default = true` 支持其"省略 sort 即按相关性"的说法。
- `meta.count = 11915`，与文档 "11,915 records" 一致（是检索命中数，不是数据库总量）。
- 5 条记录的**顺序、标题、年份、DOI、引用数（0/1/19/167/10）、作者数与姓名、venue、摘要有无、`is_oa`、`oa_url`、第 5 条 `pdf_url`** 逐项一致（`title equal` / `doi equal` 均为 True）。
- 第 2 条"OpenAlex 记录缺作者、缺摘要"属实（`authorships` 0、无 `abstract_inverted_index`），可作为注册表不完备的教学点。
- 主题判断方向成立：4/5 条由摘要支持二语/英语写作反馈相关性，明显优于 baseline 查询。

**没有证据 / 属于推测：**

- "沙箱 403 → `BypassSandbox: true` → `HTTP/2 200 OK`"、"User-Agent: `PromptPraxisResearch/1.0`"：被引用的 JSON 内无这些字段或字样，本环境无法复核；本轮自己的请求是 urllib 发出的 HTTP 200，无 bypass。
- "Raw Response Storage" 称为原始响应：实际是包装/重新序列化的副本，缺 HTTP 状态、响应头与逐字节原始 body；`summary.json` 是派生摘要。
- "Book chapter behind publisher paywall"、"Traditional institutional subscription / paywall"、"Full-text PDF freely accessible"、"Direct Cambridge Core PDF link"：均未打开验证，不能由 `is_oa` / `oa_url` / `pdf_url` 字段推出。
- "top-tier peer-reviewed journal"、"Extremely High relevance"、"100% Applied Linguistics"、教学最优结论：评价性表述，非 API 证据；本轮只按标题与摘要做可观察的相关性判断。
- 文档正文时间戳 16:44:05Z 与文件自述 16:44:14.367728Z 不一致。

## 6. 结论：该主题是否适合教学

**适合，但有明确限定。** 检索层面：单次真实请求 HTTP 200、默认相关性排序、返回 5 条、字段完整可核对；主题层面：4/5 条有摘要直接支持二语/英语写作反馈与 AI 提示设计，且与 *Prompt & Praxis* "把 AI 作为工具"的教学主线契合，明显优于 `applied linguistics AI`。

三条限定：

1. 第 2 条缺摘要与作者，**信息不足**，只能作为"缺失元数据"示例，不能称为已核实的二语写作研究。
2. 所有 OA/PDF 可访问性、付费墙说法**未验证**；教学中若要演示"DOI ≠ 可下载全文"，需另行人工打开链接并如实记录结果。
3. **本轮未执行双轨验收**。需提示：`workbuddy-two-track-acceptance.md` 的 Step B2 要求用 `fetch_literature.py` 跑该主题，但该脚本默认写入 `sort=cited_by_count:desc`，与本轮"默认相关性排序"的参数不同，可能得到不同结果；这属于后续双轨需处理的事项，本轮未改源码、未验证。

## 7. 限制与未验证环节

- 未打开任何 DOI/OA/PDF 链接；未验证下载、付费墙、Zotero 导入。
- 未执行 Track A/B，未生成 CSV/BibTeX/RIS，未运行 `verify_zotero_import.py`。
- 未验证候选主题 2/3、其他排序或分页、API key/polite pool、429/401/403 分支。
- 摘要为 `abstract_inverted_index` 重建文本，非出版商原文；第 2 条无该字段。
- 结论只对 2026-11-11 17:00:33 GMT 这份响应成立；引用数与排序可能随时间变化。
- 写入范围核查：00:56 之后修改的文件**全部**位于本目录；`docs/example-selection.md`、`docs/workbuddy-two-track-acceptance.md`、`docs/candidate-queries/candidate1_awcf.json`、`workshop/fetch_literature.py` 的 mtime 均未变；`workshop` 下仅有既存 `cpython-314.pyc`（22:32 / 22:34），本次 `-B` 未生成新字节码。

## 8. 文件清单

```
acceptance.md（本文件）  command.txt  example_query.py
request_meta.json  raw_response.json
stdout_stderr.log  exit_code.txt  run_times.txt
evidence_inspection.txt  response_extract.txt  agy_comparison.txt
```
