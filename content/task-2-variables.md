@@ task:ch2
::: t
変数 `score` に `80` を入れて、表示してみよう。
```output
80
```
:::
::: s
```python
score = 80
print(score)
```
:::

::: t
リスト `kudamono_list` に「りんご」「みかん」「バナナ」を入れて、2番目の「みかん」を表示してみよう。
```output
みかん
```
:::
::: s
```python
kudamono_list = ["りんご", "みかん", "バナナ"]
print(kudamono_list[1])
```
番号は 0 から数えるので、2番目は `[1]` です。
:::

::: t
リスト `tensuu_list = [70, 85, 90]` に `100` を足して、合計を表示してみよう。
```output
345
```
:::
::: s
```python
tensuu_list = [70, 85, 90]
tensuu_list.append(100)
print(sum(tensuu_list))
```
:::

::: c
3人の点数 `tensuu_list = [70, 85, 92]` の**平均点**を表示しよう。平均は「合計 ÷ 人数」です。人数も、数字で書かずに `len()` で求めよう。
```output
平均は82.3点
```
:::
::: s
```python
tensuu_list = [70, 85, 92]
heikin = sum(tensuu_list) / len(tensuu_list)
print(f"平均は{round(heikin, 1)}点")
```
人数を `len()` で求めておくと、リストに人を足しても、プログラムを直さずにすみます。そのままだと `82.33333333333333` のように小数が長くなるので、`round(heikin, 1)` で小数第1位までに四捨五入しています（[[float]]）。
:::

@@ task:variable
::: t
変数 `name` に自分の名前を入れて、表示してみよう。
:::
::: s
```python
name = "はなこ"
print(name)
```
:::

::: t
変数 `x` に `10` を入れたあと、`x` に `5` を足して、`x` を表示してみよう。
```output
15
```
:::
::: s
```python
x = 10
x = x + 5
print(x)
```
:::

::: t
変数 `a = 3`、`b = 4` を作って、`a * b` の答えを変数 `menseki` に入れて、表示してみよう。
```output
12
```
:::
::: s
```python
a = 3
b = 4
menseki = a * b
print(menseki)
```
:::

@@ task:assignment
::: t
`count = 0` を作って、`count = count + 1` を2回書いてから、`count` を表示してみよう。
```output
2
```
:::
::: s
```python
count = 0
count = count + 1
count = count + 1
print(count)
```
:::

::: t
`+=` を使って、`total = 100` に `50` を足して、表示してみよう。
```output
150
```
:::
::: s
```python
total = 100
total += 50
print(total)
```
:::

::: t
`a = 1`、`b = 2` を、`a, b = b, a` で入れ替えて、`a` と `b` を表示してみよう。
```output
2
1
```
:::
::: s
```python
a = 1
b = 2
a, b = b, a
print(a)
print(b)
```
:::

@@ task:list
::: t
`tabemono_list = ["カレー", "すし", "ラーメン"]` を作って、いちばん最初の食べ物を表示してみよう。
```output
カレー
```
:::
::: s
```python
tabemono_list = ["カレー", "すし", "ラーメン"]
print(tabemono_list[0])
```
:::

::: t
空のリスト `namae_list` を作って、`"はなこ"` と `"たろう"` を足して、リスト全体を表示してみよう。
```output
['はなこ', 'たろう']
```
:::
::: s
```python
namae_list = []
namae_list.append("はなこ")
namae_list.append("たろう")
print(namae_list)
```
:::

::: t
`tensuu_list = [75, 90, 100]` の、合計・いちばん大きい数・いちばん小さい数を、1行で表示してみよう。
```output
265 100 75
```
:::
::: s
```python
tensuu_list = [75, 90, 100]
print(sum(tensuu_list), max(tensuu_list), min(tensuu_list))
```
:::

@@ task:list-index
::: t
`kudamono_list = ["りんご", "みかん", "バナナ", "ぶどう"]` の、最初と最後を表示してみよう。（最後は `-1` を使うよ）
```output
りんご
ぶどう
```
:::
::: s
```python
kudamono_list = ["りんご", "みかん", "バナナ", "ぶどう"]
print(kudamono_list[0])
print(kudamono_list[-1])
```
:::

::: t
`tensuu_list = [70, 85, 90]` の、最初の `70` を `75` に書き換えてから、リストを表示してみよう。
```output
[75, 85, 90]
```
:::
::: s
```python
tensuu_list = [70, 85, 90]
tensuu_list[0] = 75
print(tensuu_list)
```
:::

