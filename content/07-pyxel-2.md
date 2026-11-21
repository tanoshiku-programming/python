@@ pyxel-text
title: 文字を表示してみよう
type: 命令
chapter: 7
syntax: pyxel.text(x, y, "文字", 色)
summary: pyxel.text で、画面の好きな場所に、好きな色で、文字を書きます。はじめは英数字だけです。
aliases: text, テキスト, 文字を出す, 文字表示
reads: text=テキスト | cls=クリアスクリーン | str=ストリング
group: Pyxelの基本
--
## 書き方のかたち
::: tpl 文字の書き方
pyxel.text(〔x〕, 〔y〕, "〔文字〕", 〔色〕)

| 〔x〕 | 文字の左はしの位置（左から何ドット目か） |
| 〔y〕 | 文字の上はしの位置（上から何ドット目か） |
| 〔文字〕 | 書きたい文字。`"` で囲む（[[str]]） |
| 〔色〕 | 0〜15 の色の番号（[[color]]） |
:::

## まず、書いてみる
```python px
import pyxel

pyxel.init(160, 120, title="文字を書く")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(10, 10, "HELLO PYXEL!", 7)
    pyxel.text(10, 30, "RED", 8)
    pyxel.text(10, 40, "YELLOW", 10)
    pyxel.text(10, 50, "GREEN", 11)


pyxel.run(update, draw)
```
`pyxel.text(x, y, "文字", 色)` の順に書きます。詳しい説明は辞典の[[px-text]]、位置の決め方は[[coordinate]]を見よう。

::: point
画面に描く命令は、**`draw` の中**に書きます。`draw` の最初には、`pyxel.cls(色)` で画面を塗りつぶします（[[px-cls]]）。
:::

## 数や変数も表示できる
数を表示したいときは、[[typeconv]]の `str()` で文字に変えます。[[fstring]]を使うと、もっと簡単に書けます。

```python px
import pyxel

pyxel.init(160, 120, title="スコア")
score = 120


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(10, 10, "SCORE: " + str(score), 7)
    pyxel.text(10, 24, f"SCORE x2: {score * 2}", 10)


pyxel.run(update, draw)
```

::: stuck
`pyxel.text(10, 10, "SCORE: " + score, 7)` のように、数の `score` をそのまま `+` でつなげると、`TypeError` になります。`str(score)` に変えよう（[[error]]）。
:::

## 日本語はそのままでは出ない

```python px
import pyxel

pyxel.init(160, 120, title="日本語だとどうなる？")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(10, 10, "ABC abc 123", 7)
    pyxel.text(10, 30, "こんにちは", 7)


pyxel.run(update, draw)
```
英語と数字は出ますが、日本語は出ません（何も表示されません）。日本語の出し方は、[[pyxel-jp]]で学びます。

@@ shapes
title: いろいろな図形をかいてみよう
type: 命令
chapter: 7
syntax: pyxel.rect(x, y, 幅, 高さ, 色)
summary: 点・線・四角・円・だ円・三角形を描く命令があります。「b」がつくと、ふちだけです。
aliases: 図形, rect, circ, line, pset, tri, 四角, 円, 線, 三角
reads: pset=ピーセット | line=ライン | rect=レクト | rectb=レクトビー | circ=サーク | circb=サークビー | elli=エリ | tri=トライ
group: Pyxelの基本
--
## 書き方のかたち
::: tpl 四角と円の書き方
pyxel.rect(〔x〕, 〔y〕, 〔幅〕, 〔高さ〕, 〔色〕)
pyxel.circ(〔x〕, 〔y〕, 〔半径〕, 〔色〕)

| 〔x〕 | 四角は左上の位置。円は**真ん中**の位置 |
| 〔幅〕 | 四角の横の長さ（ドット） |
| 〔高さ〕 | 四角の縦の長さ（ドット） |
| 〔半径〕 | 円の半径（真ん中からふちまでの長さ） |
| 〔色〕 | 0〜15 の色の番号 |
:::

## 図形の一覧
| 描きたいもの | 命令 | ふちだけ |
| --- | --- | --- |
| 点 | [[px-pset]] | |
| 線 | [[px-line]] | |
| 四角 | [[px-rect]] | [[px-rectb]] |
| 円 | [[px-circ]] | [[px-circb]] |
| だ円 | [[px-elli]] | [[px-ellib]] |
| 三角形 | [[px-tri]] | [[px-trib]] |

名前の最後に **b**（border＝ふち）がつくと、中を塗らずにふちだけを描きます。

