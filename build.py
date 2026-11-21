#!/usr/bin/env python3
"""Pythonずかん ビルドスクリプト

content/*.md の原稿から、site/ に静的HTMLを作ります。

    python3 build.py

必要なもの: Python 3 と pygments (pip install pygments)
原稿の書き方は README.md を見てください。
"""
import html
import io
import json
import pathlib
import re
import subprocess
import sys
import tokenize
import unicodedata

from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from diagrams import DIAGRAMS
from comments import add_comments  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent
CONTENT = ROOT / "content"
ASSETS = ROOT / "assets"
OUT = ROOT / "site"

SITE_NAME = "Pythonずかん"
FONTS_URL = (
    "https://fonts.googleapis.com/css2?family=BIZ+UDGothic:wght@400;700"
    "&family=BIZ+UDPGothic:wght@400;700"
    "&family=Zen+Maru+Gothic:wght@500;700"
    "&family=Source+Code+Pro:wght@400;700&display=swap"
)

# 章の設定: 番号 -> (slug, 名前, ひとこと)
CHAPTERS = {
    0: ("ch0", "はじめる前に", "Pythonってなに？ 最初の1行"),
    1: ("ch1", "表示・計算・入力", "print と input"),
    2: ("ch2", "変数とリスト", "値に名前をつける・まとめる"),
    3: ("ch3", "繰り返し", "for と while"),
    4: ("ch4", "条件分岐", "if と else"),
    5: ("ch5", "関数", "処理に名前をつける"),
    6: ("ch6", "モジュール", "random や calendar を使う"),
    7: ("ch7", "Pyxelで作ろう", "画面に出して、動かす"),
    8: ("ch8", "クラスで作ろう", "class と self で、まとめて書く"),
    9: ("ch9", "Pyxel辞典", "関数やクラスを引く"),
    10: ("ch10", "道具と困ったとき", "エディタ・ターミナル・つまずき集"),
}
REF_CHAPTER = 9   # 辞典の章（確認テスト・課題は不要）
NO_TASK_CHAPTERS = {0, REF_CHAPTER, 10}
# 章を、大きな3つのまとまりに分けて見せる（名前、ひとこと、章の番号）
PARTS = [
    ("Pythonの基本", "まずはここ。基本を、自分で書けるようになるまで", [0, 1, 2, 3, 4, 5, 6]),
    ("Pyxelでゲームを作る", "基本を使って、レトロゲームを作ろう", [7, 8]),
    ("調べる", "分からないときに引く", [9, 10]),
]   # 課題（作ってみよう）がいらない章
PYXEL_API = {}    # Pyxelの名前（init, rect ...） -> 辞典ページの slug

# コードの中・文章中の `code` で、クリックして飛べるようにする言葉
CODE_TERMS = {
    "print": "print", "input": "input", "int": "int", "str": "str",
    "float": "float", "bool": "bool", "range": "range", "type": "datatype",
    "list": "list", "if": "if", "elif": "else", "else": "else", "for": "for",
    "while": "while", "break": "break", "continue": "break", "def": "function",
    "return": "return", "import": "import", "from": "import", "and": "logical",
    "or": "logical", "not": "logical", "True": "bool", "False": "bool",
    "random": "random", "calendar": "calendar",
    "len": "list", "sum": "list", "max": "math-func", "min": "math-func", "round": "math-func",
    "in": "for", "None": "none", "global": "update-draw", "math": "module",
    "pass": "pass", "abs": "math-func", "is": "none",
    "class": "class", "self": "init-self", "__init__": "init-self",
}

PAGES = {}       # slug -> dict
QUIZ = {}        # slug -> 確認テストの原稿
TASKS = {}       # slug -> 作ってみよう（課題）の原稿
PROBLEMS = []    # ビルド中に見つけた問題


# ---------------------------------------------------------------- 原稿の読み込み
def parse_reads(text):
    """reads: print=プリント | input=インプット  →  [("print", "プリント"), ...]"""
    out = []
    for item in text.split("|"):
        item = item.strip()
        if "=" in item:
            word, yomi = item.rsplit("=", 1)
            out.append((word.strip(), yomi.strip()))
    return out


def load_pages():
    for f in sorted(CONTENT.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        parts = re.split(r"^@@ +(\S+)[ \t]*$", text, flags=re.M)
        for i in range(1, len(parts), 2):
            slug, raw = parts[i], parts[i + 1]
            if slug.startswith("quiz:"):
                # 確認テスト: @@ quiz:ページのslug
                QUIZ[slug[5:]] = raw.strip("\n")
                continue
            if slug.startswith("task:"):
                # 作ってみよう: @@ task:ページのslug
                TASKS[slug[5:]] = raw.strip("\n")
                continue
            head, sep, body = raw.partition("\n--\n")
            if not sep:
                PROBLEMS.append(f"{f.name}: {slug} に '--' の区切りがありません")
                continue
            meta = {}
            for line in head.strip().splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip()
            if slug in PAGES:
                PROBLEMS.append(f"slug が重複しています: {slug}")
            PAGES[slug] = {
                "slug": slug,
                "title": meta.get("title", slug),
                "kind": meta.get("kind", "term"),
                "chapter": int(meta["chapter"]) if "chapter" in meta else None,
                "type": meta.get("type", ""),
                "syntax": meta.get("syntax", ""),
                "summary": meta.get("summary", ""),
                "aliases": [a.strip() for a in meta.get("aliases", "").split(",") if a.strip()],
                "reads": parse_reads(meta.get("reads", "")),
                "group": meta.get("group", ""),
                # hidden: yes のページは、章の一覧やメニューには出さない（検索とリンクからは開ける）
                "hidden": meta.get("hidden", "").lower() in ("yes", "true", "1"),
                "api": [a.strip() for a in meta.get("api", "").split(",") if a.strip()],
                "body": body.strip("\n"),
                "links": set(),
                "h2": [],
                "html": "",
                "order": len(PAGES),
            }


def build_api_map():
    for p in PAGES.values():
        for a in p["api"]:
            if a in PYXEL_API:
                PROBLEMS.append(f"api 名が重複しています: {a}")
            PYXEL_API[a] = p["slug"]


class Ctx:
    def __init__(self, page):
        self.page = page
        self.slug = page["slug"]
        self.qno = 0          # 確認テストの問題番号
        self.pending = []     # hideout のコードの実行結果（答えの中で見せる）
        self.tno = 0          # 作ってみよう の課題番号
        self.mode = None      # "task"（課題文）/ "sol"（解答例）
        self.task_expect = []  # 課題文に書いた「表示例」
        self.task_got = []     # 解答例を実際に動かした結果


# ---------------------------------------------------------------- コードの整形
def _width(text):
    return sum(2 if unicodedata.east_asian_width(c) in ("W", "F") else 1 for c in text)


def align_comments(code):
    """行の後ろに書いた # コメントの位置を、ブロック内でそろえる（日本語は2文字ぶん）。"""
    lines = code.split("\n")
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(code).readline))
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return code
    pos = {}   # 行番号 -> コメントの開始位置
    for t in toks:
        if t.type == tokenize.COMMENT:
            row, col = t.start
            if lines[row - 1][:col].strip():       # コードの後ろのコメントだけ
                pos[row] = col
    if not pos:
        return code
    heads = {r: lines[r - 1][:c].rstrip() for r, c in pos.items()}
    target = max(_width(h) for h in heads.values()) + 2
    if target > 56:
        for r, h in heads.items():
            lines[r - 1] = h + "  " + lines[r - 1][pos[r]:]
        return "\n".join(lines)
    for r, h in heads.items():
        lines[r - 1] = h + " " * (target - _width(h)) + lines[r - 1][pos[r]:]
    return "\n".join(lines)


