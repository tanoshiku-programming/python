@@ task:ch7
::: t
幅200、高さ100のウィンドウを出して、画面に「HELLO」と書いてみよう。
:::
::: s
```python px
import pyxel

pyxel.init(200, 100, title="HELLO")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(80, 45, "HELLO", 7)


pyxel.run(update, draw)
```
:::

::: t
画面を赤（8番）で塗りつぶして、真ん中に白い文字で「RED」と書いてみよう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="RED")


def update():
    pass


def draw():
    pyxel.cls(8)
    pyxel.text(70, 57, "RED", 7)


pyxel.run(update, draw)
```
:::

::: t
黄色い四角が、右に動いていくプログラムを作ってみよう。（`x` を `update` で増やす）
:::
::: s
```python px gif frames=40
import pyxel

pyxel.init(160, 120, title="うごく四角")
x = 0


def update():
    global x
    x = x + 3


def draw():
    pyxel.cls(0)
    pyxel.rect(x, 50, 20, 20, 10)


pyxel.run(update, draw)
```
:::

::: c
「10秒ぴったりゲーム」を作ろう。スペースキーでスタートして、もう一度押してストップ。10秒からどれだけずれたかを表示します。時計は表示しないで、心の中で数えるのがポイントです。（ヒント：[[app-timer]] と [[game-scene]] を組み合わせる）
:::
::: s
```python px frames=10
import pyxel

pyxel.init(160, 120, title="10秒ぴったり")
gamen = "title"
frame_kazu = 0


def update():
    global gamen, frame_kazu
    if gamen == "title":
        if pyxel.btnp(pyxel.KEY_SPACE):
            gamen = "game"
            frame_kazu = 0
    elif gamen == "game":
        frame_kazu = frame_kazu + 1
        if pyxel.btnp(pyxel.KEY_SPACE):
            gamen = "kekka"
    elif gamen == "kekka":
        if pyxel.btnp(pyxel.KEY_R):
            gamen = "title"


def draw():
    pyxel.cls(0)
    if gamen == "title":
        pyxel.text(36, 50, "STOP AT 10 SECONDS", 10)
        pyxel.text(48, 70, "PUSH SPACE KEY", 7)
    elif gamen == "game":
        pyxel.text(40, 55, "COUNT IN YOUR HEAD", 7)
    elif gamen == "kekka":
        zure = frame_kazu - 300
        if zure < 0:
            zure = -zure
        pyxel.text(40, 45, f"YOUR TIME {frame_kazu / 30:.2f}", 10)
        pyxel.text(40, 60, f"ZURE {zure / 30:.2f}", 11)
        pyxel.text(40, 80, "R: TITLE", 7)


pyxel.run(update, draw)
```
10秒は300フレームです。`zure` がマイナスのときは `-zure` でプラスに直して、「どれだけずれたか」だけを表示しています。`:.2f` は小数第2位まで表示する書き方です（[[fstring]]）。
:::

@@ task:pyxel
::: t
`pip install pyxel` で、Pyxelをインストールしよう。インストールできたら、`import pyxel` と書いたプログラムを実行して、エラーが出ないことを確かめよう。
:::
::: s
```python norun
import pyxel

print("Pyxelの準備OK！")
```
```output
Pyxelの準備OK！
```
エラーが出なければ成功です（`pip install pyxel` は、ターミナルで実行します）。
:::

::: t
画面の左上に、白い文字で「PYXEL」と書くプログラムを作ってみよう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="PYXEL")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(4, 4, "PYXEL", 7)


pyxel.run(update, draw)
```
:::

::: t
画面の色をいろいろ変えて試そう。`pyxel.cls(…)` の数を0から15まで変えて、どんな色か見てみよう。気に入った色で「MY COLOR」と書いてみよう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="MY COLOR")


def update():
    pass


def draw():
    pyxel.cls(12)
    pyxel.text(60, 57, "MY COLOR", 0)


pyxel.run(update, draw)
```
:::

@@ task:window
::: t
幅 100、高さ 100 の正方形のウィンドウを作ろう。タイトルは「SQUARE」にしよう。
:::
::: s
```python px
import pyxel

pyxel.init(100, 100, title="SQUARE")


def update():
    pass


def draw():
    pyxel.cls(1)
    pyxel.text(30, 47, "SQUARE", 7)


pyxel.run(update, draw)
```
:::

::: t
幅 240、高さ 80 の横長のウィンドウを作って、画面の左上に「WIDE」と書こう。
:::
::: s
```python px
import pyxel

pyxel.init(240, 80, title="WIDE")


def update():
    pass


def draw():
    pyxel.cls(3)
    pyxel.text(4, 4, "WIDE", 7)


pyxel.run(update, draw)
```
:::

::: t
`pyxel.run(update(), draw())` と書いて実行して、エラーを見てみよう。そのあと、直してふつうに動くようにしよう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="なおした")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(50, 55, "FIXED!", 10)


pyxel.run(update, draw)
```
`run` には、`()` をつけずに、関数の名前だけを書きます。
:::

@@ task:update-draw
::: t
`draw` の中で画面を青（1番）で塗りつぶして、「DRAW」と書いてみよう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="DRAW")


def update():
    pass