## 全部、描いてみる
```python px
import pyxel

pyxel.init(160, 120, title="図形")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 40, 30, 8)
    pyxel.rectb(60, 10, 40, 30, 10)
    pyxel.circ(25, 70, 15, 11)
    pyxel.circb(75, 70, 15, 12)
    pyxel.line(110, 10, 150, 40, 14)
    pyxel.tri(110, 100, 130, 60, 150, 100, 9)
    pyxel.elli(105, 45, 50, 10, 6)


pyxel.run(update, draw)
```

## 絵を描いてみよう
図形を重ねると、絵になります。**あとから描いたものが上に重なります。** Scratchの「最前面へ移動」のように、描く順番が重なり方を決めます。

```python px
import pyxel

pyxel.init(160, 120, title="おうち")


def update():
    pass


def draw():
    pyxel.cls(12)
    pyxel.rect(0, 90, 160, 30, 3)
    pyxel.rect(50, 55, 60, 40, 9)
    pyxel.tri(45, 55, 80, 25, 115, 55, 8)
    pyxel.rect(72, 70, 16, 25, 4)
    pyxel.circ(135, 25, 10, 10)


pyxel.run(update, draw)
```
空・地面・家・屋根・ドア・太陽の順で描いています。順番を入れ替えると、どうなるかな？

::: stuck
背景の `pyxel.cls` を**最後に**書いてしまうと、描いた図形が全部消えてしまいます。`cls` は `draw` の**いちばん最初**に書きます。
:::

@@ pyxel-var
title: 変数を使ってみよう
type: 考え方
chapter: 7
syntax: x = x + 2
summary: 位置や速さを変数にして、update で変えると、図形が動きます。壁で、跳ね返らせることもできます。
aliases: 変数, 動かす, アニメーション, 速度, はね返り
reads: global=グローバル | frame_count=フレームカウント
group: Pyxelの基本
--
## 変数で、動かす
図形の位置を `pyxel.circ(20, 60, …)` のように**数字のまま**書くと、止まったままです。位置を**変数**にして `update` の中で変えると、動きます（[[variable]]）。

```python px gif frames=60
import pyxel

pyxel.init(160, 120, title="うごく円")
x = 20
y = 60


def update():
    global x
    x = x + 2


def draw():
    pyxel.cls(0)
    pyxel.circ(x, y, 8, 10)


pyxel.run(update, draw)
```
円は右へ進んで、画面の外に消えていきます。`x` を2ずつ増やし続けているからです。

## 速さも変数にする
「何ドットずつ動くか」も変数にしておくと、あとで変えやすくなります。

```python px gif frames=90
import pyxel

pyxel.init(160, 120, title="はね返る円")
x = 20
dx = 3


def update():
    global x, dx
    x = x + dx
    if x > 150 or x < 10:
        dx = -dx


def draw():
    pyxel.cls(0)
    pyxel.circ(x, 60, 10, 8)


pyxel.run(update, draw)
```
`dx` は「1回で動く量」です。壁に当たったら `dx = -dx` で**プラスとマイナスを入れ替えて**、向きを逆にします（[[if]]・[[logical]]）。`dx` が `3` なら `-3` に、`-3` なら `3` になります。Scratchの「もし端に着いたら、跳ね返る」を、自分で作っているのと同じです。

## よく使う変数
| 変数の名前 | 入れるもの |
| --- | --- |
| `x`, `y` | 場所 |
| `dx`, `dy` | 1回で動く量（速さと向き） |
| `score` | 点数 |
| `life` | 残りのライフ |

`dx` の `d` は、**difference（ディファレンス）＝差**の頭文字です。「x がどれだけ変わるか」という意味で、ゲームを作る本や見本のプログラムでもよく使われる名前なので、このサイトでもそのまま使っています。

::: point
**`update` で変数を変えて、`draw` で変数を使って描く。** これが、動くものを作る基本のかたちです。
:::

::: stuck
`update` の中で変数を書き換えるのに `global x` を書き忘れると、エラーになります。書き換える変数は、`global x, dx` のように**全部**並べて書きます（[[scope]]）。
:::

## もうひとつの変数：frame_count
Pyxelには、はじめから用意されている変数もあります。`pyxel.frame_count` は、**ゲームが始まってから進んだフレーム数**です。時間によって何かを変えたいときに使えます（Scratchの「タイマー」に近いものです）。

