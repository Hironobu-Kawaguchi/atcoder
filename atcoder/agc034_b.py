# B - ABC
# https://atcoder.jp/contests/agc034/tasks/agc034_b

s = input()
n = len(s)
ans = 0
numa = 0
i = 0
while i < n-1:  # 最後'BC'以外は、最後の文字は関係ないので s[n-1]は不要
    if s[i] == 'A':
        numa += 1   # Aが連続で続く場合は数える
    elif s[i:i+2] == 'BC':
        ans += numa # AAAA と BC を入れ替える回数。またBCが来たら加算する
        i += 1  # BCの場合は、2文字進めるので+1
    else:
        numa = 0
    i += 1
print(ans)


# s = list(input())
# n = len(s)
# ans = 0
# i = 0
# while i < n-2:  # 3文字なので
#     if s[i:i+3] == ['A', 'B', 'C']:
#         s[i:i+3] = ['B', 'C', 'A']
#         ans += 1
#         i = max(i-1, 0)   # 1つ前がAの場合をチェック
#     else:
#         i += 1

# print(ans)

# import numpy as np
# s = np.array(list(input()))
# n = len(s)
# ans = 0
# i = 0
# while i < n-2:  # 3文字なので
#     if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
#         s[i:i+3] = ['B', 'C', 'A']
#         ans += 1
#         i = max(i-1, 0)   # 1つ前がAの場合をチェック
#     else:
#         i += 1

# print(ans)

