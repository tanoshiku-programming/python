@@ task:ch4
::: t
年齢を聞いて、18才以上なら「大人です」、そうでなければ「子どもです」と表示してみよう。
:::
::: s
```python in=20
nenrei = int(input("年齢は？"))
if nenrei >= 18:
    print("大人です")
else:
    print("子どもです")
```
:::

::: t
数を聞いて、偶数なら「偶数です」、奇数なら「奇数です」と表示してみよう。
:::
::: s
```python in=8
n = int(input("数は？"))
if n % 2 == 0:
    print("偶数です")
else:
    print("奇数です")
```
:::

::: t
点数を聞いて、90点以上なら `A`、70点以上なら `B`、それ以外なら `C` と表示してみよう。
:::
::: s
```python in=75
score = int(input("点数は？"))
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")
```
:::

::: c
3つの数を聞いて、いちばん大きい数を表示しよう。ただし、`max()` は使わずに、`if` で考えてみよう。
```output
1つ目：{{4}}
2つ目：{{9}}
3つ目：{{7}}
いちばん大きいのは 9
```
:::
::: s
```python in=4|9|7
a = int(input("1つ目："))
b = int(input("2つ目："))
c = int(input("3つ目："))
ichiban = a
if b > ichiban:
    ichiban = b
if c > ichiban:
    ichiban = c
print("いちばん大きいのは", ichiban)
```
「今のところ、いちばん大きい数」を `ichiban` に覚えておいて、それより大きい数が出てきたら入れ替えます。数が増えても、同じやり方で調べられます。
:::

@@ task:if
::: t
`kion = 32` のとき、30以上なら「暑いです」と表示してみよう。
```output
暑いです
```
:::
::: s
```python
kion = 32
if kion >= 30:
    print("暑いです")
```
:::

::: t
`n = 4` が偶数なら「偶数です」と表示するプログラムを書いてみよう。（2で割った余りを使うよ）
```output
偶数です
```
:::
::: s
```python
n = 4
if n % 2 == 0:
    print("偶数です")
```
:::

::: t
パスワードを聞いて、`"python"` と同じなら「ようこそ！」と表示してみよう。
:::
::: s
```python in=python
password = input("パスワードは？")
if password == "python":
    print("ようこそ！")
```
:::

@@ task:else
::: t
`score = 65` のとき、60点以上なら「合格」、そうでなければ「不合格」と表示してみよう。
```output
合格
```
:::
::: s
```python
score = 65
if score >= 60:
    print("合格")
else:
    print("不合格")
```
:::

::: t
`n = 0` のとき、0より大きければ「プラス」、0より小さければ「マイナス」、そうでなければ「ゼロ」と表示してみよう。
```output
ゼロ
```
:::
::: s
```python
n = 0
if n > 0:
    print("プラス")
elif n < 0:
    print("マイナス")
else:
    print("ゼロ")
```
:::

::: t
点数を聞いて、90点以上は `A`、70点以上は `B`、50点以上は `C`、それ以外は `D` と表示してみよう。
:::
::: s
```python in=55
score = int(input("点数は？"))
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 50:
    print("C")
else:
    print("D")
```
厳しい条件（大きい数）を上に書くのがポイントです。
:::

@@ task:comparison
::: t
`5 == 5` と `5 != 5` の答えを、2行で表示してみよう。
```output
True
False
```
:::
::: s
```python
print(5 == 5)
print(5 != 5)
```
:::

::: t
`x = 7` が、1以上10以下かどうかを、`1 <= x <= 10` で調べて表示してみよう。
```output
True
```
:::
::: s
```python
x = 7
print(1 <= x <= 10)
```
:::

::: t
入力した文字が `"はい"` と等しいかどうかを、`==` で調べて表示してみよう。
:::
::: s
```python in=はい
seikai = input("はい or いいえ：")
print(seikai == "はい")
```
:::

@@ task:logical
::: t
`nenrei = 11` が、10才以上 `and` 12才以下かどうかを調べて表示してみよう。
```output
True
```
:::
::: s
```python
nenrei = 11
print(nenrei >= 10 and nenrei <= 12)
```
:::

::: t
`nenrei = 5` が、10才より小さい `or` 12才より大きいかどうかを調べて表示してみよう。
```output
True
```
:::
::: s
```python
nenrei = 5
print(nenrei < 10 or nenrei > 12)
```
:::

::: t
西暦を聞いて、「4でわり切れて、100ではわり切れない」ときだけ「うるう年です」と表示してみよう。（2028 なら表示される）
:::
::: s
```python in=2028
seireki = int(input("西暦は？"))
if seireki % 4 == 0 and seireki % 100 != 0:
    print("うるう年です")
```
:::
