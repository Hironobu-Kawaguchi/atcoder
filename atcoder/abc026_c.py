# https://atcoder.jp/contests/abc026/tasks/abc026_c

n = int(input())
salary = [1] * n
salary_max = [0] * n
salary_min = [0] * n
boss = [0] * n

for i in range(n-1):
    boss[i+1] = int(input()) - 1

for i in range(n-1, 0, -1):
    salary[i] += salary_max[i] + salary_min[i]
    if salary_min[boss[i]] == 0:
        salary_max[boss[i]] = salary[i]
        salary_min[boss[i]] = salary[i]
    else:
        salary_max[boss[i]] = max(salary_max[boss[i]], salary[i])
        salary_min[boss[i]] = min(salary_min[boss[i]], salary[i])

ans = salary[0] + salary_max[0] + salary_min[0]
print(ans)
