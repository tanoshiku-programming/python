@@ pyxel-editor
title: Pyxel Editor（絵・マップ・音を作る道具）
type: 道具
chapter: 10
syntax: pyxel edit ファイル名.pyxres
summary: Pyxel Editor は、ドット絵・マップ・効果音・音楽を作るための、Pyxelについてくる道具です。作ったものは .pyxres というファイル1つに入って、pyxel.load で読みこめます。
aliases: Pyxel Editor, ピクセルエディタ, エディタ, pyxres, イメージエディタ, タイルマップエディタ, サウンドエディタ, ミュージックエディタ, リソースファイル
reads: pyxres=ピクセルレス | edit=エディット | load=ロード | resource=リソース
--
## プログラムで絵を書くのは、たいへん
[[game-image]]では、`images[0].set(0, 0, ["000aaa00", …])` のように、**文字で**ドット絵を書きました。8×8のひよこ1羽でも、それなりに手間がかかります。大きな絵や、たくさんの絵を、文字で書くのは現実的ではありません。

そこで使うのが **Pyxel Editor** です。Pyxel をインストールすると、いっしょに入っています。マウスで絵を描いたり、音符を並べたりして、**絵・マップ・効果音・音楽**を作れる道具です。

## 起動のしかた
ターミナルで、次のように打ちます（[[terminal]]）。

```bash
pyxel edit my_game.pyxres
```
`my_game.pyxres` は、自分で決めるファイル名です。まだないファイル名を書くと、新しく作る状態で始まります。使い方（どのボタンを押すか）は、授業で教わろう。

## 4つのエディタ
Pyxel Editor の中には、4つのエディタがあります。**作ったものは、プログラムの中の決まった場所に入ります。**

| エディタ | 作るもの | プログラムでの名前 | 数 |
| --- | --- | --- | --- |
| イメージエディタ | ドット絵 | `pyxel.images[番号]`（[[px-image-class]]） | 3枚（0〜2）。1枚は 256×256 |
| タイルマップエディタ | マップ | `pyxel.tilemaps[番号]`（[[px-tilemap-class]]） | 8枚（0〜7） |
| サウンドエディタ | 効果音 | `pyxel.sounds[番号]`（[[px-sound-class]]） | 64個（0〜63） |
| ミュージックエディタ | 曲（BGM） | `pyxel.musics[番号]`（[[px-music-class]]） | 8曲（0〜7） |

つまり、これまでプログラムで書いてきた `images[0].set(…)` や `sounds[0].set(…)` と、**同じ場所**に、マウスで作ったものが入るのです。

::: point
「4つのエディタ」と「プログラムの4つの置き場」は、1対1でつながっています。エディタで作る（絵）→ プログラムで使う（`blt`）、エディタで作る（音）→ プログラムで使う（`play`）。
:::

## .pyxres ファイル
Pyxel Editor で作ったもの（絵・マップ・音・曲）は、**`.pyxres` という拡張子のファイル1つ**に、まとめて保存されます（[[pyfile]]）。

```python px
import pyxel

pyxel.init(160, 120, title="pyxres を読みこむ")
pyxel.load("hiyoko.pyxres")


def update():
    pass


def draw():
    pyxel.cls(5)
    pyxel.bltm(0, 90, 0, 0, 0, 160, 24)
    pyxel.blt(76, 82, 0, 0, 0, 8, 8, 0)


pyxel.run(update, draw)
```
`pyxel.load("hiyoko.pyxres")` を `init` のあとに1回書くと、ファイルの中の絵・マップ・音・曲が、全部まとめて `images` や `sounds` などに読みこまれます（[[px-load]]）。`hiyoko.pyxres` のところは、自分で作ったファイルの名前に変えて使います。

この画面の草と土のマップ（`bltm`）と、ひよこ（`blt`）は、どちらも `hiyoko.pyxres` の中に入っているものです。プログラムの中には、絵の文字データは1つも書いていません。

この `.pyxres` を使って、ひよこを歩かせるゲームは、[[pyxres-game]]で作ります。

## ファイルの置き場所
`.pyxres` ファイルは、**プログラム（.py）と同じフォルダ**に置きます。Pyxelは、プログラムのあるフォルダからファイルを探します。

::: stuck
- ファイル名のつづりや、`.pyxres` を書き忘れていないか確かめよう。`Failed to open file '…'`（ファイルを開けません）と出たら、たいてい名前か置き場所のまちがいです（[[error]]）
- `pyxel edit` で保存したつもりでも、別のフォルダに保存されていることがあります。保存した場所を、必ず確かめよう
- `pyxel.load` は、`init` のあとに書きます。`init` の前に書くと、`Pyxel not initialized`（Pyxelが準備できていません）というエラーになります
:::

