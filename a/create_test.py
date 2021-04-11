# create_test

import random
MAX = 10**5
# MAX = 10**4

N = MAX
print(N)

# Cs = [random.randint(1, MAX) for _ in range(N)]
Cs = [i+1 for i in range(N)]
print(*Cs)

for i in range(N-1):
    # print(random.randint(1,i+1), i+2)
    print(i+1, i+2)
