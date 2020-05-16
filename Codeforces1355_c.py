# https://codeforces.com/contest/1355/problem/C

def main():
    a,b,c,d = map(int, input().split())
    cnt = [0]*(b+c+1)
    mid1 = min(a+c, 2*b)
    mid2 = max(a+c, 2*b)
    for z in range(c+1, b+c+1):
        if z < a+b: continue
        if z > 2*c: continue
        if z < mid1:
            cnt[z] = z-a-b+1
        elif z > mid2:
            cnt[z] = b+c-z+1
        else:
            cnt[z] = mid1-a-b+1
    # print(cnt[c+1:])
    # print(sum(cnt[c+1:]))
    cum = [0]*(b+c+2)
    for z in range(b+c, c, -1):
        cum[z] = cum[z+1] + cnt[z]
    # print(cum[c+1:])
    res = sum(cum[c+1:d+2])
    return res

print(main())
