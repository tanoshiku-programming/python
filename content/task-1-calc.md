@@ task:ch1
::: t
画面に「はじめまして」と表示するプログラムを書いてみよう。
```output
はじめまして
```
:::
::: s
```python
print("はじめまして")
```
:::

::: t
名前を聞いて、「○○さん、ようこそ！」と表示するプログラムを書いてみよう。（はなこ と入力したら「はなこさん、ようこそ！」）
:::
::: s
```python in=はなこ
name = input("名前は？")
print(name + "さん、ようこそ！")
```
:::

::: t
2つの数を聞いて、足した答えを表示するプログラムを書いてみよう。（3 と 4 なら `7`）
:::
::: s
```python in=3|4
a = int(input("1つ目の数は？"))
b = int(input("2つ目の数は？"))
print(a + b)
```
:::

::: c
1000円で、1個 `nedan` 円のおかしを、買えるだけ買います。値段を聞いて、「〇個買えて、〇円余ります」と表示しよう。（ヒント：`//` と `%`）
```output
値段は？{{120}}
8個買えて、40円あまります
```
:::
::: s
```python in=120
nedan = int(input("値段は？"))
kosuu = 1000 // nedan
amari = 1000 % nedan
print(f"{kosuu}個買えて、{amari}円あまります")
```
`//` で「何個買えるか（商）」、`%` で「いくらあまるか（余り）」が分かります（[[operator]]）。
:::

@@ task:print
::: t
画面に「こんにちは」と表示するプログラムを書いてみよう。
```output
こんにちは
```
:::
::: s
```python
print("こんにちは")
```
:::

::: t
`print` を2回使って、次のように2行で表示してみよう。
```output
Python
たのしい！
```
:::
::: s
```python
print("Python")
print("たのしい！")
```
:::

::: t
1つの `print` に、`"年齢："` と `12` をカンマで区切って並べて、次のように表示してみよう。
```output
年齢： 12
```
:::
::: s
```python
print("年齢：", 12)
```
カンマで区切ると、間に空白が入ります。
:::

@@ task:input
::: t
「好きな食べ物は？」と聞いて、入力した食べ物をそのまま表示するプログラムを書いてみよう。
:::
::: s
```python in=カレー
tabemono = input("好きな食べ物は？")
print(tabemono)
```
:::

::: t
名前を聞いて、「こんにちは、○○さん」と表示してみよう。
:::
::: s
```python in=たろう
name = input("名前は？")
print("こんにちは、" + name + "さん")
```
:::

::: t
数を1つ聞いて、その数の2倍を表示してみよう。（`int()` を使うよ）
:::
::: s
```python in=21
n = int(input("数は？"))
print(n * 2)
```
`input()` の結果は文字なので、`int()` で数に変えてから計算します。
:::

@@ task:str
::: t
「Python」という文字を変数 `word` に入れて、表示してみよう。
```output
Python
```
:::
::: s
```python
word = "Python"
print(word)
```
:::

::: t
`"ha"` を3回繰り返した文字 `hahaha` を、かけ算を使って表示してみよう。
```output
hahaha
```
:::
::: s
```python
print("ha" * 3)
```
:::

::: t
`word = "Python"` の、いちばん最初の文字 `P` と、文字数 `6` を表示してみよう。
```output
P
6
```
:::
::: s
```python
word = "Python"
print(word[0])
print(len(word))
```
:::

@@ task:int
::: t
`10 + 3`、`10 - 3`、`10 * 3` の答えを、3行で表示してみよう。
```output
13
7
30
```
:::
::: s
```python
print(10 + 3)
print(10 - 3)
print(10 * 3)
```
:::

::: t
`"42"`（文字）を `int()` で整数に変えて、1を足した答えを表示してみよう。
```output
43
```
:::
::: s
```python
print(int("42") + 1)
```
:::

::: t
`type()` を使って、`100` のデータ型を表示してみよう。（`<class 'int'>` と出ればOK）
```output
<class 'int'>
```
:::
::: s
```python
print(type(100))
```
:::

@@ task:float
::: t
`2.5` に `2` をかけた答えを表示してみよう。
```output
5.0
```
:::
::: s
```python
print(2.5 * 2)
```
小数がまざった計算は、答えも小数になります。
:::

::: t
`10 ÷ 4` の答えを表示してみよう。
```output
2.5
```
:::
::: s
```python
print(10 / 4)
```
:::

::: t
`3.14159` を、`round()` で小数第2位までに丸めて表示してみよう。
```output
3.14
```
:::
::: s
```python
print(round(3.14159, 2))
```
:::

@@ task:datatype
::: t
`10`、`"10"`、`1.5` の3つのデータ型を、`type()` で調べて表示してみよう。
```output
<class 'int'>
<class 'str'>
<class 'float'>
```
:::
::: s
```python
print(type(10))
print(type("10"))
print(type(1.5))
```
:::

