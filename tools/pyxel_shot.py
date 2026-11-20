"""Pyxelのプログラムを、画面なしで数フレーム動かして、画面を1枚の画像（PNG）にする。
使い方: python3 pyxel_shot.py コードのファイル 出力のPNG フレーム数 [操作の指定(JSON)]
操作の指定の例: {"hold": ["KEY_RIGHT"], "click": [80, 60], "text": "abc"}
"""
import json
import sys

import pyxel

src, out, frames = sys.argv[1], sys.argv[2], int(sys.argv[3])
ops = json.loads(sys.argv[4]) if len(sys.argv) > 4 else {}

_init = pyxel.init


def init(*a, **k):
    k["headless"] = True
    _init(*a, **k)


pyxel.init = init
_run = pyxel.run


def run(update, draw):
    state = {"n": 0}

    def upd():
        n = state["n"]
        for name in ops.get("hold", []):
            pyxel.set_btn(getattr(pyxel, name), True)
        if "click" in ops:
            pyxel.set_mouse_pos(*ops["click"])
            if n == frames // 2:
                pyxel.set_btn(pyxel.MOUSE_BUTTON_LEFT, True)
        if "text" in ops and n == frames // 2:
            pyxel.set_input_text(ops["text"])
        for name, at in ops.get("press", {}).items():
            if n == at:
                pyxel.set_btn(getattr(pyxel, name), True)
        update()
        state["n"] += 1

    gif = ops.get("gif")
    shots = []

    def drw():
        draw()
        n = state["n"]
        scale = max(2, min(4, 480 // pyxel.width))
        if gif and n % gif["every"] == 0:
            p = f"{out}.{len(shots):03d}.png"
            pyxel.screen.save(p, scale)
            shots.append(p)
        if n >= frames:
            if gif:
                import os
                from PIL import Image
                ims = [Image.open(p).convert("P", palette=Image.ADAPTIVE) for p in shots]
                ims[0].save(out, save_all=True, append_images=ims[1:], loop=0,
                            duration=int(1000 / 30 * gif["every"]), disposal=2)
                for p in shots:
                    os.remove(p)
            else:
                pyxel.screen.save(out, scale)
            pyxel.quit()

    _run(upd, drw)


pyxel.run = run


def show():
    # show は「画面を出して ESC まで待つ」命令。ここでは、その画面を画像にして終わる
    pyxel.screen.save(out, max(2, min(4, 480 // pyxel.width)))
    sys.exit(0)


pyxel.show = show
code = open(src, encoding="utf-8").read()
exec(compile(code, src, "exec"), {"__name__": "__main__"})
