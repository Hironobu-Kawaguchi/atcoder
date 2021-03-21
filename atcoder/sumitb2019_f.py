# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_f

import fractions
def main():
    T1, T2 = map(int, input().split())
    f = fractions.gcd(T1, T2)
    T1 //= f
    T2 //= f
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())
    f = fractions.gcd(fractions.gcd(A1, A2), fractions.gcd(B1, B2))
    A1 //= f
    A2 //= f
    B1 //= f
    B2 //= f

    dif_half = T1*A1 - T1*B1
    dif_full = T1*A1 + T2*A2 - T1*B1 - T2*B2

    if dif_full == 0 or A1 == B1:
        print("infinity")
        return
    elif dif_full * dif_half > 0:   # 増減が入れ替わらない場合は会うことはない
        print(0)
        return
    elif dif_full > 0:
        flg = 1
    else:
        flg = -1

    if flg == 1 and dif_half <= 0:
        ans = 1
    elif flg == -1 and dif_half >= 0:
        ans = 1
    else:
        ans = 0

    ans += (- dif_half // dif_full) * 2 - (- dif_half % dif_full == 0)

    print(ans)

main()


# TLE
# import fractions
# def main():
#     T1, T2 = map(int, input().split())
#     f = fractions.gcd(T1, T2)
#     T1 //= f
#     T2 //= f
#     A1, A2 = map(int, input().split())
#     B1, B2 = map(int, input().split())
#     f = fractions.gcd(fractions.gcd(A1, A2), fractions.gcd(B1, B2))
#     A1 //= f
#     A2 //= f
#     B1 //= f
#     B2 //= f

#     a_half = T1*A1
#     a_full = a_half + T2*A2
#     b_half = T1*B1
#     b_full = b_half + T2*B2

#     if a_full == b_full:
#         print("infinity")
#         return
#     elif a_full > b_full:
#         flg = 1
#     else:
#         flg = -1

#     if flg == 1 and a_half <= b_half:
#         ans = 1
#     elif flg == -1 and a_half >= b_half:
#         ans = 1
#     else:
#         ans = 0

#     a = a_full
#     b = b_full
#     while True:
#         if flg == 1 and a + a_half < b + b_half:
#             ans += 2
#         elif flg == -1 and a + a_half > b + b_half:
#             ans += 2
#         elif a + a_half == b + b_half:
#             ans += 1
#         else:
#             break
#         a += a_full
#         b += b_full

#     print(ans)

# main()
