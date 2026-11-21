@@ ch6
title: モジュール
kind: chapter
chapter: 6
summary: 他の人が作ってくれた便利な部品（モジュール）を、importして使います。
reads: import=インポート | from=フロム | random=ランダム | calendar=カレンダー
--
## この章のゴール
Pythonには、便利な部品（**モジュール**）がたくさんあります。スマホにアプリを入れて使うように、`import` するだけで使えます。Scratchの「拡張機能を追加」です。

### まずはこれ（この順番で読もう）
1. [[module]]：部品箱ってなに？
2. [[import]]：部品を使えるようにする
3. [[random]]：くじ・サイコロ・シャッフル

ほかの言葉は「必要になったら」のページです。最初は飛ばして大丈夫です。ページのいちばん下に、一覧があります。

::: point この章で、自分でできるようになること
- □ `import` で、モジュールを使えるようにできる
- □ `random.randint` で、ランダムな数を作れる
- □ `random.choice` で、リストから1つ選べる

ゲームを作る前に、ここにあることを、**お手本を見ないで書けるように**、くりかえし練習しよう。
:::

## サイコロをふる
```python norun
import random
print(random.randint(1, 6))
```
```output
4
```
実行するたびに、1から6のどれかが出ます（ここに出ている結果は一例です）。

## やってみよう
::: try おみくじ
「大吉」「中吉」「小吉」「凶」のどれかを、ランダムで表示しましょう。
:::
::: answer
```python norun
import random
uranai_list = ["大吉", "中吉", "小吉", "凶"]
print(random.choice(uranai_list))
```
```output
中吉
```
`random.choice(リスト)` は、[[list]]の中から1つを選びます。
:::

::: try 数当てゲーム
1から10のあいだで、コンピュータが数を決めます。当たるまで入力して、当てたら「正解」と表示しましょう。
:::
::: answer
```python norun
import random
seikai = random.randint(1, 10)
yosou = 0
while yosou != seikai:
    yosou = int(input("1から10の数は？"))
print("正解！")
```
```output
1から10の数は？{{3}}
1から10の数は？{{7}}
正解！
```
[[while]]で、当たるまで繰り返しています。
:::

@@ module
title: モジュール
type: 考え方
chapter: 6
summary: 便利な関数や道具をまとめた部品です。import して使います。
reads: import=インポート | math=マス | sqrt=スクエアルート | pi=パイ
group: まずはこれ
--
::: scratch
Scratchの左下の「拡張機能を追加」ボタンで、「ペン」や「音楽」のブロックを足しましたね。Pythonのモジュールは、あの拡張機能と同じです。`import` が、「拡張機能を追加」にあたります。
:::

## 部品箱のイメージ
モジュールは、関連する[[function]]などをひとまとめにした部品箱です。使いたいときに、箱ごと持ってきて、中の道具を取り出します（[[import]]）。

```python
import math
print(math.sqrt(16))
print(math.pi)
```
`math.sqrt(16)` は「`math` の中の `sqrt`（平方根）」という意味です。`.`（ドット）で、箱の中の道具を指定します。

## 最初から入っているモジュール
Pythonをインストールすると、最初から使えるモジュールがたくさんあります。これを標準ライブラリといいます。

| 名前 | できること |
| --- | --- |
| [[random]] | ランダムな数や選択 |
| [[calendar]] | カレンダー、うるう年、曜日 |
| `math` | 平方根、円周率など数学の計算 |
| `datetime` | 日付や時刻 |
| `time` | 待つ、時間をはかる |

## あとから追加するモジュール
標準には入っていない、ほかの人が作った部品もあります。スマホにストアから新しいアプリを入れるように、あとから追加して（`pip install`）使います。ゲームを作る Pyxel も、そのひとつです。呼び名のちがいは、[[library]]で整理しています。

