@@ ch4
title: 条件分岐
kind: chapter
chapter: 4
summary: 条件によって、実行する処理を変える if文を学びます。
reads: if=イフ | elif=エルイフ | else=エルス | and=アンド | or=オア | not=ノット
--
## この章のゴール
「18才以上なら大人、そうでなければ子ども」のように、状況によって動きを変えるのが条件分岐です。

- [[if]]：条件が合うときだけ実行する
- [[else]]：合わなかったときの処理を書く
- [[comparison]]と[[logical]]：条件の作り方


::: point この章で、自分でできるようになること
- □ `if` で、条件に合うときだけ動かせる
- □ `elif` と `else` で、3つ以上に分けられる
- □ `==` と `=` のちがいが分かる
- □ `and` と `or` で、条件をつなげられる

ゲームを作る前に、ここにあることを、**お手本を見ないで書けるように**、くりかえし練習しよう。
:::

## if と else
```python in=20
nenrei = int(input("年齢は？"))
if nenrei >= 18:
    print("大人です")
else:
    print("子どもです")
```
`nenrei >= 18` が `True`（[[bool]]）なら上の処理、`False` なら `else` の処理が動きます。

::: scratch
`if` は「もし〜なら」、`if` と `else` は「もし〜なら、でなければ」ブロックと同じです。Scratchでは、ブロックの口の中に入れたものが実行されました。Pythonでは、`:` の次の**インデントした行**が口の中です。
:::

## 3つ以上に分ける
```python in=85
score = int(input("点数："))
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")
```
上から順に調べて、最初に当てはまったところだけが実行されます。

## 条件を組み合わせる
```python
nenrei = 11
if nenrei >= 10 and nenrei <= 12:
    print("10才から12才です")
```
`and`（かつ）、`or`（または）、`not`（ではない）で、条件をつなげられます。

::: point
`if` の行の最後の `:` と、次の行の[[indent]]を忘れない。
:::

## やってみよう
::: try 偶数か奇数か
数を入力して、偶数か奇数かを表示しましょう。
:::
::: answer
```python in=7
n = int(input("数を入力："))
if n % 2 == 0:
    print("偶数です")
else:
    print("奇数です")
```
`n % 2` は2で割った余りです（[[operator]]）。
:::

::: try うるう年の判定
西暦を入力して、うるう年かどうかを表示しましょう。4で割り切れる年がうるう年ですが、100で割り切れる年は除きます。ただし、400で割り切れる年はうるう年です。
:::
::: answer
```python in=2028
seireki = int(input("西暦："))
if (seireki % 4 == 0 and seireki % 100 != 0) or seireki % 400 == 0:
    print("うるう年です")
else:
    print("うるう年ではありません")
```
第6章では、[[calendar]]を使って同じことを1行で調べます。
:::

@@ if
title: if文
type: 構文
chapter: 4
syntax: if 条件:
summary: 条件が True のときだけ、決まった処理を実行する文です。
reads: if=イフ | ===ダブルイコール
--
::: scratch
Scratchの「もし〈 〉なら」ブロックです。ブロックの口の中に入れたものが、Pythonでは `:` の次の、インデントした行になります。
:::

## 書き方のかたち
::: tpl if文の書き方
if 〔条件〕:
····〔条件が True のときの処理〕

| 〔条件〕 | True か False になる式（age >= 18 など） |
| 〔条件が True のときの処理〕 | 条件が True のときだけ実行される。False なら飛ばされる |
:::

::: flow if if文の流れ
:::

## 書き方
```python
kion = 30
if kion >= 30:
    print("暑いです")
print("おわり")
```
`if 条件:` のあとに、条件が `True` のときに実行したい処理を[[indent]]を下げて書きます。`print("おわり")` は、インデントが下がっていないので、条件に関係なく実行されます。

## 条件に合わなければ、何も起きない
```python
kion = 20
if kion >= 30:
    print("暑いです")
print("おわり")
```
`20 >= 30` は `False` なので、`暑いです` は表示されません。

## 合わなかったときの処理
[[else]]を使います。

## 条件の作り方
条件には、[[comparison]]（`>=` など）の結果の[[bool]]を使います。複数の条件は[[logical]]（`and` や `or`）でつなげます。

::: stuck
`=` と `==` はちがいます。`=` は代入（[[assignment]]）、`==` は「等しいかどうか」を調べる記号です。

