# https://atcoder.jp/contests/ABC284/tasks/abc284_f

import sys
def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
T = input()
T_ord = list(map(lambda c: ord(c) - ord('a') + 1, T))
# print(T_ord)

# 100 の n 乗を前計算
MOD = 2147483647
power100 = [ None ] * (N*2 + 1)
power100[0] = 1
for i in range(N*2):
	power100[i + 1] = power100[i] * 100 % MOD
# print(power100)

# H[1], H[2], ..., H[N] を計算する
H = [ None ] * (N*2 + 1)
H[0] = 0
for i in range(N*2):
	H[i + 1] = (H[i] * 100 + T_ord[i]) % MOD
# print(H)

H2 = [ None ] * (N*2 + 1)
H2[0] = 0
for i in range(N*2):
	H2[i + 1] = (H2[i] * 100 + T_ord[N*2-1-i]) % MOD
# print(H2)

# ハッシュ値を求める関数
# S[l-1:r] のハッシュ値は (H[r] - H[l - 1] * power100[r - l + 1]) % MOD で計算
# C++ とは異なり、（負の値）% M (M >= 1) も 0 以上 M-1 以下になることに注意
def hash_value(l, r, hash=H):
	return (hash[r] - hash[l] * power100[r - l]) % MOD

# # クエリに答える
# for a, b, c, d in queries:
# 	hash1 = hash_value(a, b)
# 	hash2 = hash_value(c, d)
# 	if hash1 == hash2:
# 		print("Yes")
# 	else:
# 		print("No")
for i in range(N+1):
    # print(i, T[i:i+N][::-1])
    # print(hash_value(0, i), T[0:i])
    # print(hash_value(N-i, N, H2), T[::-1][N-i:N])
    # print(hash_value(i+N, N*2))
    # print(hash_value(N, N*2-i, H2))
    if hash_value(0, i)==hash_value(N-i, N, H2) and hash_value(i+N, N*2)==hash_value(N, N*2-i, H2):
        print(T[i:i+N][::-1])
        print(i)
        break
else:
    print(-1)



# import sys
# def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.buffer.readline
# # sys.setrecursionlimit(10 ** 7)

# N = int(input())
# T = input()

# for i in range(N+1):
#     S = T[i:i+N][::-1]
#     # print(i, S)
#     if T[:i]==S[:i] and T[i+N:]==S[i:]:
#         print(S)
#         print(i)
#         break
# else:
#     print(-1)
