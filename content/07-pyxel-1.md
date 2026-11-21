@@ ch7
title: はじめの一歩
kind: chapter
chapter: 7
summary: Pyxelで、自分の画面（ウィンドウ）を出します。Pyxelのプログラムがどう動くのか、しくみを知るところから始めます。
reads: pyxel=ピクセル | init=イニット | run=ラン | update=アップデート | draw=ドロー
--
## ここから、Pyxelでゲームを作る
ここまでは、`print` で文字を出すだけでした。ここからは**自分の画面（ウィンドウ）**を開いて、文字や図形を出したり、動かしたりします。使うのは、レトロゲームが作れる[[pyxel]]というライブラリです。

たった20行ほどのプログラムで、こんなふうに動きます。

```python px gif frames=60
import pyxel

pyxel.init(160, 120, title="はじめてのPyxel")
x = 0


def update():
    global x
    x = (x + 2) % 160


def draw():
    pyxel.cls(1)
    pyxel.circ(x, 60, 10, 10)
    pyxel.text(40, 20, "HELLO PYXEL!", 7)


pyxel.run(update, draw)
```
今は意味が分からなくて大丈夫。Pyxel 1を読み終わるころには、1行ずつ説明できるようになります。

::: scratch
Scratchでは「緑の旗が押されたとき」→「ずっと」の中にブロックを入れて、キャラクターを動かしました。Pyxelでは、その「ずっと」の役目を `pyxel.run` がやってくれます。「ずっと」の中身を書く場所が、`update` と `draw` です（[[update-draw]]）。
:::

### Pyxel 1 で読むページ（この順番で）
1. [[pyxel]]：Pyxelってなに？ どうやって入れる？
2. [[window]]：ウィンドウを出す（`init` と `run`）
3. [[update-draw]]：`update` と `draw` のしくみ（いちばん大事）
4. [[coordinate]]：画面の「場所」の決め方
5. [[color]]：16色のパレット

::: point このあとの進み方
| 区切り | 中身 |
| --- | --- |
| Pyxel 1 はじめの一歩 | 画面を出して、しくみを知る（ここ） |
| Pyxel 2 描く・動かす | 文字・図形を描いて、キーやマウスで動かす（[[pyxel2]]） |
| Pyxel 3 作品を作る | 占い・ストップウォッチ・ゲームを作る（[[pyxel3]]） |
| Pyxel 4 絵と音 | ドット絵や音を使う、作品を配る（[[pyxel4]]） |
| Pyxel 5 ゲームの技 | 作りたいゲームに合わせて選ぶ（[[pyxel5]]） |
| Pyxel 6 クラスで作ろう | 同じゲームを、クラスで書く（[[ch8]]） |

分からない命令が出てきたら、[[ch9|Pyxel辞典]]で引けます。コードの中の言葉をクリックしてもOKです。
:::

@@ pyxel
title: Pyxel（ピクセル）
type: ライブラリ
chapter: 7
syntax: import pyxel
summary: レトロゲーム風の画面（16色・ドット絵）のゲームが作れる、Pythonのライブラリです。pip install で追加して使います。
aliases: ピクセル, ぴくせる, レトロゲーム
api: pyxel
reads: pyxel=ピクセル | import=インポート | init=イニット | run=ラン
--
## Pyxelってなに？
Pyxel（ピクセル）は、**レトロゲームを作るための、Pythonのライブラリ**です。ファミコンのようなドット絵と電子音のゲームを、Pythonだけで作れます。

**ライブラリ**は、Pythonにあとから足して使う、便利な部品のセットです。スマホに、ストアからアプリを入れるのと同じです。だから、Pyxelは最初からは入っておらず、`pip install pyxel` で入れて使います。`import pyxel` で読みこむので、「Pyxelモジュール」と呼んでもまちがいではありません。この図鑑では、ライブラリと呼びます（[[library]]）。

## Pyxelでできること
| やりたいこと | Pyxelでは |
| --- | --- |
| 画面に絵や文字を出す | `rect`、`text`、`blt` など |
| キーやマウスを調べる | `btn`、`mouse_x` など |
| 音を鳴らす | `play`、`sounds` など |
| ゲームを動かしつづける（1秒に30回、`update` と `draw` を呼ぶ） | `run` |
| 絵・マップ・音を作る | [[pyxel-editor|Pyxel Editor]] |

ゲームに必要なことが、ひととおりそろっています。

