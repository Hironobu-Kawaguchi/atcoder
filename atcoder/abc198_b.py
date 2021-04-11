# https://atcoder.jp/contests/abc198/tasks/abc198_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

def main():
    n = input()
    l, r = 0, len(n)-1
    flg = True
    while (l<r):
        if flg and n[r]=='0':
            r -= 1
            continue
        else:
            flg = False
        if n[l]==n[r]:
            l += 1
            r -= 1
        else:
            print("No")
            # print(l, r)
            return
    print("Yes")
    # print(l, r)
    return

main()



# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
