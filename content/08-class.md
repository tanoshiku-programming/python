@@ ch8
title: クラスで作ろう
kind: chapter
chapter: 8
summary: 「クラス」を使うと、キャラクターの変数と動きを1つにまとめて書けます。7章で作ったゲームを、クラスの書き方で作りなおして、見比べます。
reads: class=クラス | self=セルフ | __init__=イニット | App=アップ
--
## この章のゴール
7章では、ほしの位置を `hoshi_x`、`hoshi_y`、バーの位置を `bar_x`……と、変数をどんどん増やしてゲームを作りました。`update` で変数を書きかえるたびに、`global` も書きましたね。

ゲームが大きくなると、変数が何十個にもなって、「どの変数が、何のものだっけ？」と分からなくなってきます。そこで使うのが**クラス**です。クラスを使うと、

- 「ほしの位置」「ほしの速さ」「ほしを動かす」「ほしを描く」を、**ほしのクラス1つにまとめられる**
- `global` を書かなくてよくなる
- 同じキャラクターを、いくつでも簡単に作れる

::: scratch
Scratchの**スプライト**を思い出そう。ネコのスプライトは、自分の「x座標」「y座標」と、自分の「スクリプト」を持っていました。クラスは、このスプライトの**設計図**です。そして、Scratchの「**クローンを作る**」のように、設計図から同じキャラクターを何体でも作れます。
:::

## クラスなしと、クラスあり。どっちが正解？
**どちらも正解です。** 同じゲームを、どちらの書き方でも作れます。

| | クラスなし（7章） | クラスあり（この章） |
| --- | --- | --- |
| 書く量 | 少ない | 少し多い |
| 分かりやすさ | 短いプログラムなら、こっちが簡単 | 大きなプログラムになるほど、こっちが整理しやすい |
| `global` | 必要 | いらない |
| 同じキャラを増やす | リストを何本も用意する | クラスから何体でも作れる |

どちらから始めるかは、先生と相談して決めよう。7章の書き方に慣れてからこの章に進んでも、最初からクラスで書いても、どちらでも大丈夫です。

## 学ぶ順番
1. [[class]]：クラスとインスタンス（設計図と実物）
2. [[init-self]]：`__init__` と `self`
3. [[method]]：メソッド（クラスの中の関数）
4. [[pyxel-class]]：Pyxelをクラスで書く
5. [[class-catch]]：ほしキャッチを、クラスで書きかえて見比べる
6. [[class-many]]：クラスで、たくさん動かす

@@ class
title: クラスとインスタンス
type: 構文
chapter: 8
syntax: class 名前:
summary: クラスは「設計図」、インスタンスは設計図から作った「実物」です。1つのクラスから、インスタンスをいくつでも作れます。
aliases: クラス, インスタンス, オブジェクト, 設計図, class
reads: class=クラス | instance=インスタンス | object=オブジェクト
--
::: scratch
Scratchの「クローン」を思い出そう。ネコのスプライトで「自分自身のクローンを作る」を使うと、同じ見た目・同じスクリプトのネコが何匹も出てきて、1匹ずつ、自分のx座標で動きましたね。**クラスはスプライト（もと）**、**インスタンスはクローン（作ったもの）**です。
:::

## ひとことで
| 言葉 | たとえ | Pythonでは |
| --- | --- | --- |
| **クラス** | たい焼きの**型**（設計図） | `class Hiyoko:` |
| **インスタンス** | 型で焼いた**たい焼き**（実物） | `a = Hiyoko("ピヨ太")` |

型が1つあれば、たい焼きはいくつでも焼けます。焼いたたい焼きは1つ1つ別のもので、片方を食べても、もう片方はなくなりません。

## 書き方のかたち
::: tpl クラスの作り方と使い方
class 〔クラス名〕:
····def __init__(self):
········〔最初の準備〕

〔変数〕 = 〔クラス名〕()

