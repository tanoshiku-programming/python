@@ ch9
title: Pyxel辞典
kind: chapter
chapter: 9
summary: Pyxelの関数・変数・クラスを、辞書のように引ける一覧です。分類ごとの表と名前順の早見から探せます。
--
## この辞典の使い方
Pyxelの命令を**1つずつ**詳しく説明したページが集まっています。コードの中の `pyxel.○○` の言葉をクリックしても、ここに来られます。

- **分類から探す**：下の表から、したいことに近いものを選ぶ
- **名前から探す**：いちばん下の「名前順の早見」から選ぶ
- **言葉で探す**：画面上の検索ボックスに `rect` や「四角」と入れる

::: point
`pyxel.` のついた命令を使う前に、プログラムの最初で `import pyxel` と `pyxel.init(…)` を書くのを忘れずに（[[window]]）。
:::

::: refindex
:::

@@ px-init
title: init（画面の準備）
type: Pyxelの命令
chapter: 9
group: 基本
syntax: pyxel.init(幅, 高さ, title=タイトル, fps=30)
summary: ゲームの最初に1回だけ書く命令。画面（ウィンドウ）の大きさを決めて、Pyxelを使える状態にします。
aliases: イニット, 初期化, ウィンドウ, 画面サイズ
api: init
reads: init=イニット | title=タイトル | fps=エフピーエス
--
## 書き方のかたち
::: tpl init の書き方
pyxel.init(〔幅〕, 〔高さ〕, title="〔タイトル〕", fps=〔fps〕)

| 〔幅〕 | 画面の横の大きさ（ドット数）。必ず書く |
| 〔高さ〕 | 画面の縦の大きさ（ドット数）。必ず書く |
| 〔タイトル〕 | ウィンドウの上に出る名前。なくてもOK |
| 〔fps〕 | 1秒に何回画面を描き換えるか。書かなければ30 |
:::

## どんな命令？
`init` は **initialize（イニシャライズ）＝はじめの準備**を短くした言葉です。ゲームを始める前に「**画面の大きさはこれだよ**」とPyxelに教えます。

Pyxelの命令は、**`init` を呼んでから**でないと使えません。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="init")


def update():
    pass


def draw():
    pyxel.cls(5)
    pyxel.text(8, 8, "pyxel.init(160, 120)", 7)
    pyxel.rectb(0, 0, 160, 120, 7)


pyxel.run(update, draw)
```

画面の大きさは 160 × 120 がよく使われます。数字は小さく見えても、ウィンドウは自動で拡大されます。

- 幅と高さには、**ドットの数**を書きます
- `title=` と `fps=` は、名前をつけて書く引数です（[[argument]]）
- `fps` を増やすと動きがなめらかになりますが、`update` が呼ばれる回数も増えるので、動きも速くなります。ふつうは変えません

::: stuck
`pyxel.init` を2回書いたり、`run` の後に書いたりしないように注意しよう。**プログラムの最初に1回だけ**です。詳しくは[[window]]を見よう。
:::

@@ px-run
title: run（ゲームを動かす）
type: Pyxelの命令
chapter: 9
group: 基本
syntax: pyxel.run(update, draw)
summary: update と draw を1秒に30回繰り返し呼び出して、ゲームを動かしはじめる命令です。
aliases: ラン, 実行, 動かす, ゲームループ
api: run
reads: run=ラン | update=アップデート | draw=ドロー
--
## 書き方のかたち
::: tpl run の書き方
pyxel.run(〔update関数〕, 〔draw関数〕)

| 〔update関数〕 | 動かす係の関数の**名前**（`()` はつけない） |
| 〔draw関数〕 | 描く係の関数の**名前**（`()` はつけない） |
:::

## どんな命令？
`run` を書くと、ウィンドウが開いてゲームが動きはじめます。あなたが作った `update` と `draw` を、**1秒に30回ずつ**繰り返し呼び出します。

`run` は**プログラムのいちばん最後**に書きます。ウィンドウを閉じる（または ESC を押す）まで、`run` の次の行には進みません。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="run")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(30, 50, "pyxel.run(update, draw)", 7)


pyxel.run(update, draw)
```

詳しい仕組みは[[update-draw]]を見よう。

::: stuck
`pyxel.run(update(), draw())` のように `()` をつけると、エラーになります。ここでは関数を**呼び出す**のではなく、Pyxelに**渡す**ので、名前だけを書きます（[[window]]）。
:::

@@ px-show
title: show（画面を表示して待つ）
type: Pyxelの命令
chapter: 9
group: 基本
syntax: pyxel.show()
summary: それまでに描いた画面を表示して、ESCキーが押されるまで待ちます。update と draw を作らずに、絵を1枚だけ見せたいときに使います。
aliases: ショー, 表示, 1枚だけ, 静止画
api: show
reads: show=ショー
--
## 書き方のかたち
::: tpl show の書き方
import pyxel
pyxel.init(〔幅〕, 〔高さ〕)
〔描く命令〕
pyxel.show()

| 〔描く命令〕 | cls や circ、text など。ここで描いたものが表示される |
:::

## どんな命令？
ふつうのPyxelのプログラムは、`update` と `draw` を作って `run` で動かします（[[px-run]]）。でも、「動かさずに、絵を1枚だけ見せたい」ときは、`show` を使うともっと短く書けます。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="show")
pyxel.cls(1)
pyxel.circ(80, 55, 30, 10)
pyxel.text(52, 100, "pyxel.show()", 7)
pyxel.show()
```

`update` も `draw` もありません。`init` のあとに描いて、最後に `show` を書くだけです。ESCキーを押すと終わります。

画像を表示するだけなら、次の3行でもできます。`image.png` は、プログラムと同じフォルダに置きます。

```python norun
import pyxel

pyxel.init(160, 120)
pyxel.screen.load(0, 0, "image.png")
pyxel.show()
```
`pyxel.screen` は画面そのもので、そこに画像を直接読みこんでいます。色は、Pyxelの16色のうち近い色に置き換わります。

::: point
`show` の画面は動きません。キーで動かしたり、アニメーションしたりしたいときは、`run` を使います（[[update-draw]]）。
:::

@@ px-quit
title: quit（終了する）
type: Pyxelの命令
chapter: 9
group: 基本
syntax: pyxel.quit()
summary: プログラムをすぐに終わらせる命令です。ウィンドウが閉じます。
aliases: クイット, 終了, 終わる
api: quit
reads: quit=クイット
--
## 書き方のかたち
::: tpl quit の書き方
pyxel.quit()
:::

## どんな命令？
ふつうはESCキーで終わります。ゲームの中の「やめる」ボタンなど、**自分のタイミングで終わらせたい**ときに使います。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="quit")


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


def draw():
    pyxel.cls(1)
    pyxel.text(20, 56, "PUSH Q TO QUIT", 7)


pyxel.run(update, draw)
```

上のプログラムは、Qキーを押すと終わります（[[px-btnp]]）。

`init` の `quit_key=` を使うと、ESC以外のキーで終わるように変えられます。

@@ px-title
title: title（ウィンドウの名前）
type: Pyxelの命令
chapter: 9
group: 基本
syntax: pyxel.title(タイトル)
summary: ウィンドウの上に出る名前を、あとから変えます。
aliases: タイトル, ウィンドウ名
api: title
reads: title=タイトル
--
## 書き方のかたち
::: tpl title の書き方
pyxel.title("〔新しいタイトル〕")

| 〔新しいタイトル〕 | ウィンドウの上に出す名前 |
:::

## どんな命令？
ふつうは `init` の `title=` で決めます。`pyxel.title` は、ゲームの途中で名前を変えたいときに使います。

@@ px-size
title: width・height（画面の大きさ）
type: Pyxelの命令
chapter: 9
group: 基本
syntax: pyxel.width / pyxel.height
summary: 画面の幅と高さが入った変数です。init で決めた大きさを、あとから調べるのに使います。
aliases: 幅, 高さ, 画面サイズ, ウィズ, ハイト
api: width, height
reads: width=ウィズ | height=ハイト
--
## 書き方のかたち
::: tpl width・height の書き方
pyxel.width
pyxel.height
:::