# ---------------------------------------------------------------- コード実行
RUNNER = r'''
import sys, json, io, builtins, traceback, contextlib
d = json.load(sys.stdin)
code, inputs = d["code"], iter(d["inputs"])
buf = io.StringIO()
def fake_input(prompt=""):
    try:
        v = next(inputs)
    except StopIteration:
        raise EOFError("EOF when reading a line")
    buf.write(str(prompt) + "\x01" + v + "\x02\n")
    return v
builtins.input = fake_input
err = None
try:
    c = compile(code, "main.py", "exec")
except SyntaxError as e:
    txt = (e.text or "").strip()
    err = 'File "main.py", line %s\n    %s\n%s: %s' % (e.lineno, txt, type(e).__name__, e.msg)
else:
    g = {"__name__": "__main__"}
    try:
        with contextlib.redirect_stdout(buf):
            exec(c, g)
    except BaseException as e:
        lines = code.splitlines()
        parts = ["Traceback (most recent call last):"]
        for fs in traceback.extract_tb(e.__traceback__):
            if fs.filename == "main.py":
                parts.append('  File "main.py", line %d, in %s' % (fs.lineno, fs.name))
                parts.append("    " + lines[fs.lineno - 1].strip())
        parts.append("".join(traceback.format_exception_only(type(e), e)).rstrip())
        err = "\n".join(parts)
json.dump({"out": buf.getvalue(), "err": err}, sys.__stdout__)
'''


def run_code(code, inputs):
    p = subprocess.run(
        [sys.executable, "-I", "-c", RUNNER],
        input=json.dumps({"code": code, "inputs": inputs}),
        capture_output=True, text=True, timeout=15,
    )
    if p.returncode != 0:
        raise RuntimeError(p.stderr)
    return json.loads(p.stdout)


# ---------------------------------------------------------------- コードの色つけ
def pyxel_slug(name):
    if name in PYXEL_API:
        return PYXEL_API[name]
    if name.startswith("KEY_") or name.startswith("MOUSE_BUTTON") or name.startswith("GAMEPAD"):
        return PYXEL_API.get("KEY_")
    if name.startswith("COLOR_"):
        return PYXEL_API.get("COLOR_")
    return None


def highlight(code, ctx):
    out = []
    toks = list(lex(code.rstrip("\n"), PythonLexer()))
    for ti, (tt, val) in enumerate(toks):
        esc = html.escape(val, quote=False)
        cls = None
        if tt in Token.Comment:
            cls = "cm"
        elif tt in Token.Literal.String:
            cls = "st"
        elif tt in Token.Literal.Number:
            cls = "nu"
        elif tt in Token.Keyword.Constant:
            cls = "kc"
        elif tt in Token.Keyword or tt is Token.Operator.Word:
            cls = "kw"
        elif tt in Token.Name.Builtin:
            cls = "bi"
        elif tt in Token.Name.Function or tt in Token.Name.Class:
            cls = "fn"
        elif tt in Token.Operator:
            cls = "op"
        linkable = (tt in Token.Keyword or tt in Token.Name or tt is Token.Operator.Word)
        slug = CODE_TERMS.get(val) if linkable else None
        if linkable and tt in Token.Name:
            prev = [t for t in toks[max(0, ti - 2):ti]]
            if len(prev) == 2 and prev[1][1] == "." and prev[0][1] == "pyxel":
                slug = pyxel_slug(val) or slug
            elif val == "pyxel":
                slug = PYXEL_API.get("pyxel")
        if slug and slug != ctx.slug and slug in PAGES:
            ctx.page["links"].add(slug)
            c = f"cterm {cls}" if cls else "cterm"
            out.append(f'<a class="{c}" data-slug="{slug}" href="{slug}.html">{esc}</a>')
        elif cls:
            out.append(f'<span class="{cls}">{esc}</span>')
        else:
            out.append(esc)
    return "".join(out)


# ---------------------------------------------------------------- Pyxelの画面画像
PX_CACHE = ROOT / "px_cache"
PX_TOOL = ROOT / "tools" / "pyxel_shot.py"
PX_USED = set()


