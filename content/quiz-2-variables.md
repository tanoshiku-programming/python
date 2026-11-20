@@ quiz:ch2
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
x = 10
x = x + 5
print(x)
```
:::
::: a
`x = x + 5` は、右側を先に計算して（`10 + 5`）、結果を `x` に入れ直します。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
kudamono_list = ["りんご", "みかん", "バナナ"]
print(kudamono_list[1])
```
:::
::: a
番号は0から数えるので、`1` は2番目の「みかん」です。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
tensuu_list = [70, 85, 90]
print(len(tensuu_list))
```
:::
::: a
`len()` は、リストの中身の個数を返します。
:::

@@ quiz:variable
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
score = 80
score = 95
print(score)
```
:::
::: a
入れ直すと、前の値は消えて新しい値になります。
:::

::: q
次のうち、変数の名前として使えるものはどれ？ `score`、`1st`、`if`、`total_price`
:::
::: a
`score` と `total_price` です。数字で始まる `1st` と、Pythonの言葉の `if` は使えません。
:::

::: q
次のプログラムを実行すると、どうなる？
```python hideout error
print(total)
```
:::
::: a
`NameError` になります。`total` に値を入れる前に使おうとしたからです。
:::

@@ quiz:assignment
::: q
`=` は、プログラムの中でどんな意味？
:::
::: a
「等しい」ではなく、**右の値を左の変数に入れる**という意味です。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
count = 0
count += 1
count += 1
print(count)
```
:::
::: a
`count += 1` は `count = count + 1` と同じ意味で、1ずつ増えます。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
count = 5
count = count + 3
print(count)
```
:::
::: a
今の `count`（5）に3を足して、`count` に入れ直しているので `8` です。
:::

@@ quiz:list
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
kazu_list = [10, 20, 30]
print(kazu_list[0])
```
:::
::: a
0番目は、最初の値です。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
tensuu_list = [70, 85, 90]
tensuu_list.append(100)
print(tensuu_list)
```
:::
::: a
`append(値)` は、リストの最後に値を足します。
:::

::: q
3つ入ったリスト `kudamono_list` に `kudamono_list[3]` を使うと、どうなる？
```python hideout error
kudamono_list = ["りんご", "みかん", "バナナ"]
print(kudamono_list[3])
```
:::
::: a
`IndexError` になります。番号は `0`、`1`、`2` までしかありません。
:::

@@ quiz:list-index
::: q
3つ入ったリストで、最後の値の番号は何番？
:::
::: a
`2` です。数え始めが0なので、3つなら `0`、`1`、`2` になります。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
kudamono_list = ["りんご", "みかん", "バナナ"]
print(kudamono_list[-1])
```
:::
::: a
マイナスの番号は、うしろから数えます。`-1` は最後の値です。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
kudamono_list = ["りんご", "みかん", "バナナ", "ぶどう"]
print(kudamono_list[0:2])
```
:::
::: a
`[0:2]` は、0番目から2番目の**手前**までです。終わりの番号は含まれません。
:::

@@ quiz:bool
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
print(5 > 3)
print(5 < 3)
```
:::
::: a
比べた結果は、`True` か `False` になります。
:::

::: q
`True` と `False` は、何というデータ型？
:::
::: a
真偽値（`bool`）です。
:::

::: q
次のプログラムを実行すると、どうなる？
```python hideout error
print(true)
```
:::
::: a
`NameError` になります。`True` は先頭が大文字です。小文字の `true` は、Pythonは知らない名前です。
:::

@@ quiz:naming
::: q
次のプログラムで、**自分でつけた名前**はどれ？
```python norun
kion = 30
if kion >= 30:
    print("暑い")
```
:::
::: a
`kion` です。`if` はPythonの決まった言葉、`print` はPythonが用意した関数です。
:::

::: q
次のうち、変数の名前に**使えない**ものは？（`tensuu`、`while`、`score2`）
:::
::: a
`while` です。Pythonの決まった言葉（予約語）は、名前に使えません。
:::

::: q
「値段」を入れる変数を、このサイトのルールで名前をつけると？
:::
::: a
`nedan` です。ローマ字は、キーボードで打つときと同じつづりで書きます。
:::

@@ quiz:tuple
::: q
リスト `[1, 2]` とタプル `(1, 2)` のうち、あとから中身を変えられるのはどっち？
:::
::: a
**リスト**です。タプルは、作ったあとで中身を変えられません。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
basho = (40, 30)
x, y = basho
print(y)
```
:::
::: a
タプルの中身が、順番に `x` と `y` に入ります。
:::

@@ quiz:dict
::: q
辞書 `tensuu = {"国語": 80, "数学": 95}` から、数学の点数を取り出すには？
:::
::: a
`tensuu["数学"]` です。辞書は、番号ではなくキーで取り出します。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
chara = {"x": 10, "hp": 3}
chara["hp"] = chara["hp"] - 1
print(chara["hp"])
```
:::
::: a
`hp` の `3` から1を引いて、`2` を入れ直しています。
:::

::: q
辞書にないキーを取り出そうとすると、何というエラーになる？
:::
::: a
`KeyError` です。キーのつづりがまちがっていないか確かめます。
:::

@@ quiz:list2d
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
hyou = [[1, 2, 3], [4, 5, 6]]
print(hyou[1][0])
```
:::
::: a
`hyou[1]` は2行目の `[4, 5, 6]`。その0番なので `4` です。
:::

::: q
二次元リストは、`[たて][よこ]` と `[よこ][たて]` の、どちらの順番で書く？
:::
::: a
`[たて][よこ]` です。先に「何行目か」、次に「何列目か」を書きます。座標の `(x, y)` とは逆です。
:::
