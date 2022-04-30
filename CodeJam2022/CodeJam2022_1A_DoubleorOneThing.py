# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8e9c

# from string import ascii_uppercase
# import random

t = int(input())
for x in range(1, t + 1):
    s = input()
    # s = "".join(random.choices(ascii_uppercase, k=10))
    # print("Case #{}: {}".format(x, s))
    ans = ""
    stk = ""
    for i in range(len(s)):
        ans += s[i]
        if i==len(s)-1: continue
        if s[i]==s[i+1]:
            stk += s[i]
        elif s[i]<s[i+1]:
            stk += s[i]
            ans += stk
            stk = ""
        else:
            stk = ""
    print("Case #{}: {}".format(x, ans))

    # n = len(s)
    # cand = []
    # for bi in range(1<<n):
    #     tmp = ""
    #     for j in range(n):
    #         tmp += s[j]
    #         if bi>>j&1:
    #             tmp += s[j]
    #     cand.append(tmp)
    # cand.sort()
    # print("Case #{}: {}".format(x, cand[0]))