def px_screenshot(code, frames, ops, ctx):
    """Pyxelのコードを、画面なしで動かして、画面の画像を作る（同じコードなら前の画像を使う）。"""
    import hashlib
    key = hashlib.sha1(json.dumps([code, frames, ops], ensure_ascii=False).encode()).hexdigest()[:12]
    ext = "gif" if ops.get("gif") else "png"
    png = PX_CACHE / f"{key}.{ext}"
    PX_USED.add(png.name)
    if not png.exists():
        PX_CACHE.mkdir(exist_ok=True)
        src = ROOT / "tools" / f"_tmp_{key}.py"   # フォントと同じ場所で動かす
        src.write_text(code, encoding="utf-8")
        env = dict(__import__("os").environ, SDL_VIDEODRIVER="dummy", SDL_AUDIODRIVER="dummy")
        try:
            p = subprocess.run(
                [sys.executable, str(PX_TOOL), str(src), str(png), str(frames), json.dumps(ops)],
                capture_output=True, text=True, timeout=60, env=env, cwd=str(ROOT / "tools"),
            )
            err = "\n".join(l for l in p.stderr.splitlines() if "ALSA" not in l and "audio" not in l.lower())
        except subprocess.TimeoutExpired:
            err = "タイムアウト（quit できないプログラム？）"
        src.unlink(missing_ok=True)
        if not png.exists():
            PROBLEMS.append(f"{ctx.slug}: Pyxelの画面画像が作れませんでした（pip install pyxel が必要）:\n{code}\n{err}")
            return '<p class="muted">（画面画像なし）</p>'
    return f'<img class="pxshot" src="img/px-{key}.{ext}" alt="実行したときの画面" loading="lazy">'


def format_output(text, err=None):
    esc = html.escape(text, quote=False)
    esc = esc.replace("\x01", '<span class="typed">').replace("\x02", "</span>")
    esc = re.sub(r"\{\{(.+?)\}\}", r'<span class="typed">\1</span>', esc)
    esc = esc.rstrip("\n")
    parts = []
    if esc:
        parts.append(esc)
    if err:
        parts.append(f'<span class="err">{html.escape(err, quote=False)}</span>')
    if not parts:
        return '<span class="muted">（何も表示されません）</span>'
    return "\n".join(parts)


def out_figure(inner, caption="実行結果"):
    return (f'<figure class="out"><figcaption>{caption}</figcaption>'
            f"<pre>{inner}</pre></figure>")


def code_figure(code, ctx):
    return (
        '<figure class="code"><figcaption><span>プログラム</span>'
        '<button type="button" class="copy">コピー</button></figcaption>'
        f"<pre><code>{highlight(code, ctx)}</code></pre></figure>"
    )


def render_code(code, info, ctx, manual_out=None):
    toks = info.split()
    lang = toks[0] if toks else ""
    flags = toks[1:]
    inputs, norun, expect_err, noout, hideout = [], False, False, False, False
    px, px_frames, px_ops = False, 30, {}
    for f in flags:
        if f.startswith("in="):
            inputs = f[3:].split("|")
        elif f == "norun":
            norun = True
        elif f == "error":
            expect_err = True
        elif f == "noout":
            noout = True
        elif f == "px":
            px = True           # Pyxelのプログラム: 実行して、画面の画像を作る
        elif f == "gif":
            px_ops["gif"] = {"every": 2}   # うごく画像（GIF）にする
        elif f.startswith("frames="):
            px_frames = int(f[7:])
        elif f.startswith("hold="):
            px_ops["hold"] = f[5:].split(",")
        elif f.startswith("click="):
            px_ops["click"] = [int(v) for v in f[6:].split(",")]
        elif f.startswith("text="):
            px_ops["text"] = f[5:]
        elif f.startswith("press="):
            px_ops.setdefault("press", {})
            for item in f[6:].split(","):
                k, at = item.split("@")
                px_ops["press"][k] = int(at)
        elif f == "hideout":
            hideout = True   # 実行はするが、結果は問題文では見せず、答えの中に出す
    if lang == "output":
        if ctx.mode == "task":
            ctx.task_expect.append(code)
        cap = "こう表示されればOK" if ctx.mode == "task" else "実行結果"
        return f'<div class="runbox single">{out_figure(format_output(code), cap)}</div>'
    if lang != "python":
        return f'<pre class="plain"><code>{html.escape(code)}</code></pre>'
    if lang == "python" and ctx.mode in (None, "sol") and not hideout:
        code, missing = add_comments(code, expect_err)
        for ln in missing:
            PROBLEMS.append(f"{ctx.slug}: コメントをつけられない行があります: {ln}")
    code = align_comments(code)
    parts = ['<div class="runbox">', code_figure(code, ctx)]
    if px:
        img = px_screenshot(code, px_frames, px_ops, ctx)
        fig = (f'<figure class="out px"><figcaption>実行すると、こう見える</figcaption>{img}</figure>')
        if hideout:
            ctx.pending.append(fig)
        else:
            parts.append(fig)
    elif noout:
        pass
    elif norun:
        if manual_out is not None:
            parts.append(out_figure(format_output(manual_out)))
    else:
        r = run_code(code, inputs)
        if expect_err and not r["err"]:
            PROBLEMS.append(f'{ctx.slug}: エラーになるはずのコードが成功しました:\n{code}')
        if not expect_err and r["err"]:
            PROBLEMS.append(f'{ctx.slug}: コードがエラーになりました:\n{code}\n{r["err"]}')
        if ctx.mode == "sol":
            ctx.task_got.append(r["out"])
        fig = out_figure(format_output(r["out"], r["err"]))
        if hideout:
            ctx.pending.append(fig)
        else:
            parts.append(fig)
    parts.append("</div>")
    return "".join(parts)


# ---------------------------------------------------------------- 文章の変換
def norm_code_term(c):
    c = c.strip().rstrip(":")
    return re.split(r"[(.]", c)[0].strip()