## どんな命令？
`init` で決めた画面の**幅**と**高さ**が入っています。数字をそのまま書かずにこれを使うと、あとで画面の大きさを変えても、プログラムを直さずにすみます。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="size")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(10, 10, f"width = {pyxel.width}", 7)
    pyxel.text(10, 24, f"height = {pyxel.height}", 7)
    pyxel.circ(pyxel.width // 2, pyxel.height // 2, 20, 10)


pyxel.run(update, draw)
```

`pyxel.width // 2` で、画面の真ん中の `x` が出ます（[[operator]]）。

@@ px-frame-count
title: frame_count（フレーム数）
type: Pyxelの命令
chapter: 9
group: 基本
syntax: pyxel.frame_count
summary: ゲームが始まってから進んだフレーム数が入った変数です。時間によって変化をつけるのに使います。
aliases: フレーム, 時間, 点滅
api: frame_count
reads: frame_count=フレームカウント
--
## 書き方のかたち
::: tpl frame_count の書き方
pyxel.frame_count
:::

## どんな命令？
ゲームが始まってから**何フレーム進んだか**が入っています。1秒に30フレーム進むので、30で1秒です。

`%`（余り）と組み合わせると、一定の間隔で繰り返す動きが作れます（[[operator]]）。

## 使い方
```python px gif frames=60
import pyxel

pyxel.init(160, 120, title="frame_count")


def update():
    pass


def draw():
    pyxel.cls(0)
    if pyxel.frame_count % 20 < 10:
        pyxel.text(48, 57, "PUSH START", 10)


pyxel.run(update, draw)
```

10フレームごとに、文字が出たり消えたりします（[[pyxel-var]]）。

@@ px-screenshot
title: screenshot（画面を保存）
type: Pyxelの命令
chapter: 9
group: 基本
syntax: pyxel.screenshot()
summary: いまの画面を、画像ファイル（PNG）として保存します。
aliases: スクリーンショット, 画面保存, 画像保存
api: screenshot
reads: screenshot=スクリーンショット
--
## 書き方のかたち
::: tpl screenshot の書き方
pyxel.screenshot()
:::

## どんな命令？
作ったゲームの画面を、画像として残せます。保存される場所は、パソコンの「デスクトップ」です。

ゲームを実行中に、**Alt + 1**（Macは Option + 1）を押しても、同じことができます。

@@ px-cls
title: cls（画面を消す）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.cls(色)
summary: 画面全体を1つの色で塗りつぶします。draw のいちばん最初に書きます。
aliases: クリアスクリーン, 画面を消す, 背景, 背景色
api: cls
reads: cls=クリアスクリーン | color=カラー
--
## 書き方のかたち
::: tpl cls の書き方
pyxel.cls(〔色〕)

| 〔色〕 | 0〜15 の色の番号（[[color]]） |
:::

## どんな命令？
`cls` は **clear screen（クリアスクリーン）＝画面を消す**を短くした言葉です。前のフレームで描いた絵をすべて消して、背景の色で塗りつぶします。

`draw` の**いちばん最初**に書きます。書かないと、前のフレームの絵が残ったまま重なっていきます。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="cls")


def update():
    pass


def draw():
    pyxel.cls(1)
    pyxel.text(50, 57, "cls(1)", 7)


pyxel.run(update, draw)
```

背景の色を変えたいときは、`cls` の数を変えます。

::: stuck
`cls` を図形を描いたあとに書くと、描いた図形が全部消えます。**先に `cls`、そのあとに図形**です。
:::

@@ px-pset
title: pset（点を打つ）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.pset(x, y, 色)
summary: 画面の1ドットだけを、指定した色にします。
aliases: ピーセット, 点, ドット
api: pset
reads: pset=ピーセット
--
## 書き方のかたち
::: tpl pset の書き方
pyxel.pset(〔x〕, 〔y〕, 〔色〕)

| 〔x〕 | 点の位置（左から） |
| 〔y〕 | 点の位置（上から） |
| 〔色〕 | 0〜15 の色の番号 |
:::

## どんな命令？
`pset` は **point set（ポイントセット）**を短くした言葉です。いちばん小さな図形である**点**を描きます。星空などに使えます。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="pset")


def update():
    pass


def draw():
    pyxel.cls(0)
    for i in range(30):
        pyxel.pset(pyxel.rndi(0, 159), pyxel.rndi(0, 119), 7)


pyxel.run(update, draw)
```

ランダムな場所に点を30個打っています（[[px-rndi]]）。毎フレーム場所が変わるので、星がちらちら光って見えます。

@@ px-pget
title: pget（色を調べる）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.pget(x, y)
summary: 画面の (x, y) にあるドットの色の番号を調べます。
aliases: ピーゲット, 色を調べる, ピクセルの色
api: pget
reads: pget=ピーゲット
--
## 書き方のかたち
::: tpl pget の書き方
〔変数〕 = pyxel.pget(〔x〕, 〔y〕)

| 〔変数〕 | 調べた色の番号を入れる名前 |
| 〔x〕, 〔y〕 | 調べたい場所 |
:::

## どんな命令？
`pset` の反対で、**そこに何色が塗られているか**を数で教えてくれます。当たり判定（壁の色を調べるなど）に使えます。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="pget")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rect(20, 20, 40, 40, 8)
    iro = pyxel.pget(30, 30)
    pyxel.text(80, 40, f"COLOR {iro}", 7)


pyxel.run(update, draw)
```

(30, 30) は赤（8番）の四角の中なので、`8` が出ます。

@@ px-line
title: line（線を引く）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.line(x1, y1, x2, y2, 色)
summary: 2つの点を結ぶ、まっすぐな線を引きます。
aliases: ライン, 線, 直線
api: line
reads: line=ライン
--
## 書き方のかたち
::: tpl line の書き方
pyxel.line(〔x1〕, 〔y1〕, 〔x2〕, 〔y2〕, 〔色〕)

| 〔x1〕, 〔y1〕 | 線のはじまりの位置 |
| 〔x2〕, 〔y2〕 | 線の終わりの位置 |
| 〔色〕 | 0〜15 の色の番号 |
:::

## どんな命令？
始まりの点と終わりの点を、線で結びます。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="line")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.line(10, 10, 150, 110, 8)
    pyxel.line(10, 110, 150, 10, 10)
    pyxel.line(80, 0, 80, 119, 7)


pyxel.run(update, draw)
```

@@ px-rect
title: rect（四角を塗る）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.rect(x, y, 幅, 高さ, 色)
summary: 中を塗りつぶした四角を描きます。
aliases: レクト, 四角, 長方形, 正方形, ボタン
api: rect
reads: rect=レクト
--
## 書き方のかたち
::: tpl rect の書き方
pyxel.rect(〔x〕, 〔y〕, 〔幅〕, 〔高さ〕, 〔色〕)

| 〔x〕, 〔y〕 | 四角の**左上**の位置 |
| 〔幅〕 | 四角の横の長さ |
| 〔高さ〕 | 四角の縦の長さ |
| 〔色〕 | 0〜15 の色の番号 |
:::

## どんな命令？
`rect` は **rectangle（レクタングル）＝長方形**を短くした言葉です。いちばんよく使う図形で、キャラクター、ボタン、バーなど、何にでも使えます。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="rect")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rect(20, 20, 60, 40, 8)
    pyxel.rect(70, 50, 60, 40, 10)


pyxel.run(update, draw)
```

あとから描いたものが上に重なります。

::: point
`x` と `y` は、四角の**左上**の位置です。真ん中ではありません。
:::

ふちだけの四角は[[px-rectb]]です。

@@ px-rectb
title: rectb（四角のふち）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.rectb(x, y, 幅, 高さ, 色)
summary: ふちだけの四角を描きます（中は塗りません）。
aliases: レクトビー, 枠, わく, 枠線
api: rectb
reads: rectb=レクトビー
--
## 書き方のかたち
::: tpl rectb の書き方
pyxel.rectb(〔x〕, 〔y〕, 〔幅〕, 〔高さ〕, 〔色〕)

| 〔x〕, 〔y〕 | 四角の**左上**の位置 |
| 〔幅〕, 〔高さ〕 | 四角の大きさ |
| 〔色〕 | 0〜15 の色の番号 |
:::

## どんな命令？
`rectb` の **b** は **border（ボーダー）＝ふち**です。書き方は[[px-rect]]と同じで、中を塗りません。枠線やボタンの外枠に使えます。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="rectb")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rect(30, 30, 60, 40, 1)
    pyxel.rectb(30, 30, 60, 40, 7)
    pyxel.rectb(0, 0, 160, 120, 13)


pyxel.run(update, draw)
```

@@ px-circ
title: circ（円を塗る）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.circ(x, y, 半径, 色)
summary: 中を塗りつぶした円を描きます。
aliases: サーク, 円, ボール, まる
api: circ
reads: circ=サーク
--
## 書き方のかたち
::: tpl circ の書き方
pyxel.circ(〔x〕, 〔y〕, 〔半径〕, 〔色〕)

| 〔x〕, 〔y〕 | 円の**真ん中**の位置 |
| 〔半径〕 | 真ん中からふちまでの長さ |
| 〔色〕 | 0〜15 の色の番号 |
:::

## どんな命令？
`circ` は **circle（サークル）＝円**を短くした言葉です。ボール、太陽、弾などに使います。

::: point
四角とちがって、`x` と `y` は円の**真ん中**の位置です。
:::

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="circ")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.circ(50, 60, 30, 10)
    pyxel.circ(110, 60, 15, 8)


pyxel.run(update, draw)
```

ふちだけの円は[[px-circb]]です。

@@ px-circb
title: circb（円のふち）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.circb(x, y, 半径, 色)
summary: ふちだけの円を描きます（中は塗りません）。
aliases: サークビー, 輪, 輪っか
api: circb
reads: circb=サークビー
--
## 書き方のかたち
::: tpl circb の書き方
pyxel.circb(〔x〕, 〔y〕, 〔半径〕, 〔色〕)

| 〔x〕, 〔y〕 | 円の**真ん中**の位置 |
| 〔半径〕 | 真ん中からふちまでの長さ |
| 〔色〕 | 0〜15 の色の番号 |
:::

## どんな命令？
書き方は[[px-circ]]と同じで、**ふちだけ**を描きます（b = border）。波紋やバリアのような、輪の形に使えます。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="circb")


def update():
    pass


def draw():
    pyxel.cls(0)
    for r in (10, 20, 30, 40):
        pyxel.circb(80, 60, r, 12)


pyxel.run(update, draw)
```

@@ px-elli
title: elli（だ円を塗る）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.elli(x, y, 幅, 高さ, 色)
summary: 中を塗りつぶしただ円（たまご形）を描きます。
aliases: エリ, だ円, 楕円, たまご
api: elli
reads: elli=エリ
--
## 書き方のかたち
::: tpl elli の書き方
pyxel.elli(〔x〕, 〔y〕, 〔幅〕, 〔高さ〕, 〔色〕)

