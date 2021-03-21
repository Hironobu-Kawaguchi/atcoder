import math
import itertools

n = 8
r = 3

ans = len(list(itertools.permutations(range(n), r)))
# ans = len(list(itertools.combinations(range(n), r)))
# for i in itertools.permutations(range(n), r):
# for i in itertools.combinations(range(n), r):
    # ans += 1

print(ans)

print(math.factorial(n) // math.factorial(n-r))
# print(math.factorial(n) // (math.factorial(r) * math.factorial(n-r)))
