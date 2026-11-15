#!/bin/bash
# サイトを作り直す（content/ の原稿 → site/）。できたら site/index.html をブラウザで開いて確認する。
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
  echo "はじめての準備をします（1回だけ）…"
  python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt || exit 1
fi
.venv/bin/python build.py || { echo; echo "ビルドが止まりました。上の「問題が見つかりました」を直してください。"; exit 1; }
if [ "$1" = "open" ]; then open site/index.html; fi