def draw():
    pyxel.cls(1)
    pyxel.text(65, 57, "DRAW", 7)


pyxel.run(update, draw)
```
:::

::: t
変数 `count` を `update` で1ずつ増やして、`draw` で `str(count)` を画面に表示しよう。数がどんどん増えていけばOKです。
:::
::: s
```python px gif frames=60
import pyxel

pyxel.init(160, 120, title="カウント")
count = 0


def update():
    global count
    count = count + 1


def draw():
    pyxel.cls(0)
    pyxel.text(70, 57, str(count), 7)


pyxel.run(update, draw)
```
:::

::: t
赤い円が、下に向かって動いていくプログラムを作ろう。（`y` を増やす）
:::
::: s
```python px gif frames=60
import pyxel

pyxel.init(160, 120, title="おちる円")
y = 0


def update():
    global y
    y = y + 2


def draw():
    pyxel.cls(0)
    pyxel.circ(80, y, 8, 8)


pyxel.run(update, draw)
```
:::

@@ task:coordinate
::: t
画面の4つのすみ（左上・右上・左下・右下）に、それぞれ点を打とう。画面は 160 × 120 だよ。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="4つのすみ")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.pset(0, 0, 8)
    pyxel.pset(159, 0, 10)
    pyxel.pset(0, 119, 11)
    pyxel.pset(159, 119, 12)


pyxel.run(update, draw)
```
:::

::: t
画面の真ん中 `(80, 60)` に、白い文字で「CENTER」と書こう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="CENTER")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(66, 57, "CENTER", 7)


pyxel.run(update, draw)
```
文字の左上が `(x, y)` なので、少し左にずらすと真ん中に見えます。
:::

::: t
画面の左から10ドット、上から20ドットの場所に、幅40・高さ30の黄色い四角を描こう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="四角")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rect(10, 20, 40, 30, 10)


pyxel.run(update, draw)
```
:::

@@ task:color
::: t
高さ10の太い横線を3本、赤・黄・緑の順に並べて描こう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="3色")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rect(0, 20, 160, 10, 8)
    pyxel.rect(0, 40, 160, 10, 10)
    pyxel.rect(0, 60, 160, 10, 11)


pyxel.run(update, draw)
```
:::

::: t
色の名前（`pyxel.COLOR_PINK` など）を使って、画面をピンクで塗りつぶそう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="PINK")


def update():
    pass


def draw():
    pyxel.cls(pyxel.COLOR_PINK)
    pyxel.text(70, 57, "PINK", pyxel.COLOR_WHITE)


pyxel.run(update, draw)
```
:::

::: t
`for` を使って、0〜15 の16色の細い縦線（幅10・高さ120）を横に並べよう。画面の幅は 160 だよ。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="にじ")


def update():
    pass


def draw():
    pyxel.cls(0)
    for i in range(16):
        pyxel.rect(i * 10, 0, 10, 120, i)


pyxel.run(update, draw)
```
:::

@@ task:pyxel-text
::: t
画面に、英語のメッセージを3行書こう。色は赤・黄・緑の3色にしよう（`"GAME"`、`"START"`、`"GO"` など）。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="3行")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(10, 10, "GAME", 8)
    pyxel.text(10, 24, "START", 10)
    pyxel.text(10, 38, "GO", 11)


pyxel.run(update, draw)
```
:::

::: t
変数 `hp = 30` を作って、画面に「HP: 30」と表示しよう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="HP")
hp = 30


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(10, 10, "HP: " + str(hp), 7)


pyxel.run(update, draw)
```
:::

::: t
f文字列を使って、`name = "TARO"` と `score = 100` から「TARO: 100」と表示しよう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="名前と点数")
name = "TARO"
score = 100


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(10, 10, f"{name}: {score}", 7)


pyxel.run(update, draw)
```
:::

@@ task:shapes
::: t
赤い四角と青い円を、横に並べて描こう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="四角と円")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rect(20, 40, 40, 40, 8)
    pyxel.circ(110, 60, 20, 12)


pyxel.run(update, draw)
```
:::

::: t
`rectb` で、画面のふち（いちばん外側）に白い枠を描こう。画面は 160 × 120 だよ。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="枠")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rectb(0, 0, 160, 120, 7)


pyxel.run(update, draw)
```
:::

::: t
図形を重ねて、自分の好きな絵（ロケット、顔、車など）を描いてみよう。四角・円・三角のうち、3種類以上を使おう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="ロケット")


def update():
    pass


def draw():
    pyxel.cls(1)
    pyxel.rect(70, 40, 20, 50, 7)
    pyxel.tri(70, 40, 80, 20, 90, 40, 8)
    pyxel.tri(70, 80, 55, 95, 70, 95, 8)
    pyxel.tri(90, 80, 105, 95, 90, 95, 8)
    pyxel.circ(80, 55, 5, 12)
    pyxel.tri(74, 90, 80, 108, 86, 90, 10)


pyxel.run(update, draw)
```
自由な作品なので、解答例と同じでなくてOKです。
:::

@@ task:pyxel-var
::: t
白い円が、画面の左から右へ動いていくプログラムを作ろう。
:::
::: s
```python px gif frames=60
import pyxel

