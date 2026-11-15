@@ ch5
title: 関数
kind: chapter
chapter: 5
summary: 処理に名前をつけて、何度でも呼び出せるようにする「関数」を作ります。
reads: def=デフ | return=リターン
--
## この章のゴール
`print()` や `input()` は、Pythonが最初から用意してくれている関数でした。この章では、自分で関数を作ります。

- [[function]]：処理に名前をつけてまとめる
- [[argument]]：関数に値を渡す
- [[return]]：関数から結果を受け取る
- [[scope]]：変数が使える範囲

## 関数をつくって、呼び出す
```python
def hello():
    print("こんにちは！")

hello()
hello()
```
`def` で作って、名前を書いて呼び出します。同じ処理を何度でも使えます。

::: scratch
関数は、Scratchの「ブロックを作る」（ブロック定義）と同じです。「定義 hello」の下につなげたブロックが、`def hello():` の下のインデントした行にあたります。作ったブロックを置くと動いたように、Pythonでは `hello()` と書くと動きます。
:::

## 引数：値を渡す
```python
def hello(name):
    print(name + "さん、こんにちは！")

hello("はなこ")
hello("たろう")
```
かっこの中の `name` は、呼び出すときに値を受け取る入れ物です。

## 戻り値：結果を返す
```python
def zeikomi(nedan):
    return int(nedan * 1.1)

print(zeikomi(1000))
```
`return` で、計算の結果を呼び出した場所に返します。

## 関数の中で、if や for を使う
```python
def hantei(score):
    if score >= 60:
        return "合格"
    else:
        return "不合格"

print(hantei(75))
print(hantei(40))
```
関数の中でも、[[if]]や[[for]]は同じように書けます。インデントが1段深くなるので注意してください（[[indent]]）。

::: point
作って終わりではなく、**呼び出して**はじめて動きます。
:::

## やってみよう
::: try 足し算の関数
2つの数を受け取って、足した結果を返す関数 `add` を作りましょう。
:::
::: answer
```python
def add(a, b):
    return a + b

print(add(3, 4))
```
:::

::: try 偶数かどうかを返す関数
数を受け取って、偶数なら `True`、そうでなければ `False` を返す関数 `guusuu_ka` を作りましょう。
:::
::: answer
```python
def guusuu_ka(n):
    return n % 2 == 0

print(guusuu_ka(4))
print(guusuu_ka(7))
```
`n % 2 == 0` は、そのまま[[bool]]なので、`if` なしで返せます。
:::

@@ function
title: 関数
type: 構文
chapter: 5
syntax: def 関数名(引数):
summary: 処理に名前をつけてまとめたものです。名前を書くだけで、何度でも使えます。
reads: def=デフ | return=リターン | print=プリント
--
## 書き方のかたち
::: tpl 関数の作り方
def 〔関数名〕(〔引数〕):
····〔関数の中の処理〕
····return 〔戻り値〕

| 〔関数名〕 | 自分でつける名前。あとで呼び出すときに使う |
| 〔引数〕 | 外から受け取る値の名前（なければ空っぽでOK） |
| 〔戻り値〕 | 呼び出した場所に返す答え（return は書かなくてもOK） |
:::

::: tpl 関数の使い方（呼び出し）
〔関数名〕(〔渡す値〕)

| 〔渡す値〕 | 引数に入る値。関数を作った順番どおりに書く |
:::

::: flow function 関数は「入れると出てくる」しくみ
:::

## 関数とは
`print()` も `input()` も関数です。自分で作るときは、`def` を使います。

::: scratch
Scratchの「ブロックを作る」で作った自分だけのブロックが、Pythonの関数です。`def` の行が「定義」ブロック、`return` は Scratch にはない「答えを返す」しくみです（[[return]]）。
:::

```python
def hello():
    print("こんにちは！")
    print("今日もがんばろう")

hello()
```
- `def`：関数を作る合図
- `hello`：関数の名前（自由につけられる）
- `()`：[[argument]]を書く場所（なくてもいい）
- `:` と[[indent]]：関数の中身

## 呼び出す
関数の名前に `()` をつけて書くと、中身が実行されます。作っただけでは、何も起きません。

```python
def hello():
    print("こんにちは！")
```
このプログラムを実行しても、何も表示されません。`hello` を作っただけで、まだ呼び出していないからです。最後に `hello()` の1行を足すと、`こんにちは！` と表示されます。
## なぜ関数を作るの？
- 同じ処理を、1か所にまとめられる
- 直すときも、1か所だけ直せばいい
- 名前をつけると、何をしているか分かりやすい

## 関数の中の処理
関数の中では、[[if]]や[[for]]も使えます。

```python
def count_down(n):
    for i in range(n, 0, -1):
        print(i)
    print("スタート！")

count_down(3)
```

## 順番に注意
関数は、**呼び出す前に作っておく**必要があります。

