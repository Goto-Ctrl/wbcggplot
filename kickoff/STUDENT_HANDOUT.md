# B3事例研究 — 9/25 Kickoff Student Handout

## 今日のゴール

今日のゴールはLab 0を完成させることではありません。**自分のrepositoryで、同じbaselineを再現し、その状態をGitで記録できること**です。

この事例研究では、最終的に次の流れを自分で説明・実行できることを目指します。

`PCAP -> Packet -> Flow/Session -> Burst -> Representation -> Learning -> Audit -> Own Project -> Claim`

精度が高いことだけでは研究上の主張にはなりません。毎週、`What can you claim?` と `What can you NOT claim?` の両方を考えます。

## 1. Repositoryをcloneし、2つのremoteを設定する

学生には**student-safe course repository**のURLと、自分専用のprivate repository URLを配布します。Instructor repositoryは学生からは見えません。

```bash
git clone <COURSE_REPOSITORY_URL> b3-case-study-2026
cd b3-case-study-2026
git remote rename origin course
git remote add origin <YOUR_PRIVATE_REPOSITORY_URL>
git push -u origin main
git remote -v
```

以後、`origin`は自分のprivate repository、`course`は教材更新を受け取るread-only upstreamとして使います。Instructor-private repositoryをremoteに追加してはいけません。

## 2. Python環境を作る

Python 3.11以上を推奨します。

```bash
python --version
git --version
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

依存関係を導入します。

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

## 3. Kickoff checkを実行する

```bash
python -m labs.tools.kickoff_check
```

PASSにならない場合は、エラーを消してから先へ進むのではなく、**どのcommandで何が起きたかを残して**Working Seminarの材料にします。

## 4. 最初のPCAP baselineを再現する

```bash
python -m labs.tools.make_fixture
python -m labs.lab0_pcap.demo
python -m pytest -q
```

次の3点を自分で確認してください。

- canonical fixtureのpacket数
- TCP/UDPのpacket数
- それを確認しているtest file

canonical fixtureは「現実のtrafficの代表」ではなく、pipelineが同じように動くことを確認するためのdeterministic smoke fixtureです。

## 5. 最初の記録を作る

```bash
mkdir -p reports environment
cp templates/reports/kickoff.md reports/kickoff.md
```

WindowsではExplorerまたはPowerShellで同じファイルをcopyして構いません。

`reports/kickoff.md`を埋めます。`environment/README.md`には少なくともPython version、OS、Git version、baseline test resultを書きます。

## 6. 最初のstudent commit

```bash
git status
git add reports/kickoff.md environment/README.md
git commit -m "Complete B3 kickoff baseline"
git status
```

remoteへのpush方法は教員が指定したrepository運用に従ってください。

## 今日のExit Ticket

帰る前に、次の3問を自分の言葉で答えられるようにしてください。

1. observationとrepresentationは何が違うか。
2. canonical PCAP fixtureを固定するのはなぜか。
3. unit testがPASSしてもresearch claimが証明されたことにならないのはなぜか。

## 9/28までの準備

`labs/lab0_pcap/README.md` と `labs/RUNNING.md` のLab 0部分を読み、`reports/lab0_plan.md`を作成してください。

含める内容:

- packet field候補を observed / derived / metadata に分類した表
- IP address / port / protocol / direction / packet length / IAT をmodel inputとして使うかどうかの初期方針と理由
- baseline parserが意図的に対応していないものの要約
- 9/28のBriefingで議論したい疑問を1つ以上

**9/28までにstarter.pyの正解を探してコピーする必要はありません。** 先にmeasurement/observation contractを考えます。
