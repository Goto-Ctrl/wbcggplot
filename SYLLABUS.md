# 2026年度 B3事例研究シラバス

## PCAPからTraffic Representation Researchへ

**実施期間:** 2026年9月25日（金）〜2027年1月15日（金）  
**通常実施:** 月・火・金 5限（大学暦上の休校・試験・冬期休業を除く）  
**形式:** Briefing / Working Seminar / Evidence Seminar / Milestone

## 1. 目的

この事例研究の目的は、特定のGNNや分類器を実装することではない。PCAPという観測データから出発し、packet、flow/session、burst、sequence、hierarchy、graphへと抽象化し、学習実験と実験監査を経て、自分自身のrepresentation hypothesisを小規模な研究として検証できるようになることである。

最終的に学生は、**何を観測したか、何を捨てたか、何をexplicitにしたか、比較は公平か、その結果から何を主張してよいか**を説明できなければならない。

## 2. Learning Outcomes

修了時に学生は次を自力で行えることを目標とする。

1. PCAPからpacket recordを抽出し、parserの対応範囲と限界を説明する。
2. packetをbidirectional flow/session/burstへ集約し、その定義を説明する。
3. 同じtrafficをstatistics / packet sequence / burst sequence / hierarchy / graphで表現し、preservation/lossを監査する。
4. graphのnode/edge semanticsとedge provenance (P/O/B/A/L/H) を説明し、non-graph equivalentを検討する。
5. matched-information comparisonを設計し、Information / Representation / Model advantageを混同しない。
6. leakage、normalization、seed、parameter count、feature engineeringなどのexperimental confoundを監査する。
7. 自分のrepresentation hypothesisと、それを否定し得るfalsification experimentを設計する。
8. evidenceに基づき What I can claim / What I cannot claim を明示して研究発表する。

## 2.5 PCAP学習の階段

PCAP実習は、最初から大規模処理の完成形を教えるのではなく、**小規模PCAPで親しむ → 少し大きくして変化を実測する → なぜ限界が生じるか説明する → 必要になった段階で改善法を学ぶ → 研究規模へ進む**順で行う。

学生向けには次の階段を共有する。

1. See — tiny PCAPを観察する。
2. Touch — Pythonでpacketを触る。
3. Represent — packet / flow / burstを小さな例で作る。
4. Enlarge — 同じ考え方を少し大きな入力へ広げる。
5. Measure — 時間とメモリの挙動を測る。
6. Explain — どこで、なぜ資源消費が増えるかをコードとdataflowから説明する。
7. Improve — 観測した問題に適した処理設計を学ぶ。
8. Separate — ingestionとrepresentationの責務を分ける。
9. Research — research-scaleのrepresentation比較へ進む。

各段は **Text → short Beamer → Hands-on → Observe → Explain → Next Question** で進む。後半の具体的な解法は、その必要性を実測・説明した後に段階公開する。

### 2.6 週次講義プラン

各週・各回の目的とexit conditionは `docs/B3_WEEKLY_TEACHING_PLAN_AND_SLIDE_MAP.md` で共有する。将来週についてはresearch questionと到達目標を先に共有し、具体的なtutorial / slides / starter codeは授業進行に合わせてreleaseする。

## 3. 週内の基本リズム

- **Briefing（月）:** 概念導入、前週の問題整理、今週のresearch questionとexit conditionを確認する。
- **Working Seminar（火）:** コード、PCAP、途中結果、失敗例を持ち込み、研究室全体でdebugする。完成スライドは不要。
- **Evidence Seminar（金）:** Question → Method → Evidence → Interpretation → Next question の順で短く発表する。
- **Milestone:** Phaseを閉じるGate。提出物と説明の両方がexit conditionを満たして初めて次Phaseへ進む。

毎回の発表で必ず **What can you claim? / What can you NOT claim?** を確認する。

## 4. Git運用

学生ごとにprivate repositoryを1つ作成する。最低限、`src/`, `tests/`, `data/README.md`, `reports/`, `results/`, `environment/` を置く。PCAPや大容量datasetそのものは原則commitせず、`data/README.md`に取得元、利用条件、checksum、前処理、件数を記録する。

各ゼミ前に作業をcommitする。Milestoneではtag `m1-observe`, `m2-represent`, `m3-experiment`, `m4-proposal`, `m5-year-end`, `m6-freeze`, `final` を付ける。結果を後から上書きせず、実験条件とseedを記録する。

## 5. 実施カレンダー

