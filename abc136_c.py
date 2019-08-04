# https://atcoder.jp/contests/abc136/tasks/abc136_c

N = int(input())
H = list(map(int, input().split()))[::-1]

ans = 'Yes'
for i in range(1, N):
    if H[i] == H[i-1] + 1:
        H[i] -= 1
    elif H[i] > H[i-1] + 1:
        ans = 'No'
        break

print(ans)
