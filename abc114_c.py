"""
C - 755
https://atcoder.jp/contests/abc114/tasks/abc114_c
整数 N が与えられます。1 以上 N 以下の整数のうち、七五三数 は何個あるでしょうか？
ここで、七五三数とは以下の条件を満たす正の整数です。
十進法で表記したとき、数字 7, 5, 3 がそれぞれ 1 回以上現れ、これら以外の数字は現れない。
"""
"""
N = int(input())
def dfs(s):
    if int(s) > N:
        return 0
    ret = 1 if all(s.count(c) > 0 for c in "753") else 0
    for c in "753":
        ret += dfs(s + c)
    return ret
print(dfs("0"))
"""
from itertools import product
N = int(input())
cnt = 0
for i in range(3, len(str(N))+1):
    for p in product(["7", "5", "3"], repeat = i):
        if "7" in p and "5" in p and "3" in p:
            n = int("".join(p))
            if n <= N:
                cnt += 1
print(cnt)