pyxel.init(160, 120, title="右へ")
x = 0


def update():
    global x
    x = x + 2


def draw():
    pyxel.cls(0)
    pyxel.circ(x, 60, 6, 7)


pyxel.run(update, draw)
```
:::

::: t
変数 `y` を使って、画面の下から上へゆっくり上がっていく四角を作ろう（`y` を減らす）。
:::
::: s
```python px gif frames=60
import pyxel

pyxel.init(160, 120, title="上へ")
y = 120


def update():
    global y
    y = y - 2


def draw():
    pyxel.cls(0)
    pyxel.rect(70, y, 20, 20, 10)


pyxel.run(update, draw)
```
:::

::: t
画面の上と下で跳ね返る円を作ろう。`dy` を使って、速さと向きを変数にしよう。
:::
::: s
```python px gif frames=90
import pyxel

pyxel.init(160, 120, title="上下にはね返る")
y = 20
dy = 3


def update():
    global y, dy
    y = y + dy
    if y > 110 or y < 10:
        dy = -dy


def draw():
    pyxel.cls(0)
    pyxel.circ(80, y, 10, 11)


pyxel.run(update, draw)
```
:::

@@ task:pyxel-key
::: t
左右のキーで、四角が左右に動くプログラムを作ろう。
:::
::: s
```python px gif frames=40 hold=KEY_LEFT
import pyxel

pyxel.init(160, 120, title="左右")
x = 76


def update():
    global x
    if pyxel.btn(pyxel.KEY_LEFT):
        x = x - 2
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 2


def draw():
    pyxel.cls(0)
    pyxel.rect(x, 56, 8, 8, 10)


pyxel.run(update, draw)
```
画像は、左キーを押しつづけたときの様子です。
:::

::: t
上の問題に、「画面の外に出ない」ようにするしくみを足そう。（`max` と `min`）
:::
::: s
```python px gif frames=60 hold=KEY_RIGHT
import pyxel

pyxel.init(160, 120, title="外に出ない")
x = 76


def update():
    global x
    if pyxel.btn(pyxel.KEY_LEFT):
        x = max(0, x - 2)
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = min(152, x + 2)


def draw():
    pyxel.cls(0)
    pyxel.rect(x, 56, 8, 8, 10)


pyxel.run(update, draw)
```
画像は、右キーを押しつづけたときの様子です。右はしで止まります。
:::

::: t
スペースキーを押すたびに、画面の背景色が変わるプログラムを作ろう（`btnp` を使う）。
:::
::: s
```python px press=KEY_SPACE@5 frames=15
import pyxel

pyxel.init(160, 120, title="背景色")
haikei_iro = 0


def update():
    global haikei_iro
    if pyxel.btnp(pyxel.KEY_SPACE):
        haikei_iro = haikei_iro + 1


def draw():
    pyxel.cls(haikei_iro)
    pyxel.text(50, 57, "PUSH SPACE", 7)


pyxel.run(update, draw)
```
:::

@@ task:pyxel-mouse
::: t
マウスの場所に、赤い四角（10 × 10）がついてくるプログラムを作ろう。
:::
::: s
```python px click=60,80
import pyxel

pyxel.init(160, 120, title="ついてくる")
pyxel.mouse(True)


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, 10, 10, 8)


pyxel.run(update, draw)
```
:::

::: t
画面をクリックするたびに `count` が1ずつ増えて、その数が画面に出るプログラムを作ろう。
:::
::: s
```python px click=80,60 frames=20
import pyxel

pyxel.init(160, 120, title="クリックカウンター")
pyxel.mouse(True)
count = 0


def update():
    global count
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        count = count + 1


def draw():
    pyxel.cls(1)
    pyxel.text(60, 57, "CLICK: " + str(count), 7)


pyxel.run(update, draw)
```
:::

::: t
画面の左半分をクリックしたら「LEFT」、右半分をクリックしたら「RIGHT」と表示するプログラムを作ろう（画面の幅は160だよ）。
:::
::: s
```python px click=120,60 frames=20
import pyxel

pyxel.init(160, 120, title="左右判定")
pyxel.mouse(True)
message = ""


def update():
    global message
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        if pyxel.mouse_x < 80:
            message = "LEFT"
        else:
            message = "RIGHT"


def draw():
    pyxel.cls(1)
    pyxel.line(80, 0, 80, 120, 13)
    pyxel.text(70, 57, message, 10)


pyxel.run(update, draw)
```
:::

@@ task:pyxel-jp
::: t
日本語で「こんにちは、Pyxel！」と表示しよう。フォントは `umplus_j12r.bdf` を使おう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="あいさつ")
font = pyxel.Font("umplus_j12r.bdf")


def update():
    pass


def draw():
    pyxel.cls(1)
    pyxel.text(30, 55, "こんにちは、Pyxel！", 7, font)


pyxel.run(update, draw)
```
:::

::: t
自分の名前と好きな食べ物を、日本語で2行に分けて表示しよう。色も行ごとに変えよう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="じこしょうかい")
font = pyxel.Font("umplus_j12r.bdf")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.text(10, 30, "名前：はなこ", 10, font)
    pyxel.text(10, 60, "好きな食べ物：カレー", 11, font)


