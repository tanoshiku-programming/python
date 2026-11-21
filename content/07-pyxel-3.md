@@ app-fortune
title: 占いアプリを作ろう
type: 作品
chapter: 7
syntax: ボタンを押すと、ランダムに結果が出る
summary: ボタンをクリックすると、おみくじの結果がランダムに出るアプリ。マウス・リスト・randomの、まとめの作品です。
aliases: 占い, おみくじ, うらない, アプリ
reads: random=ランダム | randint=ランディント | Font=フォント | mouse_x=マウスエックス
group: 作品を作る
--
## 作るもの
ボタンを押すと、「大吉」「中吉」「小吉」「凶」のどれかがランダムで出る**占いアプリ**です。Pyxelはゲームだけでなく、こうした「ボタンで操作する小さなアプリ」も作れます。

使うものは、これまでに学んだことばかりです。

| 使うもの | どこで学んだ？ |
| --- | --- |
| リスト `uranai_list` | [[list]] |
| ランダムに選ぶ | [[random]] |
| マウスのクリック | [[pyxel-mouse]] |
| 日本語の表示 | [[pyxel-jp]] |
| 結果を入れる変数 | [[pyxel-var]] |

## 設計図
いきなりプログラムを書き始めずに、まず「何が必要か」を日本語で書き出してみます。

1. 結果の候補の**リスト**を作る
2. 今の結果を入れる**変数** `kekka` を作る（はじめは空っぽ）
3. `update`：ボタンがクリックされたら、リストから**ランダムに1つ**選んで、`kekka` に入れる
4. `draw`：タイトル・結果・ボタンを描く

## プログラム
```python px click=80,90 frames=20
import pyxel
import random

pyxel.init(160, 120, title="うらない")
pyxel.mouse(True)
font = pyxel.Font("umplus_j12r.bdf")
uranai_list = ["大吉", "中吉", "小吉", "凶"]
iro_list = [10, 11, 12, 8]
kekka = ""
kekka_iro = 7


def update():
    global kekka, kekka_iro
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        if 40 <= pyxel.mouse_x <= 120 and 80 <= pyxel.mouse_y <= 100:
            n = random.randint(0, 3)
            kekka = uranai_list[n]
            kekka_iro = iro_list[n]


def draw():
    pyxel.cls(1)
    pyxel.text(46, 12, "今日のうらない", 7, font)
    pyxel.text(64, 44, kekka, kekka_iro, font)
    pyxel.rect(40, 80, 80, 20, 8)
    pyxel.text(52, 85, "ボタンをおす", 7, font)


pyxel.run(update, draw)
```
フォントファイル（`umplus_j12r.bdf`）を、プログラムと同じフォルダに置くのを忘れずに（[[pyxel-jp]]）。

画像は、ボタンを1回クリックしたあとの画面です。押すたびに、結果が変わります。

## 仕組みを読み解く
- `uranai_list[n]`：リストの `n` 番目を取り出す（[[list-index]]）
- `random.randint(0, 3)`：0〜3の数をランダムに作る。4つ入ったリストの番号（0, 1, 2, 3）とちょうど同じ
- `iro_list[n]`：結果ごとに色を変える。`uranai_list` と `iro_list` は、同じ番号どうしが組になるように並べておく（0番の「大吉」は0番の色10）

::: stuck
リストの中身を増やしたのに `randint(0, 3)` のままだと、増やした分は出ません。リストの数に合わせて `randint` の数も変えよう。`random.randint(0, len(uranai_list) - 1)` と書けば、自動で合います。
:::

::: deep もっと知りたい人へ
`random.choice(uranai_list)` を使うと、番号を使わずにリストから1つ選べます。ただし、何番が選ばれたか分からないので、色も同じ番号で選ぶことができません。色も一緒に選びたいときは、`randint` で番号を決めるほうが便利です。
:::

@@ app-timer
title: ストップウォッチを作ろう
type: 作品
chapter: 7
syntax: スペースでスタート・ストップ
summary: スペースキーでスタート・ストップできるストップウォッチ。フレームの数から秒を計算する、割り算・True/False・キー操作のまとめです。
aliases: ストップウォッチ, タイマー, 時計, 秒, 計算アプリ
reads: btnp=ボタンピー | not=ノット | KEY_R=キーアール | ugoiteru=ウゴイテル | byou=ビョウ | fun=フン
group: 作品を作る
--
## 作るもの
**スペースキー**でスタートとストップ、**Rキー**で0に戻せる**ストップウォッチ**です。

## 設計図
ストップウォッチに必要なのは、「何フレーム進んだか」と「今、動いているか」の2つだけです。

| 覚えておくこと | 変数 | はじめの値 |
| --- | --- | --- |
| 進んだフレームの数 | `frame_kazu` | `0` |
| 今、動いているか | `ugoiteru` | `False`（止まっている） |

1. `update`：スペースが押されたら、動く／止まるを切り替える → 動いているなら、`frame_kazu` を1増やす
2. `draw`：`frame_kazu` から「何分何秒か」を計算して、表示する

## プログラム
```python px gif frames=100 press=KEY_SPACE@3
import pyxel

pyxel.init(160, 120, title="ストップウォッチ")
font = pyxel.Font("umplus_j12r.bdf")
frame_kazu = 0
ugoiteru = False


def update():
    global frame_kazu, ugoiteru
    if pyxel.btnp(pyxel.KEY_SPACE):
        ugoiteru = not ugoiteru
    if pyxel.btnp(pyxel.KEY_R):
        frame_kazu = 0
        ugoiteru = False
    if ugoiteru:
        frame_kazu = frame_kazu + 1


def draw():
    pyxel.cls(1)
    byou = frame_kazu // 30
    fun = byou // 60
    pyxel.text(32, 10, "ストップウォッチ", 7, font)
    pyxel.text(50, 45, f"{fun}分 {byou % 60}秒", 10, font)
    if ugoiteru:
        pyxel.text(28, 80, "スペース：ストップ", 11, font)
    else:
        pyxel.text(28, 80, "スペース：スタート", 13, font)
    pyxel.text(28, 96, "R：リセット", 13, font)


pyxel.run(update, draw)
```
画像は、スペースキーを1回押して、スタートしたあとの様子です。

## 仕組みを読み解く
### フレームの数から、秒を出す
Pyxelは、1秒に30回 `update` を呼びます（[[update-draw]]）。だから、**30フレームで1秒**です。

| 計算 | 意味 | `frame_kazu` が 2000 のとき |
| --- | --- | --- |
| `byou = frame_kazu // 30` | 30で割った商が、たった秒数 | `66` 秒 |
| `fun = byou // 60` | 60で割った商が、分 | `1` 分 |
| `byou % 60` | 60で割った余りが、「〇分」のあとの秒 | `6` 秒 |

2000フレームは「1分6秒」です。`//`（商）と `%`（余り）は、時計の計算にぴったりです（[[operator]]）。

### not で、スイッチを切り替える
`ugoiteru = not ugoiteru` は、`ugoiteru` を**反対にする**行です（[[logical]]の `not`）。

| 押す前 | 押したあと |
| --- | --- |
| `False`（止まっている） | `True`（動いている） |
| `True`（動いている） | `False`（止まっている） |

1つのキーで、スタートとストップを交互に切り替えられます。電気のスイッチと同じです。

### 動いているときだけ、数える
`if ugoiteru:` は、`if ugoiteru == True:` と同じ意味です。`ugoiteru` が `True` のときだけ、`frame_kazu` が増えます。

::: point
`ugoiteru` のように、**「今どうなっているか」を True / False で覚えておく変数**は、ゲームでも大活躍します。「ポーズ中か」「ゲームオーバーか」「ジャンプ中か」なども、同じ考え方で作れます（[[bool]]）。
:::

::: stuck
`btn` を使うと、スペースキーを押しているあいだ、毎フレーム切り替わってしまいます。1回押すごとに1回だけ切り替えたいので、`btnp` を使います（[[pyxel-key]]）。
:::

::: scratch
Scratchの「タイマー」ブロックは、自動で時間を数えてくれました。Pythonでは、`frame_kazu` を自分で1ずつ増やして、時間を数えています。Scratchのタイマーを、自分で作っているのと同じです。
:::

