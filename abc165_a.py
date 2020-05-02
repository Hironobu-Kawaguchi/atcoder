# https://atcoder.jp/contests/abc165/tasks/abc165_a
import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

def main():
    K = int(input())
    A, B = map(int, input().split())

    for i in range(A, B+1):
        if i%K==0:
            print("OK")
            return
    else:
        print("NG")
    return
main()

# S = input()
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