pyxel.run(update, draw)
```
:::

::: t
`font.text_width` を使って、「ようこそ」を画面の横の真ん中にそろえて表示しよう。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="まん中")
font = pyxel.Font("umplus_j12r.bdf")
message = "ようこそ"
haba = font.text_width(message)


def update():
    pass


def draw():
    pyxel.cls(1)
    pyxel.text((160 - haba) // 2, 55, message, 7, font)


pyxel.run(update, draw)
```
文字の長さ `haba` を引いて2で割ると、真ん中になります。
:::

@@ task:app-fortune
::: t
占いアプリの結果の言葉を、自分の好きな言葉（たとえば「ラッキー」「アンラッキー」など）に変えてみよう。
:::
::: s
```python px click=80,90 frames=20
import pyxel
import random

pyxel.init(160, 120, title="うらない")
pyxel.mouse(True)
font = pyxel.Font("umplus_j12r.bdf")
uranai_list = ["ラッキー", "まあまあ", "ざんねん"]
kekka = ""


def update():
    global kekka
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        if 40 <= pyxel.mouse_x <= 120 and 80 <= pyxel.mouse_y <= 100:
            kekka = random.choice(uranai_list)


def draw():
    pyxel.cls(1)
    pyxel.text(46, 12, "今日のうらない", 7, font)
    pyxel.text(56, 44, kekka, 10, font)
    pyxel.rect(40, 80, 80, 20, 8)
    pyxel.text(52, 85, "ボタンをおす", 7, font)


pyxel.run(update, draw)
```
`random.choice` を使うと、番号なしで選べます。
:::

::: t
結果の種類を1つ増やそう（リストの数が変わるので、`randint` の数にも注意）。
:::
::: s
```python px click=80,90 frames=20
import pyxel
import random

pyxel.init(160, 120, title="うらない")
pyxel.mouse(True)
font = pyxel.Font("umplus_j12r.bdf")
uranai_list = ["大吉", "中吉", "小吉", "吉", "凶"]
kekka = ""


def update():
    global kekka
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        if 40 <= pyxel.mouse_x <= 120 and 80 <= pyxel.mouse_y <= 100:
            n = random.randint(0, len(uranai_list) - 1)
            kekka = uranai_list[n]


def draw():
    pyxel.cls(1)
    pyxel.text(46, 12, "今日のうらない", 7, font)
    pyxel.text(64, 44, kekka, 10, font)
    pyxel.rect(40, 80, 80, 20, 8)
    pyxel.text(52, 85, "ボタンをおす", 7, font)


pyxel.run(update, draw)
```
`len(uranai_list) - 1` を使うと、リストの数を増やしても自動で合います。
:::

::: t
「じゃんけんアプリ」を作ろう。ボタンを押すと、コンピュータの手（グー・チョキ・パー）がランダムで出るようにする。
:::
::: s
```python px click=80,90 frames=20
import pyxel
import random

pyxel.init(160, 120, title="じゃんけん")
pyxel.mouse(True)
font = pyxel.Font("umplus_j12r.bdf")
te_list = ["グー", "チョキ", "パー"]
te = ""


def update():
    global te
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        if 40 <= pyxel.mouse_x <= 120 and 80 <= pyxel.mouse_y <= 100:
            te = random.choice(te_list)


def draw():
    pyxel.cls(3)
    pyxel.text(40, 12, "コンピュータの手は？", 7, font)
    pyxel.text(66, 44, te, 10, font)
    pyxel.rect(40, 80, 80, 20, 8)
    pyxel.text(60, 85, "ぽん！", 7, font)


pyxel.run(update, draw)
```
:::

@@ task:app-timer
::: t
ストップウォッチの秒を、いつも2けたで表示しよう。「0分 5秒」ではなく「0分 05秒」のようにします。（ヒント：f文字列の `{byou % 60:02}` と書くと、2けたにそろいます）
:::
::: s
```python px frames=160 press=KEY_SPACE@3
import pyxel

pyxel.init(160, 120, title="2けたの秒")
font = pyxel.Font("umplus_j12r.bdf")
frame_kazu = 0
ugoiteru = False


def update():
    global frame_kazu, ugoiteru
    if pyxel.btnp(pyxel.KEY_SPACE):
        ugoiteru = not ugoiteru
    if ugoiteru:
        frame_kazu = frame_kazu + 1


def draw():
    pyxel.cls(1)
    byou = frame_kazu // 30
    fun = byou // 60
    pyxel.text(50, 50, f"{fun}分 {byou % 60:02}秒", 10, font)


pyxel.run(update, draw)
```
`:02` は「2けたにして、足りないところは0でうめる」という意味です（[[fstring]]）。
:::

