# https://atcoder.jp/contests/abc130/tasks/abc130_d

N, K = map(int, input().split())
a = list(map(int, (input().split())))

ans = 0

# 尺取法
left = 0
right = 0
sums = a[0]
flg = True
while flg:
    if sums >= K:
        ans += N - right
        sums -= a[left]
        left += 1
    elif sums < K and right < N-1:
        right += 1
        sums += a[right]
    else:
        flg = False
    # print(left, right, sums, ans)

print(ans)
