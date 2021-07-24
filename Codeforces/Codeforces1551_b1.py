# http://codeforces.com/contest/1551/problem/B1

from collections import Counter

def main():
    s = input().rstrip()
    cnt = Counter(s)
    color_nums = 0
    for k, v in cnt.items():
        color_nums += min(v, 2)
    ans = color_nums // 2
    print(ans)
    return

t = int(input())
for i in range(t):
    main()
