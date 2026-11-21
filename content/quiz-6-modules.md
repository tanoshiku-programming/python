@@ quiz:ch6
::: q
モジュールを使えるようにするために、最初に書く言葉は？
:::
::: a
`import` です。たとえば `import random` と書きます。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
import calendar
print(calendar.isleap(2028))
```
:::
::: a
2028年は4で割り切れて、100では割り切れないので、うるう年です。
:::

::: q
1から6のどれかの整数を、ランダムに作りたい。`____` に入る関数の名前は？
```python norun
import random
print(random.____(1, 6))
```
:::
::: a
`randint` です。サイコロと同じです。
:::

@@ quiz:module
::: q
モジュールとは、どんなもの？
:::
::: a
便利な関数や道具をまとめた部品（部品箱）です。`import` して使います。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
import math
print(math.sqrt(16))
```
:::
::: a
`math.sqrt` は平方根です。「`math` の中の `sqrt`」と、`.`（ドット）で指定します。
:::

::: q
標準ライブラリとは、どんなモジュール？
:::
::: a
Pythonを入れると、最初から使えるモジュールのことです。`random` や `calendar` もその仲間です。
:::

@@ quiz:import
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
import math
print(math.sqrt(25))
```
:::
::: a
`import math` と書いたときは、`math.sqrt` のように、モジュール名を前につけます。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
from math import sqrt
print(sqrt(25))
```
:::
::: a
`from ... import ...` と書くと、モジュール名を省いて `sqrt(25)` と書けます。答えは上の問題と同じです。
:::

::: q
次のプログラムを実行すると、どうなる？
```python hideout error
import ramdom
```
:::
::: a
エラー（`ModuleNotFoundError`）になります。`random` の打ち間違いで、見つからないからです。
:::

@@ quiz:random
::: q
サイコロのように、1から6のどれかの整数をランダムに作るには、どう書く？
:::
::: a
`random.randint(1, 6)` です。先頭に `import random` が必要です。
:::

::: q
リストの中から、ランダムに1つ選ぶ関数は？
:::
::: a
`random.choice(リスト)` です。おみくじなどに使えます。
:::

::: q
リスト `namae_list` の順番を、ランダムに入れ替えたい。`____` に入る関数は？
```python norun
import random
namae_list = ["はなこ", "たろう", "じろう"]
random.____(namae_list)
```
:::
::: a
`shuffle` です。`random.shuffle(namae_list)` と書きます。
:::

@@ quiz:calendar
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
import calendar
print(calendar.isleap(2100))
```
:::
::: a
2100年は、100で割り切れるけれど400では割り切れないので、うるう年ではありません。
:::

::: q
`calendar.weekday(2026, 10, 17)` の答えが `5` だった。これは何曜日？
:::
::: a
土曜日です。`0` が月曜日、`6` が日曜日なので、`5` は土曜日です。
:::

::: q
2026年10月のカレンダーを表示したい。`____` に入る関数は？
```python norun
import calendar
print(calendar.____(2026, 10))
```
:::
::: a
`month` です。`calendar.month(年, 月)` と書きます。
:::

@@ quiz:mymodule
::: q
`keisan.py` というファイルの関数を使うには、どう書く？
:::
::: a
`import keisan` と書きます。`.py` はつけません。使うときは `keisan.tasu(3, 4)` のように書きます。
:::

::: q
`from keisan import tasu` と書くと、何ができる？
:::
::: a
`keisan.` をつけずに、`tasu(3, 4)` とそのまま使えます。
:::

::: q
自分のファイル `keisan.py` を `import` したら、同じフォルダに `__pycache__` ができた。どうすればいい？
:::
::: a
**何もしなくて大丈夫**です。Pythonが、次に読みこむのを早くするために、自動で作ったメモです。消しても、また自動でできます。
:::

@@ quiz:library
::: q
`random.py` のように、`.py` ファイル1つぶんの部品を、何という？ また、フォルダにまとめたものは？
:::
::: a
ファイル1つは**モジュール**、フォルダにまとめたものは**パッケージ**です。
:::

::: q
スマホのアプリにたとえると、`pip install pyxel` と `import pyxel` は、それぞれ何にあたる？
:::
::: a
`pip install pyxel` は、ストアで**アプリを入手する**こと（1回だけ）、`import pyxel` は、**アプリを開いて使う**こと（プログラムを書くたび）です。
:::

::: q
`random.randint(1, 6)` と `pyxel.run(update, draw)` では、自分が書いた関数を、相手が呼んでくれるのはどっち？
:::
::: a
`pyxel.run(update, draw)` です。Pyxelが、自分の書いた `update` と `draw` を、1秒に30回呼んでくれます。こういう部品を、エンジンやフレームワークと呼びます。
:::
