@@ quiz:ch3
::: q
次のプログラムを実行すると、何行表示される？ 何が表示される？
```python hideout
for i in range(3):
    print("こんにちは")
```
:::
::: a
`range(3)` は3回という意味なので、3行表示されます。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
count = 3
while count > 0:
    print(count)
    count -= 1
print("スタート！")
```
:::
::: a
`count` が `0` になると、`count > 0` が `False` になって、ループが終わります。
:::

::: q
回数が決まっているときは `for` と `while` のどちらを使う？
:::
::: a
`for` です。いつ終わるか分からないときは `while` を使います。
:::

@@ quiz:for
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
for i in range(3):
    print(i)
```
:::
::: a
`i` には、`0`、`1`、`2` が順番に入ります。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
for kudamono in ["りんご", "みかん"]:
    print(kudamono)
```
:::
::: a
リストの中身が、1つずつ `kudamono` に入ります。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
total = 0
for n in [10, 20, 30]:
    total += n
print(total)
```
:::
::: a
繰り返すたびに、`total` に10、20、30が足されて、`60` になります。最後の `print` は、インデントが下がっていないので、1回だけ実行されます。
:::

@@ quiz:while
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
n = 1
while n <= 3:
    print(n)
    n += 1
```
:::
::: a
`n` が `4` になると、`n <= 3` が `False` になって、終わります。
:::

::: q
`while` 文は、条件が何のあいだ繰り返す？
:::
::: a
`True` のあいだです。`False` になると終わります。
:::

::: q
3から1まで数えたい。`____` に入る行は？
```python norun
count = 3
while count > 0:
    print(count)
    ____
```
:::
::: a
`count -= 1` です。これを忘れると、`count` が変わらないので、終わらなくなります。
:::

@@ quiz:range
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
print(list(range(5)))
```
:::
::: a
`range(5)` は、0から4までの5個です。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
print(list(range(1, 6)))
```
:::
::: a
`range(始め, 終わり)` の終わりの数は、含まれません。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
print(list(range(0, 10, 2)))
```
:::
::: a
3つ目の数は「増え方」です。2ずつ増えます。
:::

@@ quiz:break
::: q
次のプログラムを実行すると、何が表示される？
```python hideout
for i in range(1, 10):
    if i == 4:
        break
    print(i)
```
:::
::: a
`i` が `4` になったところで `break` が実行されて、ループ全体が終わります。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```
:::
::: a
`i` が `3` のときだけ、`print` を飛ばします。ループは続きます。
:::

::: q
`break` と `continue` のちがいを、ひとことで説明しよう。
:::
::: a
`break` はループを終わらせます。`continue` は今回の分だけ飛ばして、次の回に進みます。
:::

@@ quiz:indent
::: q
Pythonで、インデント（行の頭の空白）は何を表している？
:::
::: a
どこまでが同じかたまりか、を表しています。
:::

::: q
次のプログラムを実行すると、何が表示される？
```python hideout
for i in range(2):
    print("A")
print("B")
```
:::
::: a
`print("B")` はインデントが下がっていないので、繰り返しの外です。だから `B` は1回だけです。
:::

::: q
インデントは、半角スペース何個分下げる？
:::
::: a
4個分です。Tabキーを1回押してもOKです。
:::

@@ quiz:infinite-loop
::: q
無限ループとは、どんなループ？
:::
::: a
終わらずに、ずっと続いてしまうループです。
:::

::: q
無限ループになってしまったとき、止める方法は？
:::
::: a
`Ctrl` キーを押しながら `C` キーを押します。使っているソフトに「停止」ボタンがあれば、それでもOKです。
:::

::: q
次のプログラムは無限ループになる。止まるようにするには、どの行を足せばいい？
```python norun
n = 1
while n <= 3:
    print(n)
```
:::
::: a
`n += 1` を、`print(n)` の下に足します。`n` が増えないと、`n <= 3` がずっと `True` のままだからです。
:::
