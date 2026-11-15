@@ task:ch3
::: t
`for` を使って、「がんばろう」を5回表示してみよう。
```output
がんばろう
がんばろう
がんばろう
がんばろう
がんばろう
```
:::
::: s
```python
for i in range(5):
    print("がんばろう")
```
:::

::: t
`for` と `range` を使って、1から5までの数を表示してみよう。
```output
1
2
3
4
5
```
:::
::: s
```python
for i in range(1, 6):
    print(i)
```
`range(1, 6)` は、6の手前の5までです。
:::

::: t
`while` を使って、5から1までを数えて、最後に「スタート！」と表示してみよう。
```output
5
4
3
2
1
スタート！
```
:::
::: s
```python
count = 5
while count > 0:
    print(count)
    count -= 1
print("スタート！")
```
:::

::: c
`for` を使って、`*` の階段を作ろう。1行目は1個、5行目は5個です。（ヒント：`"*" * 3` は `***` になります）
```output
*
**
***
****
*****
```
:::
::: s
```python
for i in range(1, 6):
    print("*" * i)
```
`i` が 1, 2, 3, 4, 5 と変わるので、`"*" * i` の数も1つずつ増えます（[[str]]）。
:::

@@ task:for
::: t
`for` を使って、「こんにちは」を3回表示してみよう。
```output
こんにちは
こんにちは
こんにちは
```
:::
::: s
```python
for i in range(3):
    print("こんにちは")
```
:::

::: t
`for` で、リスト `["りんご", "みかん", "バナナ"]` の中身を、1つずつ表示してみよう。
```output
りんご
みかん
バナナ
```
:::
::: s
```python
for kudamono in ["りんご", "みかん", "バナナ"]:
    print(kudamono)
```
:::

::: t
`for` で、1から10までの合計を求めて、表示してみよう。（`total` を使うよ）
```output
55
```
:::
::: s
```python
total = 0
for i in range(1, 11):
    total += i
print(total)
```
繰り返しのあとに、`print` を1回だけ書くのがポイントです（インデントを下げない）。
:::

@@ task:while
::: t
`while` で、1、2、3 を順番に表示してみよう。
```output
1
2
3
```
:::
::: s
```python
n = 1
while n <= 3:
    print(n)
    n += 1
```
:::

::: t
`while` で、10から2ずつ減らして、`10 8 6 4 2` を1行ずつ表示してみよう。
```output
10
8
6
4
2
```
:::
::: s
```python
n = 10
while n > 0:
    print(n)
    n -= 2
```
:::

::: t
「やめる」と入力するまで、入力した文字を「○○ですね」と表示しつづけるプログラムを書いてみよう。
:::
::: s
```python in=りんご|みかん|やめる
while True:
    moji = input("何か入力（やめる で終了）：")
    if moji == "やめる":
        break
    print(moji + "ですね")
```
:::

@@ task:range
::: t
`range(5)` の中身を、`list()` を使って表示してみよう。
```output
[0, 1, 2, 3, 4]
```
:::
::: s
```python
print(list(range(5)))
```
:::

::: t
`range` を使って、`[1, 2, 3, 4, 5]` を表示してみよう。
```output
[1, 2, 3, 4, 5]
```
:::
::: s
```python
print(list(range(1, 6)))
```
:::

::: t
`range` の3つ目の数を使って、`[0, 5, 10, 15, 20]` を表示してみよう。
```output
[0, 5, 10, 15, 20]
```
:::
::: s
```python
print(list(range(0, 25, 5)))
```
:::

@@ task:break
::: t
`for` で 1から10まで表示するけれど、`6` になったら `break` で終わるようにしてみよう。
```output
1
2
3
4
5
```
:::
::: s
```python
for i in range(1, 11):
    if i == 6:
        break
    print(i)
```
:::

::: t
`for` で 1から5まで表示するけれど、`2` のときだけ `continue` で飛ばしてみよう。
```output
1
3
4
5
```
:::
::: s
```python
for i in range(1, 6):
    if i == 2:
        continue
    print(i)
```
:::

::: t
`for` で 1から20までを調べて、最初に見つかった `7` の倍数を表示して、終わるプログラムを書いてみよう。
```output
7
```
:::
::: s
```python
for i in range(1, 21):
    if i % 7 == 0:
        print(i)
        break
```
:::

@@ task:indent
::: t
次のように表示されるように、`for` の中と外に `print` を書いてみよう。（`A` は2回、`B` は1回）
```output
A
A
B
```
:::
::: s
```python
for i in range(2):
    print("A")
print("B")
```
`print("B")` は、インデントを下げないので、繰り返しの外です。
:::

::: t
次のように表示されるように、`for` の中に `print` を2つ書いてみよう。
```output
A
B
A
B
```
:::
::: s
```python
for i in range(2):
    print("A")
    print("B")
```
:::

::: t
`for` の中の `print` からインデントを消して実行してみよう。どんなエラーになる？
:::
::: s
```python error
for i in range(2):
print("A")
```
`IndentationError` になります。繰り返したい行は、4つ分右にずらします。
:::

@@ task:infinite-loop
::: t
`n = 1` から始めて、1、2、3 と表示して終わる `while` を、無限ループにならないように書いてみよう。
```output
1
2
3
```
:::
::: s
```python
n = 1
while n <= 3:
    print(n)
    n += 1
```
`n += 1` を忘れると、`n` が変わらず、ずっと続きます。
:::

::: t
`count = 3` から、1ずつ減らして `3 2 1` と表示して終わる `while` を書いてみよう。
```output
3
2
1
```
:::
::: s
```python
count = 3
while count > 0:
    print(count)
    count -= 1
```
:::

::: t
「やめる」と入力すると終わる、わざとの無限ループ（`while True`）を書いてみよう。
:::
::: s
```python in=a|やめる
while True:
    moji = input("やめる で終了：")
    if moji == "やめる":
        break
```
わざとの無限ループは、`break` で止めるしくみを必ず入れます。
:::