| 〔x〕, 〔y〕 | だ円がぴったり入る四角の、**左上**の位置 |
| 〔幅〕, 〔高さ〕 | だ円の大きさ |
| 〔色〕 | 0〜15 の色の番号 |
:::

## どんな命令？
`elli` は **ellipse（イリプス）＝だ円**を短くした言葉です。影、雲、UFOなどに使えます。円とちがい、四角と同じように「左上の位置と、幅・高さ」で指定します。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="elli")


def update():
    pass


def draw():
    pyxel.cls(12)
    pyxel.elli(30, 50, 100, 30, 7)
    pyxel.elli(50, 70, 60, 20, 13)


pyxel.run(update, draw)
```

@@ px-ellib
title: ellib（だ円のふち）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.ellib(x, y, 幅, 高さ, 色)
summary: ふちだけのだ円を描きます。
aliases: エリビー, だ円のふち
api: ellib
reads: ellib=エリビー
--
## 書き方のかたち
::: tpl ellib の書き方
pyxel.ellib(〔x〕, 〔y〕, 〔幅〕, 〔高さ〕, 〔色〕)

| 〔x〕, 〔y〕 | だ円がぴったり入る四角の、**左上**の位置 |
| 〔幅〕, 〔高さ〕 | だ円の大きさ |
| 〔色〕 | 0〜15 の色の番号 |
:::

## どんな命令？
[[px-elli]]の**ふちだけ**版です（b = border）。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="ellib")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.ellib(20, 30, 120, 60, 11)
    pyxel.ellib(40, 45, 80, 30, 10)


pyxel.run(update, draw)
```

@@ px-tri
title: tri（三角形を塗る）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.tri(x1, y1, x2, y2, x3, y3, 色)
summary: 3つの点を結んで、中を塗りつぶした三角形を描きます。
aliases: トライ, 三角, 三角形
api: tri
reads: tri=トライ
--
## 書き方のかたち
::: tpl tri の書き方
pyxel.tri(〔x1〕, 〔y1〕, 〔x2〕, 〔y2〕, 〔x3〕, 〔y3〕, 〔色〕)

| 〔x1〕〜〔y3〕 | 三角形の3つの角の位置 |
| 〔色〕 | 0〜15 の色の番号 |
:::

## どんな命令？
`tri` は **triangle（トライアングル）＝三角形**を短くした言葉です。3つの角の位置を、x と y の組で3つ書きます。屋根、矢印、ロケットの先などに使います。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="tri")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.tri(80, 20, 30, 100, 130, 100, 9)
    pyxel.tri(80, 50, 60, 90, 100, 90, 10)


pyxel.run(update, draw)
```

ふちだけの三角形は[[px-trib]]です。

@@ px-trib
title: trib（三角形のふち）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.trib(x1, y1, x2, y2, x3, y3, 色)
summary: ふちだけの三角形を描きます。
aliases: トライビー, 三角のふち
api: trib
reads: trib=トライビー
--
## 書き方のかたち
::: tpl trib の書き方
pyxel.trib(〔x1〕, 〔y1〕, 〔x2〕, 〔y2〕, 〔x3〕, 〔y3〕, 〔色〕)

| 〔x1〕〜〔y3〕 | 三角形の3つの角の位置 |
| 〔色〕 | 0〜15 の色の番号 |
:::

## どんな命令？
[[px-tri]]の**ふちだけ**版です（b = border）。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="trib")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.trib(80, 20, 30, 100, 130, 100, 11)


pyxel.run(update, draw)
```

@@ px-fill
title: fill（塗りつぶす）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.fill(x, y, 色)
summary: (x, y) と同じ色でつながっている部分を、まとめて別の色で塗ります。
aliases: フィル, バケツ, ぬりつぶし
api: fill
reads: fill=フィル
--
## 書き方のかたち
::: tpl fill の書き方
pyxel.fill(〔x〕, 〔y〕, 〔色〕)

| 〔x〕, 〔y〕 | ぬりはじめる場所 |
| 〔色〕 | 塗る色の番号 |
:::

## どんな命令？
お絵かきソフトの「バケツ」と同じ働きです。`(x, y)` と同じ色でつながっている部分が、まとめて塗られます。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="fill")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rectb(30, 30, 100, 60, 7)
    pyxel.fill(80, 60, 3)


pyxel.run(update, draw)
```

四角のふちの**内側**だけが緑に塗られます。ふちが途切れていると、すき間から外まで塗られてしまうので注意しよう。

@@ px-text
title: text（文字を書く）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.text(x, y, 文字, 色)
summary: 画面の好きな場所に、好きな色で文字を書きます。はじめは英数字だけです。
aliases: テキスト, 文字, 文字を書く, 文字表示, 日本語
api: text
reads: text=テキスト | font=フォント
--
## 書き方のかたち
::: tpl text の書き方
pyxel.text(〔x〕, 〔y〕, "〔文字〕", 〔色〕)
pyxel.text(〔x〕, 〔y〕, "〔日本語〕", 〔色〕, 〔font〕)

| 〔x〕, 〔y〕 | 文字の**左上**の位置 |
| 〔文字〕 | 書きたい文字。`"` で囲む |
| 〔色〕 | 0〜15 の色の番号 |
| 〔font〕 | 日本語を書くときに使う、読みこんだフォント（[[px-font-class]]） |
:::

## どんな命令？
画面に文字を書く命令です。`print` のPyxel版です。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="text")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(10, 10, "HELLO", 7)
    pyxel.text(10, 24, "SCORE: " + str(100), 10)


pyxel.run(update, draw)
```

- 数は `str()` で文字に変えてからつなげます（[[typeconv]]）。f文字列でもOKです（[[fstring]]）
- 日本語は、フォントを読みこんで、最後に `font` をつけます（[[pyxel-jp]]）
- 文字の大きさは変えられません（日本語フォントの大きさは、ファイルで決まります）

詳しくは[[pyxel-text]]を見よう。

@@ px-blt
title: blt（画像をはる）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.blt(x, y, 画像番号, u, v, 幅, 高さ, 透明色)
summary: イメージバンク（ドット絵を入れておく場所）の絵の一部を、画面にはりつけます。
aliases: ブリット, 画像, ドット絵, キャラクター, スプライト
api: blt
reads: blt=ブリット | image=イメージ
--
## 書き方のかたち
::: tpl blt の書き方
pyxel.blt(〔x〕, 〔y〕, 〔画像番号〕, 〔u〕, 〔v〕, 〔幅〕, 〔高さ〕, 〔透明色〕)

| 〔x〕, 〔y〕 | 画面のどこにはるか（左上の位置） |
| 〔画像番号〕 | イメージバンクの番号（0〜2） |
| 〔u〕, 〔v〕 | イメージバンクの、どこから切り取るか（左上の位置） |
| 〔幅〕, 〔高さ〕 | 切りとる大きさ |
| 〔透明色〕 | この色のドットははらずに、透明にする（書かなくてもOK） |
:::

## どんな命令？
`blt` は **block transfer（ブロックトランスファー）＝かたまりを写す**を短くした言葉です。ドット絵のキャラクターを画面に出すときの、基本の命令です。Scratchでいう「コスチューム」を画面に出すイメージです。

ドット絵は **Pyxel Editor**（`pyxel edit ファイル名.pyxres`）で描いて、`pyxel.load` で読みこむのがふつうです（[[px-load]]）。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="blt")
pyxel.images[0].set(0, 0, ["00088000", "00888800", "08888880", "88800888", "88800888", "08888880", "00888800", "00088000"])


def update():
    pass


def draw():
    pyxel.cls(1)
    pyxel.blt(60, 40, 0, 0, 0, 8, 8, 0)
    pyxel.text(40, 80, "blt: image bank 0", 7)


pyxel.run(update, draw)
```

上の例では、`pyxel.images[0].set(…)` で小さな絵を自分で作ってから、`blt` で画面にはっています（[[px-image-class]]）。

@@ px-bltm
title: bltm（マップをはる）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.bltm(x, y, マップ番号, u, v, 幅, 高さ, 透明色)
summary: タイルマップ（小さな絵を並べて作ったマップ）の一部を、画面にはりつけます。RPGやアクションゲームの背景に使います。
aliases: ブリットエム, マップ, タイルマップ, 背景, ステージ
api: bltm
reads: bltm=ブリットエム | tilemap=タイルマップ
--
## 書き方のかたち
::: tpl bltm の書き方
pyxel.bltm(〔x〕, 〔y〕, 〔マップ番号〕, 〔u〕, 〔v〕, 〔幅〕, 〔高さ〕)

| 〔x〕, 〔y〕 | 画面のどこにはるか（左上の位置） |
| 〔マップ番号〕 | タイルマップの番号（0〜7） |
| 〔u〕, 〔v〕 | マップの、どこから切り取るか（ドット数で書く） |
| 〔幅〕, 〔高さ〕 | 切り取る大きさ（ドット数） |
:::

## どんな命令？
`bltm` の **m** は **map（マップ）**です。[[px-blt]]が「イメージバンクの絵」をはるのに対して、`bltm` は「**タイルマップ**」をはります。

