# https://atcoder.jp/contests/abc177/tasks/abc178_e

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c, d = [0]*(n+1), [0]*(n+1)
    for i in range(n):
        c[a[i]] += 1
        d[b[i]] += 1
    for i in range(1,n+1):
        if c[i]+d[i]>n:
            print("No")
            return
    for i in range(1,n+1):
        c[i] = c[i] + c[i-1]
        d[i] = d[i] + d[i-1]
    x = 0
    for i in range(1,n+1):
        x = max(x, c[i]-d[i-1])
    print("Yes")
    ans = b[n-x:] + b[:n-x]
    print(*ans)
    return

main()



# WA
# def main():
#     from collections import Counter
#     import bisect
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     cnta = Counter(a)
#     cntb = Counter(b)
#     for k,v in cnta.items():
#         if v + cntb[k] > n:
#             print("No")
#             return
#     print("Yes")
#     ans = [0]*n
#     for kb, vb in sorted(cntb.items(), key=lambda x:x[1], reverse=True):
#         for ka, va in sorted(cnta.items(), key=lambda x:x[1], reverse=True):
#             if ka==kb: continue
#             r = bisect.bisect_right(a, ka)
#             chg = min(va, vb)
#             for i in range(chg):
#                 ans[r-va+i] = kb
#             vb -= chg
#             cnta[ka] -= chg
#             if vb==0: break
#     print(*ans)
#     return

# main()