| 日付 | 種別 | 主題 | 事前課題 | ゼミで見せるもの | 終了条件 | Git提出物 |
|---|---|---|---|---|---|---|
| 9/25 金 | Briefing / Kickoff | 全体像 | Python/Git動作確認 | 環境、canonical PCAP | PCAP→claimの全体像を説明できる | `environment/`, first commit |
| 9/28 月 | Briefing | Lab 0: PCAP | Lab 0 READMEを読む | packet fields候補 | observationとderived fieldを区別 | `reports/lab0_plan.md` |
| 9/29 火 | Working | Lab 0 | starterを実行 | parser出力、エラー | canonical PCAPを再現可能に読む | `src/lab0*`, log |
| 10/2 金 | Evidence | Lab 0 | 手計数と照合 | parser evidence | parserが読む/捨てるものを説明 | `reports/lab0.md` |
| 10/5 月 | Briefing | Lab 1: Flow | flow定義を考える | 5-tuple案 | bidirectional keyとFW/BWを説明 | `reports/lab1_plan.md` |
| 10/6 火 | Working | Lab 1 | flow/session実装 | packet→flow表 | 手計算と一致 | code + tests |
| 10/9 金 | Evidence | Lab 1 | session境界を確認 | flow/session counts | inactivity splitの意味を説明 | `reports/lab1.md` |
| 10/12 月 | Briefing | Lab 2: Burst | burst候補定義 | direction pattern | burstをresearcher-defined abstractionとして説明 | `reports/lab2_plan.md` |
| 10/13 火 | Working | Lab 2 | burst実装 + scaling予測 | boundary比較 + larger-PCAP予測 | canonical burstを再現し、時間/RSSを測る | code + tests + measurement log |
| **10/16 金** | **Milestone M1** | **Observe + Scaling Wall** | Lab 0–2統合 + scaling evidence | PCAP→burst trace + time/RSS table | Measurement Contractと観測したscaling bottleneckを説明できる | `reports/M1.md`, `m1-observe` tag |
| 10/19 月 | Briefing | Lab 3: Representation | 4表現を読む | preservation/loss予想 | raw-observable budgetを固定 | `reports/lab3_plan.md` |
| 10/20 火 | Working | Lab 3 | tiny flowを手変換 | manual vs code表 | 4表現が一致 | code + audit output |
| 10/23 金 | Evidence | Lab 3 | lossを整理 | preservation/loss matrix | first irreversible lossを説明 | `reports/lab3.md` |
| 10/26 月 | Briefing | Lab 4: Graph | node/edge案 | graph sketch | edge semanticsを文章化 | `reports/lab4_plan.md` |
| 10/27 火 | Working | Lab 4 | 3 graphを構築 | node/edge list | raw budgetを増やさず構築 | code + tests |
| **10/30 金** | **休校** | 振替休校 | — | — | — | — |
| **11/2 月** | **休校** | 世田谷祭片付・振替休校 | — | — | — | — |
| **11/3 火** | **祝日** | 文化の日 | — | — | — | — |
| 11/6 金 | Evidence | Lab 4 | graphを手監査 | edge semantics + P/O/B/A/L/H | 「なぜこのedgeか」を説明 | `reports/lab4.md` |
| 11/9 月 | Briefing | Lab 4 Design Audit | deletion/replacementを予想 | perturbation案 | graph constructionとlearningを区別 | `reports/lab4_audit_plan.md` |
| 11/10 火 | Working | Lab 4 Design Audit | edge/node perturbation | before/after graph | non-graph equivalentを示す | audit code/output |
| **11/13 金** | **Milestone M2** | **Represent** | Lab 3–4統合 | representation defense | explicit/implicit/lossを比較説明 | `reports/M2.md`, `m2-represent` tag |
| 11/16 月 | Briefing | Lab 5: Matched Information | comparison案 | matched pair | 3 advantagesを区別 | `reports/lab5_plan.md` |
| 11/17 火 | Working | Lab 5 | baseline実行 | linear/MLP results | split/budgetを固定して再現 | code + raw results |
| **11/20 金** | **ゼミなし** | 後期前半末試験期間 | — | — | — | — |
| 11/23 月 | Briefing | Lab 5 Experimental Audit | 「Graphが勝った」を疑う | confound list | alternative explanationを3つ以上出す | `reports/lab5_audit_plan.md` |
| 11/24 火 | Working | Lab 5 Audit | control実験 | relation-feature control | non-graph reconstructionを検証 | audit code/results |
| 11/27 金 | Evidence | Lab 5 Audit | seed/capacity等整理 | audited result table | apparent advantageを再解釈 | `reports/lab5_audit.md` |
| 11/30 月 | Briefing | Lab 5 Closure | missing control確認 | claim table | main claimとlimitationsを固定 | `reports/lab5_claims.md` |
| 12/1 火 | Working | Lab 5 Closure | 再現実行 | clean rerun | clean checkoutから再現 | final Lab 5 results |
| **12/4 金** | **Milestone M3** | **Experiment** | Lab 5最終発表 | can/cannot claim | matched-information audit完了 | `reports/M3.md`, `m3-experiment` tag |
| 12/7 月 | Briefing | Lab 6: Open Project | topic候補3案 | RQ候補 | taskとmeasurementを先に定義 | `reports/project_ideas.md` |
| 12/8 火 | Working | Lab 6 Proposal | closest baseline調査 | hypothesis/baseline | comparatorを具体化 | `reports/proposal_draft.md` |
| **12/11 金** | **Milestone M4** | **Proposal Pitch** | proposal完成 | RQ, hypothesis, falsification | “If Y, hypothesis unsupported”と言える | `PROJECT_BRIEF.md`, `EXPERIMENT_PLAN.md`, `m4-proposal` tag |
| 12/14 月 | Briefing | Lab 6 Design Freeze | feedback反映 | revised protocol | main protocolをfreeze | `reports/protocol.md` |
| 12/15 火 | Working | Lab 6 Baseline | data/preprocess | real-data trace | baseline end-to-end実行 | baseline code/results |
| 12/18 金 | Evidence | Lab 6 Baseline | baseline評価 | first evidence | failureも含め説明 | `reports/baseline.md` |
| 12/21 月 | Briefing | Lab 6 Main Experiment | ablation再確認 | experiment matrix | 何を比較するか固定 | `reports/experiment_matrix.md` |
| 12/22 火 | Working | Lab 6 Main Experiment | 実験実行 | logs/results/errors | 再現可能な途中結果 | results + logs |
| **12/25 金** | **Milestone M5** | **Year-end Review** | 年内結果整理 | evidence/failures/open items | 年明けに必要な実験を限定 | `reports/M5.md`, `m5-year-end` tag |
| 12/28–1/5 | 休み | 冬期休業中 | — | — | — | — |
| 1/8 金 | Working | Lab 6 Final Experiment | 年末TODO確認 | missing evidence | 必須実験を完了 | final raw results |
| **1/11 月** | **祝日** | 成人の日 | — | — | — | — |
| **1/12 火** | **Milestone M6** | **Experiment Freeze** | 全結果を整理 | final figures/tables/claims | 新規大実験を停止、claimをfreeze | `reports/M6.md`, `m6-freeze` tag |
| **1/15 金** | **Final Milestone** | **修了発表** | final package完成 | 研究発表 + reproducibility demo | end-to-endで研究をdefend | `FINAL_REPORT.md`, `reproducibility.json`, `final` tag |

