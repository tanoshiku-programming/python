"""コードの各行に、その行が何をしているかのコメントを自動でつける。
決まった形（print, input, 代入, for, if, def ...）はルールで、特別な行は OVERRIDE で書く。
コメントがつけられなかった行は、ビルドのときに知らせる。
"""
import re

# 行そのもの（前後の空白なし）→ コメント。ルールより優先される
OVERRIDE = {
    'print("あ", end="")': "「あ」を表示する。改行はしない",
    'print("い")': "「い」を表示する（直前の「あ」につづけて表示される）",
    'print("2026", "10", "17", sep="/")': "3つの文字を、空白のかわりに「/」で区切って表示する",
    'print("点数は", 80, "点です")': "3つをカンマで区切って、並べて表示する",
    "print(type(10))": "10 のデータ型を調べて表示する",
    "print(int(3.9))": "3.9 の小数部分を切り捨てて、整数にして表示する",
    "print(0.1 + 0.2)": "0.1 + 0.2 の結果を表示する",
    "print(len(word))": "word の文字数を数えて表示する",
    "print(len(kudamono_list))": "kudamono_list の中身の個数を数えて表示する",
    "print(len(tensuu_list))": "tensuu_list の中身の個数を数えて表示する",
    "print(sum(tensuu_list))": "tensuu_list の合計を表示する",
    "print(sum(tensuu_list), max(tensuu_list), min(tensuu_list))": "合計、いちばん大きい数、いちばん小さい数を表示する",
    "print(n % 2 == 0)": "n が偶数かどうかを調べて、True か False を表示する",
    "print(round(3.14159, 2))": "3.14159 を小数第2位までに丸めて表示する",
    "print(10 // 3)": "10 ÷ 3 の商（整数部分）を表示する",
    "print(7 // 2)": "7 ÷ 2 の商（整数部分）の 3 を表示する",
    "print(7 % 2)": "7 ÷ 2 の余りの 1 を表示する",
    "print(2 ** 10)": "2 の10乗を表示する",
    "print(2 ** 100)": "2 の100乗を表示する（大きな数でもOK）",
    "print(1 + 2 * 3)": "かけ算が先なので 1 + 6 = 7 を表示する",
    "print((1 + 2) * 3)": "かっこの中が先なので 3 * 3 = 9 を表示する",
    "print(10 == \"10\")": "整数の 10 と文字の \"10\" を比べる（型がちがうので False）",
    "print(x == 1 or 2)": "「x が1か2」のつもりだが、書き方がまちがっている",
    "print(not nenrei < 10)": "「nenrei < 10」の答えを、反対にして表示する",
    "print(not False)": "False を反対にして、True を表示する",
    "print()": "何も書かずに、改行だけする",
    "a, b = 1, 2": "a に 1 を、b に 2 を、同時に入れる",
    "a, b = b, a": "a と b の中身を入れ替える",
    "x = x + 5": "x に 5 を足して、x に入れ直す",
    "count = count + 1": "count に 1 を足して、count に入れ直す",
    "count += 1": "count を 1 増やす（count = count + 1 と同じ）",
    "count -= 1": "count を 1 減らす",
    "n += 1": "n を 1 増やす",
    "total += i": "total に i を足していく",
    "total += n": "total に n を足していく",
    "1 + 2": "1 + 2 を計算する（ファイルでは、計算しても表示はされない）",
    "pass": "何もしない",
    "return": "ここで関数を終わらせる（これより下は実行しない）",
    "continue": "今回の分を飛ばして、次の回へ進む",
    "break": "繰り返しを、ここで終わらせる",
    "x = 5": "x に 5 を入れる",
    "while True:": "True はずっと True なので、繰り返しつづける",
    "if True:": "条件が True なので、中の処理が実行される",
    "for i in range(3):": "i に 0, 1, 2 を順番に入れながら、3回繰り返す",
    "for i in range(2):": "2回繰り返す",
    "for i in range(1, 11):": "i に 1 から 10 まで順番に入れながら繰り返す",
    "for i in range(1, 10):": "i に 1 から 9 まで順番に入れながら繰り返す",
    "for i in range(1, 6):": "i に 1 から 5 まで順番に入れながら繰り返す",
    "for i in range(1, 4):": "i に 1 から 3 まで順番に入れながら繰り返す",
    "for a in range(1, 4):": "外側の繰り返し。a に 1 から 3 まで入れる",
    "for b in range(1, 4):": "内側の繰り返し。b に 1 から 3 まで入れる",
    "for i in range(n, 0, -1):": "i に n から 1 まで、1つずつ減らしながら入れる",
    "for i in range(kaisuu):": "kaisuu 回繰り返す",
    'for moji in "ABC":': "「ABC」の文字を1つずつ moji に入れながら繰り返す",
    "def hello():": "hello という関数を作る（引数なし）",
    "def hello(name):": "hello という関数を作る（引数は name）",
    "def add(a, b):": "add という関数を作る（引数は a と b）",
    "def aisatsu(name, kaisuu):": "aisatsu という関数を作る（引数は name と kaisuu）",
    'def aisatsu(name="ゲスト"):': "aisatsu という関数を作る（name を書かなければ「ゲスト」になる）",
    "return a + b": "a + b の答えを、呼び出した場所に返す",
    "hello()": "hello 関数を呼び出す（実行する）",
    "aisatsu()": "引数なしで aisatsu を呼び出す（「ゲスト」が使われる）",
    "random.shuffle(namae_list)": "namae_list の順番を、ランダムに入れ替える",
    "import random": "random モジュールを使えるようにする",
    "import calendar": "calendar モジュールを使えるようにする",
    "import math": "math モジュールを使えるようにする",
    "from math import sqrt": "math の中から sqrt だけを取り出して、そのまま使えるようにする",
    "kudamono_list.append(\"ぶどう\")": "リストの最後に「ぶどう」を足す",
    "tensuu_list.append(100)": "リストの最後に 100 を足す",
    "tensuu_list.remove(85)": "リストの中から 85 を取り除く",
    "tensuu_list[0] = 75": "0番目の中身を 75 に書き換える",
    "calendar.setfirstweekday(calendar.SUNDAY)": "週の始まりを、日曜日に変える",
    "print(calendar.month(2026, 10))": "2026年10月のカレンダーを表示する",
    "print(calendar.weekday(2026, 10, 17))": "2026年10月17日の曜日を数字で表示する（0=月 … 6=日）",
    "print(math.pi)": "円周率を表示する",
}