```python error
x = 5
if x = 5:
    print("5です")
```
`if x == 5:` と書きます。
:::

@@ else
title: elif と else
type: 構文
chapter: 4
syntax: elif 条件: / else:
summary: if の条件に合わなかったときの処理を、elif（別の条件）と else（それ以外）で書きます。
reads: elif=エルイフ | else=エルス
--
::: scratch
`else` は、Scratchの「もし〈 〉なら、でなければ」ブロックの「でなければ」です。Scratchには `elif` にあたるブロックはありませんが、「でなければ」の中に、もう1つ「もし〜なら」を入れたのと同じです。
:::

## 書き方のかたち
::: tpl if / elif / else の書き方
if 〔条件1〕:
····〔処理A〕
elif 〔条件2〕:
····〔処理B〕
else:
····〔処理C〕

| 〔条件1〕 | 最初に調べる条件 |
| 〔条件2〕 | 条件1が False だったときに、次に調べる条件（elif は何個でも足せる） |
| 〔処理C〕 | どれも False だったときの処理（else には条件を書かない） |
:::

::: flow ifelse else があるとき：AかBの、どちらか一方
:::

::: flow elif elif があるとき：上から順に調べる
:::

## else：それ以外
```python
n = 4
if n > 5:
    print("大きい")
else:
    print("小さい")
```
`if` の条件が `False` のときだけ、`else` の処理が動きます。`else` には条件は書きません。

## elif：別の条件
```python
n = 5
if n > 5:
    print("5より大きい")
elif n == 5:
    print("ちょうど5")
else:
    print("5より小さい")
```
`elif` は「そうでなくて、もしこの条件なら」という意味です。いくつでも増やせます。

## 上から順に、最初の1つだけ
```python
score = 95
if score >= 70:
    print("B")
elif score >= 90:
    print("A")
```
`A` になってほしいのに、`B` になりました。`95` は `70` 以上なので、最初の条件に当てはまって、そこで終わるからです。**厳しい条件（90以上）を上に書く**のがコツです。

::: point
`if`・`elif`・`else` のうち、実行されるのは最大でひとつだけです。
:::

@@ comparison
title: 比較演算子
type: 演算子
chapter: 4
syntax: == != > < >= <=
summary: 2つの値を比べて、True か False にする記号です（== != > < >= <=）。
reads: ===ダブルイコール | !==ノットイコール | >==ダイナリイコール | <==ショウナリイコール
--
## 書き方のかたち
::: tpl 比べる式のかたち
〔左〕 〔記号〕 〔右〕

| 〔左〕 | 比べたいもの（数、変数、文字） |
| 〔記号〕 | ==、!=、>、<、>=、<= のどれか |
| 〔右〕 | 比べる相手。答えは True か False になる |
:::

## 比べる記号
| 記号 | 意味 | 例 | 答え |
| --- | --- | --- | --- |
| `==` | 等しい | `3 == 3` | `True` |
| `!=` | 等しくない | `3 != 4` | `True` |
| `>` | より大きい | `5 > 3` | `True` |
| `<` | より小さい | `5 < 3` | `False` |
| `>=` | 以上 | `5 >= 5` | `True` |
| `<=` | 以下 | `4 <= 3` | `False` |

答えは[[bool]]（`True` か `False`）になります。

```python
print(5 > 3)
print(5 == 6)
print("apple" == "apple")
```
文字列も比べられます。

## = と == のちがい
- `=`：右の値を左の変数に入れる（[[assignment]]）
- `==`：左右が等しいか調べる

::: scratch
Scratchでは、緑の「（ ）=（ ）」ブロックで「等しいか」を調べました。Pythonでは、それは `==`（イコール2つ）です。`=` が1つだと「入れる」（Scratchの「〇〇を〜にする」）の意味になるので、間違えないようにしよう。

また、Scratchには「以上」「以下」のブロックがありませんでしたが、Pythonには `>=`（以上）と `<=`（以下）があります。
:::

## 含まれているか調べる（in）
`in` を使うと、「リストや文字の中に、それが入っているか」を `True` か `False` で調べられます。

```python
kudamono_list = ["りんご", "みかん", "バナナ"]
print("みかん" in kudamono_list)
print("ぶどう" in kudamono_list)
print("ぶどう" not in kudamono_list)
print("ン" in "ピーマン")
```
| 書き方 | 意味 |
| --- | --- |
| `A in B` | B の中に A が入っている |
| `A not in B` | B の中に A が入っていない |

