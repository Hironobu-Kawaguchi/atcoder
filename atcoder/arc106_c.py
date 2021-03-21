# https://atcoder.jp/contests/arc106/tasks/arc106_c

def main():
    N, M = map(int, input().split())
    if N==1 and M==0:
        print(1,2)
        return
    if M<0 or M>N-2:
        print(-1)
        return
    ans = []
    x = M+1
    if M==0:
        y = 0
    else:
        y = 1
    z = N - x- y
    for i in range(x):
        ans.append((i*2+2, i*2+3))
    if y:
        ans.append([1, x*2+2])
    for i in range(z):
        ans.append((x*2+3+i*2,x*2+3+i*2+1))
    for L, R in ans:
        print(L, R)
    return

main()