ERR_OVERRIDE = {'print(こんにちは)': '「 」で囲み忘れ。名前だと思われて、エラーになる',
    'print（"こんにちは"）': 'かっこが全角の（ ）になっている（エラーになる）',
    'x　= 5': 'x と = のあいだに、全角スペースが入っている（エラーになる）',
    'Print("こんにちは")': 'P が大文字になっている（エラーになる）',
    'print("こんにちは"': 'かっこを閉じ忘れている（エラーになる）',
    'print("こんにちは)': '文字を囲む記号を、閉じ忘れている（エラーになる）',
    'if x > 3': '行の最後の : を書き忘れている（エラーになる）',
    'print(10 / 0)': '0 で割り算をしようとする（エラーになる）',
    'print(true)': '小文字の true は名前だと思われて、エラーになる',
    'print(nmae)': '変数名を打ち間違えている（エラーになる）',
    'print(kazu_list[3])': '4番目を取り出そうとする（3つしかないのでエラー）',
    'print(total)': 'total という変数は、まだ作っていない（エラーになる）',
    'print(himitsu)': '関数の外から、中の変数を使おうとする（エラーになる）',
    'print(int("3.5"))': '小数の文字を、いきなり整数にしようとする（エラーになる）',
    'print("3" + 4)': '文字と数を足そうとする（エラーになる）',
    'import ramdom': 'random の打ち間違い（見つからないのでエラー）',
    'if x = 5:': '「=」ではなく「==」と書くのが正しい（エラーになる）',
    'print(kudamono_list[3])': '4番目を取り出そうとする（3つしかないのでエラー）',
    'print(word[5])': '6番目の文字を取り出す'}


def _short(s, n=24):
    s = s.strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def _expr(e):
    return e.strip()



# ---------------------------------------------------------------- Pyxel
KEYNAMES = {"LEFT": "左", "RIGHT": "右", "UP": "上", "DOWN": "下", "SPACE": "スペース",
            "RETURN": "Enter", "ESCAPE": "Esc", "SHIFT": "Shift"}


