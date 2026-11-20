@@ task:ch8
::: t
`Inu`（イヌ）というクラスを作ろう。インスタンスを作るときに名前を受け取って、`hoeru` メソッドを呼ぶと「〇〇：ワン！」と表示されるようにします。「ポチ」で試そう。
```output
ポチ：ワン！
```
:::
::: s
```python
class Inu:
    def __init__(self, namae):
        self.namae = namae

    def hoeru(self):
        print(f"{self.namae}：ワン！")


a = Inu("ポチ")
a.hoeru()
```
:::

::: t
7章の「うごく四角」（右に動いていく黄色い四角）を、クラスの形で書きかえよう。
:::
::: s
```python px gif frames=40
import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="うごく四角")
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = self.x + 3

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 50, 20, 20, 10)


App()
```
:::

::: t
クラスで書いた Pyxel のプログラムで、スペースキーを押すたびに `self.count` が1増えて、画面に表示されるようにしよう。
:::
::: s
```python px press=KEY_SPACE@3 frames=10
import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="カウンター")
        self.count = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.count = self.count + 1

    def draw(self):
        pyxel.cls(1)
        pyxel.text(60, 56, f"COUNT {self.count}", 7)


App()
```
:::

@@ task:class
::: t
`Hiyoko` クラスから、「ピヨ太」「ピヨ子」「ピヨ助」の3羽を作って、3羽の名前を表示しよう。
```output
ピヨ太
ピヨ子
ピヨ助
```
:::
::: s
```python
class Hiyoko:
    def __init__(self, namae):
        self.namae = namae


a = Hiyoko("ピヨ太")
b = Hiyoko("ピヨ子")
c = Hiyoko("ピヨ助")
print(a.namae)
print(b.namae)
print(c.namae)
```
:::

::: t
`Hiyoko` クラスに、`self.nenrei = 0`（年齢）を足そう。`a` だけ年齢を1にして、`a` と `b` の年齢を並べて表示しよう。
```output
1 0
```
:::
::: s
```python
class Hiyoko:
    def __init__(self, namae):
        self.namae = namae
        self.nenrei = 0


a = Hiyoko("ピヨ太")
b = Hiyoko("ピヨ子")
a.nenrei = a.nenrei + 1
print(a.nenrei, b.nenrei)
```
`a` と `b` は別々のインスタンスなので、`a` の年齢を変えても、`b` は変わりません。
:::

::: t
`Kuruma`（車）クラスを作ろう。名前と速さ（`hayasa`）を受け取って、「〇〇 は時速 △ km」と表示する `setsumei` メソッドを作ります。
```output
赤い車 は時速 60 km
```
:::
::: s
```python
class Kuruma:
    def __init__(self, namae, hayasa):
        self.namae = namae
        self.hayasa = hayasa

    def setsumei(self):
        print(f"{self.namae} は時速 {self.hayasa} km")


k = Kuruma("赤い車", 60)
k.setsumei()
```
:::

@@ task:init-self
::: t
インスタンスを作るたびに「生まれた！」と表示される `Hiyoko` クラスを作って、2羽作ろう。
```output
生まれた！
生まれた！
```
:::
::: s
```python
class Hiyoko:
    def __init__(self):
        print("生まれた！")


a = Hiyoko()
b = Hiyoko()
```
:::

::: t
次のプログラムはエラーになります。正しく直して、`3` と表示されるようにしよう。
```python norun
class Hiyoko:
    def __init__(self):
        genki = 3

    def miru(self):
        print(self.genki)


a = Hiyoko()
a.miru()
```
```output
3
```
:::
::: s
```python
class Hiyoko:
    def __init__(self):
        self.genki = 3

    def miru(self):
        print(self.genki)


a = Hiyoko()
a.miru()
```
`genki` に `self.` をつけると、ほかのメソッドからも使える「自分の変数」になります。
:::

::: t
クラス変数 `kazu` を使って、作ったインスタンスの数を数えよう。`Hiyoko` を4羽作って、`4` と表示します。
```output
4
```
:::
::: s
```python
class Hiyoko:
    kazu = 0

    def __init__(self):
        Hiyoko.kazu = Hiyoko.kazu + 1


for i in range(4):
    Hiyoko()
print(Hiyoko.kazu)
```
:::

