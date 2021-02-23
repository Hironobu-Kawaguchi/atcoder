# https://atcoder.jp/contests/abc192/tasks/abc192_d

def main():
    X = input()
    M = int(input())
    if len(X)==1:
        if int(X)<=M: print(1)
        else:         print(0)
        return
    
    d = 0
    for c in X: d = max(d, int(c))

    ac = d
    wa = M+1
    while wa - ac > 1:
        wj = (ac+wa)//2
        v = 0
        for c in X:
            if v > M/wj:
                v = M+1
                break
            v = v*wj + int(c)
        if v<=M: ac = wj
        else:    wa = wj
    
    print(ac-d)
    return

main()
