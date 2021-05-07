# create_test

import random
# MAX = 10**6
MAX = 10**5
# MAX = 10**4

t = 10000
# t = 4
print(t)
# for i in range(t):
#     # print(random.randint(1,min((i+1)*100,MAX)), random.randint(1,min((i+1)*100,MAX)))
#     print(random.randint(1,min((i+1)*100,MAX)), random.randint(1,min((i+1)*100,MAX)))

for _ in range(t):
    # N = random.randint(1,MAX)
    N = random.randint(1,20)
    print(N)

    a = [random.randint(1, 10**9) for _ in range(N)]
    # a = [i+1 for i in range(N)]
    print(*a)

    # for i in range(N-1):
    #     # print(random.randint(1,i+1), i+2)
    #     print(i+1, i+2)
