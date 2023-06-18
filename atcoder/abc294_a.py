# https://atcoder.jp/contests/abc294/tasks/abc294_a

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main():
    N = int(input())
    A = list(map(int, (input().split())))
    ans = []
    for i in range(N):
        if A[i]%2==0:
            ans.append(A[i])
    print(*ans)
    return

main()


    # S = input()
    # N = int(input())
    # N, K = map(int, input().split())
    # A = list(map(int, (input().split())))
    # A = [[int(i) for i in input().split()] for _ in range(N)]