::: deep 自分のファイルもモジュールになる
自分で書いた `.py` ファイルも、`import` で使えます（[[mymodule]]）。ただし、`random.py` のように、標準のモジュールと同じ名前をつけると、自分のファイルのほうが読みこまれてしまうので、つけないようにします（[[pyfile]]）。
:::

@@ import
title: import
type: 構文
chapter: 6
syntax: import モジュール名
summary: モジュールを、自分のプログラムで使えるようにする命令です。
reads: import=インポート | from=フロム | math=マス | sqrt=スクエアルート
group: まずはこれ
--
::: scratch
Scratchの「拡張機能を追加」ボタンと同じです。`import random` と書くと、`random` のブロック（命令）が使えるようになります。
:::

## 書き方のかたち
::: tpl import の書き方（2種類）
import 〔モジュール名〕
〔モジュール名〕.〔関数名〕(〔値〕)

from 〔モジュール名〕 import 〔関数名〕
〔関数名〕(〔値〕)

| 〔モジュール名〕 | random や math など、使いたい部品箱の名前 |
| 〔関数名〕 | その中にある、使いたい関数の名前 |
:::

## 書き方
```python
import math
print(math.sqrt(25))
```
`import モジュール名` で、そのモジュールが使えるようになります。使うときは、`モジュール名.関数名` と書きます（[[module]]）。

## 名前だけ取り出す
`from モジュール名 import 関数名` と書くと、モジュール名を省いて使えます。

```python
from math import sqrt
print(sqrt(25))
```
| 書き方 | 使い方 |
| --- | --- |
| `import math` | `math.sqrt(25)` |
| `from math import sqrt` | `sqrt(25)` |

## 書く場所
`import` は、プログラムのいちばん上にまとめて書くのが普通です。

::: stuck
モジュールの名前を打ち間違えると、見つからなくて[[error]]になります。

```python error
import ramdom
```
`random` と書くところを、間違えました。
:::

@@ random
title: random
type: モジュール
chapter: 6
syntax: random.randint(1, 6)
summary: ランダム（でたらめ）な数や選択を作るモジュールです。ゲームやくじに使えます。
reads: random=ランダム | randint=ランディント | choice=チョイス | shuffle=シャッフル
group: まずはこれ
--
::: scratch
Scratchの「（1）から（10）までの乱数」ブロックが、`random.randint(1, 10)` です。
:::

## 書き方のかたち
::: tpl random の使い方
import random
random.randint(〔始め〕, 〔終わり〕)
random.choice(〔リスト〕)

| 〔始め〕 | 出る数の最小（この数も出る） |
| 〔終わり〕 | 出る数の最大（この数も出る） |
| 〔リスト〕 | この中から1つ選ぶ |
:::

## 使うまえに
先頭に `import random` と書きます（[[import]]）。以下の例の結果は、実行するたびに変わります。

## randint：範囲の数を1つ
```python norun
import random
for i in range(3):
    print(random.randint(1, 6))
```
```output
4
1
6
```
`randint(1, 6)` は、1から6の整数のどれか（6も含む）を返します。サイコロです。Scratchの「（1）から（6）までの乱数」と同じです。

## choice：リストから1つ選ぶ
```python norun
import random
uranai_list = ["大吉", "中吉", "小吉", "凶"]
print(random.choice(uranai_list))
```
```output
中吉
```
[[list]]の中から、ランダムに1つ選びます。

## shuffle：順番をシャッフル
```python norun
import random
namae_list = ["はなこ", "たろう", "じろう"]
random.shuffle(namae_list)
print(namae_list)
```
```output
['たろう', 'じろう', 'はなこ']
```
リストの中身の順番を、入れ替えます。

::: deep 同じ結果を繰り返したいとき
`random.seed(1)` のように、最初に数を決めておくと、毎回同じ順番で「ランダム」な数が出ます。ゲームのテストで、結果をそろえたいときに使います。
:::