@@ game-catch
title: ゲームを作ろう（ほしキャッチ）
type: 作品
chapter: 7
syntax: 落ちてくるものを、キーで受け止める
summary: 上から落ちてくる「ほし」を、キーで動かすバーで受け止めるゲーム。ここまでの総まとめです。
aliases: ゲーム, ほしキャッチ, 初めてのゲーム, キャッチゲーム
reads: rndi=ランディー | max=マックス | min=ミン | score=スコア | miss=ミス
group: 作品を作る
--
## 作るもの
上から落ちてくる**ほし**を、**左右キー**で動かす**バー**で受け止めるゲームです。受け止めたら点が入り、逃したらミスが増えます。

## 設計図
| 必要なもの | 変数 |
| --- | --- |
| バーの位置 | `bar_x` |
| ほしの位置 | `hoshi_x`, `hoshi_y` |
| 点数 | `score` |
| ミスの数 | `miss` |

1. `update`：キーでバーを動かす → ほしを落とす → 受け止めたか調べる
2. `draw`：バー・ほし・点数を描く

## プログラム
```python px hold=KEY_RIGHT frames=90 gif
import pyxel

pyxel.init(160, 120, title="ほしキャッチ")
bar_x = 70
hoshi_x = pyxel.rndi(8, 150)
hoshi_y = 0
score = 0
miss = 0


def update():
    global bar_x, hoshi_x, hoshi_y, score, miss
    if pyxel.btn(pyxel.KEY_LEFT):
        bar_x = max(0, bar_x - 3)
    if pyxel.btn(pyxel.KEY_RIGHT):
        bar_x = min(144, bar_x + 3)
    hoshi_y = hoshi_y + 2
    if hoshi_y > 104 and bar_x - 4 <= hoshi_x <= bar_x + 20:
        score = score + 1
        hoshi_y = 0
        hoshi_x = pyxel.rndi(8, 150)
    elif hoshi_y > 120:
        miss = miss + 1
        hoshi_y = 0
        hoshi_x = pyxel.rndi(8, 150)


def draw():
    pyxel.cls(0)
    pyxel.rect(bar_x, 110, 16, 6, 11)
    pyxel.circ(hoshi_x, hoshi_y, 4, 10)
    pyxel.text(4, 4, f"SCORE {score}", 7)
    pyxel.text(100, 4, f"MISS {miss}", 8)


pyxel.run(update, draw)
```
画像は、右キーを押しつづけたときの様子です。実際は、あなたのキー操作で、バーが動きます。

## 仕組みを読み解く
- `max(0, bar_x - 3)` と `min(144, bar_x + 3)`：バーが画面の外に出ないようにする（144は「画面の幅160 − バーの幅16」）
- `hoshi_y = hoshi_y + 2`：ほしを1フレームごとに2ドットずつ落とす
- `hoshi_y > 104 and bar_x - 4 <= hoshi_x <= bar_x + 20`：ほしがバーの高さまで来て、**かつ**バーの横の範囲に入っているか（[[logical]]）。ほしの半径が4なので、バーの左右に4ドットずつ広めに判定している
- 受け止めたら `score` が増えて、ほしは上に戻り、新しい場所から落ちる
- 受け止められずに画面の下（`hoshi_y > 120`）まで落ちたら、`miss` が増える
- `pyxel.rndi(8, 150)`：8〜150のランダムな整数。ほしが落ちてくる横の位置を決める（[[px-rndi]]）

::: point
このゲームは、ここまでに学んだ**変数・if・キー操作・図形・文字**の組み合わせだけでできています。
:::

## もっと面白くしよう
自分でつけ足してみよう。上のほうが簡単です。

- ミスが3回になったら、「GAME OVER」と出して、止める（場面の切り替えは[[game-scene]]）
- 点数が増えたら、ほしの落ちる速さを上げる
- ほしを2つ、3つに増やす（[[game-list]]）
- ほしの色を、ランダムに変える

作り方の見本は、このページの下の「作ってみよう」にあります。分からない命令があったら、[[ch9|Pyxel辞典]]を引こう。

@@ game-scene
title: 画面を切り替えよう（タイトル・ゲーム・結果）
type: 作品
chapter: 7
syntax: gamen = "title"
summary: タイトル画面 → ゲーム → 結果画面のように、場面を切り替える方法です。「今どの場面か」を変数に覚えておきます。
aliases: 場面, シーン, タイトル画面, ゲームオーバー, 切り替え, 連打ゲーム
reads: gamen=ガメン | title=タイトル | game=ゲーム | over=オーバー | KEY_R=キーアール
group: 作品を作る
--
## ゲームには「場面」がある
ふつうのゲームは、いきなり始まりません。

1. **タイトル画面**：「スペースキーでスタート」
2. **ゲーム中**：遊ぶ
3. **結果画面**：点数を見て、もう一度遊ぶ

この「今どの場面か」を、変数 `gamen`（画面）に**文字で**覚えておきます。

| `gamen` の中身 | 場面 |
| --- | --- |
| `"title"` | タイトル画面 |
| `"game"` | ゲーム中 |
| `"kekka"` | 結果画面 |

## 5秒間の連打ゲーム
5秒のあいだに、スペースキーを何回押せるかを競うゲームです。

```python px gif frames=60 press=KEY_SPACE@20
import pyxel

pyxel.init(160, 120, title="連打ゲーム")
gamen = "title"
score = 0
nokori = 0


def update():
    global gamen, score, nokori
    if gamen == "title":
        if pyxel.btnp(pyxel.KEY_SPACE):
            gamen = "game"
            score = 0
            nokori = 150
    elif gamen == "game":
        nokori = nokori - 1
        if pyxel.btnp(pyxel.KEY_SPACE):
            score = score + 1
        if nokori <= 0:
            gamen = "kekka"
    elif gamen == "kekka":
        if pyxel.btnp(pyxel.KEY_R):
            gamen = "title"


def draw():
    pyxel.cls(0)
    if gamen == "title":
        pyxel.text(52, 40, "RENDA GAME", 10)
        pyxel.text(44, 70, "PUSH SPACE KEY", 7)
    elif gamen == "game":
        pyxel.text(56, 40, f"SCORE {score}", 7)
        pyxel.text(56, 60, f"TIME {nokori // 30}", 11)
    elif gamen == "kekka":
        pyxel.text(52, 40, f"RESULT {score}", 10)
        pyxel.text(30, 70, "PUSH R KEY TO TITLE", 7)


pyxel.run(update, draw)
```
画像は、タイトル画面でスペースキーを押して、ゲームが始まったところです。

## 仕組みを読み解く
- `update` と `draw` の両方で、`if gamen == "title":` のように**場面ごとに分けて**書く
- 場面を変えたいときは、`gamen = "game"` のように**中身を入れ替えるだけ**
- `nokori = 150`：残り時間をフレームで持っている。150フレーム ＝ 5秒（[[app-timer]]）
- ゲームを始めるときに `score = 0` にしている。こうしないと、2回目に遊ぶとき、前の点数が残ってしまう

::: point
場面が増えても、やることは同じです。`if gamen == "〇〇":` を1つ足して、その場面でしたいことを書きます。「ポーズ画面」「ステージ2」なども、この形で作れます。
:::

::: scratch
Scratchでは、「（ゲームスタート）を送る」と「（ゲームスタート）を受け取ったとき」で、場面を切り替えましたね。Pythonでは、`gamen` という変数の中身で、今どの場面かを覚えておきます。
:::

::: stuck
`gamen = "Game"` のように、つづりや大文字・小文字がちがうと、どの `if` にも当てはまらず、画面が真っ黒になります。`"title"`、`"game"`、`"kekka"` の書き方を、全部そろえよう。
:::

@@ game-list
title: たくさん動かそう（リストを使う）
type: 作品
chapter: 7
syntax: for i in range(30):
summary: 雪や敵のように、たくさんのものを動かすときは、位置をリストに入れて、for でまとめて動かします。
aliases: たくさん, 複数, 敵を増やす, 雪, リスト, 弾幕
reads: append=アペンド | range=レンジ | x_list=エックスリスト | y_list=ワイリスト
group: 作品を作る
--
## 1つなら変数、たくさんならリスト
ほしキャッチでは、ほしの位置を `hoshi_x` と `hoshi_y` の2つの変数で覚えていました。でも、ほしが30個になったら、変数を60個も作るのは大変です。

そこで、**位置をリストに入れて**（[[list]]）、[[for]]で1つずつ動かします。

| 番号（`i`） | 0 | 1 | 2 | … |
| --- | --- | --- | --- | --- |
| `x_list[i]`（横の位置） | 25 | 130 | 72 | … |
| `y_list[i]`（縦の位置） | 10 | 88 | 40 | … |

