"""ブックマーク用のアイコン（ひよこ＋図鑑）を作る。
16×16 のドット絵を、SVG と PNG と ICO にして assets/icons/ に書き出す。
おなかの 4×4 は Pyxel の16色パレット。
絵を変えたいときは、下の PIXELS の文字を直して、python3 tools/make_icon.py を実行する。
"""
import pathlib
import struct

from PIL import Image, ImageDraw

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "icons"

# Pyxel の16色パレット（pyxel.colors と同じ）。0〜9、a〜f の文字で、パレットの色番号を表す
PYXEL_COLORS = ['#000000', '#2B335F', '#7E2072', '#19959C', '#8B4852', '#395C98', '#A9C1FF', '#EEEEEE', '#D4186C', '#D38441', '#E9C35B', '#70C6A9', '#7696DE', '#A3A3A3', '#FF9798', '#EDC7B0']
PALETTE = {hex(n)[2:]: c for n, c in enumerate(PYXEL_COLORS)}
PALETTE.update({
    "N": PYXEL_COLORS[1],    # こい青（背景）
    "Y": PYXEL_COLORS[10],   # 黄色（ひよこ）
    "O": PYXEL_COLORS[9],    # オレンジ（くちばし・あし）
    "K": PYXEL_COLORS[1],    # 目
})

# 大きなひよこ。おなかの 4×4 は、Pyxelの16色パレット（左上から順に 0〜15 番）
PIXELS = [
    "NNNNNNNNNNNNNNNN",
    "NNNNNNNYYYYNNNNN",
    "NNNNNYYYYYYYYNNN",
    "NNNNYYYYYYYYYYNN",
    "NNNNYYYYYYKYYYNN",
    "NNNYYYYYYYYYYYOO",
    "NNNYYYYYYYYYYYON",
    "NNYYYYYYYYYYYYNN",
    "NNYYYY0123YYYYNN",
    "NNYYYY4567YYYYNN",
    "NNYYYY89abYYYYNN",
    "NNNYYYcdefYYYNNN",
    "NNNNYYYYYYYYNNNN",
    "NNNNNYYYYYYNNNNN",
    "NNNNNOONNOONNNNN",
    "NNNNNNNNNNNNNNNN",
]
assert len(PIXELS) == 16 and all(len(r) == 16 for r in PIXELS)


def rgb(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))


def image(size, rounded):
    big = Image.new("RGBA", (16, 16))
    for y, row in enumerate(PIXELS):
        for x, ch in enumerate(row):
            big.putpixel((x, y), rgb(PALETTE[ch]) + (255,))
    im = big.resize((size, size), Image.NEAREST)
    if rounded:
        mask = Image.new("L", (size * 4, size * 4), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, size * 4 - 1, size * 4 - 1], radius=size * 4 * 0.2, fill=255)
        im.putalpha(mask.resize((size, size), Image.LANCZOS))
    return im


def svg():
    rects = []
    for y, row in enumerate(PIXELS):
        x = 0
        while x < 16:
            ch = row[x]
            if ch == "N":
                x += 1
                continue
            x2 = x
            while x2 + 1 < 16 and row[x2 + 1] == ch:
                x2 += 1
            rects.append(f'<rect x="{x}" y="{y}" width="{x2 - x + 1}" height="1" fill="{PALETTE[ch]}"/>')
            x = x2 + 1
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" shape-rendering="crispEdges">'
            f'<rect width="16" height="16" rx="3" fill="{PALETTE["N"]}"/>' + "".join(rects) + "</svg>\n")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "favicon.svg").write_text(svg(), encoding="utf-8")
    image(32, True).save(OUT / "favicon-32.png")
    image(180, False).save(OUT / "apple-touch-icon.png")
    image(48, True).save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print("書き出しました:", ", ".join(sorted(p.name for p in OUT.iterdir())))


if __name__ == "__main__":
    main()
