# https://atcoder.jp/contests/abc200/tasks/abc200_e

def main():
    N, K = map(int, input().split())

    def c2(s):
        if s<0: return 0
        return s*(s-1)//2

    def f(s):
        res = c2(s-1)
        res -= c2(s-1-N)*3
        res += c2(s-1-N*2)*3
        res -= c2(s-1-N*3)
        return res

    def f2(s):
        l = max(1, s-N)
        r = min(N, s-1)
        if l>r: return 0
        return r-l+1

    for s in range(3, N*3+1):
        x = f(s)
        if K>x:
            K -= x
        else:
            for a in range(1, N+1):
                x = f2(s-a)
                if K>x:
                    K -= x
                else:
                    for b in range(1, N+1):
                        c = s-a-b
                        if c<=0 or c>N: continue
                        if K>1:
                            K -= 1
                        else:
                            print(a, b, c)
                            return

main()



# N, K = map(int, input().split())

# cum = 0
# for sum_ijk in range(3, 3*N+1):
#     comb = 0
#     for i in range(1, min(N,sum_ijk-2)+1):
#         comb += min(min(N, sum_ijk-(i-1)-2), max(0, 2*N-(sum_ijk-i)+1))
#     # print(sum_ijk, comb)
#     if cum+comb>=K:
#         break
#     cum += comb
# # print(K, cum, sum_ijk)

# cum2 = 0
# for i in range(max(1,sum_ijk-2*N), min(sum_ijk-2,N)+1):
#     if K-cum-cum2 > sum_ijk-i-1:
#         cum2 += sum_ijk-i-1
#     else:
#         j = (K-cum-cum2) + max(1, sum_ijk-i-N) - 1
#         cum2 += K-cum-cum2
#         break
# # print(K, cum+cum2)
# print(i, j, sum_ijk-i-j)



# from itertools import product
# N = 6
# cnt = [0]*(3*N+1)
# for i, j, k in product(range(1,N+1), repeat=3):
#     cnt[i+j+k] += 1

# print('sum', sum(cnt))
# for K in range(3, 3*N+1):
#     # ncr = (N+i-3-2)*(N+i-4-2)//2
#     comb = 0
#     for i in range(1, min(N,K-2)+1):
#         comb += min(min(N, K-(i-1)-2), max(0, 2*N-(K-i)+1))
#     print(K, cnt[K], comb)
