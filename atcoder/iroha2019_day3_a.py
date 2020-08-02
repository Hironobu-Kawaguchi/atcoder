# A - 宇宙人
# https://atcoder.jp/contests/iroha2019-day3/tasks/iroha2019_day3_a

A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = map(int, input().split())
x1 = A - B
print(x1)
x2 = C + D
print(x2)
x3 = F - E if F > E else 0
print(x3)
x4 = (G + H + I) // 3 + 1
print(x4)
if J == 8:
    x5 = 'dagabaji'
elif J == 7:
    x5 = 'agabaji'
elif J == 6:
    x5 = 'aabaji'
elif J == 5:
    x5 = 'aaaji'
elif J == 4:
    x5 = 'aaai'
elif J == 3:
    x5 = 'aaa'
elif J == 2:
    x5 = 'aa'
elif J == 1:
    x5 = 'a'
else:
    x5 = ''
print(x5)

mcount = 0
num = 62
while mcount < M:
    if num % 59 == K and num % 61 == L:
        x6x = num
        mcount += 1
    num += 1
if x6x >= N + 6:
    x6 = 6
    x7 = x6x
else:
    flg = False
    num = x6x + N
    while flg == False:
        m = 0
        for i in range(1, num):
            if num % i == 0:
                m += i
        if num == m:
            flg = True
        num += 1
    x6 = x6x
    x7 = num
print(x6)
print(x7)

x8 = (O+P+Q)*(R+S+T)*(U+V+W)*(X+Y+Z) % 9973
print(x8)