```python px gif frames=60
import pyxel

pyxel.init(160, 120, title="点滅")


def update():
    pass


def draw():
    pyxel.cls(0)
    if pyxel.frame_count % 20 < 10:
        pyxel.text(55, 57, "PUSH START", 10)


pyxel.run(update, draw)
```
`%` は割り算の余りを出す[[operator]]です。`frame_count % 20` は 0, 1, 2, …, 19, 0, 1, … と繰り返すので、そのうち10未満のときだけ文字を出すと、10フレームごとに文字が出たり消えたりします。

@@ pyxel-key
title: キー操作をやってみよう
type: 命令
chapter: 7
syntax: pyxel.btn(pyxel.KEY_LEFT)
summary: btn でキーが押されているかを調べて、キャラクターを動かします。btnp は、押した瞬間だけです。
aliases: キー, btn, btnp, キーボード, 操作, 矢印キー
reads: btn=ボタン | btnp=ボタンピー | KEY_LEFT=キーレフト
group: Pyxelの基本
--
## 書き方のかたち
::: tpl キーを調べる書き方
if pyxel.btn(pyxel.KEY_〔キー名〕):
····〔押されているときの処理〕

| 〔キー名〕 | LEFT（左）、RIGHT（右）、UP（上）、DOWN（下）、SPACE、A〜Z など |
| 〔押されているときの処理〕 | 押されているあいだ、毎フレーム実行される |
:::

## 矢印キーで動かす
`update` の中でキーが押されているかを調べて、位置の変数を変えます（[[if]]）。Scratchの「もし（右向き矢印）キーが押されたなら」と同じ考え方です。

```python px gif frames=30 hold=KEY_RIGHT
import pyxel

pyxel.init(160, 120, title="キーで動かす")
x = 76
y = 56


def update():
    global x, y
    if pyxel.btn(pyxel.KEY_LEFT):
        x = x - 2
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 2
    if pyxel.btn(pyxel.KEY_UP):
        y = y - 2
    if pyxel.btn(pyxel.KEY_DOWN):
        y = y + 2


def draw():
    pyxel.cls(0)
    pyxel.rect(x, y, 8, 8, 10)


pyxel.run(update, draw)
```
画像は、右キーを押しつづけたときの様子です。実際に動かすと、あなたのキー操作で動きます。

::: point
**上はマイナス、下はプラス**。Pyxelは、下に行くほど `y` が大きくなるからです（[[coordinate]]）。
:::

## btn と btnp のちがい
| 命令 | True になるとき | 使いどころ |
| --- | --- | --- |
| [[px-btn]] | **押しているあいだ**ずっと | 歩く、動かす |
| [[px-btnp]] | **押した瞬間**の1回だけ | ジャンプ、決定、切り替え |

```python px press=KEY_SPACE@5 frames=15
import pyxel

pyxel.init(160, 120, title="スペースで色が変わる")
iro = 8


def update():
    global iro
    if pyxel.btnp(pyxel.KEY_SPACE):
        iro = iro + 1


def draw():
    pyxel.cls(0)
    pyxel.rect(60, 40, 40, 40, iro)
    pyxel.text(40, 100, "PUSH SPACE", 7)


pyxel.run(update, draw)
```
スペースキーを1回押すごとに、色の番号が1つ増えます。`btn` だと、押しているあいだ毎フレーム（1秒に30回）変わってしまいます。

## 画面の外に出ないように
`min()` は「小さいほう」、`max()` は「大きいほう」を選ぶ関数です（[[list]]でも出てきました）。この2つを組み合わせると、はみ出しを止められます。

```python norun
x = max(0, min(152, x))
```
- `min(152, x)`：`x` が152より大きくなったら、152にする
- `max(0, …)`：0より小さくなったら、0にする

これで `x` は0〜152の範囲におさまります。152は「画面の幅160 − 四角の幅8」です。同じことは辞典の[[px-clamp]]でも書けます。

@@ pyxel-mouse
title: マウス操作をやってみよう
type: 命令
chapter: 7
syntax: pyxel.mouse_x / pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
summary: マウスの位置は mouse_x と mouse_y。クリックは、btnp に MOUSE_BUTTON_LEFT を渡して調べます。
aliases: マウス, クリック, mouse_x, mouse_y, ボタン
reads: mouse=マウス | mouse_x=マウスエックス | mouse_y=マウスワイ | click=クリック
group: Pyxelの基本
--
## マウスの位置と、クリック
| 知りたいこと | 書き方 |
| --- | --- |
| マウスの横の位置 | `pyxel.mouse_x` |
| マウスの縦の位置 | `pyxel.mouse_y` |
| 左クリックした | `pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)` |
| マウスの矢印を表示する | `pyxel.mouse(True)` |

