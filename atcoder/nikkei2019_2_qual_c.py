# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_c
# https://atcoder.jp/contests/nikkei2019-2-qual/submissions/8359475

def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines

    import numpy as np

    N = int(readline())
    A = np.array(readline().split(), np.int32)
    B = np.array(readline().split(), np.int32)

    idx = B.argsort(); B = B[idx]; A = A[idx]

    Asorted = np.msort(A)
    if any(Asorted > B):
        print('No')
        return

    if any(Asorted[1:] <= B[:-1]):
        print('Yes')
        return

    perm = A.argsort().tolist()
    x = 0
    period = 0
    while True:
        period += 1
        x = perm[x]
        if x == 0:
            break

    print('Yes' if period != N else 'No')
    return

main()

# import numpy as np
# N = int(input())
# A = np.array(list(map(int, input().split())))
# B = np.array(list(map(int, input().split())))
# cnt = np.count_nonzero(A>B)

# if cnt > (N-2)*2:
#     print("No")
# elif all(np.sort(A) <= np.sort(B)):
#     print("Yes")
# else:
#     print("No")
