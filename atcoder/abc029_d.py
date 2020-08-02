# D - 1
# https://abc029.contest.atcoder.jp/tasks/abc029_d

N = input()
ans = 0
for i in range(len(N)):
    left = int(N[:i])+1 if i > 0 else 1
    if N[i] == '0':
        left -= 1

    if i == len(N)-1:
        ans += left
        # print(i, ans, left)
    elif N[i] == '1':
        ans += (left -1) * 10 ** (len(N)-i-1) + (int(N[i+1:])+1)
        # print(i, ans, left, (left -1) * 10 ** (len(N)-i-1) + (int(N[i+1:])+1))
    else:
        ans += left * 10 ** (len(N)-i-1)
        # print(i, ans, left, left * 10 ** (len(N)-i-1))
print(ans)


# N = int(input())
n = int(N)
ans = 0
for i in range(n+1):
    x = str(i)
    ans += x.count('1')
print(ans)