タイルマップは、8×8ドットの小さな絵（タイル）を、碁盤の目のように並べたものです。同じタイルを何度も使えるので、広いマップを少ないデータで作れます（[[px-tilemap-class]]）。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="bltm")
pyxel.images[0].set(0, 0, ["33333333", "33b33333", "33333b33", "33333333", "3b333333", "333333b3", "33333333", "333b3333"])
pyxel.images[0].set(8, 0, ["44444444", "44494444", "44444444", "49444449", "44444444", "44449444", "44444444", "94444444"])
pyxel.tilemaps[0].set(0, 0, ["0000 0000 0100 0100 0000", "0000 0100 0100 0000 0000", "0100 0100 0000 0000 0100", "0000 0000 0000 0100 0100"])


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.bltm(40, 40, 0, 0, 0, 40, 32)


pyxel.run(update, draw)
```

1. `pyxel.images[0].set(…)` で、草（左）と土（右）の2つのタイルを描く
2. `pyxel.tilemaps[0].set(…)` で、タイルの並べ方を決める。`0000` が草、`0100` が土。4けたのうち、前の2けたがイメージバンクの横の何番目、後ろの2けたが縦の何番目かです
3. `bltm` で、マップの左上から 40×32 ドット（タイル5×4枚分）を画面にはる

ふつうは、マップは **Pyxel Editor** のタイルマップエディタで描いて、`pyxel.load` で読みこみます（[[px-load]]）。

::: deep スクロールに使う
`u` と `v` を少しずつ変えると、マップの見える場所が動いて、**スクロール**になります。広いマップの中を歩くゲームは、この仕組みで作ります。
:::

@@ px-clip
title: clip（描く範囲をしぼる）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.clip(x, y, 幅, 高さ)
summary: 描く範囲を四角の中だけにしぼります。範囲の外には描かれません。
aliases: クリップ, 描画範囲, はみ出し
api: clip
reads: clip=クリップ
--
## 書き方のかたち
::: tpl clip の書き方
pyxel.clip(〔x〕, 〔y〕, 〔幅〕, 〔高さ〕)
pyxel.clip()

| 〔x〕, 〔y〕 | 範囲の左上の位置 |
| 〔幅〕, 〔高さ〕 | 範囲の大きさ |
| （何も書かない） | 範囲を画面全体に戻す |
:::

## どんな命令？
`clip` のあとに描いたものは、指定した四角の**中だけ**に出ます。画面の一部だけに絵を出したいときに使います。終わったら `pyxel.clip()` で元に戻します。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="clip")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.clip(40, 30, 80, 60)
    pyxel.circ(80, 60, 50, 10)
    pyxel.clip()
    pyxel.rectb(40, 30, 80, 60, 7)


pyxel.run(update, draw)
```

大きな円が、四角の中だけに描かれています。

@@ px-camera
title: camera（画面をずらす）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.camera(x, y)
summary: 描く位置をまとめてずらします。広いマップを動かすときや、画面をゆらすときに使います。
aliases: カメラ, スクロール, 画面ゆれ, ずらす
api: camera
reads: camera=カメラ
--
## 書き方のかたち
::: tpl camera の書き方
pyxel.camera(〔x〕, 〔y〕)
pyxel.camera()

| 〔x〕, 〔y〕 | 画面の左上に来る場所。描いたものは、その分だけ逆向きにずれる |
| （何も書かない） | ずれを0に戻す |
:::

## どんな命令？
`camera` は、**カメラ**を動かすように、画面に映る場所を変えます。`camera(10, 0)` にすると、カメラが右に10ドット動くので、描いたものは全部左に10ドットずれて見えます。

画面の「ゆれ」や、マップのスクロールに使えます。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="camera")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.camera(20, 10)
    pyxel.rect(40, 30, 40, 40, 8)
    pyxel.camera()
    pyxel.rectb(40, 30, 40, 40, 7)


pyxel.run(update, draw)
```

白いふちが本来の位置、赤い四角が `camera(20, 10)` のあとに同じ位置へ描いたものです。左上にずれています。

@@ px-pal
title: pal（色を入れ替える）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.pal(色1, 色2)
summary: 描くときの色1を色2に入れ替えます。同じ絵を色違いで描けます。
aliases: パル, パレット, 色違い, 色替え
api: pal
reads: pal=パル | palette=パレット
--
## 書き方のかたち
::: tpl pal の書き方
pyxel.pal(〔色1〕, 〔色2〕)
pyxel.pal()

| 〔色1〕 | 入れ替えられる色の番号 |
| 〔色2〕 | かわりに使う色の番号 |
| （何も書かない） | 入れ替えを全部元に戻す |
:::

## どんな命令？
`pal` は **palette（パレット）**を短くした言葉です。`pal(8, 12)` と書くと、それより後で赤（8）を描くところが、水色（12）になります。敵キャラの色違いによく使います。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="pal")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rect(20, 40, 40, 40, 8)
    pyxel.pal(8, 12)
    pyxel.rect(100, 40, 40, 40, 8)
    pyxel.pal()


pyxel.run(update, draw)
```

同じ `8`（赤）で描いているのに、右の四角は水色になっています。最後に `pyxel.pal()` で元に戻しています。

@@ px-dither
title: dither（半透明）
type: Pyxelの命令
chapter: 9
group: 描く（画面）
syntax: pyxel.dither(0〜1)
summary: 細かい点々で、半透明のように見せて描きます。0.0 が透明、1.0 がふつうの描き方です。
aliases: ディザー, 半透明, 透明, かげ
api: dither
reads: dither=ディザー
--
## 書き方のかたち
::: tpl dither の書き方
pyxel.dither(〔濃さ〕)

| 〔濃さ〕 | 0.0〜1.0 の数。小さいほど薄くなる |
:::

## どんな命令？
細かい点々で、半透明のように見せます。影や、ゲームオーバーのときに「画面が暗くなる」演出に使えます。使い終わったら `pyxel.dither(1)` で元に戻します。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="dither")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rect(20, 30, 70, 50, 10)
    pyxel.dither(0.5)
    pyxel.rect(60, 50, 70, 50, 8)
    pyxel.dither(1)


pyxel.run(update, draw)
```

@@ px-btn
title: btn（キーが押されている？）
type: Pyxelの命令
chapter: 9
group: 入力
syntax: pyxel.btn(キー)
summary: そのキーがいま押されているかを調べます。押されているあいだ、ずっと True です。
aliases: ボタン, キー, 押している, キー入力
api: btn
reads: btn=ボタン | button=ボタン
--
## 書き方のかたち
::: tpl btn の書き方
if pyxel.btn(pyxel.KEY_〔キー名〕):
····〔押されているときの処理〕

| 〔キー名〕 | LEFT、RIGHT、UP、DOWN、SPACE、A〜Z など（[[px-keycodes]]） |
:::

## どんな命令？
`btn` は **button（ボタン）**を短くした言葉です。キーを押している**あいだ**、ずっと `True` になります。キャラクターを歩かせるときなど、**押しつづけたら動きつづける**動きに使います。

## 使い方
```python px hold=KEY_SPACE frames=10
import pyxel

pyxel.init(160, 120, title="btn")


def update():
    pass


def draw():
    pyxel.cls(0)
    if pyxel.btn(pyxel.KEY_SPACE):
        pyxel.text(52, 57, "SPACE IS DOWN", 10)
    else:
        pyxel.text(52, 57, "PUSH SPACE", 7)


pyxel.run(update, draw)
```

画像は、スペースキーを押しているときの画面です。

押した**瞬間だけ**を調べたいときは[[px-btnp]]を使います。詳しくは[[pyxel-key]]を見よう。

@@ px-btnp
title: btnp（押した瞬間）
type: Pyxelの命令
chapter: 9
group: 入力
syntax: pyxel.btnp(キー)
summary: そのキーを押した瞬間の1回だけ True になります。ジャンプや決定ボタンに使います。
aliases: ボタンピー, 押した瞬間, 1回だけ, ジャンプ, 決定
api: btnp
reads: btnp=ボタンピー | hold=ホールド | repeat=リピート
--
## 書き方のかたち
::: tpl btnp の書き方
if pyxel.btnp(pyxel.KEY_〔キー名〕):
····〔押した瞬間の処理〕
pyxel.btnp(pyxel.KEY_〔キー名〕, 〔hold〕, 〔repeat〕)

| 〔キー名〕 | LEFT、SPACE、A〜Z など（[[px-keycodes]]） |
| 〔hold〕 | 押しつづけたとき、何フレーム後から連続で True にするか（書かなくてもOK） |
| 〔repeat〕 | 繰り返しの間隔（フレーム数） |
:::

## どんな命令？
`btnp` の **p** は **pressed（プレスト）＝押された**です。キーを**押した瞬間の1フレームだけ** True になります。押しつづけても、2フレーム目からは False です。

ジャンプ、決定、メニューの切り替えなど、**1回押すごとに1回だけ**起こしたいことに使います。

## 使い方
```python px press=KEY_SPACE@5 frames=12
import pyxel

pyxel.init(160, 120, title="btnp")
count = 0


def update():
    global count
    if pyxel.btnp(pyxel.KEY_SPACE):
        count = count + 1


def draw():
    pyxel.cls(0)
    pyxel.text(40, 40, f"COUNT: {count}", 10)
    pyxel.text(40, 70, "PUSH SPACE", 7)