::: t
10秒たったら、自動で止まって「時間です！」と表示される**10秒タイマー**を作ろう。スペースキーでスタートします。
:::
::: s
```python px frames=320 press=KEY_SPACE@3
import pyxel

pyxel.init(160, 120, title="10秒タイマー")
font = pyxel.Font("umplus_j12r.bdf")
frame_kazu = 0
ugoiteru = False


def update():
    global frame_kazu, ugoiteru
    if pyxel.btnp(pyxel.KEY_SPACE):
        ugoiteru = True
    if ugoiteru:
        frame_kazu = frame_kazu + 1
    if frame_kazu >= 300:
        ugoiteru = False


def draw():
    pyxel.cls(1)
    nokori = 10 - frame_kazu // 30
    if frame_kazu >= 300:
        pyxel.text(50, 50, "時間です！", 8, font)
    else:
        pyxel.text(50, 50, f"のこり {nokori}秒", 10, font)


pyxel.run(update, draw)
```
10秒は `10 × 30 = 300` フレームです。`frame_kazu` が300以上になったら、`ugoiteru` を `False` にして止めます。残りの秒数 `nokori` は、「10 − たった秒数」で計算しています。
:::

::: t
ストップウォッチに、**ラップ**（とちゅうの記録）をつけよう。Lキーを押すと、その時の秒数が `lap` という変数に記録されて、画面の下に「ラップ 〇秒」と表示されるようにします。
:::
::: s
```python px frames=100 press=KEY_SPACE@3,KEY_L@70
import pyxel

pyxel.init(160, 120, title="ラップ")
font = pyxel.Font("umplus_j12r.bdf")
frame_kazu = 0
ugoiteru = False
lap = 0


def update():
    global frame_kazu, ugoiteru, lap
    if pyxel.btnp(pyxel.KEY_SPACE):
        ugoiteru = not ugoiteru
    if pyxel.btnp(pyxel.KEY_L):
        lap = frame_kazu // 30
    if ugoiteru:
        frame_kazu = frame_kazu + 1


def draw():
    pyxel.cls(1)
    byou = frame_kazu // 30
    pyxel.text(50, 40, f"{byou}秒", 10, font)
    pyxel.text(50, 80, f"ラップ {lap}秒", 11, font)


pyxel.run(update, draw)
```
`lap` も `update` の中で書き換えるので、`global` に足すのを忘れずに。画像は、スタートしてから2秒あたりでLキーを押したときの画面です。
:::

@@ task:game-catch
::: t
ほしの落ちる速さを変数 `speed` にして、`3` に変えてみよう。ゲームが難しくなるよ。
:::
::: s
```python px hold=KEY_RIGHT frames=60 gif
import pyxel

pyxel.init(160, 120, title="ほしキャッチ")
bar_x = 70
hoshi_x = pyxel.rndi(8, 150)
hoshi_y = 0
score = 0
speed = 3


def update():
    global bar_x, hoshi_x, hoshi_y, score
    if pyxel.btn(pyxel.KEY_LEFT):
        bar_x = max(0, bar_x - 3)
    if pyxel.btn(pyxel.KEY_RIGHT):
        bar_x = min(144, bar_x + 3)
    hoshi_y = hoshi_y + speed
    if hoshi_y > 104 and bar_x - 4 <= hoshi_x <= bar_x + 20:
        score = score + 1
        hoshi_y = 0
        hoshi_x = pyxel.rndi(8, 150)
    elif hoshi_y > 120:
        hoshi_y = 0
        hoshi_x = pyxel.rndi(8, 150)


def draw():
    pyxel.cls(0)
    pyxel.rect(bar_x, 110, 16, 6, 11)
    pyxel.circ(hoshi_x, hoshi_y, 4, 10)
    pyxel.text(4, 4, f"SCORE {score}", 7)


pyxel.run(update, draw)
```
:::

::: t
ミスが3回になったら、画面に「GAME OVER」と出して、ゲームが止まるようにしよう。
:::
::: s
```python px hold=KEY_RIGHT frames=240
import pyxel

pyxel.init(160, 120, title="ほしキャッチ")
bar_x = 70
hoshi_x = pyxel.rndi(8, 150)
hoshi_y = 0
score = 0
miss = 0


def update():
    global bar_x, hoshi_x, hoshi_y, score, miss
    if miss >= 3:
        return
    if pyxel.btn(pyxel.KEY_LEFT):
        bar_x = max(0, bar_x - 3)
    if pyxel.btn(pyxel.KEY_RIGHT):
        bar_x = min(144, bar_x + 3)
    hoshi_y = hoshi_y + 4
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
    if miss >= 3:
        pyxel.text(58, 56, "GAME OVER", 8)


pyxel.run(update, draw)
```
`update` の最初で `return` すると、そこで `update` が終わるので、それより下の「バーを動かす」「ほしを落とす」が実行されなくなり、ゲームが止まります（[[return]]）。`draw` は動き続けるので、画面の表示は残ります。画像は、右キーを押しつづけて、ほしを逃しつづけたあとの画面です。
:::

::: t
ゲームオーバーのあと、スペースキーを押すと点数とミスを0に戻して、もう一度遊べるようにしよう。
:::
::: s
```python px hold=KEY_RIGHT frames=240
import pyxel

pyxel.init(160, 120, title="ほしキャッチ")
bar_x = 70
hoshi_x = pyxel.rndi(8, 150)
hoshi_y = 0
score = 0
miss = 0


def update():
    global bar_x, hoshi_x, hoshi_y, score, miss
    if miss >= 3:
        if pyxel.btnp(pyxel.KEY_SPACE):
            score = 0
            miss = 0
            hoshi_y = 0
        return
    if pyxel.btn(pyxel.KEY_LEFT):
        bar_x = max(0, bar_x - 3)
    if pyxel.btn(pyxel.KEY_RIGHT):
        bar_x = min(144, bar_x + 3)
    hoshi_y = hoshi_y + 4
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
    if miss >= 3:
        pyxel.text(58, 56, "GAME OVER", 8)
        pyxel.text(44, 70, "PUSH SPACE", 7)


pyxel.run(update, draw)
```
:::

