@@ task:ch5
::: t
「こんにちは！」と表示する関数 `hello` を作って、2回呼び出してみよう。
```output
こんにちは！
こんにちは！
```
:::
::: s
```python
def hello():
    print("こんにちは！")

hello()
hello()
```
:::

::: t
2つの数を足した答えを返す関数 `add` を作って、`add(3, 4)` の答えを表示してみよう。
```output
7
```
:::
::: s
```python
def add(a, b):
    return a + b

print(add(3, 4))
```
:::

::: t
数を受け取って、偶数なら `True`、奇数なら `False` を返す関数 `guusuu_ka` を作って、`4` と `7` で試してみよう。
```output
True
False
```
:::
::: s
```python
def guusuu_ka(n):
    return n % 2 == 0

print(guusuu_ka(4))
print(guusuu_ka(7))
```
:::

::: c
合計金額と人数を受け取って、1人いくら払えばいいかを返す関数 `warikan` を作ろう。1円より細かくは分けられないので、割り切れないときは切り捨てます。`warikan(1000, 3)` を表示しよう。
```output
333
```
:::
::: s
```python
def warikan(goukei, ninzuu):
    return goukei // ninzuu


print(warikan(1000, 3))
```
`//` を使うと、割り算の答えが整数になります。あまった1円は、だれかが多めに払いましょう。
:::

@@ task:function
::: t
「今日もがんばろう」と表示する関数 `ganbaro` を作って、呼び出してみよう。
```output
今日もがんばろう
```
:::
::: s
```python
def ganbaro():
    print("今日もがんばろう")

ganbaro()
```
作っただけでは動きません。`ganbaro()` と呼び出して、はじめて動きます。
:::

::: t
名前を受け取って、「○○さん、こんにちは！」と表示する関数 `hello` を作って、`"はなこ"` と `"たろう"` で呼び出してみよう。
```output
はなこさん、こんにちは！
たろうさん、こんにちは！
```
:::
::: s
```python
def hello(name):
    print(name + "さん、こんにちは！")

hello("はなこ")
hello("たろう")
```
:::

::: t
数を受け取って、その数を2倍した答えを返す関数 `double` を作って、`double(21)` を表示してみよう。
```output
42
```
:::
::: s
```python
def double(n):
    return n * 2

print(double(21))
```
:::

@@ task:argument
::: t
文字を受け取って、その文字を3回繰り返して表示する関数 `sankai_hyouji` を作ってみよう。`sankai_hyouji("ha")` を呼び出すと `hahaha` と出る。
```output
hahaha
```
:::
::: s
```python
def sankai_hyouji(word):
    print(word * 3)

sankai_hyouji("ha")
```
:::

::: t
2つの数を受け取って、かけ算の答えを返す関数 `kakezan` を作って、`kakezan(6, 7)` を表示してみよう。
```output
42
```
:::
::: s
```python
def kakezan(a, b):
    return a * b

print(kakezan(6, 7))
```
:::

::: t
名前を受け取る関数 `aisatsu` を作ろう。名前を書かなかったときは「ゲスト」になるように、初期値を使ってみよう。
```output
こんにちは、ゲストさん
こんにちは、はなこさん
```
:::
::: s
```python
def aisatsu(name="ゲスト"):
    print("こんにちは、" + name + "さん")

aisatsu()
aisatsu("はなこ")
```
:::

@@ task:return
::: t
数を受け取って、その数に1を足して返す関数 `plus1` を作って、`plus1(9)` を表示してみよう。
```output
10
```
:::
::: s
```python
def plus1(n):
    return n + 1

print(plus1(9))
```
:::

::: t
点数を受け取って、60点以上なら「合格」、そうでなければ「不合格」を返す関数 `hantei` を作って、`75` と `40` で試してみよう。
```output
合格
不合格
```
:::
::: s
```python
def hantei(score):
    if score >= 60:
        return "合格"
    else:
        return "不合格"

print(hantei(75))
print(hantei(40))
```
:::

::: t
2つの数の「小さいほうと大きいほう」を一度に返す関数 `saisho_saidai` を作って、`3` と `8` で試してみよう。
```output
3 8
```
:::
::: s
```python
def saisho_saidai(a, b):
    return min(a, b), max(a, b)

saisho, saidai = saisho_saidai(3, 8)
print(saisho, saidai)
```
`return` にカンマで2つ並べると、2つ同時に返せます。
:::

@@ task:scope
::: t
関数の中で作った変数を、関数の外で使うとどうなるか試してみよう。エラーの名前は？
:::
::: s
```python error
def tsukuru():
    himitsu = 42

tsukuru()
print(himitsu)
```
`NameError` になります。関数の中の変数は、外から見えません。
:::

::: t
外の `x = 10` と、関数の中の `x = 99` が、別の変数になることを確かめてみよう。
```output
中: 99
外: 10
```
:::
::: s
```python
x = 10

def kaeru():
    x = 99
    print("中:", x)

kaeru()
print("外:", x)
```
:::

::: t
関数の中で計算した答えを、外で使えるように `return` で返して、変数 `kekka` に受け取って表示してみよう。（`3 * 4` の答え）
```output
12
```
:::
::: s
```python
def tsukuru():
    himitsu = 3 * 4
    return himitsu

kekka = tsukuru()
print(kekka)
```
:::
