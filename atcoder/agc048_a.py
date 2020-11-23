# https://atcoder.jp/contests/agc048/tasks/agc048_a

def main():
    S = input()
    if S>'atcoder':
        return 0
    for i in range(len(S)):
        if S[i] != 'a':
            if S[i]<='t':
                return i
            else:
                return i-1
    return -1

T = int(input())
for i in range(T):
    print(main())