**大学暦上の注意:** 10/12と11/23は祝日授業日。10/30と11/2はそれぞれ振替休校。11/18–20は後期前半末試験期間のため、本プログラムでは11/20のゼミを置かない。冬期休業は大学暦に従い、年末年始は研究室ゼミを実施しない。

## 6. Milestone Gate

- **M1 Observe:** 同じPCAPから同じpacket/flow/session/burst countsを再現し、Measurement Contractを説明できる。加えて、boundedなlarger-PCAP実験で時間/peak RSSを測り、観測したscaling bottleneckをコードとdataflowから説明できる。解決法の習得はこのGateでは要求しない。
- **M2 Represent:** representationごとのpreservation/lossと、graph relationのnon-graph equivalentを説明できる。
- **M3 Experiment:** matched-information comparisonを実施し、Information / Representation / Model advantageを混同しない。
- **M4 Proposal:** 独自RQ、closest comparator、falsification conditionを事前に宣言する。
- **M5 Year-end:** positive resultだけでなくfailureとunresolved issueをevidenceとして整理する。
- **M6 Freeze:** data, code, split, seed, figures, claimsを凍結し、発表直前の結果追いを止める。
- **Final:** What I can claim / cannot claim を含むmini researchとしてdefendする。

## 7. 最終発表の共通構成

1. Research Question
2. Measurement / Dataset
3. Representation Hypothesis
4. Information preserved / lost
5. Closest comparator
6. Experimental design
7. Results
8. Falsification / ablation
9. What I can claim
10. What I cannot claim
11. Next research question

negative resultは減点理由ではない。仮説が支持されなかった場合でも、比較が公平で、再現可能で、結果を正しく解釈できていれば研究成果として評価する。

## 8. 評価

- Weekly research process / seminar contribution: 30%
- M1–M3 common Lab checkpoints: 25%
- M4–M6 Lab 6 research project: 25%
- Final presentation and reproducibility package: 20%

accuracy、F1、AUCなどの絶対値そのものは採点しない。問いの明確さ、measurement discipline、比較の公平性、再現性、falsification、結果解釈を評価する。