同じ番号の `x_list[i]` と `y_list[i]` が、1つの雪の位置です（[[list-index]]）。

## 雪をふらせる
```python px gif frames=60
import pyxel

pyxel.init(160, 120, title="雪がふる")
x_list = []
y_list = []
for i in range(30):
    x_list.append(pyxel.rndi(0, 159))
    y_list.append(pyxel.rndi(0, 119))


def update():
    for i in range(30):
        y_list[i] = y_list[i] + 1
        if y_list[i] > 120:
            y_list[i] = 0
            x_list[i] = pyxel.rndi(0, 159)


def draw():
    pyxel.cls(1)
    for i in range(30):
        pyxel.circ(x_list[i], y_list[i], 1, 7)


pyxel.run(update, draw)
```

## 仕組みを読み解く
1. **はじめに**：`for` で30回繰り返して、空っぽのリストに、ランダムな位置を `append` で足していく
2. **update**：`for` で30個の雪を1つずつ下に動かす。画面の下まで来た雪は、上に戻す
3. **draw**：`for` で30個の雪を1つずつ描く

`i` には、0, 1, 2, …, 29 が順番に入るので、30個全部を同じやり方で動かせます。

::: point
**「位置はリスト、動かすのは for」**。雪でも、敵でも、弾でも、たくさんのものを動かすときの基本のかたちです。
:::

::: deep global がなくても動くのはなぜ？
`update` の中で `y_list[i] = …` と書いても、`global` はいりません。`global` が必要なのは、`y_list = …` のように**変数そのものに新しい値を入れる**ときです。リストの**中身だけ**を書き換えたり、`append` で足したりするときは、`global` を書かなくても大丈夫です（書いてもエラーにはなりません）。
:::

## ほしキャッチを、ほし3つにする
同じやり方で、[[game-catch]]のほしを3つに増やせます。

```python px hold=KEY_RIGHT frames=90 gif
import pyxel

pyxel.init(160, 120, title="ほしキャッチ（3つ）")
bar_x = 70
hoshi_x_list = [30, 80, 130]
hoshi_y_list = [0, -40, -80]
score = 0


def update():
    global bar_x, score
    if pyxel.btn(pyxel.KEY_LEFT):
        bar_x = max(0, bar_x - 3)
    if pyxel.btn(pyxel.KEY_RIGHT):
        bar_x = min(144, bar_x + 3)
    for i in range(3):
        hoshi_y_list[i] = hoshi_y_list[i] + 2
        if hoshi_y_list[i] > 104 and bar_x - 4 <= hoshi_x_list[i] <= bar_x + 20:
            score = score + 1
            hoshi_y_list[i] = 0
            hoshi_x_list[i] = pyxel.rndi(8, 150)
        elif hoshi_y_list[i] > 120:
            hoshi_y_list[i] = 0
            hoshi_x_list[i] = pyxel.rndi(8, 150)


def draw():
    pyxel.cls(0)
    pyxel.rect(bar_x, 110, 16, 6, 11)
    for i in range(3):
        pyxel.circ(hoshi_x_list[i], hoshi_y_list[i], 4, 10)
    pyxel.text(4, 4, f"SCORE {score}", 7)


pyxel.run(update, draw)
```
ほしキャッチの「ほしを動かす」「受け止めたか調べる」の部分を、`for i in range(3):` の中に入れて、`hoshi_y` を `hoshi_y_list[i]` に書き換えただけです。はじめの `y` を `0, -40, -80` とずらしているので、ほしが1つずつ順番に落ちてきます（マイナスは、画面の上の外です）。

::: stuck
`IndexError: list index out of range` が出たら、リストに入っている数より大きい番号を使っています。`range(30)` の数と、リストに入れた数がそろっているか確かめよう（[[error]]）。
:::

@@ object
title: オブジェクトとメソッド（ドットが2回出てくるわけ）
type: 考え方
chapter: 7
syntax: モノ.命令()
summary: pyxel.text() のドットは1回、pyxel.sounds[0].set() のドットは2回。ドットは「〜の」という意味です。命令のついた「モノ」がオブジェクト、そのモノについた命令がメソッドです。
aliases: オブジェクト, メソッド, ドット, ピリオド, 関数とのちがい, 持ち物, 棚, スロット, ドットが2回
reads: object=オブジェクト | method=メソッド | sounds=サウンズ | images=イメージズ | set=セット
group: ゲームの技
--
## ドットは「〜の」と読む
Pyxelの命令は `pyxel.text(…)` のように**ドットが1回**でした。ところが、音や絵を作るところでは、**ドットが2回**出てきます。むずかしく見えますが、ドットの意味はどちらも同じで、「**〜の**」と読むだけです。

| 書き方 | 読み方 |
| --- | --- |
| `pyxel.text(…)` | pyxel **の** text |
| `pyxel.sounds[0].set(…)` | pyxel **の** sounds **の** 0番**の** set |

ドットが2回なのは、「**〜の、〜の**」と、2つつないでいるからです。

## 関数とメソッド
| 名前 | だれへのお願い？ | 例 |
| --- | --- | --- |
| **関数** | pyxel **本体**にお願いする | `pyxel.cls(0)`、`pyxel.play(0, 0)` |
| **メソッド** | **持ち物**（`sounds[0]` など）にお願いする | `pyxel.sounds[0].set(…)` |

この「持ち物」のように、中身と命令がセットになったモノを、**オブジェクト**といいます。

## たとえ：スマホのボイスメモ
スマホのボイスメモには、録音がずらっと並んでいて、1つ選ぶと「再生」や「名前の変更」ができますね。

| ボイスメモ | Pyxel |
| --- | --- |
| 録音が並んだ一覧 | `pyxel.sounds`（64個まで入る） |
| 一覧から1つ選ぶ | `pyxel.sounds[2]`（**番号は0から**） |
| 選んだ録音 | **オブジェクト** |
| その録音の「録音し直す」ボタン | `.set(…)`（**メソッド**） |
| スマホの電源ボタン | `pyxel.quit()` などの**関数** |

電源ボタンはスマホ**全体**へのお願い、「録音し直す」はその**録音1つ**へのお願いです。

::: scratch
Scratchのスプライトも、オブジェクトのようなものです。ネコには「x座標」などのデータと、「10歩動かす」などの命令が、セットでついていました。
:::

## じつは、もう使っている
```python
kudamono_list = ["りんご", "みかん"]
kudamono_list.append("ぶどう")
print(kudamono_list)
```
`kudamono_list.append(…)` は、「リストというモノに『足して』とお願いする」メソッドです（[[list]]）。

::: deep Pyxelには、どんなオブジェクトがある？
番号つきの棚が5つあります。`images`（絵・3枚）、`tilemaps`（マップ・8個）、`sounds`（効果音・64個）、`musics`（曲・8個）、`channels`（スピーカー・4本）です。番号は0からなので、`pyxel.sounds[64]` はエラー（`IndexError`）になります。くわしくは辞典の[[px-objects]]を見よう。

オブジェクトの設計図（クラス）は、8章の[[class]]で、自分でも作れるようになります。
:::

@@ game-image
title: 画像を表示して動かそう
type: 作品
chapter: 7
syntax: pyxel.blt(x, y, 0, u, v, 8, 8, 0)
summary: ドット絵のキャラクターを blt で画面に出して、キーで動かします。透明色・アニメーション・左右の向きの変え方も学びます。
aliases: 画像, ドット絵, キャラクター, スプライト, アニメーション, 歩く, 反転
reads: blt=ブリット | images=イメージズ | muki=ムキ
group: ゲームの技
--
## 図形から、ドット絵へ
ここまでは、`rect` や `circ` の図形でキャラクターを作ってきました。ゲームらしくするなら、**ドット絵**を使いたいですね。

Pyxelでは、ドット絵を**イメージバンク**という置き場所に入れておいて、[[px-blt]]で画面にはります。

| 手順 | 命令 |
| --- | --- |
| ① イメージバンクに絵を入れる | `pyxel.images[0].set(…)`、または `pyxel.images[0].load(…)` |
| ② 画面にはる | `pyxel.blt(…)` |

