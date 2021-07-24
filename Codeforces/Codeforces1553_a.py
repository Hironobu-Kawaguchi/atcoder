# http://codeforces.com/contest/1553/problem/A

def S(x):
    res = 0
    while x>0:
        x, y = divmod(x, 10)
        res += y
    return res

def main():
    n = int(input())
    # ss = []
    # for i in range(n+1):
    #     ss.append(S(i+1))
    # ans = 0
    # for i in range(n):
    #     if ss[i+1]<ss[i]:
    #         ans += 1
    # print(ans)
    ans, mod = divmod(n, 10)
    if mod==9: ans += 1
    print(ans)
    return

t = int(input())
for i in range(t):
    main()