@@ task:game-scene
::: t
連打ゲームの背景の色を、場面ごとに変えよう。タイトルは紺（1番）、ゲーム中は黒（0番）、結果は紫（2番）にします。
:::
::: s
```python px frames=10
import pyxel

pyxel.init(160, 120, title="場面ごとの色")
gamen = "title"


def update():
    global gamen
    if gamen == "title":
        if pyxel.btnp(pyxel.KEY_SPACE):
            gamen = "game"
    elif gamen == "game":
        if pyxel.btnp(pyxel.KEY_E):
            gamen = "kekka"
    elif gamen == "kekka":
        if pyxel.btnp(pyxel.KEY_R):
            gamen = "title"


def draw():
    if gamen == "title":
        pyxel.cls(1)
        pyxel.text(60, 55, "TITLE", 7)
    elif gamen == "game":
        pyxel.cls(0)
        pyxel.text(64, 55, "GAME", 7)
    elif gamen == "kekka":
        pyxel.cls(2)
        pyxel.text(60, 55, "RESULT", 7)


pyxel.run(update, draw)
```
`pyxel.cls` を、それぞれの場面の `if` の中に入れます。この例では、スペースでゲームへ、Eキーで結果へ、Rキーでタイトルへ進みます。
:::

::: t
連打ゲームの結果画面で、20回以上押せたら「GREAT!」、そうでなければ「TRY AGAIN」と表示しよう。
:::
::: s
```python px frames=10
import pyxel

pyxel.init(160, 120, title="結果のメッセージ")
gamen = "kekka"
score = 23


def update():
    pass


def draw():
    pyxel.cls(0)
    if gamen == "kekka":
        pyxel.text(52, 40, f"RESULT {score}", 10)
        if score >= 20:
            pyxel.text(60, 60, "GREAT!", 11)
        else:
            pyxel.text(52, 60, "TRY AGAIN", 8)


pyxel.run(update, draw)
```
結果画面の `if` の中に、もう1つ `if` を書きます。確かめやすいように、この例では、はじめから結果画面（`score = 23`）にしています。
:::

::: t
ほしキャッチに、タイトル画面をつけよう。はじめは「HOSHI CATCH / PUSH SPACE」と出して、スペースキーでゲームが始まるようにします。
:::
::: s
```python px frames=10
import pyxel

pyxel.init(160, 120, title="ほしキャッチ")
gamen = "title"
bar_x = 70
hoshi_x = pyxel.rndi(8, 150)
hoshi_y = 0
score = 0


def update():
    global gamen, bar_x, hoshi_x, hoshi_y, score
    if gamen == "title":
        if pyxel.btnp(pyxel.KEY_SPACE):
            gamen = "game"
            score = 0
            hoshi_y = 0
    elif gamen == "game":
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
            hoshi_y = 0
            hoshi_x = pyxel.rndi(8, 150)


def draw():
    pyxel.cls(0)
    if gamen == "title":
        pyxel.text(54, 45, "HOSHI CATCH", 10)
        pyxel.text(54, 65, "PUSH SPACE", 7)
    elif gamen == "game":
        pyxel.rect(bar_x, 110, 16, 6, 11)
        pyxel.circ(hoshi_x, hoshi_y, 4, 10)
        pyxel.text(4, 4, f"SCORE {score}", 7)


pyxel.run(update, draw)
```
ほしキャッチの `update` と `draw` の中身を、`elif gamen == "game":` の中に入れて、インデントを1段下げます。
:::

@@ task:game-list
::: t
雪の数を、30個から60個に増やそう。数を変える場所が3か所あるので、`kazu = 60` という変数を作って、`range(kazu)` と書くと、1か所直すだけですみます。
:::
::: s
```python px frames=30
import pyxel

pyxel.init(160, 120, title="60この雪")
kazu = 60
x_list = []
y_list = []
for i in range(kazu):
    x_list.append(pyxel.rndi(0, 159))
    y_list.append(pyxel.rndi(0, 119))


def update():
    for i in range(kazu):
        y_list[i] = y_list[i] + 1
        if y_list[i] > 120:
            y_list[i] = 0
            x_list[i] = pyxel.rndi(0, 159)


def draw():
    pyxel.cls(1)
    for i in range(kazu):
        pyxel.circ(x_list[i], y_list[i], 1, 7)


pyxel.run(update, draw)
```
`kazu` を `update` の中で書き換えていないので、`global` はいりません。
:::