## ひよこを出してみる
```python px
import pyxel

pyxel.init(160, 120, title="ひよこ")
pyxel.images[0].set(0, 0, ["000aaa00", "00aaaaa0", "00aaa1a0", "0aaaaaa9", "aaaaaaa0", "0aaaaaa0", "00aaaa00", "00900900"])


def update():
    pass


def draw():
    pyxel.cls(5)
    pyxel.blt(50, 56, 0, 0, 0, 8, 8)
    pyxel.blt(100, 56, 0, 0, 0, 8, 8, 0)


pyxel.run(update, draw)
```
`images[0].set(0, 0, […])` で、イメージバンク0番の左上に、8×8のひよこを描いています（`pyxel.images[0].set` のドットが2回出てくるわけは、[[object]]で説明します）。1文字が1ドットで、`a` が黄色、`1` が目、`9` がくちばし、`0` が何もないところです（[[px-image-class]]）。

`blt(x, y, 0, 0, 0, 8, 8)` は、「イメージバンク0番の (0, 0) から 8×8 を切り取って、画面の (x, y) にはる」という意味です。

::: point
左のひよこは、まわりが黒い四角になっています。右のひよこは、最後に `0` を足したので、**0番の色（黒）が透明**になって、背景が見えています。キャラクターをはるときは、透明色をつけるのが基本です。
:::

## キーで動かして、歩かせる
```python px gif frames=40 hold=KEY_LEFT
import pyxel

pyxel.init(160, 120, title="歩くひよこ")
pyxel.images[0].set(0, 0, ["000aaa00", "00aaaaa0", "00aaa1a0", "0aaaaaa9", "aaaaaaa0", "0aaaaaa0", "00aaaa00", "00900900"])
pyxel.images[0].set(8, 0, ["000aaa00", "00aaaaa0", "00aaa1a0", "0aaaaaa9", "aaaaaaa0", "0aaaaaa0", "00aaaa00", "00099000"])
x = 76
muki = 1


def update():
    global x, muki
    if pyxel.btn(pyxel.KEY_LEFT):
        x = x - 1
        muki = -1
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 1
        muki = 1


def draw():
    pyxel.cls(5)
    u = pyxel.frame_count // 8 % 2 * 8
    pyxel.blt(x, 56, 0, u, 0, 8 * muki, 8, 0)


pyxel.run(update, draw)
```
画像は、左キーを押しつづけたときの様子です。

## 仕組みを読み解く
### 足を動かす（アニメーション）
イメージバンクの (0, 0) と (8, 0) に、足の形がちがう2枚の絵を描いています。

`u = pyxel.frame_count // 8 % 2 * 8` は、8フレームごとに `0` と `8` を交互にくり返す計算です。

| `frame_count` | `// 8` | `% 2` | `* 8` ＝ `u` |
| --- | --- | --- | --- |
| 0〜7 | 0 | 0 | 0（1枚目） |
| 8〜15 | 1 | 1 | 8（2枚目） |
| 16〜23 | 2 | 0 | 0（1枚目） |

切り取る場所 `u` が変わるので、2枚の絵が交互に表示されて、歩いているように見えます。パラパラ漫画と同じです。

### 向きを変える（左右反転）
`blt` の幅を**マイナス**にすると、絵が左右反転します。`muki` は、右向きなら `1`、左向きなら `-1` です。幅を `8 * muki` にしているので、左に歩くときは `-8` になって、ひよこが左を向きます。

::: scratch
Scratchの「次のコスチュームにする」がアニメーション、「回転方法を左右のみにする」が左右反転にあたります。Pyxelでは、どちらも `blt` の数を変えるだけでできます。
:::

::: deep 自分で描いた画像を使う
本格的な絵は、文字で書くより、**Pyxel Editor**（ターミナルで `pyxel edit ファイル名.pyxres`）で描くほうが簡単です。描いた絵は `pyxel.load("ファイル名.pyxres")` で読みこみます（[[px-load]]）。PNG画像なら、`pyxel.images[0].load(0, 0, "ファイル名.png")` で、イメージバンクに読みこめます。
:::

@@ game-hit
title: 当たり判定を作ろう
type: 作品
chapter: 7
syntax: x1 < x2 + w2 and x2 < x1 + w1 and …
summary: キャラクターと敵がぶつかったかどうかを調べる「当たり判定」の作り方です。四角どうし・近さ・円どうしの3つの方法を学びます。
aliases: 当たり判定, 衝突判定, ヒットチェック, ぶつかる, 重なる, あたりはんてい
reads: kasanatteru=カサナッテル | kyori=キョリ | sqrt=スクエアルート
group: ゲームの技
--
## 当たり判定ってなに？
シューティングで弾が敵に当たったか、アクションでキャラクターが敵にぶつかったか。ゲームでは「**2つのものが重なっているか**」を、毎フレーム調べます。これを**当たり判定**といいます。

::: scratch
Scratchには「（敵）に触れた」ブロックがありました。Pythonには、そのブロックはありません。位置と大きさから、自分で計算して調べます。
:::

## 方法1：四角どうしが重なっているか
2つの四角が重なっているのは、次の4つが**全部**成り立つときです。

| 条件 | 意味 |
| --- | --- |
| `x1 < x2 + w2` | Aの左はしが、Bの右はしより左にある |
| `x2 < x1 + w1` | Bの左はしが、Aの右はしより左にある |
| `y1 < y2 + h2` | Aの上はしが、Bの下はしより上にある |
| `y2 < y1 + h1` | Bの上はしが、Aの下はしより上にある |

1つでも成り立たなければ、2つの四角は、どこかで離れています。この4つを `and` でつなげて、関数にしておくと便利です（[[function]]・[[logical]]）。

```python px gif frames=70 hold=KEY_RIGHT
import pyxel

pyxel.init(160, 120, title="当たり判定")
x = 20


def kasanatteru(x1, y1, w1, h1, x2, y2, w2, h2):
    return x1 < x2 + w2 and x2 < x1 + w1 and y1 < y2 + h2 and y2 < y1 + h1


def update():
    global x
    if pyxel.btn(pyxel.KEY_LEFT):
        x = x - 1
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 1


def draw():
    pyxel.cls(0)
    if kasanatteru(x, 50, 16, 16, 80, 45, 24, 24):
        pyxel.rect(80, 45, 24, 24, 8)
        pyxel.text(70, 100, "HIT!", 8)
    else:
        pyxel.rect(80, 45, 24, 24, 13)
    pyxel.rect(x, 50, 16, 16, 11)


pyxel.run(update, draw)
```
画像は、右キーを押しつづけたときの様子です。緑の四角が灰色の四角に重なると、赤くなって `HIT!` と出ます。

`kasanatteru` は、重なっていれば `True`、離れていれば `False` を返す関数です（[[bool]]）。1回作っておけば、敵が何体いても、同じ関数で調べられます。

## 方法2：近いかどうか（同じ大きさのとき）
2つが同じくらいの大きさなら、もっと簡単に「x も y も、近ければ当たり」と考えられます。

```python
x1 = 40
y1 = 50
x2 = 46
y2 = 53
print(abs(x1 - x2) < 8 and abs(y1 - y2) < 8)
```
`abs` は「ちがいの大きさ」を出す関数です（[[math-func]]）。横の差も縦の差も8より小さければ、当たりとしています。

## 方法3：円どうし
ボールや弾のように丸いものは、**中心どうしの距離**で調べます。距離が「2つの半径の合計」より小さければ、重なっています。

```python
import math

x1 = 10
y1 = 10
x2 = 16
y2 = 18
kyori = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(kyori)
print(kyori < 5 + 6)
```
距離は、横の差と縦の差から、`√(横の差² ＋ 縦の差²)` で求めます。中学3年で習う「三平方の定理」です。Pyxelでは `pyxel.sqrt` も使えます（[[px-sqrt]]）。

::: point
| 方法 | 向いているもの |
| --- | --- |
| 四角どうし | ほとんどのゲーム。まずはこれ |
| 近いかどうか（abs） | 同じ大きさのキャラクターどうし |
| 円どうし | ボール、弾、丸い敵 |
:::

::: stuck
キャラクターの見た目より当たり判定を少し**小さく**すると、「当たってないのにやられた！」という不満が減って、遊びやすくなります。
:::

@@ game-sound
title: 音を鳴らそう
type: 作品
chapter: 7
syntax: pyxel.sounds[0].set(…) / pyxel.play(0, 0)
summary: 効果音を作って鳴らします。ジャンプやアイテムを取ったときに音が鳴ると、ゲームが一気に楽しくなります。
aliases: 音, 効果音, サウンド, BGM, 鳴らす, ドレミ
reads: sounds=サウンズ | set=セット | play=プレイ
group: ゲームの技
--
## 2つの手順
| 手順 | 命令 |
| --- | --- |
| ① 音を作る（最初に1回） | `pyxel.sounds[番号].set(音の高さ, 音色, 大きさ, 効果, 速さ)` |
| ② 鳴らす（鳴らしたいとき） | `pyxel.play(チャンネル, 音の番号)` |

