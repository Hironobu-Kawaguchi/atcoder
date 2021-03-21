// https://atcoder.jp/contests/abc187/tasks/abc187_e
// https://atcoder.jp/contests/abc187/submissions/19167133
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

int n;
vector<vector<int>> es;
vector<int> a, b;
vector<int> depth;
vector<ll> dp;

// 深さを求めるDFS
void DepthDFS(int a, int d) {
    depth[a] = d;
    for (int next : es[a]) {
        if (depth[next] == -1) {
            DepthDFS(next, d+1);
        }
    }
}

// 差分から実際の値に変換するDFS
void ImosDFS(int a, ll now) {
    now += dp[a];
    dp[a] = now;
    for (int next : es[a]) {
        if (depth[next] > depth[a]) {
            ImosDFS(next ,now);
        }
    }
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    cin >> n;
    // es = vector<vector<int>>(n);
    // a = vector<int>(n);
    // b = vector<int>(n);
    es.resize(n);
    a.resize(n-1);
    b.resize(n-1);
    depth = vector<int>(n, -1);
    // dp = vector<ll>(n, 0);
    dp.resize(n);
    rep(i,n-1) {
        cin >> a[i] >> b[i];
        a[i]--; b[i]--;
        es[a[i]].push_back(b[i]);
        es[b[i]].push_back(a[i]);
    }
    DepthDFS(0,0);
    int q;
    cin >> q;
    int t, e, x;
    int va, vb;
    rep(qi,q) {
        cin >> t >> e >> x;
        e--;
        if (t==1) {
            va = a[e];
            vb = b[e];
        } else {
            va = b[e];
            vb = a[e];
        }
        // 通る方が上、通らない方が下
        if (depth[va] < depth[vb]) {
            // 根に足す
            dp[0] += x;
            // 通らない方を引く
            dp[vb] -= x;
        } else {  //通るほうが下
            ///部分木に足す
            dp[va] += x;
        }
    }
    ImosDFS(0,0);
    rep(i,n) cout << dp[i] << "\n";
	return 0;
}
