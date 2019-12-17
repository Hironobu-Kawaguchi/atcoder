# https://atcoder.jp/contests/arc046/tasks/arc046_a

N = int(input())

ans, num = 0, 0
while num < N:
    ans += 1
    s = str(ans)
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            break
    else:
        num += 1

print(ans)
