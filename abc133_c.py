# 
L, R = map(int, input().split())

if (L // 2019) == (R //2019):
    LL = L % 2019
    RR = R % 2019
    ans = 2019
    for i in range(LL, RR):
        for j in range(i+1, RR+1):
            ans = min(((i * j) % 2019), ans)
else:
    ans = 0

print(ans)