```python error
hello()

def hello():
    print("こんにちは")
```

@@ argument
title: 引数
type: 構文
chapter: 5
syntax: 関数名(値)
summary: 関数に渡す値です。関数のかっこの中に書きます。
reads: def=デフ | name=ネーム
--
## 書き方のかたち
::: tpl 引数のかたち
def 〔関数名〕(〔引数1〕, 〔引数2〕):
····〔処理〕

〔関数名〕(〔値1〕, 〔値2〕)

| 〔引数1〕 | 関数を作るときの、受け取り口の名前 |
| 〔値1〕 | 関数を呼ぶときに、渡す中身。〔引数1〕に入る |
:::

## 引数とは
関数に、材料として渡す値です。

```python
def aisatsu(name, kaisuu):
    for i in range(kaisuu):
        print("こんにちは、" + name)

aisatsu("はなこ", 2)
```
`aisatsu("はなこ", 2)` と呼び出すと、`name` に `"はなこ"`、`kaisuu` に `2` が入ります。書いた順番どおりに入ります。Scratchの「ブロックを作る」で「引数を追加」したのと同じしくみです。

## 2種類の呼び方
- 作る側（`def` の行）の名前：仮引数
- 呼び出す側に渡す値：実引数

どちらも、まとめて「引数」と呼ぶことが多いです。

## 初期値をつける
```python
def aisatsu(name="ゲスト"):
    print("こんにちは、" + name + "さん")

aisatsu()
aisatsu("はなこ")
```
値が渡されなかったときは、`=` のあとの初期値が使われます。

::: deep 名前を指定して渡す
順番を気にせず、名前をつけて渡すこともできます。

```python
def aisatsu(name, kaisuu):
    for i in range(kaisuu):
        print("こんにちは、" + name)

aisatsu(kaisuu=2, name="たろう")
```
:::

::: stuck
引数の数が合わないと、[[error]]になります。

```python error
def aisatsu(name, kaisuu):
    print(name * kaisuu)

aisatsu("はなこ")
```
2つ必要なのに、1つしか渡していません。
:::

@@ return
title: 戻り値（return）
type: 構文
chapter: 5
syntax: return 値
summary: 関数が計算した結果を、呼び出した場所に返す仕組みです。
reads: return=リターン | None=ナン | print=プリント
--
## 書き方のかたち
::: tpl return の書き方
def 〔関数名〕(〔引数〕):
····return 〔返したいもの〕

〔変数〕 = 〔関数名〕(〔値〕)

| 〔返したいもの〕 | 計算の答えなど。return で関数は終わる |
| 〔変数〕 | 返ってきた答えを受け取る入れ物 |
:::

## 結果を受け取る
```python
def add(a, b):
    return a + b

x = add(3, 4)
print(x * 2)
```
`add(3, 4)` の結果の `7` が `x` に入ります（[[variable]]）。`return` は、**関数の結果を返す**ためのものです。

## print と return のちがい
```python
def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

x = add_return(3, 4)
y = add_print(3, 4)
print(x, y)
```
`add_print` は、画面に表示するだけで、結果は返しません。返すものがないときは `None`（何もない）になります。計算結果をあとで使いたいなら、`return` を使います。

## return で関数は終わる
```python
def check(n):
    if n < 0:
        return "マイナス"
    return "0以上"

print(check(-5))
print(check(5))
```
`return` が実行されると、そこで関数が終わります。そのあとの行は実行されません。

::: deep 2つの値を返す
```python
def saisho_saidai(kazu_list):
    return min(kazu_list), max(kazu_list)

saisho, saidai = saisho_saidai([3, 1, 2])
print(saisho, saidai)
```
:::

@@ scope
title: スコープ（変数の有効範囲）
type: 考え方
chapter: 5
summary: 変数が使える範囲のことです。関数の中で作った変数は、関数の外では使えません。
reads: def=デフ | return=リターン
--
## 関数の中の変数は、外から見えない
```python error
def tsukuru():
    himitsu = 42

tsukuru()
print(himitsu)
```
`himitsu` は、`tsukuru` の中だけで使える[[variable]]です。関数が終わると、消えてしまいます（[[error]]）。

## 名前が同じでも、別のもの
```python
x = 10

def kaeru():
    x = 99
    print("中:", x)

kaeru()
print("外:", x)
```
関数の中の `x` と、外の `x` は、名前が同じでも別の変数です。

## 外の変数を読むことはできる
```python
zeiritsu = 1.1

def zeikomi(nedan):
    return int(nedan * zeiritsu)

print(zeikomi(1000))
```

::: point
関数の中で出した結果を外で使いたいときは、[[return]]で返します。
:::

::: deep 関数の中から、外の変数を書き換えたいときは？
`global 変数名` と書くと、関数の中から外の変数を書き換えられます。7章のPyxelでは、`update` の中で位置や点数を変えるために、この `global` をよく使います（[[update-draw]]）。
:::
