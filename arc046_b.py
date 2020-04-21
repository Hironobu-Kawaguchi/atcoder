# https://atcoder.jp/contests/arc046/tasks/arc046_b


def main():
    N = int(input())
    A, B = map(int, input().split())
    if N <= A:
        print("Takahashi")
        return
    else:
        if A == B:
            if N%(A+1):
                print("Takahashi")
                return
            else:
                print("Aoki")
                return
        elif A > B:
            print("Takahashi")
            return
        else:
            print("Aoki")
            return

main()
