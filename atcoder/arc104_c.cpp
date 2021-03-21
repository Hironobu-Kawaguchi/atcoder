// https://atcoder.jp/contests/arc104/tasks/arc104_c
// https://atcoder.jp/contests/arc104/submissions/17081716
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
// #include<map>
// #include<tuple>
// #include<set>
// #include<queue>
// #include<deque>
// #include<regex>
// #include<bitset>
// #include<iomanip>
// #include<complex>
// #include<stack>
// #include<functional>

#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define drep(i,n) for(int i = (n-1); i >= 0; i--)
#define all(v) (v).begin(),(v).end()
#define maxs(x,y) (x = max(x,y))
#define mins(x,y) (x = min(x,y))
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
    int N;
    cin >> N;
    vector<int> A(N), B(N);
    int sz = N * 2;
    vector<int> tp(sz), com(sz, -1);    // tp:その階で乗る人(i+1),降りる人-(i+1), com:乗り降りのペアになる階

    bool ng = false;    // ng == true だったら "No"

    rep(i, N) {
        cin >> A[i] >> B[i];    // 入力
        if (A[i] != -1) {
            --A[i];
            if (tp[A[i]]) ng = true;    // 重複
            tp[A[i]] = i + 1;   // その階で乗る人
        }
        if (B[i] != -1) {
            --B[i];
            if (tp[B[i]]) ng = true;    // 重複
            tp[B[i]] = -(i + 1);    // その階で降りる人
        }

        if (A[i] != -1 && B[i] != -1) {
            com[A[i]] = B[i];   // 乗り降りのペア
            com[B[i]] = A[i];   // 乗り降りのペア
        }
    }
    if (ng) {
        puts("No");
        return 0;
    }

    vector<bool> dp(sz + 1);
    dp[0] = true;

    rep(i, sz) {
        if (!dp[i]) continue;
        for (int j = i + 1; j < sz; ++j) {
            int w = j - i + 1;      // j=i-1+2w
            if (w & 1) continue;    // i->jが同じ移動階数の組み合わせであるかを見るがiを含めて偶数だけを見る
            w /= 2;     // w:移動階数
            bool ok = true;     // ok==true ならj+1階まで(A,B)の組み合わせが可能
            vector<bool> exist(N);

            rep(k, w) { // (A,B)が(i,i+w),(i+1,i+w+1),...(i+k,i+k+w),...,(i+w-1,i+2w-1)の人が乗り降りするような区間に分割できるか
                int p = i + k, q = i + k + w;   // (p,q)の移動を考える
                if (com[p] != -1 && !(i <= com[p] && com[p] <= j)) {    // 確定している乗り降りペアが範囲外だったらダメ
                    ok = false;
                }
                if (com[q] != -1 && !(i <= com[q] && com[q] <= j)) {    // 確定している乗り降りペアが範囲外だったらダメ
                    ok = false;
                }

                // bool same = true;   // ???意味わからん
                bool same = false;
                if (tp[p] != 0 && tp[q] != 0) { // pもqも乗り降りする人が決まっている
                    if (tp[p] < 0 || tp[p] + tp[q] != 0) {  // pが降りる階 or pとqが乗り降りのペアでない
                        ok = false;
                    } else {
                        same = true;    // p,qが乗り降りのペア
                    }
                }
                if (tp[p] < 0 || tp[q] > 0) {   // pが降りる階 or qが乗る階
                    ok = false;
                } else {
                    if (tp[p] != 0) {       // pで乗る人が決まっている
                        int v = tp[p] - 1;  // v:pで乗る人
                        if (exist[v]) {
                            ok = false;
                        }
                        exist[v] = true;
                    }
                    if (!same && tp[q] != 0) {  // qで降りる人が決まっている and p,qは乗り降りのペアじゃない
                        int v = -tp[q] - 1;     // v:qで降りる人
                        if (exist[v]) {
                            ok = false;
                        }
                        exist[v] = true;
                    }
                }
            }
            if (ok) {
                dp[j + 1] = true;
            }
        }
    }
    puts(dp[sz] ? "Yes" : "No");

    return 0;
}