::: t
`kudamono_list = ["りんご", "みかん", "バナナ", "ぶどう"]` の、2番目から3番目（`みかん` と `バナナ`）を、スライスで取り出して表示してみよう。
```output
['みかん', 'バナナ']
```
:::
::: s
```python
kudamono_list = ["りんご", "みかん", "バナナ", "ぶどう"]
print(kudamono_list[1:3])
```
`[1:3]` は、1番目から3番目の手前までです。
:::

@@ task:bool
::: t
`5 > 3` と `5 < 3` の答えを、2行で表示してみよう。
```output
True
False
```
:::
::: s
```python
print(5 > 3)
print(5 < 3)
```
:::

::: t
`bool()` を使って、`0` と `1` を True / False に直して表示してみよう。
```output
False
True
```
:::
::: s
```python
print(bool(0))
print(bool(1))
```
:::

::: t
数を聞いて、10以上なら `True`、そうでなければ `False` と表示してみよう。
:::
::: s
```python in=15
n = int(input("数は？"))
print(n >= 10)
```
:::

@@ task:naming
::: t
「値段」を入れる変数と、「個数」を入れる変数を、ローマ字の名前で作ろう。値段は120、個数は3にして、かけ算した答えを表示しよう。
```output
360
```
:::
::: s
```python
nedan = 120
kosuu = 3
print(nedan * kosuu)
```
`nedan` と `kosuu` は、自分でつけた名前です。`a` と `b` にしても動きますが、何が入っているか分からなくなります。
:::

::: t
次のプログラムはエラーになります。変数の名前を直して、`りんご` と表示されるようにしよう。
```python norun
1ban = "りんご"
print(1ban)
```
:::
::: s
```python
ichiban = "りんご"
print(ichiban)
```
名前は、数字で始められません。`ichiban` や `ban1` のようにします。
:::

::: t
次のプログラムはエラーになります。`sum` を使わない名前に直して、合計の `6` が表示されるようにしよう。
```python norun
sum = 0
print(sum([1, 2, 3]))
```
```output
6
```
:::
::: s
```python
goukei = sum([1, 2, 3])
print(goukei)
```
`sum` はPythonが用意した「合計を出す関数」です。同じ名前の変数を作ると、関数が使えなくなってしまいます。
:::

@@ task:tuple
::: t
タプル `iro = (8, 10)` を作って、0番の値を表示しよう。
```output
8
```
:::
::: s
```python
iro = (8, 10)
print(iro[0])
```
:::

::: t
タプル `(40, 30)` の中身を、`x` と `y` に分けて入れて、`x + y` を表示しよう。
```output
70
```
:::
::: s
```python
x, y = (40, 30)
print(x + y)
```
:::

::: t
曜日のタプル `("月", "火", "水", "木", "金", "土", "日")` を作って、6番の曜日を表示しよう。
```output
日
```
:::
::: s
```python
youbi = ("月", "火", "水", "木", "金", "土", "日")
print(youbi[6])
```
曜日のように、あとから変わらないものはタプルにしておくと安心です。
:::

@@ task:dict
::: t
辞書 `nedan = {"りんご": 120, "みかん": 80}` を作って、みかんの値段を表示しよう。
```output
80
```
:::
::: s
```python
nedan = {"りんご": 120, "みかん": 80}
print(nedan["みかん"])
```
:::

::: t
さっきの辞書に、`"バナナ": 150` を足してから、辞書全体を表示しよう。
```output
{'りんご': 120, 'みかん': 80, 'バナナ': 150}
```
:::
::: s
```python
nedan = {"りんご": 120, "みかん": 80}
nedan["バナナ"] = 150
print(nedan)
```
まだないキーに値を入れると、新しく増えます。
:::

::: t
`for` を使って、辞書の中身を「りんご 120円」のように1行ずつ表示しよう。
```output
りんご 120円
みかん 80円
```
:::
::: s
```python
nedan = {"りんご": 120, "みかん": 80}
for kudamono in nedan:
    print(kudamono, f"{nedan[kudamono]}円")
```
:::

@@ task:list2d
::: t
`hyou = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]` を作って、まん中の `5` を表示しよう。
```output
5
```
:::
::: s
```python
hyou = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(hyou[1][1])
```
:::

::: t
二重ループを使って、3×3 の表を、1行ずつ並べて表示しよう。
```output
1 2 3 
4 5 6 
7 8 9 
```
:::
::: s
```python
hyou = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for gyou in hyou:
    for kazu in gyou:
        print(kazu, end=" ")
    print()
```
:::

::: t
文字のマップ `mappu = ["###", "#.G", "###"]` で、ゴールの `G` がある場所（2行目の3文字目）を取り出して表示しよう。
```output
G
```
:::
::: s
```python
mappu = ["###", "#.G", "###"]
print(mappu[1][2])
```
:::
