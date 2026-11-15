@@ task:ch6
::: t
`random` を使って、1から6のどれかの数（サイコロ）を表示してみよう。（毎回ちがう数が出るよ）
:::
::: s
```python norun
import random

print(random.randint(1, 6))
```
```output
4
```
実行するたびに、1〜6のどれかが出ます。
:::

::: t
`calendar` を使って、2028年がうるう年かどうかを表示してみよう。
```output
True
```
:::
::: s
```python
import calendar

print(calendar.isleap(2028))
```
:::

::: t
`["大吉", "中吉", "小吉", "凶"]` から、ランダムに1つ選んで表示するおみくじを作ってみよう。
:::
::: s
```python norun
import random

uranai_list = ["大吉", "中吉", "小吉", "凶"]
print(random.choice(uranai_list))
```
```output
中吉
```
:::

::: c
サイコロを2つふって、それぞれの目と合計を表示しよう。2つが同じ目（ゾロ目）だったら、「ゾロ目！」とも表示しよう。
:::
::: s
```python norun
import random
me1 = random.randint(1, 6)
me2 = random.randint(1, 6)
print(me1, me2, "合計", me1 + me2)
if me1 == me2:
    print("ゾロ目！")
```
```output
3 3 合計 6
ゾロ目！
```
実行するたびに、結果が変わります。ゾロ目が出るまで、何回か試してみよう。
:::

@@ task:module
::: t
`math` モジュールを使って、`81` の平方根を表示してみよう。
```output
9.0
```
:::
::: s
```python
import math

print(math.sqrt(81))
```
:::

::: t
`math` モジュールの、円周率 `pi` を表示してみよう。
```output
3.141592653589793
```
:::
::: s
```python
import math

print(math.pi)
```
:::

::: t
半径 `r = 10` の円の面積（`半径 × 半径 × pi`）を、`math.pi` を使って求めて、表示してみよう。小数第2位までに丸めよう。
```output
314.16
```
:::
::: s
```python
import math

r = 10
menseki = r * r * math.pi
print(round(menseki, 2))
```
:::

@@ task:import
::: t
`import math` を使って、`49` の平方根を表示してみよう。
```output
7.0
```
:::
::: s
```python
import math

print(math.sqrt(49))
```
:::

::: t
`from math import sqrt` を使って、`math.` をつけずに `100` の平方根を表示してみよう。
```output
10.0
```
:::
::: s
```python
from math import sqrt

print(sqrt(100))
```
:::

::: t
`import` の名前を打ち間違えて（`import ramdom`）、エラーの名前を確かめてみよう。
:::
::: s
```python error
import ramdom
```
`ModuleNotFoundError` は、そんなモジュールは見つからない、というエラーです。つづりを見直そう。
:::

@@ task:random
::: t
1から10のどれかの数を、ランダムに表示してみよう。
:::
::: s
```python norun
import random

print(random.randint(1, 10))
```
```output
7
```
:::

::: t
`["グー", "チョキ", "パー"]` から、ランダムに1つ選ぶ「じゃんけんコンピュータ」を作ってみよう。
:::
::: s
```python norun
import random

te_list = ["グー", "チョキ", "パー"]
print(random.choice(te_list))
```
```output
パー
```
:::

::: t
1から10の数をランダムに作って、それを当てるゲームを作ってみよう。当たるまで入力しつづけて、当たったら「正解！」と表示しよう。
:::
::: s
```python norun
import random

seikai = random.randint(1, 10)
yosou = 0
while yosou != seikai:
    yosou = int(input("1から10の数は？"))
print("正解！")
```
```output
1から10の数は？3
1から10の数は？7
正解！
```
:::

@@ task:calendar
::: t
2026年10月のカレンダーを表示してみよう。
:::
::: s
```python
import calendar

print(calendar.month(2026, 10))
```
:::

::: t
西暦を聞いて、うるう年なら「うるう年です」、そうでなければ「うるう年ではありません」と表示してみよう。
:::
::: s
```python in=2100
import calendar

seireki = int(input("西暦は？"))
if calendar.isleap(seireki):
    print("うるう年です")
else:
    print("うるう年ではありません")
```
:::

::: t
2026年10月17日が何曜日かを、`calendar.weekday` で数字にして表示してみよう。（0が月曜日、6が日曜日）
```output
5
```
:::
::: s
```python
import calendar

print(calendar.weekday(2026, 10, 17))
```
5 は土曜日です。
:::