def inline(s, ctx, autolink=True, in_link=False):
    s = html.escape(s, quote=False)
    stash = []

    def keep(h):
        stash.append(h)
        return f"\x00{len(stash) - 1}\x00"

    def link_sub(m):
        slug, text = m.group(1), m.group(2)
        if slug not in PAGES:
            PROBLEMS.append(f"{ctx.slug}: リンク先がありません [[{slug}]]")
            return keep(f'<span class="missing">{html.escape(text or slug)}</span>')
        label = inline(text, ctx, autolink=False, in_link=True) if text else html.escape(PAGES[slug]["title"], quote=False)
        if slug == ctx.slug:
            return keep(label)
        ctx.page["links"].add(slug)
        return keep(f'<a class="term" data-slug="{slug}" href="{slug}.html">{label}</a>')

    s = re.sub(r"\[\[([\w-]+)(?:\|([^\]]+))?\]\]", link_sub, s)

    def code_sub(m):
        c = m.group(1)
        h = f"<code>{c}</code>"
        if autolink and not in_link:
            raw = html.unescape(c).strip()
            slug = CODE_TERMS.get(norm_code_term(raw))
            m = re.match(r"pyxel\.(\w+)", raw)
            if m:
                slug = pyxel_slug(m.group(1)) or slug
            elif raw == "pyxel":
                slug = PYXEL_API.get("pyxel")
            elif not slug and ctx.page["chapter"] in (7, 8, 9):
                slug = pyxel_slug(re.split(r"[(\s.]", raw)[0])
            if slug and slug != ctx.slug and slug in PAGES:
                ctx.page["links"].add(slug)
                h = f'<a class="term" data-slug="{slug}" href="{slug}.html">{h}</a>'
        return keep(h)

    s = re.sub(r"`([^`]+)`", code_sub, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    while re.search(r"\x00\d+\x00", s):
        s = re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], s)
    return s


NOTE_LABELS = {"point": "ポイント", "stuck": "つまずいたら", "try": "やってみよう",
               "scratch": "Scratchでいうと"}
DETAILS_DEFAULT = {"deep": "もっと知りたい人へ", "answer": "こたえの例"}


def is_block_start(line):
    return bool(re.match(r"^(```|::: |## |### |\||[-*] |\d+\. )", line))


def grab_block(lines, start):
    """::: で始まるブロックの中身と、次に読む行の番号を返す。"""
    j = start + 1
    buf = []
    while j < len(lines) and lines[j].strip() != ":::":
        buf.append(lines[j])
        j += 1
    return buf, j + 1


def answer_html(inner_a, ctx):
    outs = "".join(f'<div class="runbox single">{o}</div>' for o in ctx.pending)
    ctx.pending = []
    return ('<details class="qans"><summary>こたえを見る</summary>'
            f'<div class="qans-body">{outs}{blocks(inner_a, ctx)}</div></details>')


def solution_html(inner_a, ctx):
    return ('<details class="qans tans"><summary>解答例を見る</summary>'
            f'<div class="qans-body">{blocks(inner_a, ctx)}'
            '<p class="tans-note">自分のコードと、見比べてみよう。ちがっていても、同じ結果になっていればOKです。</p>'
            '</div></details>')


def check_task_output(ctx, no):
    """課題文の「こう表示されればOK」と、解答例を実際に動かした結果が同じか確かめる。"""
    if len(ctx.task_expect) == 1 and len(ctx.task_got) == 1:
        want = ctx.task_expect[0].replace("{{", "\x01").replace("}}", "\x02")
        got = ctx.task_got[0]
        norm = lambda t: "\n".join(x.rstrip() for x in t.strip().splitlines())
        if norm(want) != norm(got):
            PROBLEMS.append(f"{ctx.slug}: 課題{no} の表示例と解答例の結果がちがいます\n--- 表示例\n{want}\n--- 結果\n{got}")


def render_tpl(title, inner, ctx):
    """書き方のテンプレート図。〔 〕は自分で決める部分、それ以外はそのまま書く言葉。"""
    k = 0
    while k < len(inner) and inner[k].strip():
        k += 1
    skel, rest = inner[:k], inner[k:]
    names = []
    has_indent = False
    lines_html = []
    for ln in skel:
        lv = 0
        while ln.startswith("····"):
            ln = ln[4:]
            lv += 1
        has_indent = has_indent or lv > 0
        parts = []
        for part in re.split(r"(〔.+?〕)", ln):
            if not part:
                continue
            m = re.fullmatch(r"〔(.+?)〕", part)
            if m:
                nm = m.group(1)
                if nm not in names:
                    names.append(nm)
                parts.append(f'<span class="ph ph-{names.index(nm) % 6 + 1}">{html.escape(nm)}</span>')
            elif part.strip() and re.fullmatch(r"[\s,()\[\]:]*", part):
                parts.append(f'<span class="pn">{html.escape(part)}</span>')   # 、 ( ) だけの部分は、枠なし
            elif part.strip():
                parts.append(f'<span class="fx">{html.escape(part)}</span>')
            else:
                parts.append(html.escape(part))
        lines_html.append(f'<span class="tl" style="--lv:{lv}">{"".join(parts)}</span>')
    legend_rows = [r for r in rest if r.startswith("|")]
    extra = [r for r in rest if not r.startswith("|")]
    dl = []
    for r in legend_rows:
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        if "〔" in cells[0]:
            bits = []
            for seg in re.split(r"(〔.+?〕)", cells[0]):
                mm = re.fullmatch(r"〔(.+?)〕", seg)
                if mm:
                    nm = mm.group(1)
                    if nm not in names:
                        names.append(nm)
                    bits.append(f'<span class="ph ph-{names.index(nm) % 6 + 1}">{html.escape(nm)}</span>')
                elif seg.strip():
                    bits.append(f'<span class="pn">{html.escape(seg)}</span>')
            dt = "".join(bits)
        else:
            dt = f'<span class="fx">{html.escape(cells[0])}</span>'
        dl.append(f"<dt>{dt}</dt><dd>{inline(cells[1], ctx)}</dd>")
    if has_indent:
        dl.append('<dt><span class="indent-mark">⇥ 行のはじめ</span></dt>'
                  "<dd>半角スペース4つ分、右にずらす（インデント）</dd>")
    key = ('<p class="tpl-key"><span class="fx">そのまま書く言葉</span>'
           '<span class="ph ph-1">自分で入れる部分</span></p>')
    return (f'<figure class="tpl"><figcaption>{html.escape(title or "書き方のかたち")}</figcaption>'
            f'{key}<pre class="tpl-code">{"".join(lines_html)}</pre>'
            f'<dl class="tpl-legend">{"".join(dl)}</dl>'
            f'{blocks(extra, ctx) if extra else ""}</figure>')


def render_flow(spec, ctx):
    name, _, caption = spec.partition(" ")
    if name not in DIAGRAMS:
        PROBLEMS.append(f"{ctx.slug}: 図がありません ::: flow {name}")
        return ""
    cap = f"<figcaption>{html.escape(caption.strip())}</figcaption>" if caption.strip() else ""
    return f'<figure class="flow">{DIAGRAMS[name]}{cap}</figure>'


