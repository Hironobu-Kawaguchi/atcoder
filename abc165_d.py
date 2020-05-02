# https://atcoder.jp/contests/abc165/tasks/abc165_d
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)


def main():
    A, B, N = map(int, input().split())
    x = min(B-1, N)
    ans = (A * (x%B))//B
    print(ans)
    return
main()

# X = int(input())
# S = input()
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