::: t
雪の落ちる速さを、1つずつちがう速さにしよう。速さを入れるリスト `hayasa_list` を作って、1〜3のランダムな数を入れます。
:::
::: s
```python px gif frames=40
import pyxel

pyxel.init(160, 120, title="速さのちがう雪")
x_list = []
y_list = []
hayasa_list = []
for i in range(30):
    x_list.append(pyxel.rndi(0, 159))
    y_list.append(pyxel.rndi(0, 119))
    hayasa_list.append(pyxel.rndi(1, 3))


def update():
    for i in range(30):
        y_list[i] = y_list[i] + hayasa_list[i]
        if y_list[i] > 120:
            y_list[i] = 0
            x_list[i] = pyxel.rndi(0, 159)


def draw():
    pyxel.cls(1)
    for i in range(30):
        pyxel.circ(x_list[i], y_list[i], 1, 7)


pyxel.run(update, draw)
```
同じ番号の `hayasa_list[i]` が、その雪の速さです。
:::

::: t
雪のかわりに、下から上へのぼっていく「あわ」を20個作ろう。あわは水色（12番）の、ふちだけの円（`circb`、半径3）にします。
:::
::: s
```python px gif frames=40
import pyxel

pyxel.init(160, 120, title="あわ")
x_list = []
y_list = []
for i in range(20):
    x_list.append(pyxel.rndi(0, 159))
    y_list.append(pyxel.rndi(0, 119))


def update():
    for i in range(20):
        y_list[i] = y_list[i] - 1
        if y_list[i] < 0:
            y_list[i] = 120
            x_list[i] = pyxel.rndi(0, 159)


def draw():
    pyxel.cls(5)
    for i in range(20):
        pyxel.circb(x_list[i], y_list[i], 3, 12)


pyxel.run(update, draw)
```
上へ動かすので、`y` を減らします。画面の上（0より小さい）まで行ったら、下（120）に戻します。
:::

@@ task:game-image
::: t
ひよこの絵を使って、画面の3か所にひよこを並べよう。黒は透明にします。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="3羽のひよこ")
pyxel.images[0].set(0, 0, ["000aaa00", "00aaaaa0", "00aaa1a0", "0aaaaaa9", "aaaaaaa0", "0aaaaaa0", "00aaaa00", "00900900"])


def update():
    pass


def draw():
    pyxel.cls(5)
    pyxel.blt(40, 56, 0, 0, 0, 8, 8, 0)
    pyxel.blt(76, 56, 0, 0, 0, 8, 8, 0)
    pyxel.blt(112, 56, 0, 0, 0, 8, 8, 0)


pyxel.run(update, draw)
```
:::

::: t
ひよこを、左を向いた形で表示しよう。（ヒント：幅をマイナスにする）
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="左向き")
pyxel.images[0].set(0, 0, ["000aaa00", "00aaaaa0", "00aaa1a0", "0aaaaaa9", "aaaaaaa0", "0aaaaaa0", "00aaaa00", "00900900"])


def update():
    pass


def draw():
    pyxel.cls(5)
    pyxel.blt(76, 56, 0, 0, 0, -8, 8, 0)


pyxel.run(update, draw)
```
くちばしが左についていればOKです。
:::

::: t
`for` を使って、ひよこを4羽、横一列に並べよう。となりのひよことは、16ドットずつはなします。
:::
::: s
```python px
import pyxel

pyxel.init(160, 120, title="ひよこの行列")
pyxel.images[0].set(0, 0, ["000aaa00", "00aaaaa0", "00aaa1a0", "0aaaaaa9", "aaaaaaa0", "0aaaaaa0", "00aaaa00", "00900900"])


def update():
    pass


def draw():
    pyxel.cls(5)
    for i in range(4):
        pyxel.blt(50 + i * 16, 56, 0, 0, 0, 8, 8, 0)


pyxel.run(update, draw)
```
`i` が 0, 1, 2, 3 と変わるので、x が 16 ずつずれていきます。
:::

@@ task:game-hit
::: t
`kasanatteru` 関数を使って、2つの四角 (10, 10, 20, 20) と (25, 15, 20, 20) が重なっているかを、`print` で表示しよう。
```output
True
```
:::
::: s
```python
def kasanatteru(x1, y1, w1, h1, x2, y2, w2, h2):
    return x1 < x2 + w2 and x2 < x1 + w1 and y1 < y2 + h2 and y2 < y1 + h1


print(kasanatteru(10, 10, 20, 20, 25, 15, 20, 20))
```
1つ目の四角は x が 10〜30、2つ目は 25〜45 なので、25〜30 のところで重なっています。
:::

::: t
マウスで動く円と、真ん中に置いた円の当たり判定を作ろう。重なったら、真ん中の円を赤（8番）にします。半径はどちらも 10 です。
:::
::: s
```python px click=75,55 frames=10
import pyxel

pyxel.init(160, 120, title="円の当たり判定")
pyxel.mouse(True)


def update():
    pass


def draw():
    pyxel.cls(0)
    dx = pyxel.mouse_x - 80
    dy = pyxel.mouse_y - 60
    kyori = pyxel.sqrt(dx * dx + dy * dy)
    if kyori < 10 + 10:
        pyxel.circ(80, 60, 10, 8)
    else:
        pyxel.circ(80, 60, 10, 13)
    pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, 10, 11)


pyxel.run(update, draw)
```
中心どうしの距離 `kyori` が、半径の合計 `20` より小さければ当たりです。
:::