::: deep 一部だけ読みこまない
`pyxel.load("my_game.pyxres", exclude_sounds=True)` のように書くと、音だけ読みこまない、という使い方もできます。絵だけを読みこみたいときなどに便利です。
:::

@@ pyxres-game
title: Editorで作った絵と音でゲームを作ろう
type: 作品
chapter: 10
syntax: pyxel.load("my_game.pyxres")
summary: Pyxel Editor で作った絵・マップ・音を、pyxel.load で読みこんで、キーで歩いて音も鳴るひよこのプログラムを作ります。
aliases: pyxres, 絵と音, ひよこ, エディタで作る, 歩く
reads: load=ロード | bltm=ブリットエム | play=プレイ
--
## 作るもの
[[pyxel-editor]]で作った `hiyoko.pyxres`（ひよこ2枚・草と土のタイル・効果音）を使って、**左右キーで歩いて、スペースキーで鳴く**ひよこを作ります。

| 中に入っているもの | 場所 |
| --- | --- |
| 歩く2枚のひよこ | イメージバンク0番の (0, 0) と (8, 0) |
| 草と土のタイル | イメージバンク0番の (16, 0) と (24, 0)。タイルマップ0番に並べてある |
| 効果音 | サウンド0番（ピコン） |

## プログラム
```python px gif frames=40 hold=KEY_RIGHT
import pyxel

pyxel.init(160, 120, title="歩くひよこ")
pyxel.load("hiyoko.pyxres")
x = 20
muki = 1


def update():
    global x, muki
    if pyxel.btn(pyxel.KEY_LEFT):
        x = x - 1
        muki = -1
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 1
        muki = 1
    if pyxel.btnp(pyxel.KEY_SPACE):
        pyxel.play(0, 0)


def draw():
    pyxel.cls(5)
    pyxel.bltm(0, 90, 0, 0, 0, 160, 24)
    u = pyxel.frame_count // 8 % 2 * 8
    pyxel.blt(x, 82, 0, u, 0, 8 * muki, 8, 0)


pyxel.run(update, draw)
```
画像は、右キーを押しつづけて、ひよこが歩いているところです。

## 仕組みを読み解く
- `pyxel.load("hiyoko.pyxres")`：絵・マップ・音を、まとめて読みこむ。**最初に1回だけ**
- `pyxel.bltm(0, 90, 0, 0, 0, 160, 24)`：タイルマップ0番の左上から 160×24 ドットを、画面の (0, 90) にはる（[[px-bltm]]）。草と土の地面がこれ
- `pyxel.blt(x, 82, 0, u, 0, 8 * muki, 8, 0)`：ひよこをはる。`u` を 0 と 8 で入れかえて足を動かし、幅を `8 * muki` にして左右の向きを変える（[[game-image]]と同じ仕組み）
- `pyxel.play(0, 0)`：サウンド0番を、チャンネル0で鳴らす（[[game-sound]]）

[[game-image]]や[[game-sound]]では、絵や音を**プログラムの中で**作りました。今回は、絵や音を**ファイルから**読みこんだので、プログラムは、動かす部分だけの短さになっています。

::: point
絵や音を作る作業（Pyxel Editor）と、動かす作業（プログラム）を分けると、それぞれに集中できます。絵を描きなおしても、プログラムは1文字も直さなくて済みます。
:::

::: scratch
Scratchの「コスチュームタブ」「音タブ」で、絵や音を作ってから、「コード」タブで動かしましたね。Pyxel Editor は、コスチュームタブと音タブにあたります。Scratchでは1つのプロジェクトにまとまっていましたが、Pyxelでは、絵や音は `.pyxres` に、動かす部分は `.py` に、**ファイルが分かれます**。
:::

@@ game-package
title: 作ったゲームを配ろう
type: 作品
chapter: 10
syntax: pyxel package APP_DIR スタートのファイル.py
summary: pyxel package でゲームを1つのファイル（.pyxapp）にまとめて、pyxel app2html でブラウザで遊べる HTML にします。友だちや家族に配る方法です。
aliases: 配る, 公開, パッケージ, pyxapp, app2html, app2exe, play, 共有, 友だちに遊んでもらう, watch
reads: package=パッケージ | pyxapp=ピクセルアップ | app2html=アップツーエイチティーエムエル | app2exe=アップツーイーエグゼ | play=プレイ | watch=ウォッチ
--
## 配るときの問題
作ったゲームは、自分のパソコンなら `.py` ファイルで動きます。でも友だちのパソコンには、Python も Pyxel も入っていないかもしれません。絵や音のファイル（`.pyxres`）も、いっしょに渡さないと動きません。

