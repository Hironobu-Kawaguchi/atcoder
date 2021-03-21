# https://atcoder.jp/contests/abc144/tasks/abc144_c

def main():
    N = int(input())
    imax = int(N**0.5)
    for i in range(imax, 0, -1):
        if N % i == 0:
            j = N//i
            print(i + j - 2)
            return
    print('No')
    return

main()
