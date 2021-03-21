# https://atcoder.jp/contests/abc093/tasks/arc094_a

ABC = list(map(int, input().split()))

ans = 0
samenum = 0
for i in range(3):
    num = (max(ABC) - ABC[i]) // 2
    ABC[i] += num * 2
    ans += num
    if ABC[i] == max(ABC):
        samenum += 1

if samenum == 2:
    ans += 2
elif samenum == 1:
    ans += 1

print(ans)