| 〔クラス名〕 | 自分で決める名前。**大文字で始める**（Hiyoko、App など） |
| 〔最初の準備〕 | 実物を作ったときに、1回だけ動く（[[init-self]]） |
| 〔変数〕 | 作った実物を入れておく名前 |
:::

## ひよこのクラスを作る
```python
class Hiyoko:
    def __init__(self, namae):
        self.namae = namae
        self.genki = 3

    def naku(self):
        print(f"{self.namae}：ピヨ！")


a = Hiyoko("ピヨ太")
b = Hiyoko("ピヨ子")
a.naku()
b.naku()
```
1. `class Hiyoko:` で、ひよこの**設計図**を作る
2. `Hiyoko("ピヨ太")` で、設計図からひよこを1羽作って、`a` に入れる
3. 同じ設計図から、もう1羽作って `b` に入れる
4. `a.naku()` で、`a` のひよこに鳴いてもらう

## 1羽ずつ、別々の値を持つ
```python
class Hiyoko:
    def __init__(self, namae):
        self.namae = namae
        self.genki = 3


a = Hiyoko("ピヨ太")
b = Hiyoko("ピヨ子")
a.genki = a.genki - 1
print(a.genki, b.genki)
```
`a` の元気を1減らしても、`b` の元気は `3` のままです。クローンが1匹ずつ自分のx座標を持っていたように、1羽ずつ**自分の変数**を持っています。

## Pyxelの sounds も、クラスでできている
7章で使った `pyxel.sounds[0]` も、じつは `Sound` という**クラスから作られた実物**です。Pyxelを作った人が、設計図を用意してくれていたのです。この章では、その設計図を、**自分でも書けるように**なります。

::: deep オブジェクト、オブジェクト指向ってなに？
作った実物（インスタンス）のことを、**オブジェクト**とも呼びます。「データと命令を、1つのモノ（オブジェクト）にまとめて、モノを中心にプログラムを考える」作り方を、**オブジェクト指向**といいます。

Pyxelの `sounds` も、自分で作る `Hiyoko` も、この作り方でできています。ちがうのは、設計図を書いたのが「Pyxelを作った人」か「自分」か、だけです。
:::

@@ init-self
title: __init__ と self
type: 構文
chapter: 8
syntax: def __init__(self): / self.x = 0
summary: __init__ は、インスタンスを作ったときに1回だけ動く準備のメソッドです。self は「このインスタンス自身」のことで、self.x は「自分の x」という意味です。
aliases: イニット, コンストラクタ, セルフ, self, __init__, インスタンス変数, クラス変数
reads: __init__=イニット | self=セルフ | constructor=コンストラクタ
--
## __init__：最初の準備
`__init__`（イニット）は、`Hiyoko()` のようにインスタンスを作った瞬間に、**自動で1回だけ**動くメソッドです。名前の前後に `_` が2つずつつきます。

```python
class Hiyoko:
    def __init__(self):
        print("ひよこが生まれた！")
        self.genki = 3


a = Hiyoko()
b = Hiyoko()
```
2回インスタンスを作ったので、`__init__` も2回動いています。最初の位置や元気など、**はじめに決めておく値**を、ここで用意します。`__init__` のことを、**コンストラクタ**と呼ぶこともあります。

## self：「自分」のこと
`self`（セルフ）は、英語で「自分」という意味です。クラスの中では、`self` が**今動いているインスタンス自身**を指します。

| 書き方 | 意味 |
| --- | --- |
| `self.genki = 3` | 自分の `genki` に 3 を入れる |
| `self.genki - 1` | 自分の `genki` から 1 を引く |
| `self.naku()` | 自分の `naku` メソッドを呼ぶ |

`a.naku()` と呼ぶと `self` は `a` に、`b.naku()` と呼ぶと `self` は `b` になります。だから、同じ設計図でも、1羽ずつ自分の値を使えます。

::: point
クラスの中の関数（メソッド）は、最初の引数に必ず `self` を書きます。呼び出すときは、`self` の分は書きません（`a.naku()` のように、かっこの中は空でOK）。
:::

