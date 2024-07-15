#!/usr/bin/env python
# coding: utf-8

# Author: UTUMI Hirosi (utuhiro78 at yahoo dot co dot jp)
# License: Apache License, Version 2.0

import gzip
import jaconv
import urllib.request
from unicodedata import normalize

urllib.request.urlretrieve('http://ftp.edrdg.org/pub/Nihongo/edict2.gz', 'edict2.gz')

with gzip.open('edict2.gz', 'rt', encoding='EUC-JP') as file:
	lines = file.read().splitlines()

# Mozc の一般名詞のID
url = "https://raw.githubusercontent.com/google/mozc/master/src/data/dictionary_oss/id.def"
with urllib.request.urlopen(url) as response:
	id_mozc = response.read().decode()

id_mozc = id_mozc.split(" 名詞,一般,")[0].split("\n")[-1]

dicname = "mozcdic-ut-edict2.txt"
l2 = []

for i in range(len(lines)):
	# 全角スペースで始まるエントリはスキップ
	# 名詞のみを収録
	if lines[i][0] == "　" or \
	" /(n" not in lines[i]:
		continue

	entry = lines[i].split(" /(n")[0]

	# カタカナ語には読みが付与されていないので、表記から読みを作る。
	# 表記または読みが複数ある場合は、それぞれ最初のものだけを採用する。
	# ブラックコーヒー;ブラック・コーヒー /(n) black coffee/EntL1113820X/
	if " [" not in entry:
		hyouki = entry.split(";")[0]
		yomi = hyouki
	# 表記または読みが複数ある場合は、それぞれ最初のものだけを採用する。
	# 暗唱;暗誦;諳誦 [あんしょう;あんじゅ(暗誦,諳誦)(ok)] /(n,vs,vt) recitation/
	# reciting from memory/EntL1154570X/
	else:
		entry = entry.split(" [")
		yomi = entry[1].split("]")[0].split(";")[0]
		hyouki = entry[0].split(";")[0]

	hyouki = hyouki.split("(")[0]
	yomi = yomi.split("(")[0]
	yomi = yomi.translate(str.maketrans("", "", " =・"))

	# 読みが2文字以下の場合はスキップ
	# 表記が1文字の場合はスキップ
	# 表記が26文字以上の場合はスキップ。候補ウィンドウが大きくなりすぎる
	if len(yomi) < 3 or \
	len(hyouki) < 2 or \
	len(hyouki) > 25:
		continue

	# 読みのカタカナをひらがなに変換
	yomi = jaconv.kata2hira(yomi)
	yomi = yomi.translate(str.maketrans("ゐゑ", "いえ"))

	# 表記の全角英数を半角に変換
	hyouki = normalize("NFKC", hyouki)

	entry = [yomi, id_mozc, id_mozc, "8000", hyouki]
	l2.append("\t".join(entry) + "\n")

lines = sorted(set(l2))
l2 = []

with open(dicname, "w", encoding="utf-8") as dicfile:
	dicfile.writelines(lines)
