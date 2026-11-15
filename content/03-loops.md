@@ ch3
title: 繰り返し
kind: chapter
chapter: 3
summary: 同じことを何回もするときに使う、for文とwhile文を学びます。
reads: for=フォー | in=イン | while=ホワイル | range=レンジ | break=ブレーク | continue=コンティニュー
--
## この章のゴール
「同じことを100回やりたい」ときに、`print` を100行書くのは大変です。繰り返しを使えば、短く書けます。

- [[for]]文：回数や、リストの中身の数だけ繰り返す
- [[while]]文：条件が続くあいだ繰り返す

## for：回数を決めて繰り返す
```python
for i in range(3):
    print("こんにちは")
```
`range(3)` は「3回」という意味です（[[range]]）。`print` の前が空いているのは[[indent]]で、「繰り返したい処理」を表します。

::: scratch
`for i in range(3):` は、Scratchの「（3）回繰り返す」ブロックです。Scratchではブロックの「口」の中に入れたものが繰り返されました。Pythonでは、**行の頭を下げた（インデントした）行**が「口の中」になります。
:::

## for：リストの中身を順番に
```python
for name in ["はなこ", "たろう"]:
    print(name + "さん")
```

## while：条件が続くあいだ繰り返す
```python
count = 3
while count > 0:
    print(count)
    count -= 1
print("スタート！")
```
`count > 0` が `True` のあいだ、繰り返します。`count -= 1` を忘れると、永遠に終わりません（[[infinite-loop]]）。

::: scratch
Scratchの「（〇〇）まで繰り返す」は、条件が**True になったらやめる**ブロックでした。Pythonの `while` は、条件が **True のあいだ続ける**ので、**条件が反対**になります。Scratchで「（count = 0）まで繰り返す」と書いていたものは、Pythonでは `while count != 0:`（または `while count > 0:`）です。
:::

## どちらを使う？
| 場面 | 使うもの |
| --- | --- |
| 回数が決まっている | `for` |
| リストの中身を順番に使う | `for` |
| いつ終わるか分からない | `while` |

::: point
途中でやめたいときは [[break]] を使います。
:::

## やってみよう
::: try 1から10までの合計
`for` を使って、1から10までの合計を表示しましょう。
:::
::: answer
```python
total = 0
for i in range(1, 11):
    total += i
print(total)
```
`range(1, 11)` は、1から10までです。終わりの数は含まれません。
:::

::: try 7のだん
九九の7のだんを表示しましょう。
:::
::: answer
```python
for i in range(1, 10):
    print(f"7 × {i} = {7 * i}")
```
:::

@@ for
title: for文
type: 構文
chapter: 3
syntax: for 変数 in 並び:
summary: 回数や、リストの中身の数だけ、同じ処理を繰り返す文です。
reads: for=フォー | in=イン | range=レンジ
--
## 書き方のかたち
::: tpl for文の書き方
for 〔変数〕 in 〔繰り返す材料〕:
····〔繰り返す処理〕

| 〔変数〕 | 1回ごとに、材料の中身が1つずつ入る名前 |
| 〔繰り返す材料〕 | リストや range(3) など。中身がなくなるまで繰り返す |
| 〔繰り返す処理〕 | 繰り返したいこと。何行でもOK |
:::

::: flow for for文の流れ
:::

## 書き方
```python
for i in range(3):
    print(i)
```
`for 変数 in 並び:` のあとに、繰り返したい処理を[[indent]]を下げて書きます。Scratchの「（3）回繰り返す」と同じですが、Pythonでは今が何回目かが `i` に入るところがちがいます。`i` には、1回ごとに `0`、`1`、`2` と順番に入ります（[[range]]、[[variable]]）。

## リストの中身を順番に
```python
kudamono_list = ["りんご", "みかん", "バナナ"]
for kudamono in kudamono_list:
    print(kudamono)
```
[[list]]の中身が、1つずつ `kudamono` に入ります。

## 文字を1つずつ
```python
for moji in "ABC":
    print(moji)
```

## 計算結果をためていく
```python
total = 0
for n in [10, 20, 30]:
    total += n
print(total)
```
最初に `total = 0` を作っておいて、繰り返すたびに足していきます。ループのあとの `print` は、インデントが下がっていないので、最後に1回だけ実行されます。

::: deep for の中に for（二重ループ）
```python
for a in range(1, 4):
    for b in range(1, 4):
        print(a * b, end=" ")
    print()
```
外側の `a` が1つ進むたびに、内側の `b` が最初から最後まで回ります。表のように並べたいときに使います。
:::

::: stuck
- 行の終わりの `:` を忘れない
- 次の行のインデントを忘れない（[[error]]になります）
- 途中で止めたいときは[[break]]
:::

@@ while
title: while文
type: 構文
chapter: 3
syntax: while 条件:
summary: 条件が True のあいだ、処理を繰り返す文です。
reads: while=ホワイル | True=トゥルー | False=フォールス
--
## 書き方のかたち
::: tpl while文の書き方
while 〔条件〕:
····〔繰り返す処理〕

| 〔条件〕 | True のあいだ、繰り返す。False になったら終わり |
| 〔繰り返す処理〕 | 条件に関わる変数を変える行（count -= 1 など）も入れる |
:::

::: flow while while文の流れ
:::

