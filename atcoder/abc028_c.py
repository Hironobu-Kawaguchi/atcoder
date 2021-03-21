"""
C - 数を3つ選ぶマン
https://atcoder.jp/contests/abc028/tasks/abc028_c
異なる整数が 5 個与えられます。
この中から 3 つ選んでその和で表すことの出来る整数のうち、3 番目に大きいものを出力してください。
"""
import itertools
l = list(map(int, (input().split())))
sm = []
for p in itertools.combinations(l, 3):
    sm.append(sum(p))
sm.sort(reverse=True)
print(sm[2])