::: stuck
`self.` をつけ忘れると、ただの「その関数の中だけの変数」になってしまい、ほかのメソッドから使えません。

```python error
class Hiyoko:
    def __init__(self):
        genki = 3

    def miru(self):
        print(self.genki)


a = Hiyoko()
a.miru()
```
`genki = 3` ではなく、`self.genki = 3` と書きます。
:::

::: deep インスタンス変数とクラス変数
`self.genki` のように、インスタンスごとに別々に持つ変数を**インスタンス変数**といいます。反対に、クラスの中にそのまま書いた変数は、**全部のインスタンスで共通**の**クラス変数**になります。

```python
class Hiyoko:
    kazu = 0

    def __init__(self):
        Hiyoko.kazu = Hiyoko.kazu + 1


a = Hiyoko()
b = Hiyoko()
c = Hiyoko()
print(Hiyoko.kazu)
```
`kazu` は、ひよこ全員で1つだけ共有している変数です。ひよこが生まれるたびに1増えるので、何羽生まれたかが分かります。
:::


@@ method
title: メソッド
type: 構文
chapter: 8
syntax: def 名前(self): / インスタンス.名前()
summary: クラスの中に作った関数を、メソッドといいます。インスタンス.メソッド名() で呼び出すと、そのインスタンスが動きます。
aliases: メソッド, method, クラスの関数
reads: method=メソッド | self=セルフ
--
## クラスの中の関数
クラスの中に `def` で作った関数を、**メソッド**といいます。そのクラスのインスタンスができること（動き）を書きます。

```python
class Hiyoko:
    def __init__(self, namae):
        self.namae = namae
        self.genki = 3

    def taberu(self):
        self.genki = self.genki + 1
        print(f"{self.namae} はごはんを食べた。元気 {self.genki}")

    def hashiru(self, kyori):
        self.genki = self.genki - 1
        print(f"{self.namae} は {kyori}m 走った。元気 {self.genki}")


a = Hiyoko("ピヨ太")
a.taberu()
a.hashiru(50)
a.hashiru(30)
```
| 書き方 | 意味 |
| --- | --- |
| `def taberu(self):` | `taberu` というメソッドを作る |
| `a.taberu()` | `a` のひよこに、`taberu` をしてもらう |
| `a.hashiru(50)` | `kyori` に 50 をわたして、`hashiru` をしてもらう |

引数や `return` の使い方は、ふつうの関数と同じです（[[function]]・[[argument]]・[[return]]）。ちがうのは、最初の引数が `self` で、自分の変数を `self.〇〇` で使えるところです。

## じつはもう使っている
メソッドは、ここまでにも何度も使ってきました。

| 使ってきた書き方 | だれの、どのメソッド？ |
| --- | --- |
| `kudamono_list.append("ぶどう")` | リストの `append` メソッド |
| `kudamono_list.sort()` | リストの `sort` メソッド |
| `pyxel.images[0].load(0, 0, "a.png")` | イメージバンクの `load` メソッド |

`〇〇.△△()` という形は、「〇〇 の △△ メソッドを呼ぶ」という意味だったのです。

::: scratch
Scratchで、スプライトごとにスクリプトを作りましたね。メソッドは、そのスプライト（クラス）専用のスクリプトです。ネコのスプライトには「ネコの動き」、イヌのスプライトには「イヌの動き」を書いたように、クラスごとにメソッドを書きます。
:::

@@ pyxel-class
title: Pyxelをクラスで書こう
type: 作品
chapter: 8
syntax: class App: / pyxel.run(self.update, self.draw)
summary: Pyxelのプログラムを、App というクラスの形で書きます。変数は self にまとめるので、global がいらなくなります。
aliases: App, クラスで書く, class App, Pyxelのクラス
reads: App=アップ | self=セルフ | __init__=イニット
--
## 7章の形と、クラスの形
7章の最初の「動く円」を、クラスの形で書きかえてみます。

```python px gif frames=60
import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="クラスで書く")
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 2) % 160

    def draw(self):
        pyxel.cls(1)
        pyxel.circ(self.x, 60, 10, 10)


App()
```