@@ library
title: モジュール・パッケージ・ライブラリのちがい
type: 考え方
chapter: 6
syntax: pip install 名前 / import 名前
summary: Pythonの部品の呼び名の整理です。モジュールは.pyファイル1つ、パッケージはそれをフォルダにまとめたもの、ライブラリは部品の集まりをさす言葉。スマホのアプリにたとえると、標準は「最初から入っているアプリ」、pipで入れるものは「ストアのアプリ」です。
aliases: ライブラリ, パッケージ, モジュール, 標準ライブラリ, 外部モジュール, サードパーティ, フレームワーク, エンジン, ゲームエンジン, PyPI, pip, 拡張機能
reads: library=ライブラリ | package=パッケージ | PyPI=パイピーアイ | pip=ピップ | engine=エンジン
group: 必要になったら
--
::: scratch
Scratchの左下の「拡張機能を追加」で、「ペン」や「音楽」のブロックを足しましたね。Pythonの部品も同じで、最初から入っているものと、あとから足すものがあります。
:::

## ひとことで
「モジュール」「パッケージ」「ライブラリ」は、どれも**Pythonに足して使う部品**のことです。最初は、**呼び方がちがうだけ**と思って大丈夫です。

## スマホのアプリにたとえると
| スマホ | Python |
| --- | --- |
| 最初から入っているアプリ（カメラ・電卓） | 最初から入っている部品（`random`・`math`・`calendar`）。**標準ライブラリ**という |
| ストアから入れるアプリ | あとから入れる部品（`pyxel`） |
| ストアで「入手」を押す | `pip install pyxel`（**1回だけ**） |
| アプリを開いて使う | `import pyxel`（**プログラムを書くたびに**） |

「入れるのは1回」「使うと書くのは毎回」の2つを覚えよう。

## Pyxelは何？
ストアから入れるアプリと同じで、`pip install` で入れる部品です。Pyxel自身は、「**ゲームエンジン**（ゲームを作るための部品セット）」と名のっています（[[pyxel]]）。

::: stuck
`pip install` のあとの名前を打ちまちがえると、別の部品が入ってしまうことがあります。だれでも部品を公開できるからです。知らない名前の部品は、先生に聞いてから入れよう（[[terminal]]）。
:::

::: deep 呼び名のちがい（くわしく）
| 言葉 | 意味 | 例 |
| --- | --- | --- |
| モジュール | `.py` ファイル1つぶんの部品 | `random`、`calendar` |
| パッケージ | モジュールをフォルダにまとめたもの | `pyxel` |
| ライブラリ | 部品の集まりを、ざっくり言う言葉 | 「Pyxelライブラリ」 |
| 標準ライブラリ | Pythonに最初から入っている部品の全部 | `random`、`math` |
:::

::: deep ライブラリとエンジンのちがい
`random.randint(1, 6)` は、**自分**が好きなときに呼びます。`pyxel.run(update, draw)` は、自分が書いた `update` と `draw` を、**Pyxelが**1秒に30回呼んでくれます（[[update-draw]]）。このように、全体の流れを用意して、自分のプログラムを呼んでくれる部品を、**エンジン**や**フレームワーク**と呼びます。
:::

@@ calendar
title: calendar
type: モジュール
chapter: 6
syntax: calendar.month(年, 月)
summary: カレンダーを表示したり、うるう年や曜日を調べたりできるモジュールです。
reads: calendar=カレンダー | month=マンス | isleap=イズリープ | weekday=ウィークデイ
group: 必要になったら
--
## 書き方のかたち
::: tpl calendar の使い方
import calendar
calendar.month(〔年〕, 〔月〕)
calendar.isleap(〔年〕)

| 〔年〕 | 西暦の数（2026 など） |
| 〔月〕 | 1 〜 12 の数 |
:::

## カレンダーを表示
```python
import calendar
print(calendar.month(2026, 10))
```
`calendar.month(年, 月)` で、その月のカレンダーが文字で作られます（[[str]]）。

## うるう年かどうか
```python
import calendar
print(calendar.isleap(2028))
print(calendar.isleap(2100))
```
答えは[[bool]]です。2100年は、100で割り切れるけれど400では割り切れないので、うるう年ではありません。