## スペースで「ピコン」
```python px press=KEY_SPACE@3 frames=10
import pyxel

pyxel.init(160, 120, title="効果音")
pyxel.sounds[0].set("c3e3g3c4", "p", "7", "n", 5)
pyxel.sounds[1].set("c2r c1", "n", "7", "f", 10)


def update():
    if pyxel.btnp(pyxel.KEY_SPACE):
        pyxel.play(0, 0)
    if pyxel.btnp(pyxel.KEY_Z):
        pyxel.play(0, 1)


def draw():
    pyxel.cls(1)
    pyxel.text(40, 50, "SPACE: PIKON", 10)
    pyxel.text(40, 64, "Z: DOON", 8)


pyxel.run(update, draw)
```
スペースキーで「ドミソド」と上がる明るい音、Zキーで「ドーン」という低い音が鳴ります。

## 音が鳴るしくみ
音の作業は、**「作る」と「鳴らす」の2つに分かれて**います。

`pyxel.sounds` は、音を入れておく**64個の棚**（0〜63番）です。スマホのボイスメモの一覧のように、番号で「どの音か」を選びます（[[object]]）。

| やること | 書き方 | 意味 |
| --- | --- | --- |
| ① 作る | `pyxel.sounds[0].set(…)` | 0番の棚に、音を作って入れる（録音のようなもの） |
| ② 鳴らす | `pyxel.play(0, 0)` | チャンネル0のスピーカーで、0番の音を流す |

`pyxel.play(チャンネル, 音の番号)` には、**数が2つ**並びます。どちらが何の番号か、まちがえやすいので、順番を覚えよう。

| 順番 | 意味 | 範囲 |
| --- | --- | --- |
| 1つ目 | どの**スピーカー（チャンネル）**で鳴らすか | 0〜3 |
| 2つ目 | どの**音**を鳴らすか | 0〜63 |

スピーカーは**4本**あるので、`pyxel.play(0, 0)` と `pyxel.play(1, 1)` を同時に呼ぶと、2つの音が重なって聞こえます。同じチャンネルで別の音を鳴らすと、鳴っていた音は止まって、新しい音に置きかわります（[[px-play]]）。

::: point
`sounds[0].set(…)` で**作る**のは、棚の中に音を入れておくだけで、**音は鳴りません**。`play` を呼んだときに、はじめて鳴ります。
:::

## 音の作り方
`set` の5つの文字で、音を決めます（[[px-sound-class]]）。

| 引数 | 書き方 | 例 |
| --- | --- | --- |
| 音の高さ | ドレミのアルファベット（c d e f g a b）と、高さの数字（0〜4）。`r` は休み | `"c3e3g3c4"` |
| 音色 | `t` 三角波（やわらかい）、`s` 四角波（ファミコン風）、`p` パルス波、`n` ノイズ（爆発など） | `"p"` |
| 大きさ | `0`〜`7` | `"7"` |
| 効果 | `n` なし、`s` スライド、`v` ビブラート、`f` だんだん小さく | `"n"` |
| 速さ | 1音の長さ。小さいほど速い | `5` |

数字を少しずつ変えて、自分だけの音を作ってみよう。

## ゲームに入れる
音は、**何かが起きた瞬間**に鳴らします。ほしキャッチなら、ほしを受け止めたところに1行足すだけです（[[game-catch]]）。

```python norun
    if hoshi_y > 104 and bar_x - 4 <= hoshi_x <= bar_x + 20:
        score = score + 1
        pyxel.play(0, 0)
```

::: point
音を作る `set` は、プログラムの最初に1回だけ。鳴らす `play` は、`update` の中の「起きた瞬間」に書きます。`draw` に書くと、毎フレーム鳴りつづけてしまいます。
:::

::: deep BGM（音楽）を流したいときは
いくつかの音を重ねた曲は、`pyxel.musics` で作って `pyxel.playm(0, loop=True)` で流します（[[px-playm]]）。曲作りは、文字で書くより **Pyxel Editor** のサウンドエディタとミュージックエディタを使うのがおすすめです。
:::

@@ game-shot
title: 弾を撃とう
type: 作品
chapter: 7
syntax: tama_list.append({"x": x, "y": y})
summary: スペースキーで弾を撃ちます。弾は辞書で作ってリストに入れ、画面の外に出た弾はリストから消します。
aliases: 弾, 発射, 撃つ, シューティング, 連射, たま
reads: tama=タマ | jibun=ジブン | nokori=ノコリ | append=アペンド
group: ゲームの技
--
## 弾は「たくさん」出てくる
弾は、撃つたびに1つずつ増えて、画面の上に消えていきます。何発出るか分からないので、[[game-list]]と同じように**リスト**で覚えます。

1つの弾には「横の位置」と「縦の位置」があります。これを[[dict]]で `{"x": 40, "y": 100}` のようにまとめて、リストに入れていきます。

## スペースで弾を撃つ
```python px gif frames=60 hold=KEY_SPACE
import pyxel

pyxel.init(160, 120, title="弾を撃つ")
jibun_x = 76
tama_list = []


def update():
    global jibun_x, tama_list
    if pyxel.btn(pyxel.KEY_LEFT):
        jibun_x = max(0, jibun_x - 2)
    if pyxel.btn(pyxel.KEY_RIGHT):
        jibun_x = min(152, jibun_x + 2)
    if pyxel.btnp(pyxel.KEY_SPACE, 8, 8):
        tama_list.append({"x": jibun_x + 3, "y": 100})
    nokori = []
    for tama in tama_list:
        tama["y"] = tama["y"] - 4
        if tama["y"] > -8:
            nokori.append(tama)
    tama_list = nokori


def draw():
    pyxel.cls(0)
    pyxel.tri(jibun_x, 112, jibun_x + 4, 104, jibun_x + 8, 112, 11)
    for tama in tama_list:
        pyxel.rect(tama["x"], tama["y"], 2, 6, 10)
    pyxel.text(4, 4, f"TAMA {len(tama_list)}", 7)


pyxel.run(update, draw)
```
画像は、スペースキーを押しつづけたときの様子です。

## 仕組みを読み解く
### 撃つ：リストに足す
スペースキーが押されたら、自分の上に新しい弾 `{"x": …, "y": 100}` を作って、`tama_list` に `append` します（[[list]]）。

`pyxel.btnp(pyxel.KEY_SPACE, 8, 8)` は、押した瞬間に1発、押しつづけると8フレームごとに1発、という**連射**の書き方です（[[px-btnp]]）。

### 動かす：全部の弾を上へ
`for tama in tama_list:` で弾を1つずつ取り出して、`tama["y"]` を4ずつ減らします。

### 消す：残す弾だけ、新しいリストに入れる
画面の上（`y` が `-8` より上）まで行った弾は、もう見えません。そのままにしておくと、リストがどんどん長くなって、ゲームが重くなります。

そこで、**まだ画面の中にある弾だけ**を、新しいリスト `nokori` に入れていきます。最後に `tama_list = nokori` として、残った弾だけのリストに入れかえます。画面左上の `TAMA` の数が、増えつづけないことを確かめよう。

::: point
「消したいものを消す」のではなく、「**残したいものだけ集めて、入れかえる**」。たくさんのものを消すときの、安全なやり方です。
:::

::: stuck
`tama_list = nokori` のように、変数そのものに新しいリストを入れているので、`global tama_list` が必要です（[[update-draw]]）。
:::

@@ game-enemy
title: 敵を出そう
type: 作品
chapter: 7
syntax: if pyxel.frame_count % 20 == 0:
summary: 一定の時間ごとに敵を出して、上から動かします。弾が当たったら、敵を消して点数を増やします。
aliases: 敵, 出現, てき, 撃ち落とす, シューティング, 点数
reads: teki=テキ | tama=タマ | atari=アタリ
group: ゲームの技
--
## 敵を、時間ごとに出す
「20フレームごとに1体」のように、時間を決めて敵を出すには、`pyxel.frame_count`（[[px-frame-count]]）と `%`（余り）を使います。

```python norun
if pyxel.frame_count % 20 == 0:
    teki_list.append({"x": pyxel.rndi(0, 152), "y": -8})
```
`frame_count % 20` は、20フレームごとに `0` になります。そのときだけ、画面の上の外（`y` が `-8`）に、新しい敵を足します。横の位置は[[px-rndi]]でランダムです。

