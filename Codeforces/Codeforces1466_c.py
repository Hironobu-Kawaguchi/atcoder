# https://codeforces.com/contest/1466/problem/C
# 回文には必ず2文字か3文字の回文が含まれるので、貪欲に変えていく

t = int(input())
for i in range(t):
    s = input()
    n = len(s)
    used = [False]*n
    ans = 0
    for j in range(n):
        use_need = False
        if j>=1 and s[j]==s[j-1] and not used[j-1]:
            use_need = True
        if j>=2 and s[j]==s[j-2] and not used[j-2]:
            use_need = True
        used[j] = use_need
        ans += use_need
    print(ans)



# ダメ
# # 偶数長含めた回文の長さを求める
# # R[2*i] = L: S[i]を中心とする奇数長の最大回文
# # R[2*i+1] = L: S[i:i+2]を中心とする偶数長の最大回文
# # ダミー文字を挟むが、各 R[i] は実際の回文の文字列長と一致する
# def manacher(S):
#     C = []
#     for a in S:
#         C.append(a)
#         C.append(0)
#     C.pop()

#     L = len(C)

#     R = [0]*L

#     i = j = 0
#     while i < L:
#         while j <= i < L-j and C[i-j] == C[i+j]:
#             j += 1
#         R[i] = j
#         k = 1
#         while j-R[i-k] > k <= i < L-k:
#             R[i+k] = R[i-k]
#             k += 1
#         i += k; j -= k
#     return R

# def main():
#     S = input()
#     res = manacher(S)
#     print(res)
#     return

# t = int(input())
# for i in range(t):
#     main()
