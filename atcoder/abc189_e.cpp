// https://atcoder.jp/contests/abc189/tasks/abc189_e
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
// #include <atcoder/all>
// using namespace atcoder;
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

// アフィン変換
struct A {
    vector<vector<int>> a;
    vector<ll> b;
    A(const vector<vector<int>>& _a = {{1,0},{0,1}},
      const vector<ll>& _b = {0,0}):a(_a), b(_b) {}
    A operator*(const A& x) const {
        A res({{0,0},{0,0}});
        rep(i,2) rep(j,2) rep(k,2) {
            res.a[i][j] += x.a[i][k] * a[k][j];
        }
        res.b = A(x.a)*b;
        rep(i,2) res.b[i] += x.b[i];
        return res;
    }
    vector<ll> operator*(const vector<ll>& x) const {
        vector<ll> res = b;
        rep(i,2) rep(j,2) res[i] += a[i][j] * x[j];
        return res;
    }
    void print() {  // デバッグ用
        // cerr << "----" << endl;
        printf("{");
        rep(i,2) printf("{%d,%d}", a[i][0], a[i][1]);
        printf("} + {%lld, %lld}\n", b[0], b[1]);
    }
};

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, m, q;
	cin >> n;
    vector<vector<ll>> p(n, vector<ll>(2));
    rep(i,n) cin >> p[i][0] >> p[i][1];
    cin >> m;
    vector<A> d(1);  // 行列を格納
    rep(i,m) {
        int op;
        cin >> op;
        A x;  // opを行列にする
        if (op == 1) {
            x = A({{0,1},{-1,0}});
        } else if (op == 2) {
            x = A({{0,-1},{1,0}});
        } else {
            int p;
            cin >> p;
            if (op == 3) x = A({{-1,0},{0,1}}, {2*p,0});
            else         x = A({{1,0},{0,-1}}, {0,2*p});
        }
        // d.back().print();
        // x.print();
        d.emplace_back(d.back()*x);
    }
    cin >> q;
    rep(i,q) {
        int a, b;
        cin >> a >> b;
        --b;
        vector<ll> ans = d[a] * p[b];
        printf("%lld %lld\n", ans[0], ans[1]);
    }
	return 0;
}
