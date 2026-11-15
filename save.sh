#!/bin/bash
# サイトを作り直して、GitHub に送る（＝公開する）。GitHub Pages なので無料・何回でもOK。
# 使い方: ./save.sh "何を変えたかのメモ"
cd "$(dirname "$0")"
msg="$1"
if [ -z "$msg" ]; then
  echo "使い方: ./save.sh \"何を変えたかのメモ\""
  exit 1
fi
if [ "$(git branch --show-current)" != "main" ]; then
  echo "main ブランチに切り替えます。"
  git checkout -q main || exit 1
fi
./build.sh || exit 1
git add -A
if git diff --cached --quiet; then
  echo "変更がないので、保存するものはありません。"
  exit 0
fi
echo "--- 今回変わったファイル ---"
git diff --cached --stat | tail -15
git commit -q -m "$msg" && git push -q origin main && echo && echo "GitHub に保存して公開しました。1〜2分でサイトに反映されます。"