pyxel.run(update, draw)
```

スペースキーを1回押すごとに、`count` が1つだけ増えます。`btn` だと、押しているあいだ毎フレーム増えてしまいます（[[px-btn]]）。

`hold` と `repeat` を書くと、**押しつづけたときに連続で True** になります。`pyxel.btnp(pyxel.KEY_UP, 8, 2)` と書くと、押した瞬間に1回、8フレーム押しつづけると、そこから2フレームごとに True になります。数を「ピピピッ」と速く増やしたいときに便利です。

@@ px-btnr
title: btnr（離した瞬間）
type: Pyxelの命令
chapter: 9
group: 入力
syntax: pyxel.btnr(キー)
summary: そのキーを離した瞬間の1回だけ True になります。
aliases: ボタンアール, はなした, リリース
api: btnr
reads: btnr=ボタンアール
--
## 書き方のかたち
::: tpl btnr の書き方
if pyxel.btnr(pyxel.KEY_〔キー名〕):
····〔離した瞬間の処理〕

| 〔キー名〕 | LEFT、SPACE、A〜Z など（[[px-keycodes]]） |
:::

## どんな命令？
`btnr` の **r** は **released（リリースト）＝離された**です。キーを**離した瞬間**だけ True です。「ためて、離して、発射」のような動きに使えます。

@@ px-mouse
title: mouse（矢印の表示）
type: Pyxelの命令
chapter: 9
group: 入力
syntax: pyxel.mouse(True)
summary: マウスの矢印（カーソル）を、画面に表示するか隠すかを決めます。
aliases: マウス, カーソル, 矢印, マウスカーソル
api: mouse
reads: mouse=マウス | True=トゥルー
--
## 書き方のかたち
::: tpl mouse の書き方
pyxel.mouse(〔True か False〕)

| True | マウスの矢印を表示する |
| False | 隠す（はじめは隠れている） |
:::

## どんな命令？
Pyxelの画面では、はじめはマウスの矢印が見えません。マウスを使うゲームやアプリでは、`init` のあとに `pyxel.mouse(True)` を書きます。

マウスの位置は[[px-mouse-xy]]で、クリックは[[px-btnp]]で調べます。詳しくは[[pyxel-mouse]]を見よう。

@@ px-mouse-xy
title: mouse_x・mouse_y（マウスの位置）
type: Pyxelの命令
chapter: 9
group: 入力
syntax: pyxel.mouse_x / pyxel.mouse_y
summary: マウスの横の位置と縦の位置が入っている変数です。
aliases: マウスの位置, マウス座標, mouse_x, mouse_y
api: mouse_x, mouse_y
reads: mouse_x=マウスエックス | mouse_y=マウスワイ
--
## 書き方のかたち
::: tpl mouse_x・mouse_y の書き方
pyxel.mouse_x
pyxel.mouse_y
:::

## どんな命令？
マウスの位置が、いつも入っています。`mouse_x` が**横**、`mouse_y` が**縦**の位置です。関数ではなく変数なので、`()` はつけずにそのまま書きます。

## 使い方
```python px click=100,70
import pyxel

pyxel.init(160, 120, title="mouse_xy")
pyxel.mouse(True)


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, 5, 10)
    pyxel.text(4, 4, f"x={pyxel.mouse_x} y={pyxel.mouse_y}", 7)


pyxel.run(update, draw)
```

ボタンの判定に使えます。「マウスが四角の中にあるか」を `if` で調べます（[[pyxel-mouse]]）。

@@ px-mouse-wheel
title: mouse_wheel（ホイール）
type: Pyxelの命令
chapter: 9
group: 入力
syntax: pyxel.mouse_wheel
summary: マウスのホイールを回した量が入った変数です。
aliases: ホイール, マウスホイール, スクロール
api: mouse_wheel
reads: mouse_wheel=マウスホイール
--
## 書き方のかたち
::: tpl mouse_wheel の書き方
pyxel.mouse_wheel
:::

## どんな命令？
ホイールを**上に回す**とプラスの数、**下に回す**とマイナスの数が入ります。回さないときは 0 です。拡大・縮小や、メニューの選択に使えます。

@@ px-input-text
title: input_text（打った文字）
type: Pyxelの命令
chapter: 9
group: 入力
syntax: pyxel.input_text
summary: そのフレームにキーボードで打たれた文字が入った変数です。名前入力などに使えます。
aliases: インプットテキスト, 文字入力, 名前入力, キーボード入力
api: input_text, input_keys
reads: input_text=インプットテキスト
--
## 書き方のかたち
::: tpl input_text の書き方
pyxel.input_text
pyxel.input_keys
:::

## どんな命令？
そのフレームに**キーボードで打たれた文字**が入っています。何も打たれていないときは空っぽ（`""`）です。名前を入力する画面などで、1文字ずつつなげて使います。

## 使い方
```python px text=abc frames=10
import pyxel

pyxel.init(160, 120, title="input_text")
name = ""


def update():
    global name
    name = name + pyxel.input_text


def draw():
    pyxel.cls(1)
    pyxel.text(10, 10, "TYPE SOMETHING", 7)
    pyxel.text(10, 30, name, 10)


pyxel.run(update, draw)
```

打った文字が、`name` の後ろにつながっていきます。

@@ px-keycodes
title: KEY_（キーの名前一覧）
type: Pyxelの命令
chapter: 9
group: 入力
syntax: pyxel.KEY_LEFT など
summary: キーを表す名前の一覧です。btn や btnp に渡して使います。マウスのボタンやゲームパッドの名前もあります。
aliases: キー名, キーコード, KEY_LEFT, KEY_SPACE, MOUSE_BUTTON_LEFT, ゲームパッド
api: KEY_
reads: KEY_LEFT=キーレフト | KEY_SPACE=キースペース | MOUSE_BUTTON_LEFT=マウスボタンレフト
--
## 書き方のかたち
::: tpl KEY_ の書き方
pyxel.KEY_〔キー名〕
pyxel.MOUSE_BUTTON_〔LEFT か RIGHT〕
:::

## どんな命令？
キーには、それぞれ**名前**がついています。`pyxel.btn(pyxel.KEY_LEFT)` のように、[[px-btn]]や[[px-btnp]]のかっこの中に書きます。

| 書き方 | キー |
| --- | --- |
| `pyxel.KEY_LEFT` | ← 左 |
| `pyxel.KEY_RIGHT` | → 右 |
| `pyxel.KEY_UP` | ↑ 上 |
| `pyxel.KEY_DOWN` | ↓ 下 |
| `pyxel.KEY_SPACE` | スペース |
| `pyxel.KEY_RETURN` | Enter |
| `pyxel.KEY_ESCAPE` | Esc |
| `pyxel.KEY_SHIFT` | Shift |
| `pyxel.KEY_A` 〜 `pyxel.KEY_Z` | アルファベット |
| `pyxel.KEY_0` 〜 `pyxel.KEY_9` | 数字 |
| `pyxel.MOUSE_BUTTON_LEFT` | マウスの左ボタン |
| `pyxel.MOUSE_BUTTON_RIGHT` | マウスの右ボタン |
| `pyxel.GAMEPAD1_BUTTON_A` | ゲームパッドのAボタン |

@@ px-rndi
title: rndi（ランダムな整数）
type: Pyxelの命令
chapter: 9
group: 計算
syntax: pyxel.rndi(a, b)
summary: a から b までの整数を、ランダムに1つ選びます（a も b も出ます）。
aliases: ランディー, ランダム, 乱数, サイコロ, 整数
api: rndi
reads: rndi=ランディー
--
## 書き方のかたち
::: tpl rndi の書き方
〔変数〕 = pyxel.rndi(〔a〕, 〔b〕)

| 〔a〕 | 出る数のうち、いちばん小さい数（この数も出る） |
| 〔b〕 | 出る数のうち、いちばん大きい数（この数も出る） |
:::

## どんな命令？
`random.randint` のPyxel版です。`import random` を書かなくても使えます。敵やアイテムが出る場所を決めるのによく使います（[[random]]）。Scratchの「1から10までの乱数」ブロックと同じです。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="rndi")


def update():
    pass


def draw():
    pyxel.cls(0)
    for i in range(8):
        pyxel.circ(pyxel.rndi(10, 150), pyxel.rndi(10, 110), 6, 10)


pyxel.run(update, draw)
```

`pyxel.rndi(10, 150)` で、10〜150のランダムな整数が出ます。上の例では、ランダムな場所に円を8個描いています。

@@ px-rndf
title: rndf（ランダムな小数）
type: Pyxelの命令
chapter: 9
group: 計算
syntax: pyxel.rndf(a, b)
summary: a から b までの小数を、ランダムに1つ選びます。
aliases: ランエフ, 小数ランダム, 乱数
api: rndf
reads: rndf=ランエフ
--
## 書き方のかたち
::: tpl rndf の書き方
〔変数〕 = pyxel.rndf(〔a〕, 〔b〕)

| 〔a〕, 〔b〕 | 出る数の範囲 |
:::

## どんな命令？
[[px-rndi]]の小数版です。`pyxel.rndf(0, 1)` で、0から1までの小数が出ます。落ちる速さに少しばらつきをつけたいときなどに使えます。

@@ px-rseed
title: rseed（ランダムの種）
type: Pyxelの命令
chapter: 9
group: 計算
syntax: pyxel.rseed(数)
summary: ランダムの「種」を決めます。同じ種なら、毎回同じ順番でランダムな数が出ます。
aliases: シード, 種, 乱数の種
api: rseed, nseed
reads: rseed=アールシード
--
## 書き方のかたち
::: tpl rseed の書き方
pyxel.rseed(〔数〕)

| 〔数〕 | 種になる数。同じ数なら、同じ結果になる |
:::