def render_refindex(ctx):
    """Pyxel辞典の一覧（分類ごとの表 + 名前順の早見）。"""
    groups = {}
    for p in terms_of(REF_CHAPTER):
        groups.setdefault(p["group"] or "その他", []).append(p)
        ctx.page["links"].add(p["slug"])
    out = []
    for g, ps in groups.items():
        hid = f"s{len(ctx.page['h2']) + 1}"
        ctx.page["h2"].append((hid, g))
        rows = "".join(
            f'<tr><td><a class="term" data-slug="{p["slug"]}" href="{p["slug"]}.html"><code>{esc(p["syntax"] or p["title"])}</code></a></td>'
            f'<td>{esc(p["summary"])}</td></tr>'
            for p in ps
        )
        out.append(f'<h2 id="{hid}">{esc(g)}</h2><div class="tbl-wrap"><table class="reftbl"><thead><tr>'
                   f'<th>書き方</th><th>はたらき</th></tr></thead><tbody>{rows}</tbody></table></div>')
    names = sorted(((a, PAGES[s]) for a, s in PYXEL_API.items() if s in PAGES and PAGES[s]["chapter"] == REF_CHAPTER),
                   key=lambda x: x[0].lower())
    chips = "".join(f'<li><a class="chip" data-slug="{p["slug"]}" href="{p["slug"]}.html">{esc(a)}</a></li>' for a, p in names)
    hid = f"s{len(ctx.page['h2']) + 1}"
    ctx.page["h2"].append((hid, "名前順の早見"))
    out.append(f'<h2 id="{hid}">名前順の早見</h2><ul class="chips az">{chips}</ul>')
    return "\n".join(out)


def blocks(lines, ctx):
    out = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        m = re.match(r"^```(.*)$", line)
        if m:
            info = m.group(1).strip()
            j = i + 1
            code = []
            while j < n and lines[j].strip() != "```":
                code.append(lines[j])
                j += 1
            i = j + 1
            manual = None
            if info.startswith("python") and "norun" in info.split():
                k = i
                while k < n and not lines[k].strip():
                    k += 1
                if k < n and lines[k].strip() == "```output":
                    e = k + 1
                    outl = []
                    while e < n and lines[e].strip() != "```":
                        outl.append(lines[e])
                        e += 1
                    manual = "\n".join(outl)
                    i = e + 1
            out.append(render_code("\n".join(code), info, ctx, manual))
            continue
        m = re.match(r"^::: *(q|a|t|c|s)\s*$", line)
        if m:
            kind = m.group(1)
            if kind in ("q", "t", "c"):
                # 確認テスト（q→a）、作ってみよう（t→s）、チャレンジ（c→s）: 問題のあとに答えを続けて書く
                is_q = kind == "q"
                ans_kind = "a" if is_q else "s"
                inner_q, i = grab_block(lines, i)
                if is_q:
                    ctx.qno += 1
                    no = ctx.qno
                else:
                    if kind == "c":
                        no = "チャレンジ"   # 3つの課題とは別に数える
                    else:
                        ctx.tno += 1
                        no = ctx.tno
                    prev_mode = ctx.mode
                    ctx.mode, ctx.task_expect, ctx.task_got = "task", [], []
                q_html = blocks(inner_q, ctx)   # 先に実行して、結果を ctx.pending にためる
                k = i
                while k < n and not lines[k].strip():
                    k += 1
                a_html = ""
                if k < n and re.match(rf"^::: *{ans_kind}\s*$", lines[k]):
                    inner_a, i = grab_block(lines, k)
                    if is_q:
                        a_html = answer_html(inner_a, ctx)
                    else:
                        ctx.mode = "sol"
                        a_html = solution_html(inner_a, ctx)
                        check_task_output(ctx, no)
                else:
                    PROBLEMS.append(f"{ctx.slug}: {'問' if is_q else '課題'}{no} に答えがありません")
                if not is_q:
                    ctx.mode = prev_mode
                if is_q:
                    out.append(f'<div class="qitem"><p class="qno">問{no}</p>'
                               f'<div class="qbody">{q_html}</div>{a_html}</div>')
                elif kind == "c":
                    out.append(f'<div class="titem challenge"><p class="tno">チャレンジ</p>'
                               f'<div class="qbody">{q_html}</div>{a_html}</div>')
                else:
                    out.append(f'<div class="titem"><p class="tno">課題{no}</p>'
                               f'<div class="qbody">{q_html}</div>{a_html}</div>')
            else:
                inner_a, i = grab_block(lines, i)
                out.append(answer_html(inner_a, ctx))
            continue
        if re.match(r"^::: *refindex\s*$", line):
            _inner, i = grab_block(lines, i)
            out.append(render_refindex(ctx))
            continue
        m = re.match(r"^::: *(tpl|flow)\b *(.*)$", line)
        if m:
            kind, title = m.group(1), m.group(2).strip()
            inner, i = grab_block(lines, i)
            if kind == "tpl":
                out.append(render_tpl(title, inner, ctx))
            else:
                out.append(render_flow(title, ctx))
            continue
        m = re.match(r"^::: *(point|stuck|deep|try|answer|scratch)\b *(.*)$", line)
        if m:
            kind, title = m.group(1), m.group(2).strip()
            j = i + 1
            inner = []
            while j < n and lines[j].strip() != ":::":
                inner.append(lines[j])
                j += 1
            i = j + 1
            body = blocks(inner, ctx)
            if kind in DETAILS_DEFAULT:
                t = html.escape(title or DETAILS_DEFAULT[kind], quote=False)
                out.append(f'<details class="note {kind}"><summary>{t}</summary>{body}</details>')
            else:
                head = f'<p class="note-label">{NOTE_LABELS[kind]}</p>'
                if kind in ("try", "point") and title:
                    head += f'<p class="note-title">{inline(title, ctx)}</p>'
                out.append(f'<aside class="note {kind}">{head}{body}</aside>')
            continue
        if line.startswith("### "):
            out.append(f"<h3>{inline(line[4:], ctx, autolink=False)}</h3>")
            i += 1
            continue
        if line.startswith("## "):
            text = line[3:].strip()
            hid = f"s{len(ctx.page['h2']) + 1}"
            ctx.page["h2"].append((hid, text.replace("`", "")))
            out.append(f'<h2 id="{hid}">{inline(text, ctx, autolink=False)}</h2>')
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < n and lines[i].startswith("|"):
                if not re.match(r"^\|[\s:|-]+\|$", lines[i].strip()):
                    rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            th = "".join(f"<th>{inline(c, ctx)}</th>" for c in rows[0])
            trs = "".join(
                "<tr>" + "".join(f"<td>{inline(c, ctx)}</td>" for c in r) + "</tr>"
                for r in rows[1:]
            )
            out.append(f'<div class="tbl-wrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')
            continue
        m = re.match(r"^([-*]|\d+\.) ", line)
        if m:
            tag = "ol" if m.group(1)[0].isdigit() else "ul"
            items = []
            while i < n and re.match(r"^([-*]|\d+\.) ", lines[i]):
                items.append(re.sub(r"^([-*]|\d+\.) ", "", lines[i]))
                i += 1
            lis = "".join(f"<li>{inline(t, ctx)}</li>" for t in items)
            out.append(f"<{tag}>{lis}</{tag}>")
            continue
        para = [line]
        i += 1
        while i < n and lines[i].strip() and not is_block_start(lines[i]):
            para.append(lines[i])
            i += 1
        out.append(f"<p>{inline(''.join(para), ctx)}</p>")
    return "\n".join(out)