## 撃って、当てる
[[game-shot]]の弾と組み合わせて、敵に当たったら消えるようにします。

```python px gif frames=120 hold=KEY_SPACE
import pyxel

pyxel.init(160, 120, title="敵を撃つ")
jibun_x = 76
tama_list = []
teki_list = []
score = 0


def update():
    global jibun_x, tama_list, teki_list, score
    if pyxel.btn(pyxel.KEY_LEFT):
        jibun_x = max(0, jibun_x - 2)
    if pyxel.btn(pyxel.KEY_RIGHT):
        jibun_x = min(152, jibun_x + 2)
    if pyxel.btnp(pyxel.KEY_SPACE, 8, 8):
        tama_list.append({"x": jibun_x + 3, "y": 100})
    if pyxel.frame_count % 20 == 0:
        teki_list.append({"x": pyxel.rndi(60, 92), "y": -8})

    for tama in tama_list:
        tama["y"] = tama["y"] - 4
    for teki in teki_list:
        teki["y"] = teki["y"] + 1

    for teki in teki_list:
        for tama in tama_list:
            if abs(teki["x"] + 4 - tama["x"]) < 6 and abs(teki["y"] + 4 - tama["y"]) < 6:
                teki["y"] = 999
                tama["y"] = -999
                score = score + 10

    tama_list = [tama for tama in tama_list if tama["y"] > -8]
    teki_list = [teki for teki in teki_list if teki["y"] < 120]


def draw():
    pyxel.cls(0)
    pyxel.tri(jibun_x, 112, jibun_x + 4, 104, jibun_x + 8, 112, 11)
    for tama in tama_list:
        pyxel.rect(tama["x"], tama["y"], 2, 6, 10)
    for teki in teki_list:
        pyxel.rect(teki["x"], teki["y"], 8, 8, 8)
    pyxel.text(4, 4, f"SCORE {score}", 7)


pyxel.run(update, draw)
```
画像は、スペースキーを押しつづけて、真ん中あたりの敵を撃っている様子です。

## 仕組みを読み解く
### 全部の敵 × 全部の弾を調べる
`for teki in teki_list:` の中に `for tama in tama_list:` を入れた**二重ループ**です。敵が3体、弾が5発あれば、3 × 5 ＝ 15 組の当たりを調べます。当たり判定は、[[game-hit]]の「近いかどうか（abs）」の方法です。

### 当たった敵と弾を、画面の外へ飛ばす
当たったら、敵の `y` を `999`（画面のずっと下）、弾の `y` を `-999`（ずっと上）にしています。こうしておくと、そのあとの「画面の外に出たものを消す」処理で、いっしょに消えます。消す処理を1か所にまとめられる工夫です。

### 1行で「残すものだけ集める」
```python norun
tama_list = [tama for tama in tama_list if tama["y"] > -8]
```
これは、[[game-shot]]で4行で書いた「残す弾だけ `nokori` に集める」を、1行で書いたものです。**リスト内包表記**といいます。

| 部分 | 意味 |
| --- | --- |
| `for tama in tama_list` | 弾を1つずつ取り出して |
| `if tama["y"] > -8` | 画面の中にある弾だけ |
| 最初の `tama` | それを集めて、新しいリストにする |

4行の書き方のほうが分かりやすければ、そちらで書いてもまったく問題ありません。

@@ game-scroll
title: スクロールさせよう
type: 作品
chapter: 7
syntax: pyxel.camera(camera_x, 0)
summary: 背景を動かして、進んでいるように見せる「スクロール」の作り方です。背景を流す方法と、カメラでキャラクターを追いかける方法の2つを学びます。
aliases: スクロール, 背景, カメラ, 横スクロール, 縦スクロール
reads: camera=カメラ | hoshizora=ホシゾラ
group: ゲームの技
--
## スクロールってなに？
画面の外まで続く広い世界を、少しずつ見せていくことを**スクロール**といいます。作り方は2つあります。

| 方法 | どんなゲーム？ |
| --- | --- |
| ① 背景を流す | 自分は画面の中にいて、背景が流れていく（宇宙を飛ぶゲームなど） |
| ② カメラで追いかける | 広い世界をキャラクターが歩いて、画面がついていく（アクションゲームなど） |

## 方法①：背景を流す
星を下に動かしつづけて、画面の下まで行ったら上に戻します。[[game-list]]の雪と同じ仕組みです。

```python px gif frames=60
import pyxel

pyxel.init(160, 120, title="星空スクロール")
hoshizora = []
for i in range(40):
    hoshizora.append({"x": pyxel.rndi(0, 159), "y": pyxel.rndi(0, 119), "hayasa": pyxel.rndi(1, 3)})


def update():
    for hoshi in hoshizora:
        hoshi["y"] = hoshi["y"] + hoshi["hayasa"]
        if hoshi["y"] > 120:
            hoshi["y"] = 0
            hoshi["x"] = pyxel.rndi(0, 159)


def draw():
    pyxel.cls(0)
    for hoshi in hoshizora:
        pyxel.pset(hoshi["x"], hoshi["y"], 7 if hoshi["hayasa"] == 3 else 5)
    pyxel.tri(76, 100, 80, 90, 84, 100, 11)


pyxel.run(update, draw)
```
自分（緑の三角）は止まっているのに、前に進んでいるように見えます。速い星を明るく、おそい星を暗くすると、遠くの星はゆっくり流れて見えて、奥行きが出ます（[[ternary]]）。

## 方法②：カメラで追いかける
幅480ドットの広い世界を作って、キャラクターが歩くと、画面がついていくようにします。

```python px gif frames=90 hold=KEY_RIGHT
import pyxel

pyxel.init(160, 120, title="カメラで追いかける")
x = 20


def update():
    global x
    if pyxel.btn(pyxel.KEY_LEFT):
        x = max(0, x - 2)
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = min(472, x + 2)


def draw():
    camera_x = min(max(x - 76, 0), 320)
    pyxel.cls(12)
    pyxel.camera(camera_x, 0)
    pyxel.rect(0, 100, 480, 20, 3)
    for i in range(6):
        pyxel.rect(40 + i * 80, 70, 16, 30, 4)
        pyxel.circ(48 + i * 80, 64, 14, 11)
    pyxel.rect(x, 92, 8, 8, 8)
    pyxel.camera()
    pyxel.text(4, 4, f"X {x}", 0)


pyxel.run(update, draw)
```
画像は、右キーを押しつづけて、木の並ぶ広い世界を歩いている様子です。

## 仕組みを読み解く
- 木もキャラクターも、**広い世界の中の位置**（0〜480）で描いている
- `pyxel.camera(camera_x, 0)` で、「世界の `camera_x` から先を、画面の左はしに見せる」ように、描く位置をまとめてずらす（[[px-camera]]）
- `camera_x = x - 76` で、キャラクターがいつも画面のまん中あたりに来る。`min` と `max` で、世界のはしより外は見せないようにしている（[[math-func]]）
- 点数などは画面に固定したいので、`pyxel.camera()` でずらすのをやめてから描く

::: deep マップを使ったスクロール
タイルマップで作った広いマップなら、[[px-bltm]]で切り取る場所 `u` を変えていく方法もあります。マップの作り方は[[game-map]]を見よう。
:::

@@ game-map
title: マップを作ろう
type: 作品
chapter: 7
syntax: mappu[y][x] == "#"
summary: 文字を並べた二次元リストで、迷路やステージのマップを作ります。マップを画面に描いて、壁のところは通れないようにします。
aliases: マップ, 迷路, ステージ, 壁, タイル, マス目
reads: mappu=マップ | masu=マス | tsugi=ツギ
group: ゲームの技
--
## マップを文字で書く
[[list2d]]で学んだように、文字を並べて、マップを作ります。

| 文字 | 意味 |
| --- | --- |
| `#` | 壁（通れない） |
| `.` | 道（通れる） |
| `G` | ゴール |

1文字を、画面の **8×8ドットのマス**として描きます。

