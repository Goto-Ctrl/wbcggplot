# Small-PCAP Analysis-First Tutorial

## 目的

この教材の目的は、最初から大規模処理やstreamingを教えることではない。まず小さなPCAPを使い、packetの中身をPythonから触り、field、PacketRecord、flow、burstが何を意味するかに親しむ。

この段階では、処理が完全にscalableである必要はない。むしろ、**見えること、手で確認できること、楽に試せること**を優先する。

## Learning question

> PCAPから何を観測でき、どのfieldを使ってtraffic representationを作り始めるのか？

## 今日の位置づけ

このコースには二つのレールがある。

- **Analysis-first rail:** 小規模PCAPをlibrary-like interfaceで触り、packet / flow / burstに親しむ。
- **Scale rail:** 少し大きくしたときに限界を観察し、その結果をもとに次の処理設計を考える。具体的な方法は必要になった週にreleaseする。

最初は左側を先行する。右側は、左側で「便利だけれど息づまる」ことを実測してから導入する。

## Step A1 — tiny PCAPを見る

最初にWiresharkまたは既存のdemoで、`labs/data/canonical_smoke.pcap` を見る。

確認するものは次だけでよい。

- packetが時刻順に並んでいること
- IP address, port, protocolが見えること
- packet lengthとpayload lengthは同じではないこと
- TCP/UDP以外やfragmentなど、readerが扱わないものがあり得ること

この段階では、全protocolを理解する必要はない。

## Step A2 — Pythonからpacketを読む

必須pathでは、repositoryに含まれる小さなreaderを使う。

```bash
python -m labs.lab0_pcap.demo
```

このreaderは授業用に小さく作られている。外部libraryを使う場合と同じように、学生はまず「packetを一つずつ取り出す」感覚を持てばよい。

Optional: Scapyなどのpacket libraryが利用できる環境では、同じPCAPをlibraryで眺めてもよい。ただし、採点・提出のcanonical pathはrepository内のreaderとPacketRecord contractに合わせる。

## Step A3 — fieldを観察する

packetごとに次を観察する。

| field | 意味 | 注意 |
|---|---|---|
| `timestamp` | capture時刻 | 絶対値より差分が重要になることが多い |
| `src_ip`, `dst_ip` | 送受信IP | directionを決める材料 |
| `src_port`, `dst_port` | transport port | TCP/UDP以外では無い場合がある |
| `protocol` | TCP/UDP等 | filtering policyを記録する |
| `packet_length` | IPv4 total length | capture上のframe sizeとは区別する |
| `payload_length` | TCP/UDP payload | 0でも重要なpacketはある |
| `tcp_flags` | TCP flags | SYN/FIN/RST/ACKなどの手掛かり |

## Step A4 — PacketRecordにする

`PacketRecord`は、この事例研究で以後の処理が受け取る共通のpacket表現である。

重要なのは、PacketRecordが「PCAPの全情報」ではないこと。PacketRecordを作る時点で、すでに多くの情報を捨てている。

問い:

> PacketRecordに残したfieldだけで、何が言えるか？ 何は言えなくなるか？

## Step A5 — packetからflow/sessionへ

小さいPCAPでは、packetを手で追える。まず手で5-tupleまたはbidirectional keyを作り、次にコード出力と照合する。

観察すること:

- A→BとB→Aを同じflowに入れるか
- directionをどう定義するか
- inactivity timeoutでsessionを切ると何が変わるか

## Step A6 — flowからburstへ

burstは観測値そのものではない。研究者が定義するabstractionである。

問い:

> 連続する同方向packetをまとめると、何が見えやすくなるか？ 逆に何を失うか？

## Run / Observe / Think

### Run

```bash
python -m labs.lab0_pcap.demo
python -m labs.lab1_flow_session.demo
python -m labs.lab2_burst.demo
```

### Observe

- packet数
- flow数
- session数
- burst数
- 手計算と一致しない場所

### Think

- どのfieldはraw observationか？
- どのfieldはderived fieldか？
- PacketRecordに入っていない情報は何か？
- flowやburstの定義を変えると、研究上の主張はどう変わるか？

## Next question

小さいPCAPでは、この方法は分かりやすい。

では、PCAPが10倍、100倍、1000倍になったらどうなるか？

次は、同じanalysis-first codeを少し大きなcaptureに当て、時間とメモリを測る。
