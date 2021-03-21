# https://atcoder.jp/contests/abc098/tasks/abc098_c

N = int(input())
S = input()

sumsW = [0]
sumsE = [0]

cnt = 0
for i in range(N):
    if S[i] == 'W':
        cnt += 1
    sumsW.append(cnt)

cnt = 0
for j in range(N-1, -1, -1):
    if S[j] == 'E':
        cnt += 1
    sumsE.append(cnt)
sumsE.reverse()

ans = 3 * 10**5
for i in range(N+1):
    ans = min(sumsW[i] + sumsE[i], ans)
    
print(ans)
