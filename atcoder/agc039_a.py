# https://atcoder.jp/contests/agc039/tasks/agc039_a

S = input()
K = int(input())

num = 0
tmp = 1
flg = True
for i in range(1, len(S)):
    if S[i] == S[i-1]:
        tmp += 1
    else:
        num += tmp // 2
        if flg:
            fst = tmp   # 最初
            flg = False
        tmp = 1
num += tmp // 2

if flg: # 全部同じ
    ans = (len(S) * K) // 2
elif S[0] == S[-1] and tmp % 2 and fst % 2:
    ans = num * K + K - 1
else:
    ans = num * K 

print(ans)
