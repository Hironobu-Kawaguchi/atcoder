# https://atcoder.jp/contests/arc104/tasks/arc104_c
import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    C = [-1] * (2*N)
    done = [0] * (2*N)
    A, B = [], []
    AB = 0
    for i in range(N):
        a, b = map(int, input().split())
        if a!=-1 and b!=-1:
            if a>=b:
                print('No')
                return
            if done[a-1]:
                print('No')
                return
            else:
                done[a-1] = 1
            if done[b-1]:
                print('No')
                return
            else:
                done[b-1] = 1
            ci = b-a-1
            for j in range(a-1, b):
                if C[j]!=-1 and C[j]!=ci:
                    print('No')
                    return
                else:
                    C[j] = ci
        elif a!=-1:
            A.append(a-1)
            if done[a-1]:
                print('No')
                return
            else:
                done[a-1] = 1
        elif b!=-1:
            B.append(b-1)
            if done[b-1]:
                print('No')
                return
            else:
                done[b-1] = 1
        else:
            AB += 1
    
    A.sort()
    for a in A:
        if C[a]!=-1:
            ci = C[a]
        elif C[a+1]!=-1:
            ci = C[a+1]
        else:
            ci = 1
        if done[a+ci]:
            print('No')
            return
        else:
            done[a+ci] = 1
        if a+ci+1>N:
            print('No')
            return
        for j in range(a,a+ci+2):
            if C[j]!=-1 and C[j]!=ci:
                print('No')
                return
            else:
                C[j] = ci
    B.sort()
    for b in B:
        if C[b]!=-1:
            ci = C[b]
        elif C[b-1]!=-1:
            ci = C[b-1]
        else:
            ci = 1
        if done[b-ci]:
            print('No')
            return
        else:
            done[b-ci] = 1
        if b-ci<0:
            print('No')
            return
        for j in range(b, b-ci-1, -1):
            if C[j]!=-1 and C[j]!=ci:
                print('No')
                return
            else:
                C[j] = ci

    for i in range(2*N):
        if done[i]: continue
        if C[i]==-1: continue
        if i+C[i]+1>N:
            print('No')
            return
        if C[i]==C[i+C[i]+1]:
            for j in range(i, i+C[i]+2):
                if C[j]!=-1 and C[j]!=C[i]:
                    print('No')
                    return
                else:
                    C[j] = C[i]
            done[i] = 1
            done[i+C[i]+1] = 1

    flg = False   # A側をまだ選んでいない
    for i in range(2*N):
        if done[i]: continue
        if flg:
            b = i
            flg = False
            ci = b-a-1
            for j in range(a,b+1):
                if C[j]!=-1 and C[j]!=ci:
                    print('No')
                    return
                else:
                    C[j] = ci
        else:
            a = i
            flg = True

    print('Yes')

main()
