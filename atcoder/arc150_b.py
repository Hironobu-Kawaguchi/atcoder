# https://atcoder.jp/contests/arc142/tasks/arc142_b

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main():
    A, B = map(int, input().split())
    ans = 1001001001
    if A*A<B:
        for x in range(A+10):
            k = (B+A+x-1) // (A+x)
            y = k * (A+x) - B
            if y<0: continue
            ans = min(ans, x+y)
            # print(x, y, k)
    else:
        for k in range(1, B//A+10):
            x = max(0, (B+k-1) // k - A)
            y = k * (A+x) - B
            if y<0: continue
            ans = min(ans, x+y)
            # print(x, y, k)
    print(ans)
    return

T = int(input())
for ti in range(T):
    main()



# import sys
# input = sys.stdin.buffer.readline
# # sys.setrecursionlimit(10 ** 7)

# def main():
#     A, B = map(int, input().split())
#     ans = 1001001001
#     M = int(B**0.5)
#     if A<M:
#         for x in range(A+1):
#             k = (B+A+x-1)//(A+x)
#             y = k*(A+x) - B
#             if y<0: continue
#             ans = min(ans, x+y)
#     else:
#         for k in range(1, (B+A-1)//A + 1):
#             x = max((B+k-1)//k - A, 0)
#             y = k*(A+x) - B
#             if y<0: continue
#             ans = min(ans, x+y)
#     print(ans)
#     return

# T = int(input())
# for t in range(T):
#     main()



# def main():
#     A, B = map(int, input().split())
#     M = int(B**0.5) + 10
#     ans = 1001001001
#     for k in range(1, M):
#         ans = min(ans, (k+1) * max(0, (B-1)//k + 1 - A) + k*A - B)
#     for q in range(M):
#         k = (B-1)//(q+1) + 1
#         ans = min(ans, (k+1) * max(0, (B-1)//k + 1 - A) + k*A - B)
#     print(ans)
#     return

# T = int(input())
# for t in range(T):
#     main()


# WA
# def main():
#     A, B = map(int, input().split())
#     tmp = B//A
#     ans = 1001001001001
#     if tmp!=0:
#         X1 = (B+tmp-1)//tmp - A
#         Y1 = (A+X1)*tmp - B
#         ans = min(ans, X1+Y1)
#         # print(tmp, X1+Y1)
#         for x in range(X1+1, ans+1):
#             tmp2 = (B+A+x-1)//(A+x)
#             if tmp2==0: continue
#             y = (A+x)*tmp2 - B
#             if x+y<ans:
#                 # print(ans, x, y)
#                 ans = x+y
#     Y2 = A*(tmp+1) - B
#     # print(tmp+1, Y2)
#     ans = min(ans, Y2)
#     print(ans)
        
#     return

# T = int(input())
# for t in range(T):
#     main()