# ---------------------------------------------------------------- ページ組み立て
def esc(s):
    return html.escape(s, quote=True)


def render_quiz(page):
    """確認テストのHTMLを作る。リンクの集計（関連・被リンク）には影響させない。"""
    raw = QUIZ.get(page["slug"])
    if not raw:
        return ""
    saved = set(page["links"])
    ctx = Ctx(page)
    ctx.mode = "quiz"
    body = blocks(raw.split("\n"), ctx)
    page["links"] = saved
    page["h2"].append(("quiz", "確認テスト"))
    return (
        '<section class="quiz"><h2 id="quiz">確認テスト</h2>'
        '<p class="quiz-lead">このページを見直せば、ぜんぶ解けます。'
        'まず自分で考えて（プログラムは、自分のVS Codeで動かしてOK）、それから答えを開こう。</p>'
        + body + "</section>"
    )


def render_tasks(page):
    """作ってみよう（課題）。リンクの集計には影響させない。"""
    raw = TASKS.get(page["slug"])
    if not raw:
        return ""
    saved = set(page["links"])
    ctx = Ctx(page)
    body = blocks(raw.split("\n"), ctx)
    page["links"] = saved
    if body.count('class="titem"') != 3:
        PROBLEMS.append(f'{page["slug"]}: 課題は3つ必要です（今は {body.count(chr(34) + "titem" + chr(34))} 個）')
    page["h2"].append(("tasks", "作ってみよう"))
    return (
        '<section class="tasks"><h2 id="tasks">作ってみよう</h2>'
        '<p class="tasks-lead">IDLE か VS Code にプログラムを書いて、実行してみよう。'
        'できたら「解答例を見る」を開いて、自分のコードと見比べよう。</p>'
        + body + "</section>"
    )


def reads_html(page):
    """このページに出てくる命令の、カタカナの読み方。"""
    if not page.get("reads"):
        return ""
    items = "".join(
        f'<li><code>{esc(w)}</code><span class="yomi">{esc(y)}</span></li>' for w, y in page["reads"]
    )
    return ('<aside class="reads"><p class="reads-label">このページの命令の読み方</p>'
            f'<ul>{items}</ul></aside>')


def make_yomi_page():
    """全ページの reads をあつめた「命令のよみかた」ページ。"""
    seen = set()
    sections = []
    for n, (cslug, name, _sub) in CHAPTERS.items():
        rows = []
        pages = [PAGES[cslug]] + terms_of(n, hidden=True) if cslug in PAGES else terms_of(n, hidden=True)
        for p in pages:
            for w, y in p.get("reads", []):
                if w in seen:
                    continue
                seen.add(w)
                rows.append(
                    f'<tr><td><code>{esc(w)}</code></td><td class="yomi">{esc(y)}</td>'
                    f'<td><a href="{p["slug"]}.html">{esc(p["title"])}</a></td></tr>'
                )
        if rows:
            sections.append(
                f'<h2 id="y{n}">{chapter_label(n)}</h2>'
                '<div class="tbl-wrap"><table><thead><tr><th>命令</th><th>読み方</th><th>くわしく</th></tr></thead>'
                f'<tbody>{"".join(rows)}</tbody></table></div>'
            )
    PAGES["yomi"] = {
        "slug": "yomi", "title": "命令のよみかた", "kind": "special", "chapter": None,
        "type": "", "syntax": "", "aliases": ["よみかた", "読み方", "カタカナ", "ふりがな"],
        "summary": "Pythonの命令や記号の、カタカナの読み方をまとめた表です。正確でなくても、声に出せればOK。",
        "reads": [], "body": "", "links": set(), "h2": [], "order": len(PAGES),
        "html": ('<p>声に出して読めると、覚えやすくなります。<strong>発音が正確でなくても大丈夫</strong>です。'
                 '先生や友だちと話すときの「呼び名」だと思ってください。</p>' + "".join(sections)),
        "quiz_html": "", "tasks_html": "",
    }


def chapter_label(n):
    return f"第{n}章 {CHAPTERS[n][1]}"


def chapter_chip(n, link=True):
    cls = f"chip ch-{n}"
    if link:
        return f'<a class="{cls}" href="{CHAPTERS[n][0]}.html">{chapter_label(n)}</a>'
    return f'<span class="{cls}">{chapter_label(n)}</span>'


def terms_of(n, hidden=False):
    return sorted(
        [p for p in PAGES.values() if p["kind"] == "term" and p["chapter"] == n
         and (hidden or not p["hidden"])],
        key=lambda p: p["order"],
    )


