"""ブックマーク用のアイコン（ひよこ＋図鑑）を作る。
16×16 のドット絵を、SVG と PNG と ICO にして assets/icons/ に書き出す。
絵を変えたいときは、下の PIXELS の文字を直して、python3 tools/make_icon.py を実行する。
"""
import pathlib
import struct

from PIL import Image, ImageDraw

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "icons"

# Pyxel の16色パレット（pyxel.colors と同じ）
PALETTE = {
    "N": "#2B335F",   # こい青（背景）
    "Y": "#E9C35B",   # 黄色（ひよこ）
    "O": "#D38441",   # オレンジ（くちばし・あし）
    "K": "#2B335F",   # 目
    "W": "#EEEEEE",   # 白（ページ）
    "R": "#D4186C",   # 赤（表紙）
    "S": "#7696DE",   # 水色（とじ目）
    "P": "#2B335F",   # >_（Pythonの入力画面の印）
    "r": "#D4186C",   # 色のドット
    "o": "#D38441",
    "t": "#19959C",
    "b": "#395C98",
}

PIXELS = [
    "NNNNNNNNNNNNNNNN",
    "NNNNNNNYYYNNNNNN",
    "NNNNNNYYYYYNNNNN",
    "NNNNNNYYYKYNNNNN",
    "NNNNNYYYYYYYONNN",
    "NNNNYYYYYYYNNNNN",
    "NNNNNYYYYYYNNNNN",
    "NNNNNNYYYYNNNNNN",
    "NNNNNNONNONNNNNN",
    "NRWWWWWSSWWWWWRN",
    "NRWPWWWSSWWrWoRN",
    "NRWWPWWSSWWWWWRN",
    "NRWPWPPSSWWtWbRN",
    "NRWWWWWSSWWWWWRN",
    "NRRRRRRRRRRRRRRN",
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
