# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_d

M = int(input())
sumd, sumc = 0, 0
for i in range(M):
    d, c = map(int, input().split())
    sumd += d * c
    sumc += c

# tmp = sumd
# while tmp > 10:
#     tmp = tmp // 10
#     sumd += tmp

# for i in range(1, len(str(sumd))):
#     tmp = sumd // (10 ** i)
#     sumd += tmp

tmp = sumd // 10
while tmp > 0:
    pre = sumd
    sumd += tmp
    tmp = sumd // 10 - pre // 10

ans = sumd // 10 + sumc - 1
print(ans)