::: t
`10 + 5` と `"10" + "5"` を表示して、答えのちがいを見てみよう。
```output
15
105
```
:::
::: s
```python
print(10 + 5)
print("10" + "5")
```
数どうしは足し算、文字どうしはつなげるだけです。
:::

::: t
`True` と `[1, 2, 3]` のデータ型を、`type()` で調べて表示してみよう。
```output
<class 'bool'>
<class 'list'>
```
:::
::: s
```python
print(type(True))
print(type([1, 2, 3]))
```
:::

@@ task:operator
::: t
`17 ÷ 5` の商（整数部分）と余りを、2行で表示してみよう。
```output
3
2
```
:::
::: s
```python
print(17 // 5)
print(17 % 5)
```
:::

::: t
`2` の 8乗 を表示してみよう。
```output
256
```
:::
::: s
```python
print(2 ** 8)
```
:::

::: t
数を1つ聞いて、それが偶数なら `True`、奇数なら `False` と表示してみよう。（ヒント：2で割った余り）
:::
::: s
```python in=7
n = int(input("数は？"))
print(n % 2 == 0)
```
2で割った余りが 0 なら偶数です。
:::

@@ task:typeconv
::: t
文字の `"365"` を整数に変えて、2倍した答えを表示してみよう。
```output
730
```
:::
::: s
```python
print(int("365") * 2)
```
:::

::: t
整数の `12` を文字に変えて、`"円"` とつなげて表示してみよう。
```output
12円
```
:::
::: s
```python
print(str(12) + "円")
```
:::

::: t
小数の入力を受け取って（`float()`）、その2倍を表示してみよう。
:::
::: s
```python in=1.5
x = float(input("小数を入力："))
print(x * 2)
```
:::

@@ task:fstring
::: t
`name = "はなこ"`、`nenrei = 12` を使って、「はなこさんは12才です」と、f文字列で表示してみよう。
```output
はなこさんは12才です
```
:::
::: s
```python
name = "はなこ"
nenrei = 12
print(f"{name}さんは{nenrei}才です")
```
:::

::: t
値段 `nedan = 120` と個数 `count = 3` から、「合計は360円です」と表示してみよう。（`{ }` の中で計算できるよ）
```output
合計は360円です
```
:::
::: s
```python
nedan = 120
count = 3
print(f"合計は{nedan * count}円です")
```
:::

::: t
`x = 3.14159` を、小数第2位まで（`:.2f`）で、f文字列で表示してみよう。
```output
3.14
```
:::
::: s
```python
x = 3.14159
print(f"{x:.2f}")
```
:::

@@ task:comment
::: t
`print("A")` の上の行に、「Aを表示する」というコメントを書いてみよう。（実行結果は `A`）
```output
A
```
:::
::: s
```python
# Aを表示する
print("A")
```
:::

::: t
`print("B")` と `print("C")` の2行のうち、`B` のほうだけをコメントにして、実行されないようにしてみよう。
```output
C
```
:::
::: s
```python
# print("B")
print("C")
```
:::

::: t
`print("こんにちは")` と同じ行の右はしに、「あいさつ」というコメントをつけてみよう。
```output
こんにちは
```
:::
::: s
```python
print("こんにちは")  # あいさつ
```
:::

@@ task:error
::: t
わざと `print(nmae)` と書いて、エラーメッセージを読んでみよう。どんなエラーの名前が出る？
:::
::: s
```python error
print(nmae)
```
`NameError` は「そんな名前は知らない」というエラーです。打ち間違いが多い原因です。
:::

::: t
`print(10 / 0)` を実行して、エラーの名前を確かめてみよう。
:::
::: s
```python error
print(10 / 0)
```
`ZeroDivisionError`（ゼロで割った）です。0でわり算はできません。
:::

::: t
`print("こんにちは)` のように `"` を1つ閉じ忘れて実行してみよう。出たエラーを読んで、直してみよう。
```output
こんにちは
```
:::
::: s
```python
print("こんにちは")
```
`"` は、始まりと終わりの2つが必要です。エラーの行番号を見て、その行を見直しましょう。
:::

@@ task:math-func
::: t
`-12` の絶対値を表示しよう。
```output
12
```
:::
::: s
```python
print(abs(-12))
```
:::

::: t
3人の点数 `72`、`95`、`88` の、いちばん高い点といちばん低い点を、1行に並べて表示しよう。
```output
95 72
```
:::
::: s
```python
print(max(72, 95, 88), min(72, 95, 88))
```
:::

::: t
朝の気温 `kion_asa = 8` と、昼の気温 `kion_hiru = 17` の差を、`abs` を使って表示しよう。
```output
9
```
:::
::: s
```python
kion_asa = 8
kion_hiru = 17
print(abs(kion_asa - kion_hiru))
```
引く順番が逆でも、`abs` を使えば答えは同じです。
:::
