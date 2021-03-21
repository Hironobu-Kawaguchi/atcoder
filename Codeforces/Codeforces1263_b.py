# https://codeforces.com/contest/1263/problem/B

digits = '0123456789'

def main():
    n = int(input())
    p = [input() for _ in range(n)]
    s = set()
    step = 0
    for i in range(n):
        num = p[i]
        if num not in s:
            s.add(num)
            continue
        else:
            state = False
            for j in range(4):
                for digit in digits:
                    temp = list(num)
                    temp[j] = digit
                    temp = ''.join(temp)
                    if temp not in s and temp not in p:
                        step += 1
                        s.add(temp)
                        p[i] = temp
                        state = True
                        break
                if state:
                    break
    print(step)
    for i in range(n):
        print(p[i])

t = int(input())
for _ in range(t):
    main()


# # WA
# t = int(input())
# for i in range(t):
#     ans = 0
#     n = int(input())
#     lines = []
#     s = set()
#     for j in range(n):
#         line = input()
#         if line in s:
#             ans += 1
#             plus = 0
#             while line in s:
#                 plus += 1
#                 keta = 3 - plus // 10
#                 chg = str((int(line[keta]) + 1) % 10)
#                 tmp = ''
#                 for k in range(4):
#                     if k == keta:
#                         tmp += chg
#                     else:
#                         tmp += line[k]
#                 line = tmp
#         s.add(line)
#         lines.append(line)
#     print(ans)
#     for line in lines:
#         print(line)
