# https://codeforces.com/contest/1325/problem/B

# import sys
# # input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = len(set(a))
    print(ans)

t = int(input())
for i in range(t):
    main()