Pyxelの画面では、はじめはマウスの矢印が見えません。`pyxel.mouse(True)` を `init` の下に書くと見えるようになります（[[px-mouse]]）。

## マウスの場所に、円を描く
```python px click=100,40
import pyxel

pyxel.init(160, 120, title="マウスで円")
pyxel.mouse(True)


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, 6, 10)


pyxel.run(update, draw)
```

## ボタンを作る
四角を「ボタン」にして、クリックされたかを調べます。クリックしたときに、マウスの場所が四角の中にあるかを[[if]]で調べます。

```python px click=80,50 frames=20
import pyxel

pyxel.init(160, 120, title="ボタン")
pyxel.mouse(True)
count = 0


def update():
    global count
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        if 40 <= pyxel.mouse_x <= 120 and 40 <= pyxel.mouse_y <= 60:
            count = count + 1


def draw():
    pyxel.cls(1)
    pyxel.rect(40, 40, 80, 20, 8)
    pyxel.text(62, 47, "CLICK ME", 7)
    pyxel.text(40, 80, "COUNT: " + str(count), 10)


pyxel.run(update, draw)
```
四角は `rect(40, 40, 80, 20, …)` なので、横は40から120（40 + 80）、縦は40から60（40 + 20）までです。「x が40〜120 **かつ** y が40〜60」なら、ボタンの中をクリックしたことになります（[[logical]]の `and`）。

::: point
ボタンは、「**四角を描く**」（draw）と「**その範囲をクリックしたか調べる**」（update）の2つで作ります。
:::

@@ pyxel-jp
title: 日本語を表示しよう
type: 命令
chapter: 7
syntax: font = pyxel.Font("umplus_j12r.bdf")
summary: 日本語は、フォントファイルを読みこんで、pyxel.text の最後に渡すと表示できます。
aliases: 日本語, フォント, Font, bdf, 漢字
reads: Font=フォント | text=テキスト | bdf=ビーディーエフ
group: Pyxelの基本
--
## 日本語が出ない理由
Pyxelの文字は、はじめは**英数字だけ**です。日本語を出すには、日本語の文字が入った**フォントファイル**を読みこみます。

## 準備：フォントファイルをコピーする
Pyxelには、練習用のフォントファイルが付いています。ターミナルで次のコマンドを実行すると、見本のプログラムとフォントが、今いるフォルダにコピーされます。

```bash
pyxel copy_examples
```
コピーされた `pyxel_examples` フォルダの中の `assets` フォルダに、`umplus_j10r.bdf`（小さめの文字）と `umplus_j12r.bdf`（大きめの文字）があります。使いたいほうを、**自分のプログラム（.py ファイル）と同じフォルダ**に置きます。

## 書き方のかたち
::: tpl 日本語の書き方
〔変数〕 = pyxel.Font("〔フォントのファイル名〕")
pyxel.text(〔x〕, 〔y〕, "〔日本語〕", 〔色〕, 〔変数〕)

| 〔変数〕 | 読みこんだフォントを入れる名前（font など） |
| 〔フォントのファイル名〕 | umplus_j12r.bdf など。同じフォルダに置く |
| 〔日本語〕 | 書きたい文章 |
:::

## 書いてみる
```python px
import pyxel

pyxel.init(160, 120, title="日本語")
font = pyxel.Font("umplus_j12r.bdf")


def update():
    pass


def draw():
    pyxel.cls(1)
    pyxel.text(10, 10, "こんにちは！", 7, font)
    pyxel.text(10, 30, "Pyxelで日本語", 10, font)
    pyxel.text(10, 50, "漢字もOK", 11, font)


pyxel.run(update, draw)
```
`pyxel.Font("…")` は、フォントファイルを読みこむ命令です（[[px-font-class]]）。日本語を書くときは、`pyxel.text` の**いちばん最後**に、読みこんだフォント `font` をつけます。

::: stuck
`Exception: Failed to open file 'umplus_j12r.bdf'`（ファイルを開けませんでした）と出たら、フォントファイルが見つかっていません。フォントファイルが、プログラム（.py）と同じフォルダにあるか確かめよう（[[error]]）。ファイル名のつづり（`umplus_j12r.bdf`）も確かめよう。
:::

::: deep もっと知りたい人へ
`font.text_width("文字")` で、その文字を書いたときの横の長さ（ドット数）が分かります。画面の真ん中にそろえたいときに使えます。

```python norun
haba = font.text_width("こんにちは")
pyxel.text((160 - haba) // 2, 50, "こんにちは", 7, font)
```
:::
