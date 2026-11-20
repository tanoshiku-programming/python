@@ ch7
title: Pyxelで作ろう
kind: chapter
chapter: 7
summary: Pyxelを使うと、画面に文字や図形を出して、動かせます。基礎から、占いアプリ・ストップウォッチ・ゲームまで作ります。
reads: pyxel=ピクセル | init=イニット | run=ラン | update=アップデート | draw=ドロー
--
## この章のゴール
ここまでは、`print` で文字を出すだけでした。この章からは**自分の画面（ウィンドウ）**を開いて、文字や図形を出したり動かしたりします。ゲームも作れます。

使うのは、レトロゲーム風の画面が作れる[[pyxel]]というモジュールです。

## 完成イメージ
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
今は意味が分からなくて大丈夫。この章を読み終わるころには、1行ずつ説明できるようになります。

## 学ぶ順番
1. [[pyxel]]：Pyxelって、なに？
2. [[window]]：ウィンドウを出す（`init` と `run`）
3. [[update-draw]]：`update` と `draw` のしくみ
4. [[coordinate]]：画面の「場所」の決め方
5. [[color]]：16色のパレット
6. [[pyxel-text]]：文字を表示する
7. [[shapes]]：いろいろな図形をかく
8. [[pyxel-var]]：変数を使って、動かす
9. [[pyxel-key]]：キーで操作する
10. [[pyxel-mouse]]：マウスで操作する
11. [[pyxel-jp]]：日本語を表示する
12. [[app-fortune]]：占いアプリを作る
13. [[app-timer]]：ストップウォッチを作る
14. [[game-catch]]：ゲームを作る
15. [[game-scene]]：タイトル画面と結果画面をつける
16. [[game-list]]：たくさんのものを動かす
17. [[game-image]]：画像を表示して動かす
18. [[game-hit]]：当たり判定を作る
19. [[game-sound]]：音を鳴らす

### ゲームの技
必要になったものから読もう。

- [[game-shot]]：弾を撃つ
- [[game-enemy]]：敵を出す
- [[game-scroll]]：スクロール
- [[game-map]]：マップ
- [[game-jump]]：ジャンプ
- [[game-wall]]：壁にぶつかったら止める
- [[game-effect]]：爆発・ゆれ・無敵時間
- [[game-highscore]]：ハイスコアとランキング

::: point
Pyxelの命令の意味は、[[ch9|Pyxel辞典]]でいつでも引けます。分からない命令が出てきたら、コードの中の言葉をクリックしてみよう。
:::

::: scratch
Scratchでは「緑の旗が押されたとき」→「ずっと」の中にブロックを入れて、キャラクターを動かしました。Pyxelでは、その「ずっと」の役目を `pyxel.run` がやってくれます。「ずっと」の中身を書く場所が `update` と `draw` です（[[update-draw]]）。
:::

@@ pyxel
title: Pyxel（ピクセル）
type: モジュール
chapter: 7
syntax: import pyxel
summary: レトロゲーム風の画面（16色・ドット絵）が作れる、ゲーム作り用のモジュールです。
aliases: ピクセル, ぴくせる, レトロゲーム
api: pyxel
reads: pyxel=ピクセル | import=インポート | init=イニット | run=ラン
--
## Pyxelってなに？
Pyxel（ピクセル）は、**レトロゲーム風のゲームが作れる**Pythonのモジュールです。[[module]]のひとつなので、[[import]]して使います。

ファミコンのようなドット絵と電子音のゲームを、Pythonだけで作れます。

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