def keyname(k):
    k = k.strip()
    if k == "pyxel.MOUSE_BUTTON_LEFT":
        return "マウスの左ボタン"
    if k == "pyxel.MOUSE_BUTTON_RIGHT":
        return "マウスの右ボタン"
    m = re.fullmatch(r"pyxel\.KEY_(\w+)", k)
    if m:
        return KEYNAMES.get(m[1], m[1]) + "キー"
    return k


def split_args(s):
    out, depth, cur, q = [], 0, "", None
    for ch in s:
        if q:
            cur += ch
            if ch == q:
                q = None
            continue
        if ch in "\"'":
            q = ch
            cur += ch
        elif ch in "([{":
            depth += 1
            cur += ch
        elif ch in ")]}":
            depth -= 1
            cur += ch
        elif ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out


def _kw(args):
    pos = [a for a in args if not re.match(r"^\w+=", a)]
    kw = {a.split("=", 1)[0]: a.split("=", 1)[1] for a in args if re.match(r"^\w+=", a)}
    return pos, kw


def px_call(name, args):
    pos, kw = _kw(args)
    g = lambda i, d="?": pos[i] if i < len(pos) else d
    if name == "init":
        t = f"（タイトルは {kw['title']}）" if "title" in kw else ""
        return f"幅 {g(0)}、高さ {g(1)} のウィンドウを用意する{t}"
    if name == "run":
        return f"{g(0)} と {g(1)} を、1秒に30回繰り返し呼び出して、ゲームを動かす"
    if name == "quit":
        return "プログラムを終わらせる"
    if name == "cls":
        return f"画面全体を、色 {g(0)} で塗りつぶす"
    if name == "pset":
        return f"({g(0)}, {g(1)}) の1ドットを、色 {g(2)} にする"
    if name == "line":
        return f"({g(0)}, {g(1)}) から ({g(2)}, {g(3)}) まで、色 {g(4)} の線を引く"
    if name == "rect":
        return f"({g(0)}, {g(1)}) から、幅 {g(2)}・高さ {g(3)} の四角を、色 {g(4)} で塗る"
    if name == "rectb":
        return f"({g(0)}, {g(1)}) から、幅 {g(2)}・高さ {g(3)} の四角の、ふちだけを色 {g(4)} で描く"
    if name == "circ":
        return f"中心 ({g(0)}, {g(1)})、半径 {g(2)} の円を、色 {g(3)} で塗る"
    if name == "circb":
        return f"中心 ({g(0)}, {g(1)})、半径 {g(2)} の円の、ふちだけを色 {g(3)} で描く"
    if name == "elli":
        return f"({g(0)}, {g(1)}) から、幅 {g(2)}・高さ {g(3)} のだ円を、色 {g(4)} で塗る"
    if name == "ellib":
        return f"({g(0)}, {g(1)}) から、幅 {g(2)}・高さ {g(3)} のだ円の、ふちだけを色 {g(4)} で描く"
    if name == "tri":
        return f"3つの点を結んだ三角形を、色 {g(6)} で塗る"
    if name == "trib":
        return f"3つの点を結んだ三角形の、ふちだけを色 {g(6)} で描く"
    if name == "fill":
        return f"({g(0)}, {g(1)}) とつながった同じ色の場所を、色 {g(2)} で塗る"
    if name == "text":
        return f"({g(0)}, {g(1)}) の位置に、{g(2)} を色 {g(3)} で書く" + ("（日本語フォント）" if len(pos) > 4 else "")
    if name == "blt":
        return "画像の一部を、画面にはりつける"
    if name == "mouse":
        return "マウスカーソルを、表示する" if g(0) == "True" else "マウスカーソルを、隠す"
    if name == "title":
        return f"ウィンドウのタイトルを {g(0)} に変える"
    if name == "screenshot":
        return "いまの画面を、画像ファイルにして保存する"
    if name == "camera":
        return f"画面の見える範囲を ({g(0, 0)}, {g(1, 0)}) だけずらす"
    if name == "clip":
        return "描く範囲を、四角の中だけにしぼる"
    if name == "pal":
        return f"色 {g(0)} を、色 {g(1)} に入れ替えて描く"
    if name == "play":
        return f"チャンネル {g(0)} で、効果音（サウンド {g(1)}）を鳴らす"
    if name == "playm":
        return f"ミュージック {g(0)} を鳴らす"
    if name == "stop":
        return "鳴っている音を止める"
    if name == "load":
        return f"{g(0)} から、画像や音のデータを読みこむ"
    if name == "show":
        return "描いた画面を表示して、ESC キーが押されるまで待つ"
    if name == "bltm":
        return f"タイルマップ {g(2)} の ({g(3)}, {g(4)}) から、幅 {g(5)}・高さ {g(6)} を、画面の ({g(0)}, {g(1)}) にはる"
    if name == "Font":
        return f"{g(0)} のフォント（日本語が書ける文字）を読みこむ"
    return None


