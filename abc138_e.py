# https://atcoder.jp/contests/abc138/tasks/abc138_e

import bisect

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)

    l = [[] for _ in range(26)]
    for i in range(n):
        l[ord(s[i]) - ord('a')].append(i)
    for i in range(n):
        l[ord(s[i]) - ord('a')].append(i+n)

    ans = 0
    p = 0
    for i in range(m):
        c = ord(t[i]) - ord('a')
        if len(l[c]) == 0:
            print(-1)
            return
        p = l[c][bisect.bisect_left(l[c], p)] + 1
        if p >= n:
            p -= n
            ans += n
    ans += p
    print(ans)
    return

main()
