"""流れ図（SVG）。色や文字の色は style.css の .dg ... で決める。"""
from html import escape

W = 480


def _t(x, y, text, cls="", anchor="middle", size=None):
    lines = text.split("\n")
    lh = 20
    y0 = y - (len(lines) - 1) * lh / 2 + 5
    st = f' font-size="{size}"' if size else ""
    out = []
    for i, ln in enumerate(lines):
        out.append(f'<text x="{x}" y="{y0 + i * lh:.0f}" text-anchor="{anchor}" class="{cls}"{st}>{escape(ln)}</text>')
    return "".join(out)


def box(cx, cy, w, h, text, cls="box"):
    return (f'<rect class="{cls}" x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="10"/>'
            + _t(cx, cy, text))


def diamond(cx, cy, w, h, text):
    pts = f"{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}"
    return f'<polygon class="cond" points="{pts}"/>' + _t(cx, cy, text)


def arrow(pts, name):
    d = " ".join(f"{x},{y}" for x, y in pts)
    return f'<polyline class="arrow" points="{d}" marker-end="url(#ah-{name})"/>'


def label(x, y, text, cls="lbl", anchor="middle"):
    return _t(x, y, text, cls, anchor)


def svg(name, h, body, alt):
    return (
        f'<svg class="dg" viewBox="0 0 {W} {h}" role="img" aria-label="{escape(alt)}" xmlns="http://www.w3.org/2000/svg">'
        f'<defs><marker id="ah-{name}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
        f'orient="auto-start-reverse"><path class="ah" d="M0,0 L10,5 L0,10 z"/></marker></defs>'
        + body + "</svg>"
    )


def _if():
    n = "if"
    b = [
        box(150, 22, 120, 34, "ここから", "box start"),
        arrow([(150, 40), (150, 52 + 0)], n) if False else "",
        arrow([(150, 39), (150, 62)], n),
        diamond(150, 100, 200, 80, "条件？"),
        arrow([(150, 140), (150, 190)], n), label(168, 166, "True（本当）", anchor="start"),
        box(150, 214, 200, 46, "処理を実行する"),
        arrow([(150, 237), (150, 276)], n),
        box(150, 296, 200, 40, "次の行へ"),
        arrow([(250, 100), (400, 100), (400, 296), (250, 296)], n),
        label(330, 90, "False（ちがう）"),
        label(400, 200, "とばす", "note"),
    ]
    return svg(n, 330, "".join(b), "if文の流れ。条件がTrueなら処理を実行し、Falseなら処理をとばして次の行へ進む")


def _ifelse():
    n = "ifelse"
    b = [
        diamond(240, 50, 220, 80, "条件？"),
        arrow([(150, 50), (100, 50), (100, 130)], n), label(112, 42, "True", anchor="start"),
        arrow([(330, 50), (380, 50), (380, 130)], n), label(368, 42, "False", anchor="end"),
        box(100, 160, 170, 56, "ifの中の処理\n（Aを実行）"),
        box(380, 160, 170, 56, "elseの中の処理\n（Bを実行）"),
        arrow([(100, 188), (100, 248), (200, 248)], n),
        arrow([(380, 188), (380, 248), (280, 248)], n),
        box(240, 248, 80, 36, "次の行", "box start"),
        label(240, 292, "AかBの、どちらか一方だけ実行される", "note"),
    ]
    return svg(n, 310, "".join(b), "if-else文の流れ。TrueならA、FalseならBのどちらか一方だけを実行する")


def _elif():
    n = "elif"
    b = [
        diamond(130, 50, 200, 80, "条件1？"),
        arrow([(230, 50), (330, 50)], n), label(280, 40, "True"),
        box(400, 50, 120, 44, "処理A"),
        arrow([(130, 90), (130, 150)], n), label(148, 122, "False", anchor="start"),
        diamond(130, 190, 200, 80, "条件2？"),
        arrow([(230, 190), (330, 190)], n), label(280, 180, "True"),
        box(400, 190, 120, 44, "処理B"),
        arrow([(130, 230), (130, 290)], n), label(148, 262, "False", anchor="start"),
        box(130, 314, 200, 44, "else：処理C"),
        label(400, 290, "実行されるのは\nどれか1つだけ", "note"),
        label(400, 120, "上から順に調べる", "note"),
    ]
    return svg(n, 350, "".join(b), "if-elif-else文の流れ。上から順に条件を調べ、最初にTrueになったところだけを実行する")


def _loop(n, cond_text, title, alt):
    b = [
        arrow([(190, 14), (190, 28)], n) if False else "",
        diamond(190, 64, 220, 80, cond_text),
        arrow([(190, 104), (190, 148)], n), label(206, 130, "True", anchor="start"),
        box(190, 176, 200, 50, "くり返す処理"),
        arrow([(190, 201), (190, 236), (50, 236), (50, 64), (80, 64)], n),
        label(120, 252, "もどる", "note"),
        arrow([(300, 64), (390, 64), (390, 150)], n), label(345, 54, "False"),
        box(390, 176, 150, 50, "ループの外へ\n（次の行）", "box start"),
    ]
    return svg(n, 270, "".join(b), alt)


