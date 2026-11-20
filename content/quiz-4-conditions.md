@@ quiz:ch4
::: q
16 と入力したとき、何が表示される？
```python hideout in=16
nenrei = int(input("年齢は？"))
if nenrei >= 18:
    print("大人です")
else:
    print("子どもです")
```
:::
::: a
`16 >= 18` は `False` なので、`else` の処理が実行されます。
:::

::: q
75 と入力したとき、何が表示される？
```python hideout in=75
score = int(input("点数："))
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")
```
:::
::: a
上から順に調べます。`75 >= 90` は `False`、`75 >= 70` は `True` なので、`B` です。
:::

::: q
「等しいかどうか」を調べるとき、`=` と `==` のどちらを使う？
:::
::: a
`==` です。`=` は、変数に値を入れる記号です。
:::

@@ quiz:if
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
kion = 20
if kion >= 30:
    print("暑いです")
print("おわり")
```
:::
::: a
`20 >= 30` は `False` なので、`暑いです` は表示されません。`おわり` はインデントが下がっていないので、いつも表示されます。
:::

::: q
「`x` が5と等しいなら」と書くとき、`if x ____ 5:` に入る記号は？
:::
::: a
`==` です。`if x == 5:` と書きます。
:::

::: q
`if` の行の最後に書く記号と、次の行に必要なことは？
:::
::: a
最後に `:`（コロン）を書いて、次の行は[[indent]]を下げます。
:::

@@ quiz:else
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
n = 4
if n > 5:
    print("大きい")
else:
    print("小さい")
```
:::
::: a
`4 > 5` は `False` なので、`else` の処理が実行されます。
:::

::: q
`95` 点のとき `A` になってほしいのに、`B` になってしまう。なぜ？
```python hideout
score = 95
if score >= 70:
    print("B")
elif score >= 90:
    print("A")
```
:::
::: a
上から順に調べて、最初に当てはまったところで終わるからです。`95 >= 70` が先に当てはまります。**厳しい条件（90以上）を上に書く**と直ります。
:::

::: q
`elif` は、どんな意味？
:::
::: a
「そうでなくて、もしこの条件なら」という意味です。
:::

@@ quiz:comparison
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
print(5 >= 5)
print(3 != 4)
```
:::
::: a
`>=` は「以上」なので、5は5以上で `True` です。`!=` は「等しくない」で、3と4は等しくないので `True` です。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
print(10 == "10")
```
:::
::: a
`False` です。`10`（整数）と `"10"`（文字列）は、データ型がちがうので、等しくありません。
:::

::: q
「以上」を表す記号は？
:::
::: a
`>=` です。
:::

@@ quiz:logical
::: q
`and` は、どんなときに `True` になる？
:::
::: a
両方の条件が `True` のときです。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
nenrei = 11
print(nenrei >= 10 and nenrei <= 12)
```
:::
::: a
`11 >= 10` も `11 <= 12` も `True` なので、`and` の答えも `True` です。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
print(not False)
```
:::
::: a
`not` は、反対にします。`False` の反対は `True` です。
:::

@@ quiz:ternary
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
n = 7
print("偶数" if n % 2 == 0 else "奇数")
```
:::
::: a
`7 % 2` は `1` なので、条件は `False`。`else` のあとの `"奇数"` が選ばれます。
:::

::: q
`kekka = "合格" if tensuu >= 60 else "不合格"` を、ふつうの `if` と `else` で書くと？
:::
::: a
```python norun
if tensuu >= 60:
    kekka = "合格"
else:
    kekka = "不合格"
```
:::