::: deep ゲームエンジンとも呼ばれる
Pyxelのように、ゲームを作るのに必要なことを、まとめて引き受けてくれる部品のセットを、**ゲームエンジン**とも呼びます。Pyxel自身も、「A retro game engine for Python（Python向けのレトロゲームエンジン）」と名のっています。UnityやGodotのような大きなゲームエンジンにくらべると、小さくてシンプルです。

「ライブラリ」「ゲームエンジン」「パッケージ」、どれで呼んでも、まちがいではありません。この図鑑では、「ライブラリ」と呼んでいます。
:::

## レトロゲームのきまり
Pyxelは、わざと昔のゲーム機と同じような「きまり」で作られています。

| きまり | 内容 |
| --- | --- |
| 画面 | 小さい（たとえば 160 × 120 ドット） |
| 色 | 16色だけ（[[color]]） |
| 音 | 同時に4つまで |
| 文字 | はじめは、英数字だけ（日本語は[[pyxel-jp]]） |

できることがしぼられているので、初心者でもすぐに形になります。

## 使えるようにする
Pyxelは最初からは入っていないので、**1回だけ**インストールします。ターミナル（コマンドを打ちこむ画面。[[terminal]]）で、次のように打ちます。

```bash
pip install pyxel
```
そして、プログラムの先頭に、次の1行を書きます。

```python norun
import pyxel
```

## いちばん小さいプログラム
文字を出すだけの、いちばん短いプログラムです。いつもPythonを書いているエディタ（VS Code など）に書いて、実行してみよう。

```python px
import pyxel

pyxel.init(160, 120, title="はじめてのPyxel")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(50, 55, "HELLO PYXEL!", 7)


pyxel.run(update, draw)
```
ウィンドウが開いて、黒い画面に文字が出ます。**ESCキー**を押すと終わります。

## print とのちがい
| | print | Pyxel |
| --- | --- | --- |
| 出る場所 | ターミナル | 自分のウィンドウ |
| 実行 | 上から下に、1回で終わる | **止まらずに、動きつづける** |
| 出せるもの | 文字 | 文字・図形・画像・音 |

「止まらずに動きつづける」のしくみは、[[update-draw]]で学びます。

::: stuck
`ModuleNotFoundError: No module named 'pyxel'` と出たら、Pyxelがまだインストールされていません。ターミナルで `pip install pyxel` を実行しよう（[[error]]）。

`pip` が見つからないと言われたときは、`pip3 install pyxel` や `python -m pip install pyxel` を試してみよう。
:::

::: deep もっと知りたい人へ
Pyxelの命令は、全部で数十個あります。[[ch9|Pyxel辞典]]に一覧があります。最初は、使うものだけ覚えればOKです。
:::

@@ window
title: ウィンドウを出す（init と run）
type: 考え方
chapter: 7
syntax: pyxel.init(幅, 高さ)
summary: init で画面の大きさを決めて、run でゲームを動かしはじめます。この2つが、Pyxelプログラムの骨組みです。
aliases: init, イニット, ウィンドウ, 画面を出す, 骨組み
reads: init=イニット | run=ラン | import=インポート | update=アップデート | draw=ドロー
--
## 書き方のかたち
::: tpl Pyxelプログラムの骨組み
import pyxel
pyxel.init(〔幅〕, 〔高さ〕, title="〔タイトル〕")
def update():
····〔動かす処理〕
def draw():
····〔描く処理〕
pyxel.run(update, draw)

| 〔幅〕 | 画面の横の大きさ（ドット数）。160 など |
| 〔高さ〕 | 画面の縦の大きさ。120 など |
| 〔タイトル〕 | ウィンドウの上に出る名前（なくてもOK） |
| 〔動かす処理〕 | [[update-draw]]で説明します |
| 〔描く処理〕 | 画面に描く命令を書きます |
:::

## init ってなに？
`init` は、**initialize（イニシャライズ）＝はじめの準備**を短くした言葉です。ゲームを始める前に「**画面の大きさはこれだよ**」とPyxelに教える命令です。

```python px
import pyxel

pyxel.init(160, 120, title="ウィンドウのテスト")


def update():
    pass


def draw():
    pyxel.cls(5)
    pyxel.text(8, 8, "WIDTH 160 x HEIGHT 120", 7)


pyxel.run(update, draw)
```
`pyxel.init(160, 120)` は、「幅160ドット、高さ120ドットの画面を用意して」という意味です。

::: point
`init` は、プログラムの**最初に1回だけ**書きます。2回書く必要はありません。
:::

