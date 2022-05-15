# https://atcoder.jp/contests/arc140/tasks/arc140_a

from string import ascii_lowercase
d = dict(zip(ascii_lowercase, range(26)))
N, K = map(int, input().split())
S = input()

for i in range(N, 1, -1):
    if N%i: continue # 割り切れないなら不可
    cnts = [[0]*26 for _ in range(N//i)]
    for j in range(N//i):
        for k in range(i):
            # print(i, j, k)
            cnts[j][d[S[j+k*(N//i)]]] += 1
    cnt = 0
    for j in range(N//i):
        cnt += i - max(cnts[j])
    # print(i, N//i, cnt, K)
    # print(cnts)
    if cnt <= K:
        print(N//i)
        break
else:
    print(N)
