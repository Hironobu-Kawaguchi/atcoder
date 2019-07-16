# A - Limited Insertion
# https://atcoder.jp/contests/agc032/tasks/agc032_a


n = int(input())
bs = list(map(int, input().split()))

ans = []

for i in range(n):
    for j in range(n-i, 0, -1):
        if bs[j-1] == j:
            ans.append(j)
            del bs[j-1]
            break
if len(ans) == n:
    ans = ans[::-1]
    for a in ans:
        print(a)
else:
    print(-1)

"""
n = int(input())
bs = list(map(int, input().split()))
ans = [0] * n

def chk(numbers, ans, n):
    m = len(numbers)
    if m == 1:
        if numbers == [1]:
            ans[n-1] = 1
            return True
        else:
            return False
    cnt = 0
    for i, b in enumerate(numbers):
        if b == i+1:
            cnt += 1
            ans[n-m] = b
            tempns = numbers.copy()
            tempns.pop(i)
            if chk(tempns, ans, n):
                return True
    if cnt == 0:
        ans[n-m] = 0
    return False

chk(bs, ans, n)

if 0 in ans:
    print(-1)
else:
    ans = ans[::-1]
    for a in ans:
        print(a)
"""