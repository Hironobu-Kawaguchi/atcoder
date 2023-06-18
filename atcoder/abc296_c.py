# https://atcoder.jp/contests/abc296/tasks/abc296_b

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main() -> None:
    # Get the number of elements and the difference
    N, X = map(int, input().split())
    # Get the set of elements
    A = set(map(int, (input().split())))
    # Check if each element is in the set
    for a in A:
        # If the difference is in the set, print "Yes"
        if a+X in A:
            print("Yes")
            return
    # If the difference is not in the set, print "No"
    print("No")
    return

main()



# import sys
# input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)
# import bisect

# def main():
#     N, X = map(int, input().split())
#     A = list(map(int, (input().split())))
#     A.sort()
#     for i in range(N):
#         j = bisect.bisect_left(A, A[i] + X)
#         # print(i, j)
#         if j<N and A[i]+X==A[j]:
#             print("Yes")
#             return
#     print("No")
#     return

# main()
