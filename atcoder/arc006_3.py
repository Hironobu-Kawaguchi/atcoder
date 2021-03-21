# C - 積み重ね
# https://atcoder.jp/contests/arc006/tasks/arc006_3

n = int(input())
w = [int(input()) for i in range(n)]

ans = 0
# 積み重ねた山の一番上のダンボール
top = []

for i in w:
    # 山を順番に見る
    for j in range(len(top) + 1):
        # 載せられる山がなければ新しい山を作る
        if j == len(top):
            ans += 1
            top.append(i)
        # 載せられる山があればそこに載せる
        if top[j] >= i:
            top[j] = i
            break

print(ans)