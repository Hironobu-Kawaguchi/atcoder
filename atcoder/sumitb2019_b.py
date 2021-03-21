# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b

N = int(input())

ans = (N*100 + 107) // 108

if int(ans * 1.08) == N:
    print(ans)
else:
    print(":(")
