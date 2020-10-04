# https://atcoder.jp/contests/arc104/tasks/arc104_c
import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    A, B = [0]*N, [0]*N
    sz = N*2
    tp = [0] * sz   # tp:その階で乗る人(i+1),降りる人-(i+1)
    com = [-1] * sz # com:乗り降りのペアになる階
    ng = False      # ng == true だったら "No"

    for i in range(N):  # 入力
        A[i], B[i] = map(int, input().split())
        if A[i]!=-1:
            A[i] -= 1
            if tp[A[i]]: ng = True  # 重複あり
            tp[A[i]] = i + 1        # その階で乗る人
        if B[i]!=-1:
            B[i] -= 1
            if tp[B[i]]: ng = True  # 重複あり
            tp[B[i]] = -(i + 1)     # その階で降りる人
        if A[i]!=-1 and B[i]!=-1:
            com[A[i]] = B[i]    # 乗り降りのペア
            com[B[i]] = A[i]    # 乗り降りのペア

    if ng:
        print("No")
        return

    dp = [False] * (sz+1)
    dp[0] = True

    for i in range(sz):
        if not dp[i]: continue
        for j in range(i+1, sz, 2): # i->jがiを含めて偶数だけを見る
            w = (j - i + 1) // 2    # j=i-1+2w, w:移動階数

            ok = True   # ok==true ならj+1階まで(A,B)の組み合わせが可能
            exist = [False] * N

            for k in range(w):  # (A,B)が(i,i+w),(i+1,i+w+1),...(i+k,i+k+w),...,(i+w-1,i+2w-1)の人が乗り降りするような区間に分割できるか
                p = i + k       # (p,q)の移動を考える
                q = i + k + w
                if com[p]!=-1 and not (i<=com[p] and com[p]<=j):
                    ok = False
                if com[q]!=-1 and not (i<=com[q] and com[q]<=j):
                    ok = False

                same = False
                if tp[p]!=0 and tp[q]!=0:   # pもqも乗り降りする人が決まっている
                    if tp[p]<0 or tp[p]+tp[q]!=0:   # pが降りる階 or pとqが乗り降りのペアでない
                        ok = False
                    else:
                        same = True     # p,qが乗り降りのペア

                if tp[p]<0 or tp[q]>0:
                    ok = False
                else:
                    if tp[p]!=0:        # pで乗る人が決まっている
                        v = tp[p] - 1   # v:pで乗る人
                        if exist[v]: ok = False
                        exist[v] = True
                    if not same and tp[q]!=0:   # qで降りる人が決まっている and p,qは乗り降りのペアじゃない
                        v = -tp[q] - 1          # v:qで降りる人
                        if exist[v]: ok = False
                        exist[v] = True
            
            if ok: dp[j+1] = True
    
    if dp[sz]: print("Yes")
    else:      print("No")
    return

main()
