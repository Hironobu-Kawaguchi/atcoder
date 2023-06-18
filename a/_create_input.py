# input.txtを作成し，テキストを書き込むpythonコード
import random

MAX_N = 2*10**5
# N = random.randint(1, MAX_N)
# N = 40000
N = MAX_N
# A = [random.randint(1, N) for _ in range(N)]
A = []
M = 100000
for i in range(M):
    A.extend([random.randint(i*(N//M)+1, (i+1)*(N//M)) for _ in range(N//M)])

with open("input.txt", "w") as f:
    f.write(str(N))
    f.write("\n")
    f.write(" ".join(map(str, A)))
    f.write("\n")
