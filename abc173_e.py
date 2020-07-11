# https://atcoder.jp/contests/abc173/tasks/abc173_e
import sys
input = sys.stdin.buffer.readline
MOD = 10**9 + 7
N, K = map(int, input().split())
A = list(map(int, (input().split())))
pos, neg = [], []
for a in A:
    if a<0:
        neg.append(a)   # 負
    else:
        pos.append(a)   # 0以上
if pos:
    if N==K:    # 全て選択で負の数が奇数ならfalse（正にできない）
        ok = (len(neg)%2 == 0)
    else:
        ok = True
else:
    ok = (K%2 == 0) # すべて負で奇数ならfalse（正にできない）
ans = 1
if ok == False: # false（正にできない）場合、絶対値が小さいものからk個かける
    A.sort(key=abs)
    for i in range(K):
        ans *= A[i]
        ans %= MOD
else:
    pos.sort()              # 後ろから取っていくので正は昇順
    neg.sort(reverse=True)  # 後ろから取っていくので負は降順
    if K%2:
        ans *= pos.pop()    # kが奇数個なら1個は正を選ぶ
    p = []  # 2個ずつかけた数を格納
    while len(pos)>=2:
        p.append(pos.pop() * pos.pop())
    while len(neg)>=2:  # 負を2回かけるのでxは正
        p.append(neg.pop() * neg.pop())
    p.sort(reverse=True)
    for i in range(K//2):   # 降順にk//2個見ていく
        ans *= p[i]
        ans %= MOD
print(ans)
