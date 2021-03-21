# https://atcoder.jp/contests/abc162/tasks/abc162_d

from collections import Counter
N = int(input())
S = input()

C = Counter(S)
ans = C['R']*C['G']*C['B']

for w in range(1, (N+1)//2+1):
    for i in range(N-(w*2)):
        if S[i]!=S[i+w] and S[i]!=S[i+2*w] and S[i+w]!=S[i+2*w]:
            ans -= 1
print(ans)


# X, Y, Z = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