::: t
ほしキャッチの当たり判定を、`kasanatteru` 関数を使った書き方に書きかえよう。ほしは 8×8 の四角、バーは 16×6 の四角と考えます。
:::
::: s
```python px hold=KEY_RIGHT frames=90 gif
import pyxel

pyxel.init(160, 120, title="ほしキャッチ")
bar_x = 70
hoshi_x = pyxel.rndi(8, 150)
hoshi_y = 0
score = 0


def kasanatteru(x1, y1, w1, h1, x2, y2, w2, h2):
    return x1 < x2 + w2 and x2 < x1 + w1 and y1 < y2 + h2 and y2 < y1 + h1


def update():
    global bar_x, hoshi_x, hoshi_y, score
    if pyxel.btn(pyxel.KEY_LEFT):
        bar_x = max(0, bar_x - 3)
    if pyxel.btn(pyxel.KEY_RIGHT):
        bar_x = min(144, bar_x + 3)
    hoshi_y = hoshi_y + 2
    if kasanatteru(hoshi_x - 4, hoshi_y - 4, 8, 8, bar_x, 110, 16, 6):
        score = score + 1
        hoshi_y = 0
        hoshi_x = pyxel.rndi(8, 150)
    elif hoshi_y > 120:
        hoshi_y = 0
        hoshi_x = pyxel.rndi(8, 150)


def draw():
    pyxel.cls(0)
    pyxel.rect(bar_x, 110, 16, 6, 11)
    pyxel.circ(hoshi_x, hoshi_y, 4, 10)
    pyxel.text(4, 4, f"SCORE {score}", 7)


pyxel.run(update, draw)
```
円の中心 (hoshi_x, hoshi_y) から4ずつ引いた位置が、ほしを囲む四角の左上です。
:::

@@ task:game-sound
::: t
スペースキーを押すと「ドレミ」と鳴るプログラムを作ろう。音色は三角波（`t`）にします。
:::
::: s
```python px frames=5
import pyxel

pyxel.init(160, 120, title="ドレミ")
pyxel.sounds[0].set("c3d3e3", "t", "7", "n", 15)


def update():
    if pyxel.btnp(pyxel.KEY_SPACE):
        pyxel.play(0, 0)


def draw():
    pyxel.cls(1)
    pyxel.text(52, 56, "PUSH SPACE", 7)


pyxel.run(update, draw)
```
:::

::: t
上の「ドレミ」を、ノイズ（`n`）・四角波（`s`）・パルス波（`p`）の音色に変えて、聞きくらべてみよう。どれがいちばんファミコンっぽい？
:::
::: s
```python px frames=5
import pyxel

pyxel.init(160, 120, title="音色くらべ")
pyxel.sounds[0].set("c3d3e3", "t", "7", "n", 15)
pyxel.sounds[1].set("c3d3e3", "s", "7", "n", 15)
pyxel.sounds[2].set("c3d3e3", "p", "7", "n", 15)
pyxel.sounds[3].set("c3d3e3", "n", "7", "n", 15)


def update():
    if pyxel.btnp(pyxel.KEY_1):
        pyxel.play(0, 0)
    if pyxel.btnp(pyxel.KEY_2):
        pyxel.play(0, 1)
    if pyxel.btnp(pyxel.KEY_3):
        pyxel.play(0, 2)
    if pyxel.btnp(pyxel.KEY_4):
        pyxel.play(0, 3)


def draw():
    pyxel.cls(1)
    pyxel.text(40, 40, "1: t  2: s", 7)
    pyxel.text(40, 56, "3: p  4: n", 7)


pyxel.run(update, draw)
```
1〜4のキーで、音色をくらべられます。ファミコンっぽいのは、四角波（`s`）とパルス波（`p`）です。
:::

::: t
ほしキャッチで、ほしを受け止めたときに「ピコン」と鳴るようにしよう。
:::
::: s
```python px hold=KEY_RIGHT frames=60
import pyxel

pyxel.init(160, 120, title="ほしキャッチ")
pyxel.sounds[0].set("c3e3g3c4", "p", "7", "n", 5)
bar_x = 70
hoshi_x = pyxel.rndi(8, 150)
hoshi_y = 0
score = 0


def update():
    global bar_x, hoshi_x, hoshi_y, score
    if pyxel.btn(pyxel.KEY_LEFT):
        bar_x = max(0, bar_x - 3)
    if pyxel.btn(pyxel.KEY_RIGHT):
        bar_x = min(144, bar_x + 3)
    hoshi_y = hoshi_y + 2
    if hoshi_y > 104 and bar_x - 4 <= hoshi_x <= bar_x + 20:
        score = score + 1
        pyxel.play(0, 0)
        hoshi_y = 0
        hoshi_x = pyxel.rndi(8, 150)
    elif hoshi_y > 120:
        hoshi_y = 0
        hoshi_x = pyxel.rndi(8, 150)


def draw():
    pyxel.cls(0)
    pyxel.rect(bar_x, 110, 16, 6, 11)
    pyxel.circ(hoshi_x, hoshi_y, 4, 10)
    pyxel.text(4, 4, f"SCORE {score}", 7)


pyxel.run(update, draw)
```
音を作る `set` は最初に1回、鳴らす `play` は受け止めた瞬間に書きます。
:::