def px_value(expr):
    """pyxel.xxx(...) を含む式の説明（代入の右辺など）。"""
    m = re.fullmatch(r"pyxel\.rndi\((.+)\)", expr)
    if m:
        a = split_args(m[1])
        return f"{a[0]} から {a[1]} までの整数を、ランダムに選ぶ"
    m = re.fullmatch(r"pyxel\.rndf\((.+)\)", expr)
    if m:
        a = split_args(m[1])
        return f"{a[0]} から {a[1]} までの小数を、ランダムに選ぶ"
    m = re.fullmatch(r"pyxel\.(sin|cos|sqrt)\((.+)\)", expr)
    if m:
        return {"sin": "サイン", "cos": "コサイン", "sqrt": "平方根"}[m[1]] + f"（{m[2]}）を求める"
    if expr == "pyxel.frame_count":
        return "いままでに進んだフレーム数"
    if expr == "pyxel.mouse_x":
        return "マウスの横の位置"
    if expr == "pyxel.mouse_y":
        return "マウスの縦の位置"
    return None


def px_line(s):
    """Pyxel関係の行のコメント。当てはまらなければ None。"""
    if s in ("def update():",):
        return "update関数を作る（ゲームの中身を動かす係。1フレームごとに呼ばれる）"
    if s in ("def draw():",):
        return "draw関数を作る（画面を描く係。1フレームごとに呼ばれる）"
    m = re.fullmatch(r"global (.+)", s)
    if m:
        return f"関数の外の変数 {m[1]} を、この中で書き換えると宣言する"
    m = re.fullmatch(r"(?:el)?if (not )?pyxel\.(btn|btnp|btnr)\((.+?)\):", s)
    if m:
        what = {"btn": "押されているあいだ", "btnp": "押された瞬間", "btnr": "離された瞬間"}[m[2]]
        pre = "もし " if s.startswith("if") else "そうでなくて、もし "
        neg = "でないなら" if m[1] else "なら"
        a = split_args(m[3])
        return f"{pre}{keyname(a[0])}が{what}{neg}、下の処理を実行する"
    m = re.match(r"pyxel\.images\[(\d+)\]\.set\(", s)
    if m:
        return f"イメージバンク {m[1]} に、文字で絵を作る（1文字が1ドット。0〜f が色の番号）"
    m = re.match(r"pyxel\.sounds\[(\d+)\]\.set\(", s)
    if m:
        return f"サウンド {m[1]} に、音を作る（音の高さ・音色・大きさ・効果・速さ）"
    m = re.match(r"pyxel\.tilemaps\[(\d+)\]\.set\(", s)
    if m:
        return f"タイルマップ {m[1]} に、タイルの並べ方を書く（4けたで1枚のタイル）"
    if s.startswith("pyxel.screen.load("):
        return "画像ファイルを、画面に直接読みこむ"
    m = re.match(r"pyxel\.musics\[(\d+)\]\.set\(", s)
    if m:
        return f"ミュージック {m[1]} に、チャンネルごとに鳴らす音の番号を並べる"
    m = re.fullmatch(r"pyxel\.(\w+)\((.*)\)", s)
    if m:
        c = px_call(m[1], split_args(m[2]))
        if c:
            return c
        return f"pyxel.{m[1]} を使う"
    m = re.fullmatch(r"(\w+) = (pyxel\..+)", s)
    if m:
        v = px_value(m[2])
        if v:
            return f"{v}。その答えを {m[1]} に入れる"
    m = re.fullmatch(r"(\w+) = pyxel\.(Font)\((.*)\)", s)
    if m:
        return f"{px_call('Font', split_args(m[3]))}。それを {m[1]} に入れる"
    m = re.fullmatch(r"(\w+) = (\w+)\[(\w+)\]", s)
    if m:
        return f"{m[2]} の {m[3]} 番目を取り出して、{m[1]} に入れる"
    return None