## どんな命令？
ふつうのランダムは、実行するたびに結果が変わります。`rseed` で種を決めると、**毎回同じ結果**になります。ゲームのテストや、「今日のステージ」のように毎回同じ内容にしたいときに使います。

@@ px-sin
title: sin（サイン）
type: Pyxelの命令
chapter: 9
group: 計算
syntax: pyxel.sin(角度)
summary: 角度（度）のサインの値を返します。円を描く動きや、ゆれる動きに使います。
aliases: サイン, 波, ゆれる, 三角関数
api: sin
reads: sin=サイン
--
## 書き方のかたち
::: tpl sin の書き方
pyxel.sin(〔角度〕)

| 〔角度〕 | 角度（単位は「度」。360で一周） |
:::

## どんな命令？
`sin` は、**ゆらゆらゆれる**動きを作るのに便利な計算です。答えは -1 から 1 のあいだを行ったり来たりします。数学で習うのは高校ですが、「-1〜1をなめらかに行き来する数が出てくる」とだけ覚えておけば使えます。

Pyxelの `sin` は、角度を**度**で書きます（ふつうのPythonの `math.sin` はラジアンという別の単位です）。

## 使い方
```python px gif frames=60
import pyxel

pyxel.init(160, 120, title="sin")


def update():
    pass


def draw():
    pyxel.cls(0)
    y = 60 + pyxel.sin(pyxel.frame_count * 6) * 30
    pyxel.circ(80, y, 8, 10)


pyxel.run(update, draw)
```

`pyxel.frame_count` を使って、時間とともに上下にゆれています。

@@ px-cos
title: cos（コサイン）
type: Pyxelの命令
chapter: 9
group: 計算
syntax: pyxel.cos(角度)
summary: 角度（度）のコサインの値を返します。sin と組み合わせて、円を描く動きを作れます。
aliases: コサイン, 円運動, ぐるぐる
api: cos
reads: cos=コサイン
--
## 書き方のかたち
::: tpl cos の書き方
pyxel.cos(〔角度〕)

| 〔角度〕 | 角度（単位は「度」。360で一周） |
:::

## どんな命令？
[[px-sin]]とペアで使います。**x に cos、y に sin** を使うと、円を描く動きになります。

## 使い方
```python px gif frames=45
import pyxel

pyxel.init(160, 120, title="cos")


def update():
    pass


def draw():
    pyxel.cls(0)
    a = pyxel.frame_count * 8
    x = 80 + pyxel.cos(a) * 30
    y = 60 + pyxel.sin(a) * 30
    pyxel.circ(x, y, 6, 11)


pyxel.run(update, draw)
```

@@ px-atan2
title: atan2（角度を求める）
type: Pyxelの命令
chapter: 9
group: 計算
syntax: pyxel.atan2(y, x)
summary: 2つの点の横と縦の差から、向きの角度（度）を求めます。
aliases: 角度, 向き, 方向, アークタンジェント
api: atan2
reads: atan2=アークタンジェントツー
--
## 書き方のかたち
::: tpl atan2 の書き方
pyxel.atan2(〔縦の差〕, 〔横の差〕)

| 〔縦の差〕 | 目的地の y − 自分の y |
| 〔横の差〕 | 目的地の x − 自分の x |
:::

## どんな命令？
敵がプレイヤーの方を向く、弾をプレイヤーに向けて撃つ、のように、**相手がいる方向の角度**を知りたいときに使います。答えを[[px-cos]]と[[px-sin]]に入れると、その方向に進めます。

@@ px-sqrt
title: sqrt（平方根）
type: Pyxelの命令
chapter: 9
group: 計算
syntax: pyxel.sqrt(数)
summary: 数の平方根（2乗するとその数になる数）を返します。
aliases: スクエアルート, 平方根, ルート, 距離
api: sqrt
reads: sqrt=スクエアルート
--
## 書き方のかたち
::: tpl sqrt の書き方
pyxel.sqrt(〔数〕)

| 〔数〕 | 平方根を求めたい数（0以上） |
:::

## どんな命令？
`math.sqrt` と同じ働きです。2つの点の**距離**は `pyxel.sqrt(dx * dx + dy * dy)` で求められます（三平方の定理）。円どうしの当たり判定に使えます（[[module]]）。

@@ px-ceil
title: ceil（切り上げ）
type: Pyxelの命令
chapter: 9
group: 計算
syntax: pyxel.ceil(数)
summary: 小数を切り上げて整数にします。
aliases: シーリング, 切り上げ
api: ceil
reads: ceil=シーリング
--
## 書き方のかたち
::: tpl ceil の書き方
pyxel.ceil(〔数〕)

| 〔数〕 | 切り上げたい数 |
:::

## どんな命令？
`pyxel.ceil(2.1)` は `3`。小数点以下が少しでもあれば、**大きいほう**の整数になります。

@@ px-floor
title: floor（切り捨て）
type: Pyxelの命令
chapter: 9
group: 計算
syntax: pyxel.floor(数)
summary: 小数を切り捨てて整数にします。
aliases: フロア, 切り捨て
api: floor
reads: floor=フロア
--
## 書き方のかたち
::: tpl floor の書き方
pyxel.floor(〔数〕)

| 〔数〕 | 切り捨てたい数 |
:::

## どんな命令？
`pyxel.floor(2.9)` は `2`。小数点以下を捨てて、**小さいほう**の整数になります。

@@ px-clamp
title: clamp（範囲におさめる）
type: Pyxelの命令
chapter: 9
group: 計算
syntax: pyxel.clamp(数, 小, 大)
summary: 数を、決めた範囲（いちばん小さい数〜いちばん大きい数）の中におさめます。
aliases: クランプ, 範囲, はみ出し防止
api: clamp
reads: clamp=クランプ
--
## 書き方のかたち
::: tpl clamp の書き方
pyxel.clamp(〔数〕, 〔最小〕, 〔最大〕)

| 〔数〕 | おさめたい数 |
| 〔最小〕 | これより小さくならない |
| 〔最大〕 | これより大きくならない |
:::

## どんな命令？
キャラクターが画面の外に出ないようにするときに使います。`max` と `min` を組み合わせて書くのと同じです（[[pyxel-key]]）。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="clamp")


def update():
    pass


def draw():
    pyxel.cls(0)
    x = pyxel.clamp(200, 0, 152)
    pyxel.rect(x, 56, 8, 8, 10)
    pyxel.text(4, 4, f"clamp(200, 0, 152) = {x}", 7)


pyxel.run(update, draw)
```

200 は 152 より大きいので、152 になります。

@@ px-sgn
title: sgn（プラス・マイナスの判定）
type: Pyxelの命令
chapter: 9
group: 計算
syntax: pyxel.sgn(数)
summary: 数がプラスなら 1、0なら 0、マイナスなら -1 を返します。
aliases: 符号, プラスマイナス, 向き
api: sgn
reads: sgn=サイン
--
## 書き方のかたち
::: tpl sgn の書き方
pyxel.sgn(〔数〕)

| 〔数〕 | 調べたい数 |
:::

## どんな命令？
**向き**だけを知りたいときに使います。たとえば敵がプレイヤーに近づくとき、`x = x + pyxel.sgn(player - x)` と書けば、左右どちらに動けばいいかが分かります。

@@ px-noise
title: noise（なめらかなランダム）
type: Pyxelの命令
chapter: 9
group: 計算
syntax: pyxel.noise(x, y, z)
summary: なめらかに変化するランダムな値を返します（パーリンノイズ）。
aliases: ノイズ, パーリンノイズ, 地形, なめらか
api: noise
reads: noise=ノイズ
--
## 書き方のかたち
::: tpl noise の書き方
pyxel.noise(〔x〕, 〔y〕, 〔z〕)

| 〔x〕, 〔y〕, 〔z〕 | 場所や時間を表す数。近い数なら、近い値が返る |
:::

## どんな命令？
ふつうのランダムは毎回バラバラですが、`noise` は**となりどうしがなめらかにつながった**値を返します。雲の形や地形、ゆらゆらした動きを作るときに使います。

@@ px-play
title: play（音を鳴らす）
type: Pyxelの命令
chapter: 9
group: 音
syntax: pyxel.play(チャンネル, 音の番号)
summary: チャンネルを決めて、効果音を鳴らします。
aliases: プレイ, 音, 効果音, サウンド, 鳴らす
api: play
reads: play=プレイ | channel=チャンネル | sound=サウンド
--
## 書き方のかたち
::: tpl play の書き方
pyxel.play(〔チャンネル〕, 〔音の番号〕)

| 〔チャンネル〕 | 0〜3。同時に鳴らせる音は4つまで |
| 〔音の番号〕 | 鳴らす音の番号（0〜63） |
:::

## どんな命令？
ジャンプしたとき、コインをとったとき、ゲームオーバーのときなどに**効果音**を鳴らします。

音は、Pyxel Editor で作る方法と、プログラムで作る方法があります（[[px-sound-class]]）。

同じチャンネルで別の音を鳴らすと、鳴っていた音は止まって、新しい音に置き換わります。チャンネルは、音を出すスピーカー4本のことです（[[px-channel-class]]）。

```python norun
import pyxel

pyxel.init(160, 120, title="おとテスト")
pyxel.sounds[0].set("c3e3g3c4", "p", "7", "n", 10)


def update():
    if pyxel.btnp(pyxel.KEY_SPACE):
        pyxel.play(0, 0)