`if "みかん" in kudamono_list:` のように、[[if]]の条件にもそのまま使えます。リストの中身を `for` で1つずつ調べなくても、1行で確かめられます。

::: deep 型がちがうと等しくない
```python
print(10 == "10")
```
`10`（[[int]]）と `"10"`（[[str]]）は、[[datatype]]がちがうので `False` です。
:::

::: deep 1 <= x <= 10 と書ける
Pythonでは、算数のように範囲をつなげて書けます。

```python
x = 5
print(1 <= x <= 10)
```
:::

@@ logical
title: 論理演算子（and / or / not）
type: 演算子
chapter: 4
syntax: and / or / not
summary: 条件を組み合わせる言葉です。and は両方、or はどちらか、not は反対にします。
reads: and=アンド | or=オア | not=ノット
--
::: scratch
Scratchの「〈 〉かつ〈 〉」が `and`、「〈 〉または〈 〉」が `or`、「〈 〉ではない」が `not` です。
:::

## 書き方のかたち
::: tpl 条件をつなぐかたち
〔条件1〕 and 〔条件2〕
〔条件1〕 or 〔条件2〕
not 〔条件〕

| and | 両方 True のときだけ True |
| or | どちらか1つでも True なら True |
| not | True と False を反対にする |
:::

## 3つの言葉
| 言葉 | 意味 | 例 |
| --- | --- | --- |
| `and` | かつ（両方 True） | `nenrei >= 10 and nenrei <= 12` |
| `or` | または（どちらかが True） | `day == "土" or day == "日"` |
| `not` | ではない（反対にする） | `not raining` |

```python
nenrei = 11
print(nenrei >= 10 and nenrei <= 12)
print(nenrei < 10 or nenrei > 12)
print(not nenrei < 10)
```
それぞれ、[[comparison]]の結果の[[bool]]を組み合わせています。

::: deep 表で整理
| A | B | `A and B` | `A or B` |
| --- | --- | --- | --- |
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |
:::

## よくある間違い
日本語では「1か2なら」と言いますが、Pythonでは `x == 1 or 2` と書いてはいけません。

```python
x = 5
print(x == 1 or 2)
```
答えが `False` ではなく `2` になっています。Pythonは、これを `(x == 1) or 2` と読みます。`x == 1` は `False` なので、`or` の右側の `2` がそのまま答えになってしまうのです。しかも `if` の中では `2` は「True のなかま」として扱われるので（[[bool]]）、`x` が何であっても条件が成り立ってしまいます。

`x == 1 or x == 2` のように、それぞれに条件を書きます。[[if]]で使うときも同じです。

@@ ternary
title: 三項演算子（1行で書く if）
type: 演算子
chapter: 4
syntax: 値1 if 条件 else 値2
summary: 「条件が True なら値1、False なら値2」を、1行で書ける書き方です。どちらかの値を選んで変数に入れたいときに便利です。
aliases: 三項演算子, 条件式, 1行if, 1行のif
reads: if=イフ | else=エルス
--
## 書き方のかたち
::: tpl 三項演算子の書き方
〔変数〕 = 〔Trueのときの値〕 if 〔条件〕 else 〔Falseのときの値〕

| 〔条件〕 | True か False になる式 |
| 〔Trueのときの値〕 | 条件が True のとき、変数に入る |
| 〔Falseのときの値〕 | 条件が False のとき、変数に入る |
:::

## 4行が1行に
ふつうの[[if]]と[[else]]で書くと、こうなります。

```python
tensuu = 75
if tensuu >= 60:
    kekka = "合格"
else:
    kekka = "不合格"
print(kekka)
```
三項演算子なら、同じことが1行で書けます。

```python
tensuu = 75
kekka = "合格" if tensuu >= 60 else "不合格"
print(kekka)
```
読むときは、「`tensuu >= 60` なら `"合格"`、そうでなければ `"不合格"`」です。名前の「三項」は、「値1」「条件」「値2」の3つでできているからです。

## ゲームでの使い方
```python
mutekichuu = True
iro = 7 if mutekichuu else 11
print(iro)
```
「無敵のときは白（7）、ふだんは緑（11）」のように、色や向きを選ぶときによく使います。

::: point
三項演算子は「2つのうち、どちらの**値**を使うか」を選ぶための書き方です。やることが2行以上あるときは、ふつうの `if` と `else` で書こう。
:::
