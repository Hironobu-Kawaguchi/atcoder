# https://atcoder.jp/contests/abc324/tasks/abc324_a

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))

ans = "Yes"
for i in range(N-1):
    if A[i]!=A[i+1]:
        ans = "No"
        break
print(ans)
