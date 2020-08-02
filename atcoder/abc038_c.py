# https://atcoder.jp/contests/abc038/tasks/abc038_c

N = int(input())
a = list(map(int, input().split()))

sums, tmps = [1], [1]
for i in range(1, N):
    if a[i] > a[i-1]:
        tmps.append(tmps[i-1] + 1)
        sums.append(sums[i-1] + tmps[i])
    else:
        tmps.append(1)
        sums.append(sums[i-1] + tmps[i])

print(sums[N-1])