@@ task:method
::: t
`Hiyoko` クラスに、`genki` を1増やす `taberu` メソッドを作ろう。3回食べさせて、元気を表示します（はじめの元気は3）。
```output
6
```
:::
::: s
```python
class Hiyoko:
    def __init__(self):
        self.genki = 3

    def taberu(self):
        self.genki = self.genki + 1


a = Hiyoko()
for i in range(3):
    a.taberu()
print(a.genki)
```
:::

::: t
`Ginkou`（銀行）クラスを作ろう。はじめの残高 `zandaka` は0。`azukeru(kingaku)` でお金を足し、`hikidasu(kingaku)` でお金を引きます。1000円あずけて、300円引き出したあとの残高を表示しよう。
```output
700
```
:::
::: s
```python
class Ginkou:
    def __init__(self):
        self.zandaka = 0

    def azukeru(self, kingaku):
        self.zandaka = self.zandaka + kingaku

    def hikidasu(self, kingaku):
        self.zandaka = self.zandaka - kingaku


g = Ginkou()
g.azukeru(1000)
g.hikidasu(300)
print(g.zandaka)
```
:::

::: t
`Shikaku`（四角）クラスに、面積を `return` で返す `menseki` メソッドを作ろう。幅5、高さ3で試します。
```output
15
```
:::
::: s
```python
class Shikaku:
    def __init__(self, haba, takasa):
        self.haba = haba
        self.takasa = takasa

    def menseki(self):
        return self.haba * self.takasa


s = Shikaku(5, 3)
print(s.menseki())
```
:::

@@ task:pyxel-class
::: t
クラスの形で、幅200・高さ100のウィンドウを出して、「HELLO CLASS」と表示しよう。
:::
::: s
```python px
import pyxel


class App:
    def __init__(self):
        pyxel.init(200, 100, title="HELLO")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.text(76, 45, "HELLO CLASS", 7)


App()
```
:::

::: t
矢印キーで上下左右に動く四角を、クラスの形で作ろう。
:::
::: s
```python px hold=KEY_UP frames=30
import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="キーで動かす")
        self.x = 76
        self.y = 56
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = self.x - 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = self.x + 2
        if pyxel.btn(pyxel.KEY_UP):
            self.y = self.y - 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y = self.y + 2

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 8, 8, 10)


App()
```
:::

::: t
画面の左右のはしで跳ね返る円を、クラスの形で作ろう。位置 `self.x` と、1回で動く量 `self.dx` を使います。
:::
::: s
```python px gif frames=90
import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="跳ね返る円")
        self.x = 20
        self.dx = 3
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = self.x + self.dx
        if self.x > 150 or self.x < 10:
            self.dx = -self.dx

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.x, 60, 10, 8)


App()
```
7章の「跳ね返る円」とくらべると、`global x, dx` がなくなっています。
:::

@@ task:class-catch
::: t
クラス版のほしキャッチで、ほしの落ちる速さを `Hoshi` の `self.hayasa` にして、`3` にしよう。（`ugoku` の中で使います）
:::
::: s
```python px hold=KEY_RIGHT frames=60
import pyxel


class Hoshi:
    def __init__(self):
        self.hayasa = 3
        self.modoru()

    def modoru(self):
        self.x = pyxel.rndi(8, 150)
        self.y = 0

    def ugoku(self):
        self.y = self.y + self.hayasa

    def kaku(self):
        pyxel.circ(self.x, self.y, 4, 10)


class App:
    def __init__(self):
        pyxel.init(160, 120, title="ほしキャッチ")
        self.bar_x = 70
        self.hoshi = Hoshi()
        self.score = 0
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
            self.hoshi.modoru()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.bar_x, 110, 16, 6, 11)
        self.hoshi.kaku()
        pyxel.text(4, 4, f"SCORE {self.score}", 7)


App()
```
:::

::: t
バーも `Bar` クラスにまとめよう。`Bar` には、位置 `self.x`、キーで動く `ugoku` メソッド、描く `kaku` メソッドを作ります。
:::
::: s
```python px hold=KEY_RIGHT frames=30
import pyxel


class Bar:
    def __init__(self):
        self.x = 70

    def ugoku(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = max(0, self.x - 3)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = min(144, self.x + 3)

    def kaku(self):
        pyxel.rect(self.x, 110, 16, 6, 11)


class App:
    def __init__(self):
        pyxel.init(160, 120, title="バーのクラス")
        self.bar = Bar()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.bar.ugoku()

    def draw(self):
        pyxel.cls(0)
        self.bar.kaku()


App()
```
App の `update` と `draw` が、それぞれ1行になりました。バーの細かい動きは、`Bar` クラスを見れば分かります。
:::