## マス目を歩くゲーム
```python px gif frames=80 hold=KEY_RIGHT
import pyxel

mappu = [
    "####################",
    "#........#.........#",
    "#.####...#..####...#",
    "#....#......#......#",
    "####.#..#####..#####",
    "#....#.........#...#",
    "#.#######..###.#.#.#",
    "#.........#......#.#",
    "#..####...#.####.#.#",
    "#.....#.......#..#.#",
    "#..#..#..###..#...G#",
    "#..#...........#####",
    "#..#..####.........#",
    "####################",
]
pyxel.init(160, 112, title="マップ")
masu_x = 1
masu_y = 1


def update():
    global masu_x, masu_y
    tsugi_x = masu_x
    tsugi_y = masu_y
    if pyxel.btnp(pyxel.KEY_LEFT, 6, 6):
        tsugi_x = masu_x - 1
    if pyxel.btnp(pyxel.KEY_RIGHT, 6, 6):
        tsugi_x = masu_x + 1
    if pyxel.btnp(pyxel.KEY_UP, 6, 6):
        tsugi_y = masu_y - 1
    if pyxel.btnp(pyxel.KEY_DOWN, 6, 6):
        tsugi_y = masu_y + 1
    if mappu[tsugi_y][tsugi_x] != "#":
        masu_x = tsugi_x
        masu_y = tsugi_y


def draw():
    pyxel.cls(0)
    for y in range(len(mappu)):
        for x in range(len(mappu[y])):
            if mappu[y][x] == "#":
                pyxel.rect(x * 8, y * 8, 8, 8, 4)
            elif mappu[y][x] == "G":
                pyxel.rect(x * 8, y * 8, 8, 8, 10)
    pyxel.rect(masu_x * 8 + 1, masu_y * 8 + 1, 6, 6, 11)
    if mappu[masu_y][masu_x] == "G":
        pyxel.text(60, 52, "GOAL!", 7)


pyxel.run(update, draw)
```
画像は、右キーを押しつづけて、壁にぶつかって止まったところです。

## 仕組みを読み解く
### マスの番号と、画面の位置
キャラクターの位置は、ドットではなく**マスの番号**（`masu_x`、`masu_y`）で覚えています。画面に描くときだけ、`× 8` してドットに直します。

| マスの番号 | 画面の位置（ドット） |
| --- | --- |
| `masu_x = 3` | `3 * 8` ＝ 24 |

### マップを描く（二重ループ）
外側の `for y` で1行ずつ、内側の `for x` でその行の1文字ずつ調べて、`#` なら茶色、`G` なら黄色の四角を描きます。

### 壁は通さない
1. 動く前に、行きたい場所を `tsugi_x`、`tsugi_y` に計算する
2. `mappu[tsugi_y][tsugi_x]` が壁 `#` でなければ、そこへ動く
3. 壁なら、動かない

「動く前に、行き先を調べる」のが、マス目のゲームで壁を作るコツです。

::: stuck
`mappu[y][x]` の順番に注意しよう。二次元リストは `[たて][よこ]` なので、`mappu[masu_x][masu_y]` と逆に書くと、ちがう場所を調べてしまいます。
:::

::: deep もっと広いマップや、絵のついたマップ
マップが画面より大きいときは、[[game-scroll]]のカメラと組み合わせます。草や岩などの絵を使いたいときは、Pyxelの**タイルマップ**（[[px-tilemap-class]]・[[px-bltm]]）を使うと、Pyxel Editor で描いたマップをそのまま使えます。
:::

@@ game-jump
title: ジャンプさせよう
type: 作品
chapter: 7
syntax: vy = vy + 0.5 / y = y + vy
summary: キャラクターをジャンプさせて、重力で落ちてくるようにします。「上下の速さ」を変数にして、毎フレーム少しずつ下向きに増やすのがコツです。
aliases: ジャンプ, 重力, 落下, 地面, アクション
reads: vy=ブイワイ | jimen=ジメン | jimen_ni_iru=ジメンニイル
group: ゲームの技
--
## ジャンプは「速さ」で作る
ジャンプを「`y` を一気に20減らす」で作ると、ワープしたように見えてしまいます。本物っぽく動かすコツは、**上下の速さ** `vy` を変数にすることです。

| タイミング | すること |
| --- | --- |
| ジャンプした瞬間 | `vy` を上向き（マイナス）にする。例：`vy = -6` |
| 毎フレーム | `y = y + vy` で動かす |
| 毎フレーム | `vy = vy + 0.5` で、少しずつ下向きに変える（これが**重力**） |
| 地面についたら | `y` を地面に合わせて、`vy = 0` にする |

上向きの速さが、重力で少しずつ弱まって、てっぺんで止まり、今度は下向きにだんだん速くなります。ボールを上に投げたときと同じ動きです。

## スペースでジャンプ
```python px gif frames=40 hold=KEY_SPACE
import pyxel

pyxel.init(160, 120, title="ジャンプ")
jimen = 92
x = 76
y = jimen
vy = 0


def update():
    global x, y, vy
    if pyxel.btn(pyxel.KEY_LEFT):
        x = x - 2
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 2
    jimen_ni_iru = y >= jimen
    if jimen_ni_iru and pyxel.btnp(pyxel.KEY_SPACE):
        vy = -6
    vy = vy + 0.5
    y = y + vy
    if y >= jimen:
        y = jimen
        vy = 0


def draw():
    pyxel.cls(12)
    pyxel.rect(0, 100, 160, 20, 3)
    pyxel.rect(x, y, 8, 8, 8)


pyxel.run(update, draw)
```
画像は、スペースキーを押して、1回ジャンプしたときの様子です。

## 仕組みを読み解く
- `vy = -6`：ジャンプした瞬間に、上向きの速さ 6 をつける（上はマイナス。[[coordinate]]）
- `vy = vy + 0.5`：毎フレーム、下向きに 0.5 ずつ強くなる。これが重力
- `if y >= jimen:`：地面より下に行こうとしたら、地面の上にもどして、速さを 0 にする
- `jimen_ni_iru`：地面にいるときだけ `True` になる変数（[[bool]]）。空中ではジャンプできないようにしている

::: point
ジャンプの高さを変えたいときは `-6` を、ふわっと感を変えたいときは重力の `0.5` を変えてみよう。数字を少し変えるだけで、ゲームの手ざわりががらっと変わります。
:::

::: stuck
`jimen_ni_iru` の確かめを入れないと、空中でもスペースを押すたびにジャンプできて、どこまでも上に飛んでいってしまいます（それはそれで「空を飛ぶゲーム」になりますが）。
:::

@@ game-wall
title: 壁にぶつかったら止めよう（押し戻し）
type: 作品
chapter: 7
syntax: 動く前の位置を覚えて、壁に重なったら戻す
summary: キャラクターが壁を通りぬけないようにする方法です。動いたあとで壁と重なっていたら、動く前の位置に戻します。
aliases: 押し戻し, 壁, すり抜け, ぶつかる, 当たり判定
reads: mae_x=マエエックス | kabe_list=カベリスト | kasanatteru=カサナッテル
group: ゲームの技
--
## 「戻す」だけで壁になる
[[game-map]]では、マス目ごとに「行き先が壁か」を調べました。1ドットずつなめらかに動くゲームでは、こう考えます。

1. 動く前の位置を、`mae_x` と `mae_y` に覚えておく
2. ふつうに動く
3. もし壁と重なっていたら（[[game-hit]]）、`mae_x` と `mae_y` に**戻す**

壁にめりこんだ瞬間に元に戻るので、見た目には「壁で止まった」ように見えます。

## 壁のある部屋
```python px gif frames=60 hold=KEY_RIGHT
import pyxel

pyxel.init(160, 120, title="押し戻し")
kabe_list = [(0, 0, 160, 8), (0, 112, 160, 8), (0, 0, 8, 120), (152, 0, 8, 120), (90, 30, 12, 60)]
x = 30
y = 56


def kasanatteru(x1, y1, w1, h1, x2, y2, w2, h2):
    return x1 < x2 + w2 and x2 < x1 + w1 and y1 < y2 + h2 and y2 < y1 + h1


def kabe_ni_atatta():
    for kabe in kabe_list:
        if kasanatteru(x, y, 8, 8, kabe[0], kabe[1], kabe[2], kabe[3]):
            return True
    return False


def update():
    global x, y
    mae_x = x
    if pyxel.btn(pyxel.KEY_LEFT):
        x = x - 2
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 2
    if kabe_ni_atatta():
        x = mae_x
    mae_y = y
    if pyxel.btn(pyxel.KEY_UP):
        y = y - 2
    if pyxel.btn(pyxel.KEY_DOWN):
        y = y + 2
    if kabe_ni_atatta():
        y = mae_y


def draw():
    pyxel.cls(1)
    for kabe in kabe_list:
        pyxel.rect(kabe[0], kabe[1], kabe[2], kabe[3], 13)
    pyxel.rect(x, y, 8, 8, 10)


pyxel.run(update, draw)
```
画像は、右キーを押しつづけて、まん中の壁にぶつかって止まったところです。