そこで、**ゲームに必要なものを、まとめて1つにする**道具が、Pyxel にあります。

## 全体の流れ
```
ゲームのフォルダ  →  .pyxapp  →  HTML（ブラウザで遊べる）
                    （まとめた1つのファイル） →  exe（Windowsで遊べる）
```
| 手順 | コマンド | できるもの |
| --- | --- | --- |
| ① 1つにまとめる | `pyxel package フォルダ スタートのファイル.py` | `フォルダ名.pyxapp` |
| ② 遊んでみる | `pyxel play フォルダ名.pyxapp` | Pyxel がある人なら、そのまま遊べる |
| ③-A ブラウザ用にする | `pyxel app2html フォルダ名.pyxapp` | `フォルダ名.html` |
| ③-B 実行ファイルにする | `pyxel app2exe フォルダ名.pyxapp` | Windows や Mac の実行ファイル（PyInstaller が必要） |

## ① まとめる（package）
ゲームを**専用のフォルダ**にまとめます。たとえば、`hiyoko_game` フォルダの中に、`main.py` と `hiyoko.pyxres` を入れます。

```bash
pyxel package hiyoko_game hiyoko_game/main.py
```
- `hiyoko_game`：まとめたいフォルダ
- `hiyoko_game/main.py`：ゲームを始めるプログラム

実行すると、`hiyoko_game.pyxapp` というファイルができます。フォルダの中の `.py` と `.pyxres` が、全部1つに入ります。

::: stuck
- 絵や音のファイルは、**そのフォルダの中**に入れておこう。フォルダの外にあると、まとめられません
- スタートのファイルの名前は、フォルダの名前をつけて書きます（`hiyoko_game/main.py`）
:::

## ② 遊んでみる（play）
```bash
pyxel play hiyoko_game.pyxapp
```
`.pyxapp` を、そのまま遊べます。Pyxel が入っている人に配るなら、この `.pyxapp` 1つを渡すだけで済みます。

## ③-A ブラウザで遊べる HTML にする（app2html）
```bash
pyxel app2html hiyoko_game.pyxapp
```
`hiyoko_game.html` ができます。**ゲームの中身は、この HTML の中に全部入っています。**ファイルが1つだけなので、渡しやすいです。

ブラウザで開くと遊べて、Python も Pyxel も入っていない人でも大丈夫です。ただし、**インターネットにつながっている必要があります**。HTML が、Pyxel を動かす部品を、ネットから読みこんでいるからです。

::: deep 世界中の人に遊んでもらう
できあがった HTML を、Webサイトとして公開すれば、URLを知っている人はだれでも遊べます。このサイトも使っている **GitHub Pages** のような、無料で公開できるしくみがあります。公開のしかたは、授業で相談しよう。
:::

::: deep ③-B 実行ファイルにする（app2exe）
```bash
pyxel app2exe hiyoko_game.pyxapp
```
ダブルクリックで遊べる、実行ファイルができます。ただし、**PyInstaller** というモジュールが、別に必要です（`pip install pyinstaller`。[[terminal]]）。入っていないと、`PyInstaller is not found` と言われます。
:::

::: stuck
実行ファイルは、**作ったパソコンの種類**用のものになります。Windowsで作れば Windows 用、Mac で作れば Mac 用です。Windows の友だちに配りたいなら、Windows で作る必要があります。
:::

::: deep おまけ：書きながら確かめる（watch）
```bash
pyxel watch フォルダ main.py
```
ゲームのフォルダを見はっていて、**ファイルを保存するたびに、自動で動かしなおして**くれます。絵や音を直しながら、すぐ画面で確かめたいときに便利です（`Ctrl + C` で止まります。[[infinite-loop]]）。
:::

## 配る前のチェック
| 確認すること | 理由 |
| --- | --- |
| 絵・音のファイルを、ゲームのフォルダに入れたか | 入っていないと、配った先で `Failed to open file` |
| ファイル名は半角英数字か | 日本語やスペースは、うまく動かないことがある |
| 自分のパソコンで、`pyxel play` で動いたか | 配る前に、まず自分で遊んでみる |