def nav_html(cur):
    parts = ['<a class="nav-home" href="index.html">はじめに</a>']
    ya = ' aria-current="page"' if cur["slug"] == "yomi" else ""
    parts.append(f'<a class="nav-home nav-yomi" href="yomi.html"{ya}>命令のよみかた</a>')
    ta = ' aria-current="page"' if cur["slug"] == "trouble" else ""
    parts.append(f'<a class="nav-home nav-yomi" href="trouble.html"{ta}>困ったとき</a>')
    first_of_part = {nums[0]: name for name, _s, nums in PARTS}
    for n, (cslug, name, _sub) in CHAPTERS.items():
        if n in first_of_part:
            parts.append(f'<p class="nav-part">{esc(first_of_part[n])}</p>')
        terms = terms_of(n)
        is_open = cur["chapter"] == n
        cur_attr = ' aria-current="page"' if cur["slug"] == cslug else ""
        items = [f'<li class="chl"><a href="{cslug}.html"{cur_attr}>この章のまとめ</a></li>']
        last_g = None
        for t in terms:
            if t["group"] and t["group"] != last_g:
                items.append(f'<li class="grp">{esc(t["group"])}</li>')
                last_g = t["group"]
            aria = ' aria-current="page"' if cur["slug"] == t["slug"] else ""
            items.append(f'<li><a href="{t["slug"]}.html"{aria}>{esc(t["title"])}</a></li>')
        parts.append(
            f'<details class="nav-ch ch-{n}"{" open" if is_open else ""}>'
            f'<summary><span class="no">{n}</span>{esc(name)}</summary>'
            f'<ul>{"".join(items)}</ul></details>'
        )
    return "".join(parts)


def toc_html(page):
    if len(page["h2"]) < 3:
        return ""
    lis = "".join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in page["h2"])
    return f'<nav class="toc" aria-label="このページの内容"><p>このページの内容</p><ol>{lis}</ol></nav>'


def infobox_html(page, incoming):
    n = page["chapter"]
    rows = []
    if page["type"]:
        rows.append(("種類", esc(page["type"])))
    if page["syntax"]:
        rows.append(("書き方", f'<code>{esc(page["syntax"])}</code>'))
    rows.append(("出てくる章", chapter_chip(n)))
    out_links = sorted(
        [PAGES[s] for s in page["links"] if s in PAGES and PAGES[s]["kind"] == "term"],
        key=lambda p: p["order"],
    )[:6]
    if out_links:
        chips = "".join(
            f'<a class="chip" data-slug="{p["slug"]}" href="{p["slug"]}.html">{esc(p["title"])}</a>'
            for p in out_links
        )
        rows.append(("関連", f'<span class="chips-inline">{chips}</span>'))
    dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    return (f'<aside class="infobox ch-{n}"><p class="ib-title">{esc(page["title"])}</p><dl>{dl}</dl></aside>')


def termlist_html(n):
    items, last_g = [], None
    for t in terms_of(n):
        if t["group"] and t["group"] != last_g:
            items.append(f'<li class="tl-grp">{esc(t["group"])}</li>')
            last_g = t["group"]
        items.append(f'<li><a data-slug="{t["slug"]}" href="{t["slug"]}.html"><strong>{esc(t["title"])}</strong>'
                     f'<span>{esc(t["summary"])}</span></a></li>')
    return f'<ul class="termlist">{"".join(items)}</ul>'


def backlinks_html(page, incoming):
    srcs = sorted(
        [PAGES[s] for s in incoming.get(page["slug"], []) if s in PAGES],
        key=lambda p: (p["chapter"] or 0, p["order"]),
    )
    if not srcs:
        return ""
    chips = "".join(
        f'<li><a class="chip" data-slug="{p["slug"]}" href="{p["slug"]}.html">{esc(p["title"])}</a></li>'
        for p in srcs
    )
    return (f'<section class="backlinks"><h2 class="plain">このページにリンクしているページ</h2>'
            f'<ul class="chips">{chips}</ul></section>')


def pager_html(n):
    prev_n, next_n = n - 1, n + 1
    left = right = "<span></span>"
    if prev_n in CHAPTERS:
        left = f'<a class="pg" href="{CHAPTERS[prev_n][0]}.html"><small>前の章</small>{chapter_label(prev_n)}</a>'
    if next_n in CHAPTERS:
        right = f'<a class="pg next" href="{CHAPTERS[next_n][0]}.html"><small>次の章</small>{chapter_label(next_n)}</a>'
    return f'<nav class="pager">{left}{right}</nav>'


def home_extra():
    sections = []
    for pname, psub, nums in PARTS:
        cards = []
        for n in nums:
            cslug, name, sub = CHAPTERS[n]
            ts = terms_of(n)
            words = "、".join(esc(t["title"].split("（")[0]) for t in ts[:5])
            words = f"{words} ほか" if words else ""
            cards.append(
                f'<li><a class="chcard ch-{n}" href="{cslug}.html"><span class="chno">{n}</span>'
                f'<strong>{esc(name)}</strong><span class="sub">{esc(sub)}</span>'
                f'<span class="words">{words}</span></a></li>'
            )
        sections.append(f'<h3 class="part-head">{esc(pname)}<span>{esc(psub)}</span></h3>'
                        f'<ol class="chapters">{"".join(cards)}</ol>')
    idx = []
    for n, (cslug, name, _sub) in CHAPTERS.items():
        links = "".join(
            f'<li><a class="term" data-slug="{t["slug"]}" href="{t["slug"]}.html">{esc(t["title"])}</a></li>'
            for t in terms_of(n)
        )
        if links:
            idx.append(f'<div class="idx ch-{n}">{chapter_chip(n)}<ul>{links}</ul></div>')
    return (
        '<p class="yomi-link"><a href="yomi.html">🔤 命令のよみかた（カタカナ表）</a>'
        '<span>range や elif の読み方が分からなくなったら</span></p>'
        '<h2>章からえらぶ</h2>' + "".join(sections) +
        '<h2>言葉からえらぶ</h2><div class="index-all">' + "".join(idx) + "</div>"
    )