## 仕組みを読み解く
- 壁は、`(x, y, 幅, 高さ)` の[[tuple]]にして、`kabe_list` に並べている
- `kabe_ni_atatta()` は、全部の壁を調べて、1つでも重なっていれば `True` を返す関数（[[function]]・[[return]]）
- **横の移動と、縦の移動を分けて**戻しているのがポイント

### なぜ横と縦を分けるの？
もし右上へななめに動いて壁に当たったとき、横と縦をまとめて戻すと、キャラクターが壁にはりついて動けなくなります。横と縦を分けて戻すと、「横は壁で止まるけど、縦にはすべって動ける」ようになって、気持ちよく動かせます。

::: deep もっとぴったり止めたいとき
この方法では、1回に動く量（ここでは2ドット）の分だけ、壁の手前で止まることがあります。ぴったり壁にくっつけたいときは、1ドットずつ動かして調べたり、重なった分だけ押し戻す計算をしたりする方法があります。
:::

@@ game-effect
title: エフェクトをつけよう（爆発・ゆれ・無敵）
type: 作品
chapter: 7
syntax: pyxel.camera(ゆれ, ゆれ) / if pyxel.frame_count % 4 < 2:
summary: 爆発の輪、画面のゆれ、やられたあとの点滅（無敵時間）。ゲームを気持ちよくする「演出」の作り方です。
aliases: エフェクト, 爆発, 画面ゆれ, 振動, 無敵, 点滅, 演出
reads: bakuhatsu=バクハツ | yure=ユレ | muteki=ムテキ
group: ゲームの技
--
## 爆発の輪
当たったところに、輪がだんだん大きくなって消える「爆発」を出します。爆発も、[[game-shot]]の弾と同じように、辞書のリストで管理します。

```python px gif frames=12 press=KEY_SPACE@2
import pyxel

pyxel.init(160, 120, title="爆発")
bakuhatsu_list = []
yure = 0


def update():
    global bakuhatsu_list, yure
    if pyxel.btnp(pyxel.KEY_SPACE):
        bakuhatsu_list.append({"x": 80, "y": 60, "r": 0})
        yure = 10
    for b in bakuhatsu_list:
        b["r"] = b["r"] + 1
    bakuhatsu_list = [b for b in bakuhatsu_list if b["r"] < 16]
    if yure > 0:
        yure = yure - 1


def draw():
    pyxel.cls(0)
    pyxel.camera(pyxel.rndi(-yure, yure) // 3, pyxel.rndi(-yure, yure) // 3)
    pyxel.rect(70, 50, 20, 20, 13)
    for b in bakuhatsu_list:
        pyxel.circb(b["x"], b["y"], b["r"], 10 if b["r"] < 8 else 8)
    pyxel.camera()


pyxel.run(update, draw)
```
スペースキーを押すと、まん中で爆発が起きて、画面がゆれます。

### 爆発の輪
- 爆発は `{"x": 80, "y": 60, "r": 0}`。`r` は輪の半径
- 毎フレーム `r` を1ずつ大きくして、`circb`（ふちだけの円）で描く（[[px-circb]]）
- 半径が16になったら、リストから消す（[[game-enemy]]の1行で集める書き方）
- 小さいうちは黄色、大きくなったら赤にして、熱が冷めていく感じを出している（[[ternary]]）

### 画面のゆれ
- `yure` は「あと何フレームゆれるか」。爆発したら10にして、毎フレーム1ずつ減らす
- `pyxel.camera(…)` で、描く位置をランダムに少しずらす（[[px-camera]]）。`yure` が小さくなるほど、ゆれも小さくなって、自然におさまる

## 無敵時間（点滅）
敵にぶつかったあと、しばらくやられないようにする時間を**無敵時間**といいます。無敵のあいだは、キャラクターを点滅させて、プレイヤーに知らせます。

```python px gif frames=60 press=KEY_SPACE@2
import pyxel

pyxel.init(160, 120, title="無敵時間")
muteki = 0


def update():
    global muteki
    if pyxel.btnp(pyxel.KEY_SPACE) and muteki == 0:
        muteki = 60
    if muteki > 0:
        muteki = muteki - 1


def draw():
    pyxel.cls(1)
    if muteki == 0 or pyxel.frame_count % 4 < 2:
        pyxel.rect(76, 56, 8, 8, 11)
    pyxel.text(48, 100, f"MUTEKI {muteki}", 7)


pyxel.run(update, draw)
```
スペースキーを（敵にぶつかった代わりに）押すと、2秒間（60フレーム）点滅します。

- `muteki` は「あと何フレーム無敵か」。0のときは、ふつうの状態
- `pyxel.frame_count % 4 < 2` は、4フレームのうち2フレームだけ `True`。そのときだけ描くので、チカチカ点滅して見える（[[px-frame-count]]）
- 当たり判定のところで `muteki == 0` のときだけやられるようにすれば、無敵時間のできあがり

::: point
「あと何フレーム続くか」を数える変数を作って、毎フレーム1ずつ減らす。爆発、ゆれ、無敵時間、どれも同じ考え方です。
:::

@@ game-highscore
title: ハイスコアとランキングを作ろう
type: 作品
chapter: 7
syntax: ranking.sort(reverse=True)
summary: いちばん良かった点数（ハイスコア）を覚えておいて、ゲームをやり直しても残るようにします。上位3つのランキングも作ります。
aliases: ハイスコア, 最高点, ランキング, 記録, ソート, 並べかえ
reads: high_score=ハイスコア | ranking=ランキング | sort=ソート | reverse=リバース
group: ゲームの技
--
## ハイスコアは「上書きしない」変数
`score` は、ゲームを始めるたびに0に戻します。でも、**ハイスコア**（いちばん良かった点数）は戻しません。ゲームが終わったときに、今回の点数がハイスコアより大きければ、入れかえます。

```python
high_score = 0
for score in [12, 30, 25]:
    if score > high_score:
        high_score = score
print(high_score)
```
3回遊んで、点数が12、30、25だったとき、ハイスコアは30です。`max(high_score, score)` と書いても同じです（[[math-func]]）。

## 上位3つのランキング
```python
ranking = [12, 30, 25]
ranking.append(41)
ranking.sort(reverse=True)
ranking = ranking[:3]
print(ranking)
```
1. 今回の点数を `append` で足す
2. `sort(reverse=True)` で、大きい順に並べかえる（[[list]]）
3. `[:3]` で、上から3つだけ残す（[[list-index]]のスライス）

## 連打ゲームにつける
[[game-scene]]の5秒連打ゲームに、ハイスコアとランキングをつけます。

```python px frames=10
import pyxel

pyxel.init(160, 120, title="ランキング")
gamen = "kekka"
score = 23
ranking = [31, 18, 9]


def kekka_ni_suru():
    global gamen, ranking
    gamen = "kekka"
    ranking.append(score)
    ranking.sort(reverse=True)
    ranking = ranking[:3]


def update():
    global gamen
    if gamen == "kekka" and pyxel.btnp(pyxel.KEY_R):
        gamen = "title"


def draw():
    pyxel.cls(0)
    if gamen == "kekka":
        pyxel.text(52, 20, f"SCORE {score}", 10)
        pyxel.text(52, 40, f"HIGH  {ranking[0]}", 11)
        for i in range(len(ranking)):
            pyxel.text(52, 60 + i * 10, f"{i + 1}. {ranking[i]}", 7)


kekka_ni_suru()
pyxel.run(update, draw)
```
確かめやすいように、はじめから「点数23で結果画面になった」ところを表示しています。

- `kekka_ni_suru()` は、ゲームが終わったときに1回だけ呼ぶ関数。ここで、点数をランキングに入れる
- ランキングの0番（`ranking[0]`）が、いつもハイスコアになる
- 連打ゲームでは、`nokori <= 0` になったところで `gamen = "kekka"` と書くかわりに、`kekka_ni_suru()` を呼びます

::: point
ランキングは、**ゲームが終わったときに1回だけ**入れます。`update` に書くと、毎フレーム同じ点数が入ってしまいます。
:::

::: deep パソコンを閉じても残したいときは
このハイスコアは、プログラムを終わらせると消えてしまいます。ずっと残したいときは、点数を**ファイルに書いて保存**して、次に起動したときに読みこみます。Pythonの `open()` という関数を使います。
:::
