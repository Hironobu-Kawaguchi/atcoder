# https://atcoder.jp/contests/tenka1-2012-qualC/tasks/tenka1_2012_9

n = int(input())
prime = []
for i in range(2,n):
    for j in prime:
        if i%j==0:
            break
    else:
        prime.append(i)
print(len(prime))
