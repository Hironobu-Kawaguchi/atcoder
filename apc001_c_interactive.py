# https://atcoder.jp/contests/apc001/tasks/apc001_c

N = int(input())

def ask(i):
    print(i, flush=True)
    s = input()
    if s == "Vacant":
        exit()
    return s

s = ask(0)

L = 0
R = N
s_L = s
s_R = s
for _ in range(19):
    M = (L+R)//2
    s_M = ask(M)
    if ((M-L)%2) ^ (s_L == s_M):
        L = M
        s_L = s_M
    else:
        R = M
        s_R = s_M