## どこが変わった？
| 7章の書き方 | クラスの書き方 |
| --- | --- |
| `pyxel.init(…)` をいちばん上に書く | `__init__` の中に書く |
| `x = 0` | `__init__` の中に `self.x = 0` |
| `def update():` | `def update(self):` |
| `global x` | **いらない** |
| `x = x + 2` | `self.x = self.x + 2` |
| `pyxel.run(update, draw)` | `pyxel.run(self.update, self.draw)` を `__init__` の最後に |
| （なし） | いちばん最後に `App()` |

最後の `App()` で、App のインスタンスが作られて `__init__` が動きます。`__init__` の中で `pyxel.run` が呼ばれて、ゲームが始まります。

::: point
`global` がいらなくなるのが、クラスで書くいちばんのうれしいところです。`self.x` は「このゲーム（App）の x」なので、`update` でも `draw` でも、そのまま使えます。
:::

::: stuck
- `def update(self):` の `self` を書き忘れると、エラーになります
- `pyxel.run(self.update, self.draw)` の `self.` を書き忘れると、`update` が見つからずにエラーになります
- 最後の `App()` を書き忘れると、何も起きません（設計図を作っただけで、実物を作っていないからです）
:::

@@ class-catch
title: ほしキャッチをクラスで書こう
type: 作品
chapter: 8
syntax: class Hoshi: / class App:
summary: 7章のほしキャッチを、クラスの書き方で作りなおします。ほしを Hoshi クラスにまとめて、クラスなし版と見比べます。
aliases: ほしキャッチ, 見比べる, クラス版, Hoshi
reads: Hoshi=ホシ | App=アップ | ugoku=ウゴク | kaku=カク
--
## クラスなし版をふり返る
[[game-catch]]のほしキャッチでは、こんな変数を使っていました。

| 何の？ | 変数 |
| --- | --- |
| バー | `bar_x` |
| ほし | `hoshi_x`、`hoshi_y` |
| ゲーム全体 | `score`、`miss` |

「ほし」に関係するのは `hoshi_x` と `hoshi_y` の2つと、`update` の中の「ほしを落とす」「上に戻す」の部分です。これを、**ほしのクラス**にまとめてみます。

## クラス版
```python px hold=KEY_RIGHT frames=90 gif
import pyxel


class Hoshi:
    def __init__(self):
        self.modoru()

    def modoru(self):
        self.x = pyxel.rndi(8, 150)
        self.y = 0

    def ugoku(self):
        self.y = self.y + 2

    def kaku(self):
        pyxel.circ(self.x, self.y, 4, 10)


class App:
    def __init__(self):
        pyxel.init(160, 120, title="ほしキャッチ（クラス版）")
        self.bar_x = 70
        self.hoshi = Hoshi()
        self.score = 0
        self.miss = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.bar_x = max(0, self.bar_x - 3)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.bar_x = min(144, self.bar_x + 3)
        self.hoshi.ugoku()
        if self.hoshi.y > 104 and self.bar_x - 4 <= self.hoshi.x <= self.bar_x + 20:
            self.score = self.score + 1
            self.hoshi.modoru()
        elif self.hoshi.y > 120:
            self.miss = self.miss + 1
            self.hoshi.modoru()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.bar_x, 110, 16, 6, 11)
        self.hoshi.kaku()
        pyxel.text(4, 4, f"SCORE {self.score}", 7)
        pyxel.text(100, 4, f"MISS {self.miss}", 8)


App()
```
動きは、7章のほしキャッチとまったく同じです。

## 見比べてみよう
| | クラスなし版 | クラス版 |
| --- | --- | --- |
| ほしの位置 | `hoshi_x`、`hoshi_y` | `self.hoshi.x`、`self.hoshi.y` |
| ほしを落とす | `hoshi_y = hoshi_y + 2` | `self.hoshi.ugoku()` |
| 上に戻す | 2行（同じことを2か所に書く） | `self.hoshi.modoru()` の1行 |
| ほしを描く | `draw` に `pyxel.circ(…)` | `self.hoshi.kaku()` |
| `global` | 5つ並べる | いらない |

