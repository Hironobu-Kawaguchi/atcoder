// https://atcoder.jp/contests/practice2/tasks/practice2_a
// https://atcoder.github.io/ac-library/production/document_ja/dsu.html
#include <bits/stdc++.h>
#include <atcoder/all>
// #include <atcoder/dsu>
// #include <cstdio>
using namespace std;
using namespace atcoder;

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
    int n, q;
    // scanf("%d %d", &n, &q);
    cin >> n >> q;
    dsu d(n);
    for (int i = 0; i < q; i++) {
        int t, u, v;
        // scanf("%d %d %d", &t, &u, &v);
        cin >> t >> u >> v;
        if (t == 0) {
            d.merge(u, v);
        } else {
            if (d.same(u, v)) {
                // printf("1\n");
                cout << 1 << endl;
            } else {
                // printf("0\n");
                cout << 0 << endl;
            }
        }
    }
    return 0;
}
