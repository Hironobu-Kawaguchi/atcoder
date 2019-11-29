# https://atcoder.jp/contests/abc012/tasks/abc012_3

N = int(input())
lst = [[] for _ in range(82)]
sm = 0
for i in range(1, 10):
    for j in range(1, 10):
        mul = i*j
        sm += mul
        lst[mul].append(str(i) + ' x ' + str(j))
dif = sm - N
for l in lst[dif]:
    print(l)