クラス版は、行の数は少し増えました。でも、`App` の `update` を読むと、「ほしが動く」「受け止めたら、ほしが戻る」と、**何をしているかが日本語のように読めます**。ほしの細かい動きは、`Hoshi` クラスの中を見れば分かります。

::: point
クラスを作るコツは、「**〇〇の変数**」と「**〇〇がすること**」をセットにすることです。ほしなら、位置（`x`、`y`）と、動く・戻る・描く。敵を足したくなったら、`Teki` クラスを作ります。
:::

::: deep `__init__` の中で modoru を呼んでいる理由
`Hoshi` の `__init__` は、`self.modoru()` を呼ぶだけです。最初の位置を決める処理と、上に戻すときの処理は同じなので、`modoru` メソッド1つにまとめています。同じことを2回書かずにすむのも、メソッドの良いところです。
:::

@@ class-many
title: クラスでたくさん動かそう
type: 作品
chapter: 8
syntax: self.yuki_list.append(Yuki())
summary: 雪や敵のように、たくさんのものを動かすときは、クラスのインスタンスをリストに入れて、for でまとめて動かします。Scratchのクローンと同じ考え方です。
aliases: クローン, たくさん, インスタンスのリスト, 雪, 敵を増やす
reads: Yuki=ユキ | append=アペンド | yuki_list=ユキリスト
--
## リスト2本から、インスタンスのリストへ
[[game-list]]では、雪の位置を `x_list` と `y_list` の**2本のリスト**に分けて覚えていました。クラスを使うと、**1本のリスト**に、雪のインスタンスをそのまま入れられます。

| | リスト版（7章） | クラス版（この章） |
| --- | --- | --- |
| 覚え方 | `x_list[i]` と `y_list[i]` | `yuki.x` と `yuki.y` |
| リストの数 | 2本（速さもあれば3本） | 1本 |
| くり返し | `for i in range(30):` | `for yuki in self.yuki_list:` |

## 雪をふらせる（クラス版）
```python px gif frames=60
import pyxel


class Yuki:
    def __init__(self):
        self.x = pyxel.rndi(0, 159)
        self.y = pyxel.rndi(0, 119)
        self.hayasa = pyxel.rndi(1, 2)

    def ugoku(self):
        self.y = self.y + self.hayasa
        if self.y > 120:
            self.y = 0
            self.x = pyxel.rndi(0, 159)

    def kaku(self):
        pyxel.pset(self.x, self.y, 7)


class App:
    def __init__(self):
        pyxel.init(160, 120, title="雪（クラス版）")
        self.yuki_list = []
        for i in range(40):
            self.yuki_list.append(Yuki())
        pyxel.run(self.update, self.draw)

    def update(self):
        for yuki in self.yuki_list:
            yuki.ugoku()

    def draw(self):
        pyxel.cls(1)
        for yuki in self.yuki_list:
            yuki.kaku()


App()
```

## 仕組みを読み解く
1. `Yuki` クラスに、雪1つぶんの「位置・速さ」と「動く・描く」をまとめる
2. `App` の `__init__` で、`Yuki()` を40回作って、`self.yuki_list` に足していく
3. `update` では、リストの雪を1つずつ取り出して `yuki.ugoku()`、`draw` では `yuki.kaku()`

`for yuki in self.yuki_list:` の `yuki` には、雪のインスタンスが1つずつ入ります。番号 `i` を使わなくても、全部の雪を動かせます。

::: scratch
Scratchで「自分自身のクローンを作る」を40回くり返して、クローンが「クローンされたとき」のスクリプトでそれぞれ動く。それと同じことを、Pythonでは `Yuki()` を40回作って、リストに入れてやっています。
:::

::: point
速さを足すのも簡単です。リスト版では `hayasa_list` という3本目のリストが必要でしたが、クラス版では `__init__` に `self.hayasa` を1行足すだけです。
:::