def draw():
    pyxel.cls(0)
    pyxel.text(40, 57, "PUSH SPACE", 7)


pyxel.run(update, draw)
```
スペースキーを押すと、「ドミソド」と音が鳴ります。

@@ px-playm
title: playm（音楽を鳴らす）
type: Pyxelの命令
chapter: 9
group: 音
syntax: pyxel.playm(音楽の番号, loop=True)
summary: BGM（音楽）を鳴らします。
aliases: プレイエム, BGM, 音楽, ミュージック
api: playm
reads: playm=プレイエム | music=ミュージック | loop=ループ
--
## 書き方のかたち
::: tpl playm の書き方
pyxel.playm(〔音楽の番号〕, loop=〔True か False〕)

| 〔音楽の番号〕 | 鳴らす音楽の番号（0〜7） |
| 〔loop〕 | True にすると、最後まで鳴ったら、また最初から鳴る |
:::

## どんな命令？
BGMのように、**いくつかの音を重ねた曲**を鳴らします。`playm` の **m** は **music** です。曲のデータは Pyxel Editor で作ります（[[px-music-class]]）。

@@ px-stop
title: stop（音を止める）
type: Pyxelの命令
chapter: 9
group: 音
syntax: pyxel.stop()
summary: 鳴っている音を止めます。
aliases: ストップ, 止める, 音を止める
api: stop
reads: stop=ストップ
--
## 書き方のかたち
::: tpl stop の書き方
pyxel.stop()
pyxel.stop(〔チャンネル〕)

| （何も書かない） | 鳴っている音を、全部止める |
| 〔チャンネル〕 | 0〜3。そのチャンネルの音だけ止める |
:::

## どんな命令？
BGMを止めたいとき（ゲームオーバーなど）に使います。

@@ px-sound-class
title: Sound（音のデータ）
type: Pyxelの命令
chapter: 9
group: 音
syntax: pyxel.sounds[番号].set(…)
summary: 音をプログラムで作るための仕組みです。音の高さ・音色・大きさ・速さを文字で決めます。
aliases: サウンド, 音を作る, ドレミ, 効果音, 音色
api: Sound, sounds
reads: Sound=サウンド | sounds=サウンズ | notes=ノーツ
--
## 書き方のかたち
::: tpl Sound の書き方
pyxel.sounds[〔番号〕].set(〔音の高さ〕, 〔音色〕, 〔大きさ〕, 〔効果〕, 〔速さ〕)

| 〔番号〕 | 0〜63。音を入れておく場所 |
| 〔音の高さ〕 | "c3e3g3" のように、ドレミのアルファベットと高さの数字をつなげる |
| 〔音色〕 | "t"（三角波）"s"（四角波）"p"（パルス波）"n"（ノイズ） |
| 〔大きさ〕 | "0"〜"7" の数字。大きいほど大きな音 |
| 〔効果〕 | "n"（なし）"s"（スライド）"v"（ビブラート）"f"（だんだん小さく） |
| 〔速さ〕 | 1音の長さ。数が小さいほど速い |
:::

## どんな命令？
`pyxel.sounds` は、**音を入れておく棚**（0〜63番）です。`set` で棚の中に音を作ります。作った音は[[px-play]]で鳴らします。

`pyxel.sounds[0].set(…)` のように、ドットが2回出てくる書き方の意味は、[[object]]で説明しています。棚の一覧は[[px-objects]]を見よう。

音の高さは、**ド（c）レ（d）ミ（e）ファ（f）ソ（g）ラ（a）シ（b）**のアルファベットと、**高さの数字**で書きます。`c3` はドで、数字が大きいほど高い音です。

```python norun
pyxel.sounds[0].set("c3e3g3c4", "p", "7", "n", 10)
pyxel.play(0, 0)
```
「ド・ミ・ソ・ド」の4つの音が鳴ります。

::: deep もっと知りたい人へ
`pyxel.sounds[0].mml("…")` で、MML（音楽を文字で書く書き方）を使うこともできます。
:::

@@ px-music-class
title: Music（曲のデータ）
type: Pyxelの命令
chapter: 9
group: 音
syntax: pyxel.musics[番号].set(…)
summary: いくつかの音（Sound）をチャンネルごとに並べて、1つの曲にまとめます。
aliases: ミュージック, 曲, BGM, 音楽を作る
api: Music, musics
reads: Music=ミュージック | musics=ミュージックス
--
## 書き方のかたち
::: tpl Music の書き方
pyxel.musics[〔番号〕].set(〔チャンネル0の音〕, 〔チャンネル1の音〕, …)

| 〔番号〕 | 0〜7。曲を入れておく場所 |
| 〔チャンネルごとの音〕 | `[0, 1]` のように、鳴らす音の番号の**リスト**。使わないときは `[]` |
:::

## どんな命令？
`pyxel.musics` は、**曲を入れておく棚**（0〜7番）です。曲は、[[px-sound-class]]で作った音をチャンネルごとに並べて作ります。作った曲は[[px-playm]]で鳴らします。

プログラムで書くのは大変なので、はじめは **Pyxel Editor** で作るのがおすすめです。

```python norun
pyxel.musics[0].set([0, 1], [2], [], [])
pyxel.playm(0, loop=True)
```
チャンネル0で音0→音1を、チャンネル1で音2を、同時に鳴らします。

@@ px-channel-class
title: Channel（音を出すスピーカー）
type: Pyxelのオブジェクト
chapter: 9
group: 音
syntax: pyxel.channels[番号].play(pyxel.sounds[番号])
summary: 音を鳴らす4本のスピーカーです。pyxel.play は、このチャンネルに音を流す命令の、短い書き方です。
aliases: チャンネル, スピーカー, channels, Channel, 同時に鳴らす
api: Channel, channels
reads: Channel=チャンネル | channels=チャンネルズ | play=プレイ | stop=ストップ
--
## 書き方のかたち
::: tpl Channel の書き方
pyxel.channels[〔番号〕].play(pyxel.sounds[〔音の番号〕])
pyxel.channels[〔番号〕].stop()

| 〔番号〕 | チャンネル（スピーカー）の番号。0〜3 |
| 〔音の番号〕 | 鳴らす音の番号。0〜63 |
:::

## どんなもの？
Pyxelの音は、**4本のスピーカー（チャンネル）**から出ます。`pyxel.channels` は、その4本が入った棚です（[[px-objects]]）。

| 番号 | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| スピーカー | チャンネル0 | チャンネル1 | チャンネル2 | チャンネル3 |

4本あるので、**最大4つの音を同時に**鳴らせます。たとえば、チャンネル0でBGM、チャンネル1で効果音、というように使い分けます。

## 使い方
```python px press=KEY_SPACE@2 frames=6
import pyxel

pyxel.init(160, 120, title="channels")
pyxel.sounds[0].set("c3e3g3c4", "p", "7", "n", 8)


def update():
    if pyxel.btnp(pyxel.KEY_SPACE):
        pyxel.channels[0].play(pyxel.sounds[0])
    if pyxel.btnp(pyxel.KEY_X):
        pyxel.channels[0].stop()


def draw():
    pyxel.cls(1)
    pyxel.text(30, 50, "SPACE: PLAY", 10)
    pyxel.text(30, 64, "X: STOP", 8)


pyxel.run(update, draw)
```
スペースキーで、チャンネル0に、サウンド0番を流します。Xキーを押すと、チャンネル0の音が止まります。

## pyxel.play との関係
いつも使っている `pyxel.play(0, 0)` は、次の書き方とほとんど同じ意味です。

| 短い書き方 | 長い書き方 |
| --- | --- |
| `pyxel.play(0, 0)` | `pyxel.channels[0].play(pyxel.sounds[0])` |
| `pyxel.stop(0)` | `pyxel.channels[0].stop()` |

長い書き方のほうが、「**チャンネル0というスピーカー**に、**サウンド0という音**を流す」と、何をしているかが、そのまま読めます（[[object]]）。

::: deep くりかえして鳴らす
`pyxel.channels[0].play(pyxel.sounds[0], loop=True)` と書くと、音が終わっても、また最初から鳴りつづけます。BGMを流したいときに使えます。止めたいときは、`stop` を呼びます。
:::

@@ px-objects
title: オブジェクト一覧（棚と画面）
type: Pyxelのオブジェクト
chapter: 9
group: オブジェクト・データ
syntax: pyxel.sounds[0].set(…) / pyxel.images[0].load(…)
summary: Pyxelに用意されている「オブジェクト」の一覧です。番号つきの5つの棚（images・tilemaps・sounds・musics・channels）と、画面そのもの（screen）があります。
aliases: オブジェクト, 棚, スロット, screen, 画面, メソッド, images, tilemaps, sounds, musics, channels, 一覧
api: screen
reads: object=オブジェクト | screen=スクリーン | images=イメージズ | tilemaps=タイルマップス | sounds=サウンズ | musics=ミュージックス | channels=チャンネルズ
--
## 書き方のかたち
::: tpl オブジェクトの使い方
pyxel.〔棚の名前〕[〔番号〕].〔メソッド〕(〔値〕)

| 〔棚の名前〕 | images、tilemaps、sounds、musics、channels のどれか |
| 〔番号〕 | 棚の何番目か。0から数える |
| 〔メソッド〕 | そのオブジェクトについている命令（set、load、play など） |
:::

## どんなもの？
`pyxel.text(…)` のような**関数**とちがって、`pyxel.sounds[0].set(…)` のように**ドットが2回**出てくるのが、オブジェクトを使うときの書き方です。「pyxel **の** sounds **の** 0番**の** set」と読みます。くわしい考え方は、[[object]]を見よう。

## 5つの棚
| 棚の名前 | 中に入っているモノ | 数 | 番号 | くわしいページ |
| --- | --- | --- | --- | --- |
| `pyxel.images` | ドット絵を置く画像（Image） | 3枚 | 0〜2 | [[px-image-class]] |
| `pyxel.tilemaps` | マップ（Tilemap） | 8個 | 0〜7 | [[px-tilemap-class]] |
| `pyxel.sounds` | 効果音（Sound） | 64個 | 0〜63 | [[px-sound-class]] |
| `pyxel.musics` | 曲（Music） | 8個 | 0〜7 | [[px-music-class]] |
| `pyxel.channels` | 音を出すスピーカー（Channel） | 4本 | 0〜3 | [[px-channel-class]] |

数は、このサイトで動かしたPyxel 2.9.9で調べた数です。バージョンが変わると、増えることもあります。

::: point
番号は**0から**です。`pyxel.sounds` は `0` 〜 `63` なので、`pyxel.sounds[64]` は `IndexError`（範囲の外）になります。
:::

## 画面そのものも、オブジェクト
`pyxel.screen` は、**画面そのもの**を表すオブジェクトです。画像バンクと同じ `Image` の仲間なので、同じ命令（`rect`、`circ`、`text` など）が使えます。

```python px
import pyxel

