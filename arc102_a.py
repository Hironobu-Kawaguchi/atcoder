# https://atcoder.jp/contests/abc108/tasks/arc102_a

N, K = map(int, input().split())

# Kの倍数3つの組み合わせ
ans = (N // K) ** 3

# Kで割った余りがK/2になる数3つの組み合わせ
if K % 2 == 0:
    ans += ((N + K//2) //K) ** 3

print(ans)


# # TLE

# N, K = map(int, input().split())

# ans = 0
# for a in range(1, N+1):
#     cnt = 0
#     tmp = K - a % K
#     if tmp > N:
#         continue
#     for b in range(tmp, N+1, K):
#         if K - b % K != tmp:
#             continue
#         for c in range(tmp, N+1, K):
#             cnt += 1
#     ans += cnt

# print(ans)
