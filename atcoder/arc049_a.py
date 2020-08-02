# https://atcoder.jp/contests/arc049/tasks/arc049_a

S = input()
A, B, C, D = map(int, input().split())
ans = S[:A]
ans += '"'
ans += S[A:B]
ans += '"'
ans += S[B:C]
ans += '"'
ans += S[C:D]
ans += '"'
ans += S[D:]
print(ans)
