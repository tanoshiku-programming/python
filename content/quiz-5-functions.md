@@ quiz:ch5
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
def hello():
    print("こんにちは！")

hello()
hello()
```
:::
::: a
関数は、呼び出すたびに中身が実行されます。2回呼び出したので、2回表示されます。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
def add(a, b):
    return a + b

print(add(3, 4))
```
:::
::: a
`return` が、計算結果の `7` を返します。
:::

::: q
関数を作るときに、最初に書く言葉は？
:::
::: a
`def` です。
:::

@@ quiz:function
::: q
関数を作るときに、最初に書く言葉は？
:::
::: a
`def` です。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
def hello():
    print("こんにちは！")
```
:::
::: a
何も表示されません。関数は、作っただけでは動きません。`hello()` と**呼び出して**はじめて動きます。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
def count_down(n):
    for i in range(n, 0, -1):
        print(i)
    print("スタート！")

count_down(3)
```
:::
::: a
関数の中でも、`for` が使えます。`range(3, 0, -1)` は、3から1までを、1ずつ減らします。
:::

@@ quiz:argument
::: q
引数とは何？
:::
::: a
関数に渡す値です。関数のかっこの中に書きます。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
def aisatsu(name="ゲスト"):
    print("こんにちは、" + name + "さん")

aisatsu()
aisatsu("はなこ")
```
:::
::: a
値が渡されなかったときは、`=` のあとの初期値（`"ゲスト"`）が使われます。
:::

::: q
次のプログラムを実行すると、どうなる？
```python hideout error
def aisatsu(name, kaisuu):
    print(name * kaisuu)

aisatsu("はなこ")
```
:::
::: a
エラー（`TypeError`）になります。引数が2つ必要なのに、1つしか渡していません。
:::

@@ quiz:return
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
def add(a, b):
    return a + b

x = add(3, 4)
print(x * 2)
```
:::
::: a
`add(3, 4)` の結果の `7` が `x` に入るので、`7 * 2` で `14` です。
:::

::: q
`print` と `return` のちがいを、ひとことで説明しよう。
:::
::: a
`print` は画面に表示するだけです。`return` は、結果を呼び出した場所に返します。計算結果をあとで使いたいときは `return` を使います。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
def check(n):
    if n < 0:
        return "マイナス"
    return "0以上"

print(check(-5))
print(check(5))
```
:::
::: a
`return` が実行されると、そこで関数が終わります。`-5` のときは、最初の `return` で終わります。
:::

@@ quiz:scope
::: q
次のプログラムを実行すると、どうなる？
```python hideout error
def tsukuru():
    himitsu = 42

tsukuru()
print(himitsu)
```
:::
::: a
`NameError` になります。関数の中で作った変数は、関数の外では使えません。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
x = 10

def kaeru():
    x = 99
    print("中:", x)

kaeru()
print("外:", x)
```
:::
::: a
関数の中の `x` と外の `x` は、名前が同じでも別の変数です。だから、外の `x` は `10` のままです。
:::

::: q
関数の中で出した結果を、関数の外で使いたいときは、何を使う？
:::
::: a
`return` です。
:::

@@ quiz:pass
::: q
`pass` は、どんな意味の命令？
:::
::: a
「**何もしない**」という意味です。中身を書かなければいけない場所を、空っぽのままにしておくときに使います。
:::

::: q
次のプログラムはエラーになる。`update` の中に何を書けば、エラーにならない？
```python norun
def update():

print("おわり")
```
:::
::: a
`pass` です。`:` の次の行には、インデントした中身が必ずいるので、`pass` を入れておきます。
:::

@@ quiz:none
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
def hello():
    print("やあ")


kekka = hello()
print(kekka)
```
:::
::: a
`hello` が「やあ」と表示したあと、`return` がないので、答えは `None` になります。
:::

::: q
変数 `x` が `None` かどうかを調べる `if` 文は？
:::
::: a
`if x is None:` です。
:::