## 書き方
```python
n = 1
while n <= 3:
    print(n)
    n += 1
```
動く順番は次のとおりです。
1. 条件（`n <= 3`）を調べる
2. `True` なら、[[indent]]を下げた処理を実行する
3. 1に戻る
4. `False` になったら、ループを終わる

条件には[[comparison]]を使います。

::: scratch
Scratchの「（〇〇）まで繰り返す」は「条件が True になったら**やめる**」、Pythonの `while` は「条件が True のあいだ**続ける**」です。条件が反対になるので注意しよう。Scratchの「（n > 3）まで繰り返す」は、Pythonでは `while n <= 3:` です。
:::

## 回数が決まっていないとき
入力された数を、0が入力されるまで足していきます。何回入力されるか、最初は分かりません。

```python in=5|3|0
total = 0
n = int(input("数を入力（0で終了）："))
while n != 0:
    total += n
    n = int(input("数を入力（0で終了）："))
print("合計は", total)
```

::: stuck
条件がずっと `True` のままだと、終わらなくなります。[[infinite-loop]]を見てください。
:::

@@ range
title: range関数
type: 関数
chapter: 3
syntax: range(終わり) / range(始め, 終わり) / range(始め, 終わり, 増え方)
summary: 0, 1, 2… のような、連続した数のならびを作る関数です。for文とよく使います。
reads: range=レンジ | list=リスト
--
## 書き方のかたち
::: tpl range の3つの形
range(〔終わり〕)
range(〔始め〕, 〔終わり〕)
range(〔始め〕, 〔終わり〕, 〔増え方〕)

| 〔始め〕 | 最初の数（書かなければ 0） |
| 〔終わり〕 | ここまで。この数は含まれない |
| 〔増え方〕 | 1回ごとに増える数（書かなければ 1） |
:::

## 3つの書き方
`list()` で包むと、中身を見られます（[[list]]）。

```python
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(0, 10, 2)))
print(list(range(5, 0, -1)))
```
| 書き方 | 意味 |
| --- | --- |
| `range(5)` | 0から4まで（5個） |
| `range(1, 6)` | 1から5まで |
| `range(0, 10, 2)` | 0から10の手前まで、2ずつ |
| `range(5, 0, -1)` | 5から1まで、1ずつ減らす |

## for文と一緒に使う
```python
for i in range(3):
    print(i)
```

::: stuck
**終わりの数は、含まれません。** `range(1, 10)` は1から9までです。1から10までにしたいときは `range(1, 11)` です。
:::

@@ break
title: break と continue
type: 構文
chapter: 3
syntax: break / continue
summary: break はループを途中で終わらせ、continue は今回の分だけ飛ばして次に進みます。
reads: break=ブレーク | continue=コンティニュー
--
## break：そこで終わる
```python
for i in range(1, 10):
    if i == 4:
        break
    print(i)
```
`i` が `4` になったところで、ループ全体が終わります。条件は[[if]]で書きます。

## continue：今回だけ飛ばす
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```
`i` が `3` のときだけ、そのあとの `print` を飛ばして、次の回に進みます。ループは続きます。

::: point
- `break`：ループをやめる
- `continue`：今回だけやめて、次へ進む
:::

[[for]]でも[[while]]でも使えます。

@@ indent
title: インデント
type: 書き方
chapter: 3
syntax: 行の頭に半角スペース4つ
summary: 行の頭の空白のことです。Pythonでは、どこまでが同じかたまりかを表す大事なルールです。
reads: indent=インデント | for=フォー | if=イフ
--
## ルール
`:` で終わる行の次の行は、半角スペース4つ分（または Tab キー1回）下げます。同じかたまりの行は、同じ深さにそろえます。

```python
for i in range(2):
    print("A")
    print("B")
print("おわり")
```
`A` と `B` は繰り返しの中、`おわり` は繰り返しの外です。

## 位置がちがうと、動きがちがう
```python
for i in range(2):
    print("A")
print("B")
```
今度は `B` が繰り返しの外なので、1回だけ表示されます。

## インデントを忘れると
```python error
if True:
print("あ")
```
[[if]]、[[for]]、[[while]]、[[function]]の次の行では、必ずインデントが必要です（[[error]]）。

::: deep スペースと Tab を混ぜない
見た目は同じでも、スペースと Tab は別のものです。混ぜると、エラーになることがあります。多くのエディタは、Tab キーを押すとスペース4つを入れてくれます。
:::

@@ infinite-loop
title: 無限ループ
type: 考え方
chapter: 3
syntax: while True:
summary: 終わらずに、ずっと続いてしまうループです。止め方を知っておけば大丈夫です。
reads: while=ホワイル | True=トゥルー | Ctrl+C=コントロール シー
--
## 原因
[[while]]の条件が、いつまでも `True` のままだと、ループが終わりません。

```python norun
n = 1
while n <= 3:
    print(n)
```
```output
1
1
1
…（ずっと続く）
```
`n` を増やしていないので、`n <= 3` が永遠に `True` です。`n += 1` が必要です。

## 止め方
- `Ctrl` キーを押しながら `C` キーを押す
- 使っているソフトに「停止」ボタンがあれば、それを押す

## わざと使う
`while True:` は、永遠に続けたいときに書きます。Scratchの「ずっと」ブロックと同じです。やめたいところで[[break]]を使います。

```python in=りんご|やめる
while True:
    moji = input("何か入力（やめる で終了）：")
    if moji == "やめる":
        break
    print(moji + "ですね")
print("おわり")
```
