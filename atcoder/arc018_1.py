# https://atcoder.jp/contests/arc018/tasks/arc018_1

Height, BMI = map(float, input().split())
ans = BMI * Height * Height / 10000
print(ans)