::: t
ミスが3回になったら「GAME OVER」と表示して止まるようにしよう。`App` に `self.miss` を足します。
:::
::: s
```python px hold=KEY_RIGHT frames=240
import pyxel


class Hoshi:
    def __init__(self):
        self.modoru()

    def modoru(self):
        self.x = pyxel.rndi(8, 150)
        self.y = 0

    def ugoku(self):
        self.y = self.y + 4

    def kaku(self):
        pyxel.circ(self.x, self.y, 4, 10)


class App:
    def __init__(self):
        pyxel.init(160, 120, title="ほしキャッチ")
        self.bar_x = 70
        self.hoshi = Hoshi()
        self.miss = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.miss >= 3:
            return
        if pyxel.btn(pyxel.KEY_LEFT):
            self.bar_x = max(0, self.bar_x - 3)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.bar_x = min(144, self.bar_x + 3)
        self.hoshi.ugoku()
        if self.hoshi.y > 104 and self.bar_x - 4 <= self.hoshi.x <= self.bar_x + 20:
            self.hoshi.modoru()
        elif self.hoshi.y > 120:
            self.miss = self.miss + 1
            self.hoshi.modoru()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.bar_x, 110, 16, 6, 11)
        self.hoshi.kaku()
        pyxel.text(100, 4, f"MISS {self.miss}", 8)
        if self.miss >= 3:
            pyxel.text(58, 56, "GAME OVER", 8)


App()
```
:::

@@ task:class-many
::: t
雪の数を、40個から80個に増やそう。
:::
::: s
```python px frames=30
import pyxel


class Yuki:
    def __init__(self):
        self.x = pyxel.rndi(0, 159)
        self.y = pyxel.rndi(0, 119)

    def ugoku(self):
        self.y = self.y + 1
        if self.y > 120:
            self.y = 0

    def kaku(self):
        pyxel.pset(self.x, self.y, 7)


class App:
    def __init__(self):
        pyxel.init(160, 120, title="80この雪")
        self.yuki_list = []
        for i in range(80):
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
`range(40)` を `range(80)` にするだけです。
:::

::: t
雪の色を、1つぶずつランダムにしよう。`Yuki` の `__init__` に `self.iro` を足して、7（白）か12（水色）のどちらかにします。
:::
::: s
```python px frames=30
import pyxel


class Yuki:
    def __init__(self):
        self.x = pyxel.rndi(0, 159)
        self.y = pyxel.rndi(0, 119)
        if pyxel.rndi(0, 1) == 0:
            self.iro = 7
        else:
            self.iro = 12

    def ugoku(self):
        self.y = self.y + 1
        if self.y > 120:
            self.y = 0

    def kaku(self):
        pyxel.pset(self.x, self.y, self.iro)


class App:
    def __init__(self):
        pyxel.init(160, 120, title="色ちがいの雪")
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
リスト版だと `iro_list` という新しいリストが必要ですが、クラス版なら `Yuki` の中に `self.iro` を足すだけです。
:::

::: t
スペースキーを押すたびに、画面のどこかに円が1つずつ増えるプログラムを作ろう。円は `Maru` クラスで作ります。
:::
::: s
```python px press=KEY_SPACE@3 frames=10
import pyxel


class Maru:
    def __init__(self):
        self.x = pyxel.rndi(10, 150)
        self.y = pyxel.rndi(10, 110)

    def kaku(self):
        pyxel.circ(self.x, self.y, 6, 10)


class App:
    def __init__(self):
        pyxel.init(160, 120, title="ふえる円")
        self.maru_list = [Maru()]
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.maru_list.append(Maru())

    def draw(self):
        pyxel.cls(0)
        for maru in self.maru_list:
            maru.kaku()
        pyxel.text(4, 4, f"MARU {len(self.maru_list)}", 7)


App()
```
Scratchで、スペースキーを押すたびに「クローンを作る」のと同じです。
:::
