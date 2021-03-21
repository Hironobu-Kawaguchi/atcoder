# B - Christmas Eve Eve
# https://atcoder.jp/contests/abc115/tasks/abc115_b
"""
とある世界では、今日はクリスマスイブの前日です。
高羽氏は、デパートで N 個の品物を買おうとしています。
i 個目の品物 (1≤i≤N) の定価は pi 円です。
彼は割引券を持っており、N 個のうち最も定価が高い品物 1 個を定価の半額で買うことができます。
残りの N−1 個の品物に対しては定価を支払います。支払金額は合計でいくらになるでしょうか？
"""
"""
N = int(input())
p = [int(input()) for i in range(N)]
print(sum(p) - max(p) // 2)
"""
N = int(input())
p = [int(input()) for _ in range(N)]
res = sum(p) - max(p) // 2
print(res)