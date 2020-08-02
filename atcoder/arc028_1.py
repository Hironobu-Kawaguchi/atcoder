# https://atcoder.jp/contests/arc028/tasks/arc028_1

N, A, B = map(int, input().split())
mod = N % (A+B)
if 1 <= mod <= A:
    print("Ant")
else:
    print("Bug") 