## 画面の大きさを変えてみる
数字を変えると、画面の大きさが変わります。

```python px
import pyxel

pyxel.init(80, 60, title="ちいさい画面")


def update():
    pass


def draw():
    pyxel.cls(3)
    pyxel.text(8, 8, "80 x 60", 7)


pyxel.run(update, draw)
```
画面を小さくしても、ウィンドウは見やすい大きさに自動で拡大されます。

## run ってなに？
`run` は、**ゲームを動かしはじめる**命令です。`run` を書くと、Pyxelがウィンドウを開いて、あなたが作った `update` と `draw` を何度も繰り返し呼び出します。

`pyxel.run(update, draw)` のかっこの中には、**関数の名前**を書きます。

::: stuck
`pyxel.run(update(), draw())` のように、関数の名前に `()` をつけるとエラーになります。ここでは関数を自分で**呼び出す**のではなく、「この関数を呼んでね」とPyxelに**渡す**ので、`()` はつけません（[[function]]）。
:::

## 順番が大切
1. `import pyxel`（Pyxelを使えるようにする）
2. `pyxel.init(...)`（画面を決める）
3. `def update()` と `def draw()`（動かす係・描く係をつくる）
4. `pyxel.run(update, draw)`（動かしはじめる）

`run` は**いちばん最後**に書きます。`run` のあとに書いたものは、ウィンドウを閉じるまで実行されません。

@@ update-draw
title: update と draw
type: 考え方
chapter: 7
syntax: def update(): / def draw():
summary: update は「動かす係」、draw は「描く係」。この2つを、Pyxelが1秒に30回繰り返し呼び出します。
aliases: アップデート, ドロー, フレーム, ゲームループ, fps
reads: update=アップデート | draw=ドロー | global=グローバル | frame=フレーム
--
## ゲームは、パラパラ漫画
ゲームの画面は、**パラパラ漫画**と同じです。1秒間に30枚の絵を次々に切り替えて、動いているように見せています。この1枚1枚を**フレーム**といいます。

Pyxelは、1フレームごとに2つの関数を呼び出します。

| 関数 | 役目 | 書くこと |
| --- | --- | --- |
| `update` | 動かす係 | 変数を変える、計算する、キーを調べる |
| `draw` | 描く係 | 画面に、文字や図形を描く |

::: flow gameloop Pyxelの流れ
:::

## 書き方のかたち
::: tpl update と draw の書き方
def update():
····〔動かす処理〕
def draw():
····pyxel.cls(〔背景の色〕)
····〔描く処理〕
pyxel.run(update, draw)

| 〔動かす処理〕 | 変数を変えるなど。画面には何も描かない |
| 〔背景の色〕 | まず画面全体を塗りつぶす（[[px-cls]]）。0〜15の数 |
| 〔描く処理〕 | 文字や図形を描く。ゲームの変数（位置や点数）は、ここでは変えない |
:::

## 動かしてみる
四角の位置 `x` を `update` で少しずつ増やして、`draw` で描きます。

```python px gif frames=60
import pyxel

pyxel.init(160, 120, title="うごく四角")
x = 0


def update():
    global x
    x = x + 2


def draw():
    pyxel.cls(1)
    pyxel.rect(x, 50, 20, 20, 10)


pyxel.run(update, draw)
```
1フレームごとに `x` が2ずつ増えるので、四角が右に動きます。

## global ってなに？
`update` の中で、関数の外にある `x` を**書き換える**ときは、`global x` と書きます。「関数の外にある、あの `x` を書き換えるよ」という宣言です（[[scope]]）。

5章の[[scope]]で、「関数の中で作った変数は、関数の外とは別もの」と学びました。`global` を書かずに `x = x + 2` とすると、Pythonは「`update` の中だけの新しい `x`」だと考えてしまいます。

::: stuck
`global` を書き忘れると、`UnboundLocalError` というエラーになります。`update` の中で変数を書き換えるときは、関数の先頭に `global 変数名` を書こう。

読むだけ（`draw` で `x` を使って描くだけ）なら、`global` はいりません。
:::

## なぜ、2つに分けるの？
「計算」と「描く」を分けると、プログラムが読みやすくなり、間違いも見つけやすくなります。**動かす係（update）は動かすだけ、描く係（draw）は描くだけ。** これがゲームづくりの基本のルールです。

