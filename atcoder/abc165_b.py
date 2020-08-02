# https://atcoder.jp/contests/abc165/tasks/abc165_b
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    X = int(input())
    now = 100
    year = 0
    while now < X:
        add = now//100
        now += add
        year += 1
    print(year)
    return
main()

# S = input()
# A, B = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
