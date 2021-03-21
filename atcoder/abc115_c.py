# C - Christmas Eve
# https://atcoder.jp/contests/abc115/tasks/abc115_c
"""
とある世界では、今日はクリスマスイブです。
高羽氏の庭には N 本の木が植えられています。
i 本目の木 (1≤i≤N) の高さは hi メートルです。
彼は、これらの木のうち K 本を選んで電飾を施すことにしました。より美しい光景をつくるために、できるだけ近い高さの木を飾り付けたいです。
より具体的には、飾り付ける木のうち最も高いものの高さを hmax メートル、最も低いものの高さを hmin メートルとすると、hmax−hmin が小さいほど好ましいです。
hmax−hmin は最小でいくつにすることができるでしょうか？
"""
"""
N, K = map(int, input().split())
h = [int(input()) for i in range(N)]
h.sort()
print(min(h[i+K-1] - h[i] for i in range(N-K+1)))
"""
N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]
h.sort()
dif = [h[i+K-1] - h[i] for i in range(N-K+1)]
res = min(dif)
print(res)