pyxel.init(160, 120, title="screen")


def update():
    pass


def draw():
    pyxel.cls(1)
    pyxel.rect(20, 30, 50, 40, 8)
    pyxel.screen.rect(90, 30, 50, 40, 8)


pyxel.run(update, draw)
```
左は `pyxel.rect(…)`、右は `pyxel.screen.rect(…)` で描きました。**まったく同じ四角**になります。いつも書いている `pyxel.rect(…)` は、「画面というオブジェクトへの命令」の、短い書き方だったのです。

## 自分で作るオブジェクト
フォントは、棚に入っていません。`pyxel.Font("ファイル名")` で、**自分で作って**変数に入れます（[[px-font-class]]）。

## どのメソッドがあるの？
主なものだけ並べます（使い方は、それぞれのページへ）。

| オブジェクト | 主なメソッド |
| --- | --- |
| Image（`images[0]`、`screen`） | `set`・`load`・`save`・`pget`・`pset`・`cls`・`line`・`rect`・`circ`・`text`・`blt`・`bltm` |
| Tilemap（`tilemaps[0]`） | `set`・`pget`・`pset`・`blt` |
| Sound（`sounds[0]`） | `set`・`mml`・`save` |
| Music（`musics[0]`） | `set`・`save` |
| Channel（`channels[0]`） | `play`・`stop` |

::: deep Pyxelのオブジェクトは、全部同じ考え方で作られている
`images` も `sounds` も `channels` も、Pyxelを作った人が用意した**クラス**（設計図）から作られたオブジェクトです。たとえば、`isinstance(pyxel.sounds[0], pyxel.Sound)` は `True` です。クラスとオブジェクトの関係は、8章の[[class]]を見よう。
:::

@@ px-image-class
title: Image（ドット絵の画像）
type: Pyxelの命令
chapter: 9
group: オブジェクト・データ
syntax: pyxel.images[番号]
summary: ドット絵を入れておく場所（イメージバンク）です。キャラクターの絵をここに入れて、blt で画面にはります。
aliases: イメージ, 画像, ドット絵, スプライト, キャラ絵
api: Image, images
reads: Image=イメージ | images=イメージズ
--
## 書き方のかたち
::: tpl Image の書き方
pyxel.images[〔番号〕].set(〔x〕, 〔y〕, 〔絵のデータ〕)

| 〔番号〕 | 0〜2。イメージバンクの番号 |
| 〔x〕, 〔y〕 | 絵を入れる場所 |
| 〔絵のデータ〕 | 文字のリスト。1文字が1ドットで、0〜f が色の番号 |
:::

## どんな命令？
`pyxel.images` は、**ドット絵をしまっておく3枚の大きな紙**（0〜2番）です。紙の中に絵を描いておいて、[[px-blt]]で必要な部分だけを画面にはります。

絵のデータは**文字**で書けます。1文字が1ドットで、`0`〜`9`・`a`〜`f` が色の番号（0〜15）です（`a` が10、`f` が15）。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="image")
pyxel.images[0].set(0, 0, ["00099000", "00999900", "09999990", "99999999", "99999999", "09999990", "00999900", "00099000"])


def update():
    pass


def draw():
    pyxel.cls(1)
    pyxel.blt(72, 52, 0, 0, 0, 8, 8, 0)
    pyxel.blt(40, 52, 0, 0, 0, 8, 8, 0)
    pyxel.blt(104, 52, 0, 0, 0, 8, 8, 0)


pyxel.run(update, draw)
```

ハートの形に並んだ文字（`9` がオレンジ、`0` は透明）で絵を作って、`blt` で3か所にはっています。

大きな絵を文字で書くのは大変なので、**Pyxel Editor**（`pyxel edit ファイル名.pyxres`）で描くのがふつうです。

@@ px-tilemap-class
title: Tilemap（マップのデータ）
type: Pyxelの命令
chapter: 9
group: オブジェクト・データ
syntax: pyxel.tilemaps[番号]
summary: 小さな絵（タイル）を碁盤の目のように並べて、広いマップを作るための仕組みです。
aliases: タイルマップ, マップ, タイル, RPG
api: Tilemap, tilemaps
reads: Tilemap=タイルマップ | tilemaps=タイルマップス | bltm=ブリットエム
--
## 書き方のかたち
::: tpl Tilemap の書き方
pyxel.bltm(〔x〕, 〔y〕, 〔タイルマップ番号〕, 〔u〕, 〔v〕, 〔幅〕, 〔高さ〕)

| 〔x〕, 〔y〕 | 画面のどこにはるか |
| 〔タイルマップ番号〕 | 0〜7 |
| 〔u〕, 〔v〕 | マップの、どこから切り取るか |
| 〔幅〕, 〔高さ〕 | 切りとる大きさ |
:::

## どんな命令？
RPGのような広いマップは、**小さなタイル（8×8ドット）を並べて**作ります。`pyxel.tilemaps` は、その並べ方を入れておく場所です（0〜7番）。

画面にはるときは `pyxel.bltm` を使います。タイルマップは **Pyxel Editor** で作るのが簡単です。

RPGなどのマップを作るときに使います。まずは、画像（[[px-image-class]]）と `blt`（[[px-blt]]）を使えるようになるのが先です。

@@ px-load
title: load（データを読みこむ）
type: Pyxelの命令
chapter: 9
group: オブジェクト・データ
syntax: pyxel.load(ファイル名)
summary: Pyxel Editor で作ったリソースファイル（.pyxres）を読みこみます。画像や音がまとめて使えるようになります。
aliases: ロード, 読みこむ, pyxres, リソース, Pyxel Editor
api: load
reads: load=ロード | pyxres=ピクセルレス
--
## 書き方のかたち
::: tpl load の書き方
pyxel.load("〔ファイル名〕.pyxres")

| 〔ファイル名〕 | 読みこむファイル。プログラムと同じフォルダに置く |
:::

## どんな命令？
**Pyxel Editor** で作ったドット絵・マップ・効果音・音楽は、`.pyxres` という1つのファイルにまとまっています。`pyxel.load` で読みこむと、`pyxel.images` や `pyxel.sounds` に入ります。

`init` のすぐあとに書きます。

Pyxel Editor は、ターミナルで `pyxel edit ファイル名.pyxres` と打つと開きます。まだないファイル名を書くと、新しいファイルとして始められます（保存すると作られます）。

@@ px-font-class
title: Font（フォント）
type: Pyxelの命令
chapter: 9
group: オブジェクト・データ
syntax: pyxel.Font(ファイル名)
summary: 日本語など、はじめから入っていない文字を書くためのフォントを読みこみます。
aliases: フォント, 日本語, 文字, bdf
api: Font
reads: Font=フォント | bdf=ビーディーエフ
--
## 書き方のかたち
::: tpl Font の書き方
〔変数〕 = pyxel.Font("〔ファイル名〕")
pyxel.text(〔x〕, 〔y〕, "〔日本語〕", 〔色〕, 〔変数〕)

| 〔変数〕 | 読みこんだフォントを入れる名前（font など） |
| 〔ファイル名〕 | umplus_j12r.bdf など。プログラムと同じフォルダに置く |
:::

## どんな命令？
Pyxelの最初から入っている文字は、英数字だけです。`pyxel.Font` で日本語が入ったフォントを読みこむと、日本語が書けます。

練習用の `umplus_j10r.bdf` と `umplus_j12r.bdf` は、`pyxel copy_examples` で手に入ります（[[pyxel-jp]]）。

## 使い方
```python px
import pyxel

pyxel.init(160, 120, title="Font")
font = pyxel.Font("umplus_j12r.bdf")


def update():
    pass


def draw():
    pyxel.cls(1)
    pyxel.text(20, 40, "日本語もOK！", 10, font)
    haba = font.text_width("日本語もOK！")
    pyxel.text(20, 70, f"よこの長さ {haba}", 7, font)


pyxel.run(update, draw)
```

`font.text_width("文字")` で、その文字の**横の長さ**が分かります。真ん中にそろえるときに便利です。

詳しくは[[pyxel-jp]]を見よう。
