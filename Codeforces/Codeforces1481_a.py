# https://codeforces.com/contest/1481/problem/A

# import sys
# sys.setrecursionlimit(10 ** 7)
# import copy
from collections import Counter

def main():
    px, py = map(int, input().split())
    s = input()
    cnt = Counter(s)
    # print(cnt)
    if -cnt['L'] <= px <= cnt['R'] and -cnt['D'] <= py <= cnt['U']:
        print('YES')
    else:
        print('NO')
    return

t = int(input())
for i in range(t):
    main()