## 曜日を調べる
```python
import calendar
print(calendar.weekday(2026, 10, 17))
```
答えは `0` が月曜日、`6` が日曜日の数です。

| 数 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 曜日 | 月 | 火 | 水 | 木 | 金 | 土 | 日 |

::: deep 日曜日はじまりにする
```python
import calendar
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2026, 10))
```
:::

@@ mymodule
title: 自分のファイルを import しよう
type: 構文
chapter: 6
syntax: from ファイル名 import 関数名
summary: プログラムが長くなったら、関数を別のファイルに分けて、import で使います。自分で作った .py ファイルも、モジュールとして使えます。
aliases: 自作モジュール, ファイルを分ける, 分割, __pycache__, pyc, メイン, __main__
reads: import=インポート | from=フロム | __name__=ネーム | __main__=メイン | pyc=ピーワイシー
group: 必要になったら
--
## プログラムを、複数のファイルに分ける
プログラムが長くなると、1つのファイルに全部書いていると、読みにくくなります。そこで、**関連するものを、別のファイルに分けて**、必要なところで `import` します。

実は、[[module]]の説明にあった「自分で書いた `.py` ファイルも、`import` で使えます」というのは、このことです。

## 例：計算用のファイルを作る
**同じフォルダ**に、2つのファイルを作ります。

`keisan.py`（関数を入れておくファイル）
```python norun
def tasu(a, b):
    return a + b


def kakeru(a, b):
    return a * b
```

`main.py`（それを使うファイル）
```python norun
import keisan

print(keisan.tasu(3, 4))
print(keisan.kakeru(3, 4))
```
```output
7
12
```
`import keisan` と書くと、`keisan.py` の中身が使えるようになります。**ファイル名から `.py` を取った名前**が、モジュールの名前です。使うときは、`モジュール名.関数名` と書きます（[[import]]）。

名前だけ取り出すこともできます。

```python norun
from keisan import tasu

print(tasu(3, 4))
```
```output
7
```

## ゲームを分けるなら
たとえば、[[game-hit]]の `kasanatteru` 関数のように、いろいろなゲームで使い回したい関数を `atari.py` に入れておけば、どのゲームからも `from atari import kasanatteru` で使えます。

| ファイル | 入れるもの |
| --- | --- |
| `main.py` | ゲームの中心（`init`、`update`、`draw`、`run`） |
| `atari.py` | 当たり判定の関数 |
| `hoshi.py` | ほしのクラス（[[class]]） |

::: point
分けるときの目安は、「**これは、別のゲームでも使えそう**」と思ったものです。1つのファイルが長くなりすぎたときにも、分けどきです。
:::

::: stuck
- 2つのファイルは、**同じフォルダ**に置こう（[[pyfile]]）
- ファイル名を、`random.py` など、もともとあるモジュールの名前にしてはいけません
- `import keisan.py` のように `.py` をつけると、エラーになります。`import keisan` と書きます
:::

::: deep `__pycache__` フォルダは何？
自分のファイルを `import` すると、同じフォルダに `__pycache__` というフォルダができて、中に `keisan.cpython-312.pyc` のようなファイルが入ります。これは、Pythonが「次に読みこむとき早く動くように」自動で作る、メモのようなものです。

自分で作ったり、直したりする必要はありません。**消してしまっても、また自動でできます**。
:::

::: deep `if __name__ == "__main__":` ってなに？
他の人のプログラムで、よく見かける書き方です。

```python norun
def tasu(a, b):
    return a + b


if __name__ == "__main__":
    print(tasu(3, 4))
```
`__name__` には、「そのファイルを直接動かしたとき」は `"__main__"` が入り、「ほかのファイルから `import` されたとき」はファイルの名前が入ります。だから、この書き方をしておくと、**直接動かしたときだけ**、`if` の中のテスト用の行が動きます。`import` したときには動きません。
:::