def render_page(page, incoming, css, js):
    slug = page["slug"]
    kind = page["kind"]
    ctx = Ctx(page)
    n = page["chapter"]
    chip = chapter_chip(n) if n is not None else ""
    ptype = f'<span class="ptype">{esc(page["type"])}</span>' if page["type"] else ""
    lede = f'<p class="lede">{inline(page["summary"], ctx, autolink=False)}</p>'
    title_tag = SITE_NAME if kind == "home" else f'{page["title"]} | {SITE_NAME}'
    nav = nav_html(page)

    if kind == "home":
        head = f'<header class="art-head"><h1><span class="prompt">&gt;&gt;&gt;</span> {esc(page["title"])}</h1></header>'
        article = head + lede + page["html"] + home_extra()
    elif kind == "special":
        article = (
            f'<header class="art-head"><h1>{esc(page["title"])}</h1></header>' + lede + page["html"]
        )
    elif kind == "chapter":
        article = (
            '<div class="trail" id="trail" hidden></div>'
            f'<header class="art-head"><p class="eyebrow">{chip}</p><h1>{esc(page["title"])}</h1></header>'
            + lede + reads_html(page) + toc_html(page) + page["html"] + page.get("quiz_html", "")
            + page.get("tasks_html", "")
            + ('' if n == REF_CHAPTER or not terms_of(n) else '<h2 id="terms">この章で出てくる言葉</h2>' + termlist_html(n))
            + pager_html(n) + backlinks_html(page, incoming)
        )
    else:
        article = (
            '<div class="trail" id="trail" hidden></div>'
            f'<header class="art-head"><p class="eyebrow">{chip}{ptype}</p><h1>{esc(page["title"])}</h1></header>'
            + infobox_html(page, incoming) + lede + reads_html(page) + toc_html(page) + page["html"]
            + page.get("quiz_html", "") + page.get("tasks_html", "") + backlinks_html(page, incoming)
        )

    data = {
        s: [p["title"], p["summary"], p["chapter"] if p["chapter"] is not None else "", " ".join(p["aliases"] + p.get("api", []) + [s] + [y for _w, y in p.get("reads", [])])]
        for s, p in PAGES.items()
    }
    chcls = f"ch-{n}" if n is not None else ""
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title_tag)}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="icon" href="favicon.ico" sizes="32x32">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS_URL}">
<style>
{css}
</style>
</head>
<body data-slug="{slug}" data-title="{esc(page["title"])}" class="{chcls}">
<header class="site-head">
  <a class="brand" href="index.html"><span class="prompt">&gt;&gt;&gt;</span>{SITE_NAME}</a>
  <div class="search">
    <input id="q" type="search" placeholder="ことばをさがす（例：if）" autocomplete="off" aria-label="ことばをさがす">
    <ul id="results" hidden></ul>
  </div>
</header>
<div class="wrap">
  <nav class="side" aria-label="もくじ">{nav}</nav>
  <main class="article">
    <details class="nav-m"><summary>もくじを開く</summary>{nav}</details>
    {article}
  </main>
</div>
<script>window.ZUKAN={{pages:{json.dumps(data, ensure_ascii=False)}}};</script>
<script>
{js}
</script>
</body>
</html>
"""


# ---------------------------------------------------------------- メイン
def main():
    load_pages()
    build_api_map()
    css = (ASSETS / "style.css").read_text(encoding="utf-8")
    js = (ASSETS / "site.js").read_text(encoding="utf-8")

    for p in PAGES.values():
        ctx = Ctx(p)
        p["html"] = blocks(p["body"].split("\n"), ctx)
        p["quiz_html"] = render_quiz(p)
        p["tasks_html"] = render_tasks(p)

    for p in PAGES.values():
        if p["kind"] == "term" and p["chapter"] is None:
            PROBLEMS.append(f'{p["slug"]}: chapter がありません')
        if not p["summary"]:
            PROBLEMS.append(f'{p["slug"]}: summary がありません')
        if p["kind"] in ("term", "chapter") and p["chapter"] != REF_CHAPTER and not p["quiz_html"]:
            PROBLEMS.append(f'{p["slug"]}: 確認テストがありません（@@ quiz:{p["slug"]}）')
    for p in PAGES.values():
        if p["kind"] in ("term", "chapter") and p["chapter"] not in NO_TASK_CHAPTERS and not p["tasks_html"]:
            PROBLEMS.append(f'{p["slug"]}: 作ってみようがありません（@@ task:{p["slug"]}）')
        if p["kind"] in ("term", "chapter") and not p["reads"] and p["slug"] != "ch9":
            PROBLEMS.append(f'{p["slug"]}: reads（カタカナ読み）がありません')
    for s in TASKS:
        if s not in PAGES:
            PROBLEMS.append(f"作ってみようのページ名が見つかりません: task:{s}")
    make_yomi_page()
    for s in QUIZ:
        if s not in PAGES:
            PROBLEMS.append(f"確認テストのページ名が見つかりません: quiz:{s}")

    incoming = {}
    for p in PAGES.values():
        for t in p["links"]:
            incoming.setdefault(t, set()).add(p["slug"])

    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.html"):
        old.unlink()
    import shutil
    for icon in (ASSETS / "icons").glob("*"):   # ブックマーク・タブ用のアイコン
        shutil.copy(icon, OUT / icon.name)
    (OUT / "img").mkdir(exist_ok=True)
    for old in list((OUT / "img").glob("px-*.png")) + list((OUT / "img").glob("px-*.gif")):
        old.unlink()
    for name in PX_USED:
        if (PX_CACHE / name).exists():
            shutil.copy(PX_CACHE / name, OUT / "img" / f"px-{name}")
    for p in PAGES.values():
        (OUT / f'{p["slug"]}.html').write_text(render_page(p, incoming, css, js), encoding="utf-8")

    # リンク切れチェック
    for f in OUT.glob("*.html"):
        for href in re.findall(r'href="([\w-]+\.html)', f.read_text(encoding="utf-8")):
            if not (OUT / href).exists():
                PROBLEMS.append(f"{f.name}: リンク切れ {href}")

    orphans = [s for s, p in PAGES.items() if p["kind"] == "term" and s not in incoming]
    terms = [p for p in PAGES.values() if p["kind"] == "term"]
    print(f"ページ数: {len(PAGES)}（用語 {len(terms)}）")
    if orphans:
        print("どこからもリンクされていない用語:", ", ".join(orphans))
    if PROBLEMS:
        print("\n問題が見つかりました:")
        for pr in PROBLEMS:
            print(" -", pr)
        sys.exit(1)
    print("OK: site/ に出力しました")


if __name__ == "__main__":
    main()
