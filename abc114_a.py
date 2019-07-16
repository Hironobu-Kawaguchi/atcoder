"""
A - 753
https://atcoder.jp/contests/abc114/tasks/abc114_a
七五三とは、7 歳、5 歳そして 3 歳の子どもの成長を祝うとある国の行事です。
いま、高橋くんは X 歳です。今回の七五三で、高橋くんの成長は祝われるでしょうか？
高橋くんの成長が祝われるなら YES, 祝われないなら NO と出力せよ。
"""
X = input()
if X in "753":
    print('YES')
else:
    print('NO')