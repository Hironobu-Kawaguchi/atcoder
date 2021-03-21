# https://atcoder.jp/contests/abc032/tasks/abc032_c

N, K = map(int, input().split())
s = [int(input()) for _ in range(N)]

if 0 in s:
    ans = N
else:
    ans = 0
    left = 0
    right = 0
    seki = s[0]
    flg = True
    while flg:
        if seki <= K:
            ans = max(ans, right - left + 1)
            if  right < N-1:
                right += 1
                seki *= s[right]
            else:
                flg = False
        elif left < right:
            seki = seki // s[left]
            left += 1
        elif left < N-1:
            left += 1
            right += 1
            seki = s[left]
        else:
            flg = False

print(ans)
