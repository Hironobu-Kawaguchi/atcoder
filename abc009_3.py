# C - 辞書式順序ふたたび
# https://atcoder.jp/contests/abc009/tasks/abc009_3

from collections import Counter

n, k = map(int, input().split())
s = list(input())

s_sort = sorted(s)
t = ""

# 元の位置と違う文字の数
diff = 0
# 見終わったけどまだ使ってない文字
counter = Counter(s[:1])
counts = sum(counter.values())

# 1文字目から順に見ていく
for i in range(n):
    # t + c が可能か調べる
    for c in s_sort:
        # t + c の中で元の位置と違う文字の数
        diff1 = diff + (c != s[i])
        # まだ使ってない文字の中で元の位置と違う文字の数
        diff2 = counts - (counter[c] > 0)

        # 両方を足して k 以下ならば t + c が可能
        if diff1 + diff2 <= k:
            t += c
            s_sort.remove(c)
            diff = diff1
            counter = Counter(s[:i + 2]) - Counter(t)
            counts = sum(counter.values())
            break
print(t)