def _function():
    n = "function"
    b = [
        label(55, 22, "入れるもの", "note"),
        box(55, 70, 90, 50, "引数\n（ひきすう）", "box"),
        arrow([(100, 70), (150, 70)], n),
        '<rect class="func" x="150" y="20" width="180" height="140" rx="12"/>',
        label(240, 42, "関数", "lbl strong"),
        _t(240, 100, "def 名前(引数):\n    処理\n    return 結果", "code"),
        arrow([(330, 70), (380, 70)], n),
        label(425, 22, "出てくるもの", "note"),
        box(425, 70, 90, 50, "戻り値\n（もどりち）", "box"),
        label(240, 190, "例：add(3, 4)", "lbl strong"),
        box(55, 230, 90, 40, "3 と 4"),
        arrow([(100, 230), (185, 230)], n),
        box(240, 230, 110, 40, "足し算する"),
        arrow([(295, 230), (380, 230)], n),
        box(425, 230, 90, 40, "7"),
    ]
    return svg(n, 270, "".join(b), "関数の流れ。引数を入れると、中で処理して、戻り値が出てくる")


def _variable():
    n = "variable"
    b = [
        _t(240, 30, "score = 80", "code big"),
        arrow([(240, 50), (240, 90)], n),
        '<rect class="box" x="160" y="96" width="160" height="70" rx="10"/>',
        _t(240, 131, "80", "num"),
        '<rect class="tag" x="190" y="170" width="100" height="30" rx="6"/>',
        _t(240, 185, "score", "tagtxt"),
        label(240, 232, "「score」という名前のふだを貼った箱に、80が入っている", "note"),
    ]
    return svg(n, 250, "".join(b), "変数は、名前のふだを貼った箱。score という箱に80が入っている")


def _listidx():
    n = "listidx"
    names = ["りんご", "みかん", "バナナ"]
    b = [_t(240, 20, 'fruits = ["りんご", "みかん", "バナナ"]', "code")]
    for i, nm in enumerate(names):
        x = 100 + i * 140
        b.append(f'<rect class="box" x="{x - 60}" y="80" width="120" height="56" rx="6"/>')
        b.append(_t(x, 108, nm))
        b.append(_t(x, 62, str(i), "idx"))
        b.append(_t(x, 168, str(i - 3), "idx neg"))
    b.append(label(30, 62, "前から", "note", "middle"))
    b.append(label(30, 168, "うしろから", "note", "middle"))
    b.append(label(240, 214, "fruits[0] → りんご　　fruits[-1] → バナナ", "note"))
    return svg(n, 232, "".join(b), "リストの番号。前からは0,1,2、うしろからは-1,-2,-3")


def _gameloop():
    n = "gameloop"
    b = [
        box(240, 24, 160, 36, "pyxel.run(update, draw)", "box start"),
        arrow([(240, 42), (240, 70)], n),
        box(130, 100, 180, 56, "update\n（動かす・計算する）"),
        arrow([(220, 100), (300, 100)], n),
        box(350, 100, 160, 56, "draw\n（画面に描く）"),
        arrow([(350, 128), (350, 170), (130, 170), (130, 128)], n),
        label(240, 190, "これを、1秒に30回くり返す（ESCキーで終わる）", "note"),
    ]
    return svg(n, 210, "".join(b), "Pyxelの流れ。run を呼ぶと、updateで動かして、drawで描くことを、1秒に30回くり返す")


def _coord():
    n = "coord"
    b = [
        '<rect class="box" x="90" y="40" width="300" height="180" rx="2"/>',
        label(90, 28, "(0, 0)", "note", "middle"),
        label(390, 28, "x が大きくなる →", "note", "end"),
        label(86, 130, "y が大きくなる ↓", "note", "end"),
        '<circle cx="240" cy="130" r="7" class="dot"/>',
        label(240, 112, "(x, y)", "lbl strong"),
        arrow([(90, 130), (233, 130)], n),
        arrow([(240, 40), (240, 123)], n),
        label(165, 150, "x（よこ）", "note"),
        label(262, 84, "y\n（たて）", "note", "start"),
        label(240, 244, "画面のいちばん左上が (0, 0)。下に行くほど y が大きい", "note"),
    ]
    return svg(n, 260, "".join(b), "Pyxelの座標。画面の左上が(0,0)で、右へ行くほどxが、下へ行くほどyが大きくなる")


DIAGRAMS = {
    "gameloop": _gameloop(),
    "coord": _coord(),
    "if": _if(),
    "ifelse": _ifelse(),
    "elif": _elif(),
    "for": _loop("for", "まだ中身が\nある？", "for", "for文の流れ。次の値があるあいだ、処理をくり返す"),
    "while": _loop("while", "条件？", "while", "while文の流れ。条件がTrueのあいだ、処理をくり返す"),
    "function": _function(),
    "variable": _variable(),
    "listidx": _listidx(),
}