@@ coordinate
title: 座標（x と y）
type: 考え方
chapter: 7
syntax: (x, y)
summary: 画面の上の「場所」を、横（x）と縦（y）の2つの数で表します。左上が (0, 0) です。
aliases: 座標, ざひょう, x, y, 位置
reads: x=エックス | y=ワイ
--
## 場所を、数で伝える
Pyxelでは、画面のどこに描くかを**2つの数**で指定します。

- **x**：左から、何ドット目か（横の位置）
- **y**：上から、何ドット目か（縦の位置）

::: flow coord 座標のしくみ
:::

::: point
数学のグラフとちがって、**y は下に行くほど大きくなります**。ここがいちばん間違えやすいところです。
:::

::: scratch
Scratchでは、画面の**真ん中**が (0, 0) で、上に行くほど y が大きくなりました。Pyxelでは、**左上**が (0, 0) で、**下に行くほど y が大きく**なります。Scratchの感覚で「上に動かすから y を増やす」と書くと、下に動いてしまうので注意しよう。
:::

## 試してみる
いろいろな場所に、点を打ってみます。

```python px
import pyxel

pyxel.init(160, 120, title="座標")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.pset(0, 0, 8)
    pyxel.pset(80, 60, 10)
    pyxel.pset(159, 119, 11)
    pyxel.text(4, 4, "(0, 0)", 7)
    pyxel.text(60, 66, "(80, 60)", 7)
    pyxel.text(100, 108, "(159, 119)", 7)


pyxel.run(update, draw)
```
画面の大きさが 160 × 120 のとき、いちばん右下は `(159, 119)` です。0から数えるので、`160` や `120` より1つ小さい数になります（[[list-index]]と同じ考え方です）。

## 四角の位置
`pyxel.rect(x, y, 幅, 高さ, 色)` の `x` と `y` は、四角の**左上**の位置です。

```python px
import pyxel

pyxel.init(160, 120, title="四角の位置")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rect(20, 30, 50, 40, 9)
    pyxel.pset(20, 30, 7)


pyxel.run(update, draw)
```
白い点が、`(20, 30)` で、四角の左上の角です。

@@ color
title: 色（16色パレット）
type: 考え方
chapter: 7
syntax: 色は 0〜15 の数
summary: Pyxelで使える色は16色。0〜15の数で指定します。
aliases: パレット, 色番号, カラー, いろ
api: COLOR_
reads: color=カラー | palette=パレット
--
## 色は、数で指定する
Pyxelで使える色は**16色だけ**です。それぞれに0から15の番号がついていて、描く命令の最後にその番号を書きます。

```python px
import pyxel

pyxel.init(160, 120, title="16色")


def update():
    pass


def draw():
    pyxel.cls(0)
    for i in range(16):
        x = (i % 4) * 40 + 4
        y = (i // 4) * 28 + 4
        pyxel.rect(x, y, 32, 20, i)
        pyxel.text(x + 2, y + 2, str(i), 7 if i < 7 or i > 8 else 0)


pyxel.run(update, draw)
```
0が黒、7が白、8が赤、10が黄色……のように決まっています。

## 色の名前でも書ける
番号の代わりに名前でも書けます。`pyxel.COLOR_RED` は `8` と同じです。

| 番号 | 名前 | 色 |
| --- | --- | --- |
| 0 | `pyxel.COLOR_BLACK` | 黒 |
| 1 | `pyxel.COLOR_NAVY` | 濃い青 |
| 2 | `pyxel.COLOR_PURPLE` | 紫 |
| 3 | `pyxel.COLOR_GREEN` | 青緑 |
| 4 | `pyxel.COLOR_BROWN` | 茶色 |
| 5 | `pyxel.COLOR_DARK_BLUE` | 青 |
| 6 | `pyxel.COLOR_LIGHT_BLUE` | 薄い青 |
| 7 | `pyxel.COLOR_WHITE` | 白 |
| 8 | `pyxel.COLOR_RED` | 赤 |
| 9 | `pyxel.COLOR_ORANGE` | オレンジ |
| 10 | `pyxel.COLOR_YELLOW` | 黄色 |
| 11 | `pyxel.COLOR_LIME` | 薄い緑 |
| 12 | `pyxel.COLOR_CYAN` | 水色 |
| 13 | `pyxel.COLOR_GRAY` | グレー |
| 14 | `pyxel.COLOR_PINK` | ピンク |
| 15 | `pyxel.COLOR_PEACH` | 肌色 |

::: point
最初は**番号**で書くのが簡単です。よく使うのは、0（黒）・7（白）・8（赤）・10（黄色）です。
:::