def comment_for(line, is_error=False):
    s = line.strip()
    if "pyxel" in s or s in ("def update():", "def draw():") or s.startswith("global "):
        c = px_line(s)
        if c:
            return c
    if is_error and s in ERR_OVERRIDE:
        return ERR_OVERRIDE[s]
    if s in OVERRIDE:
        return OVERRIDE[s]
    m = None
    # --- クラス
    if m := re.fullmatch(r"class (\w+):", s):
        return f"{m[1]} というクラス（設計図）を作る"
    if m := re.fullmatch(r"def __init__\(self(?:, (.+))?\):", s):
        return "インスタンスを作るときに、自動で1回だけ動く準備のメソッド" + (f"（{m[1]} を受け取る）" if m[1] else "")
    if s == "def update(self):":
        return "update メソッドを作る（ゲームの中身を動かす係。1フレームごとに呼ばれる）"
    if s == "def draw(self):":
        return "draw メソッドを作る（画面を描く係。1フレームごとに呼ばれる）"
    if m := re.fullmatch(r"def (\w+)\(self(?:, (.+))?\):", s):
        return f"{m[1]} というメソッド（クラスの中の関数）を作る" + (f"（{m[2]} を受け取る）" if m[2] else "")
    if m := re.fullmatch(r"self\.(\w+) = self\.\1 ([+\-]) (.+)", s):
        op = "足す" if m[2] == "+" else "引く"
        return f"自分の {m[1]} に {m[3]} を{op}"
    if m := re.fullmatch(r"self\.(\w+) = ([A-Z]\w*)\((.*)\)", s):
        return f"{m[2]} のインスタンスを作って、自分の {m[1]} に入れる"
    if m := re.fullmatch(r"self\.(\w+)\((.*)\)", s):
        return f"自分の {m[1]} メソッドを呼び出す"
    if m := re.fullmatch(r"self\.(\w+) = (.+)", s):
        v = px_value(m[2])
        if v:
            return f"{v}。その答えを、自分の {m[1]} に入れる"
        return f"自分の {m[1]} に {m[2]} を入れる"
    if m := re.fullmatch(r"self\.(\w+)\.(\w+)\((.*)\)", s):
        return f"自分の {m[1]} の、{m[2]} メソッドを呼び出す"
    if m := re.fullmatch(r"(\w+)\.(\w+) = \1\.\2 ([+\-]) (.+)", s):
        op = "足す" if m[3] == "+" else "引く"
        return f"{m[1]} の {m[2]} に {m[4]} を{op}"
    if m := re.fullmatch(r"(\w+)\.(\w+) = (.+)", s):
        return f"{m[1]} の {m[2]} に {m[3]} を入れる"
    if m := re.fullmatch(r"([A-Z]\w*)\(\)", s):
        return f"{m[1]} のインスタンスを作る（__init__ が動く）"
    if m := re.fullmatch(r"(\w+) = ([A-Z]\w*)\((.*)\)", s):
        return f"{m[2]} のインスタンスを作って、{m[1]} に入れる"
    if m := re.fullmatch(r"([\w.]+)\.append\(([A-Z]\w*)\((.*)\)\)", s):
        return f"{m[2]} のインスタンスを作って、{m[1]} の最後に足す"
    if m := re.fullmatch(r"(\w+)\.(\w+)\((.*)\)", s):
        if m[1] not in ("print", "random", "math", "calendar", "pyxel") and not m[2] in ("append", "sort", "clear", "remove"):
            return f"{m[1]} の {m[2]} メソッドを呼び出す"
    if m := re.fullmatch(r"for (\w+) in (self\.\w+):", s):
        return f"{m[2]} の中身を1つずつ {m[1]} に入れながら、くり返す"
    # --- 制御構文
    if m := re.fullmatch(r"for (\w+) in range\((.+)\):", s):
        return f"{m[1]} に range({m[2]}) の数を1つずつ入れながら、繰り返す"
    if m := re.fullmatch(r"for (\w+) in \((.+)\):", s):
        return f"{m[1]} に ({m[2]}) の数を1つずつ入れながら、繰り返す"
    if m := re.fullmatch(r"for (\w+) in (\w+):", s):
        return f"{m[2]} の中身を1つずつ {m[1]} に入れながら、繰り返す"
    if m := re.fullmatch(r"for (\w+) in (\[.*\]):", s):
        return f"リストの中身を1つずつ {m[1]} に入れながら、繰り返す"
    if m := re.fullmatch(r"while (.+):", s):
        return f"「{m[1]}」が True のあいだ、繰り返す"
    if m := re.fullmatch(r"if (.+):", s):
        return f"もし「{m[1]}」が True なら、下の処理を実行する"
    if m := re.fullmatch(r"elif (.+):", s):
        return f"そうでなくて、もし「{m[1]}」が True なら、下の処理を実行する"
    if s == "else:":
        return "どれにも当てはまらなければ、下の処理を実行する"
    if m := re.fullmatch(r"def (\w+)\((.*)\):", s):
        a = m[2].strip()
        return f"{m[1]} という関数を作る" + (f"（引数は {a}）" if a else "（引数なし）")
    if m := re.fullmatch(r"return [\"'](.*)[\"']", s):
        return f"「{m[1]}」を、呼び出した場所に返す"
    if m := re.fullmatch(r"return (\w+)", s):
        return f"{m[1]} の中身を、呼び出した場所に返す"
    if m := re.fullmatch(r"return (.+)", s):
        return f"{m[1]} の結果を、呼び出した場所に返す"
    if m := re.fullmatch(r"import (\w+)", s):
        return f"{m[1]} モジュールを使えるようにする"
    # --- 代入
    if m := re.fullmatch(r"(\w+)\.sort\(\)", s):
        return f"{m[1]} を小さい順に並べかえる"
    if m := re.fullmatch(r"(\w+)\.sort\(reverse=True\)", s):
        return f"{m[1]} を大きい順に並べかえる"
    if m := re.fullmatch(r"(\w+)\.clear\(\)", s):
        return f"{m[1]} の中身を全部消して、空っぽにする"
    if m := re.fullmatch(r"(\w+), (\w+) = (.+)", s):
        return f"{m[3]} の中身を、{m[1]} と {m[2]} に分けて入れる"
    if m := re.fullmatch(r"(\w+)\[(\w+|\"[^\"]*\")\] = \1\[\2\] ([+\-]) (.+)", s):
        op = "足す" if m[3] == "+" else "引く"
        basho = f"{m[2]} の中身" if m[2].startswith('"') else f"{m[2]} 番の中身"
        return f"{m[1]} の {basho}に、{m[4]} を{op}"
    if m := re.fullmatch(r"(\w+)\[(\w+|\"[^\"]*\")\] = (.+)", s):
        basho = m[2] if m[2].startswith('"') else f"{m[2]} 番"
        v = px_value(m[3])
        if v:
            return f"{v}。その答えを {m[1]} の {basho}に入れる"
        return f"{m[1]} の {basho}に {m[3]} を入れる"
    if m := re.fullmatch(r"(\w+) = (\w+)\[(\w+)\]", s):
        return f"{m[2]} の {m[3]} 番目を取り出して、{m[1]} に入れる"
    if m := re.fullmatch(r"(\w+) = int\(input\((.*)\)\)", s):
        return f"入力を整数に変えて、{m[1]} に入れる"
    if m := re.fullmatch(r"(\w+) = float\(input\((.*)\)\)", s):
        return f"入力を小数に変えて、{m[1]} に入れる"
    if m := re.fullmatch(r"(\w+) = input\((.*)\)", s):
        return f"入力を受け取って、{m[1]} に入れる"
    if m := re.fullmatch(r"(\w+) = int\((.+)\)", s):
        return f"{m[2]} を整数に変えて、{m[1]} に入れる"
    if m := re.fullmatch(r"(\w+) = float\((.+)\)", s):
        return f"{m[2]} を小数に変えて、{m[1]} に入れる"
    if m := re.fullmatch(r"(\w+) = str\((.+)\)", s):
        return f"{m[2]} を文字に変えて、{m[1]} に入れる"
    if m := re.fullmatch(r"(\w+) = random\.randint\((.+)\)", s):
        return f"{m[2]} の範囲から、整数をランダムに1つ選んで {m[1]} に入れる"
    if m := re.fullmatch(r"(\w+) = (-?\d+)", s):
        return f"{m[1]} に {m[2]} を入れる"
    if m := re.fullmatch(r"(\w+) = (-?\d+\.\d+)", s):
        return f"{m[1]} に小数の {m[2]} を入れる"
    if m := re.fullmatch(r"(\w+) = [\"'](.*)[\"']", s):
        return f"{m[1]} に文字「{_short(m[2])}」を入れる"
    if m := re.fullmatch(r"(\w+) = \[\]", s):
        return f"空っぽのリストを作って、{m[1]} に入れる"
    if m := re.fullmatch(r"(\w+) = \[(.*)\]", s):
        return f"{m[1]} にリストを入れる"
    if m := re.fullmatch(r"(\w+) (\+|-|\*)= (.+)", s):
        op = {"+": "足す", "-": "引く", "*": "かける"}[m[2]]
        return f"{m[1]} に {m[3]} を{op}"
    if m := re.fullmatch(r"(\w+) = ([\w.]+)\((.*)\)", s):
        return f"{m[2]}({m[3]}) の結果を、{m[1]} に入れる"
    if m := re.fullmatch(r"(\w+), (\w+) = (\w+)\((.*)\)", s):
        return f"{m[3]}({m[4]}) の2つの結果を、{m[1]} と {m[2]} に入れる"
    if m := re.fullmatch(r"(\w+) = (.+)", s):
        return f"{m[2]} を計算して、{m[1]} に入れる"
    if m := re.fullmatch(r"(\w+)\.append\((.+)\)", s):
        return f"リストの最後に {m[2]} を足す"
    # --- 呼び出し
    if m := re.fullmatch(r"print\((.+), end=(.+)\)", s):
        return "表示する。改行はしない（end で、最後の文字を指定している）"
    if m := re.fullmatch(r"print\(f[\"'](.*)[\"']\)", s):
        return "変数の値を文の中に入れて、表示する"
    if m := re.fullmatch(r"print\(\)", s):
        return "改行だけする"
    if m := re.fullmatch(r"print\([\"']([^\"']*)[\"']\)", s):
        return f"「{_short(m[1])}」と表示する"
    if m := re.fullmatch(r"print\((-?\d+(\.\d+)?)\)", s):
        return f"{m[1]} を表示する"
    if m := re.fullmatch(r"print\((\w+)\)", s):
        return f"{m[1]} の中身を表示する"
    if m := re.fullmatch(r"print\(type\((.+)\)\)", s):
        return f"{m[1]} のデータ型を調べて表示する"
    if m := re.fullmatch(r"print\(bool\((.+)\)\)", s):
        return f"{m[1]} を True / False に直して表示する"
    if m := re.fullmatch(r"print\(list\((.+)\)\)", s):
        return f"{m[1]} の数を、リストにして表示する"
    if m := re.fullmatch(r"print\((\w+)\[(-?\d+)\]\)", s):
        k = int(m[2])
        if k >= 0:
            return f"{m[1]} の {k}番（{k + 1}つ目）を表示する"
        return f"{m[1]} のうしろから {-k}つ目を表示する"
    if m := re.fullmatch(r"print\((\w+)\[(-?\d*):(-?\d*)\]\)", s):
        return f"{m[1]} の一部を取り出して表示する"
    if m := re.fullmatch(r"print\((\w+)\((.*)\)\)", s):
        return f"{m[1]}({m[2]}) の結果を表示する"
    if m := re.fullmatch(r"print\((.+)\)", s):
        if re.search(r"==|!=|[<>]|\band\b|\bor\b", m[1]) and not re.search(r"\(.*[<>=].*\)", m[1]):
            return f"{_short(m[1], 30)} が True か False かを表示する"
        if re.fullmatch(r"[^()\[\]]+(, [^()\[\]]+)+", m[1]) and "=" not in m[1]:
            return f"{_short(m[1], 30)} を並べて表示する"
        if "+" in m[1] and re.search(r"[\"']", m[1]):
            return "文字をつなげて表示する"
        return f"{_short(m[1], 30)} の結果を表示する"
    if m := re.fullmatch(r"(\w+)\((.+)\)", s):
        return f"{m[1]} 関数に {_short(m[2], 20)} を渡して呼び出す"
    if m := re.fullmatch(r"(\w+)\(\)", s):
        return f"{m[1]} 関数を呼び出す"
    return None


def add_comments(code, is_error=False):
    """コメントのない行にだけ、コメントをつける。つけられなかった行を返す。"""
    out, missing = [], []
    for line in code.split("\n"):
        s = line.strip()
        if not s or s.startswith("#") or re.search(r"\s#\s", line + " "):
            out.append(line)
            continue
        c = comment_for(line, is_error)
        if c is None:
            missing.append(s)
            out.append(line)
        else:
            out.append(f"{line}  # {c}")
    return "\n".join(out), missing
