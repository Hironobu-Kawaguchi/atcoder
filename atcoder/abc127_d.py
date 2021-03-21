# D - Integer Cards
# https://atcoder.jp/contests/abc127/tasks/abc127_d
# A*1枚 と C*B枚 全てから上位N枚の合計を出せばよい（2回以上の入れ替えば無駄）

N, M = map(int, input().split())
A = list(map(int, input().split()))
p = [[A[i], 1] for i in range(N)]   # Aのカードは各1枚ずつ

for i in range(M):
    B, C = map(int, input().split())
    p.append([C, B])    # CのカードをB枚追加

p.sort()
p.reverse()

ans = 0
cnt = N
for v, n in p:
    num = min(cnt, n)    # 残り枚数とvのカード枚数の少ない方を採用
    ans += v * num
    cnt -= num
    if cnt == 0:
        break

print(ans)



# import heapq
        
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# heapq.heapify(A)

# for i in range(M):
#     B, C = map(int, input().split())
#     for j in range(B):
#         if A[0] < C:
#             heapq.heapreplace(A, C)
#         else:
#             break
#     print(i, A)

# ans = sum(A)
# print(ans)



# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort()

# for i in range(M):
#     B, C = map(int, input().split())
#     for j in range(B):
#         if A[j] < C:
#             A[j] = C
#         else:
#             break
#     A.sort()
#     # print(i, A)

# ans = sum(A)
# print(ans)
