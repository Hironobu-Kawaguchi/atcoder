# https://codeforces.com/contest/1325/problem/D

# import sys
# # input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)


def main():
    u, v = map(int, input().split())
    dif = v-u
    if dif < 0 or dif%2:
        print(-1)
        return
    elif dif == 0 and u == 0:
        print(0)
        return
    elif dif == 0:
        ans = [u]
    else:
        half = dif >> 1
        rest = v - 2 * half
        if rest & half:
            ans = [half, half, rest]
        else:
            ans = [half, half+rest]
    print(len(ans))
    print(*ans)

    # from functools import reduce
    # print(reduce(lambda x, y: x ^ y, ans), sum(ans))
    return

main()
