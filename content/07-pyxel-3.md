@@ app-fortune
title: 占いアプリを作ろう
type: 作品
chapter: 7
syntax: ボタンを押すと、ランダムに結果が出る
summary: ボタンをクリックすると、おみくじの結果がランダムに出るアプリ。マウス・リスト・randomの、まとめの作品です。
aliases: 占い, おみくじ, うらない, アプリ
reads: random=ランダム | randint=ランディント | Font=フォント | mouse_x=マウスエックス
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

@@ game-image
title: 画像を表示して動かそう
type: 作品
chapter: 7
syntax: pyxel.blt(x, y, 0, u, v, 8, 8, 0)
summary: ドット絵のキャラクターを blt で画面に出して、キーで動かします。透明色・アニメーション・左右の向きの変え方も学びます。
aliases: 画像, ドット絵, キャラクター, スプライト, アニメーション, 歩く, 反転
reads: blt=ブリット | images=イメージズ | muki=ムキ
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
`images[0].set(0, 0, […])` で、イメージバンク0番の左上に、8×8のひよこを描いています。1文字が1ドットで、`a` が黄色、`1` が目、`9` がくちばし、`0` が何もないところです（[[px-image-class]]）。

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
