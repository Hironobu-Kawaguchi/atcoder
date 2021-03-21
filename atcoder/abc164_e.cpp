// https://atcoder.jp/contests/abc164/tasks/abc164_e
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
// #include<map>
// #include<tuple>
// #include<set>
#include<queue>
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
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

const int MAX_V = 50;
const int MAX_S = MAX_V*50+5;

struct Edge {
    int to, a, b;
    Edge(int to, int a, int b):to(to),a(a),b(b) {}
};

struct Data {
    int v, s;
    ll x;
    Data(int v, int s, ll x):v(v),s(s),x(x) {}
    bool operator<(const Data& a) const {
        return x > a.x;
    }
};

vector<Edge> g[MAX_V];
ll dp[MAX_V][MAX_S+5];

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    int n, m, s;
	cin >> n >> m >> s;
    rep(i,m) {
        int u, v, a, b;
        cin >> u >> v >> a >> b;
        --u; --v;
        g[u].emplace_back(v,a,b);
        g[v].emplace_back(u,a,b);
    }
    vector<int> c(n), d(n);
    rep(i,n) cin >> c[i] >> d[i];
    rep(i,n)rep(j,MAX_S+5) dp[i][j] = LINF;
    s = min(s, MAX_S);
    priority_queue<Data> q;
    auto push = [&](int v, int s, ll x) {
        if (s<0) return;
        if (dp[v][s]<=x) return;
        dp[v][s] = x;
        q.emplace(v,s,x);
    };
    push(0, s, 0);
    while (!q.empty()) {
        Data hoge = q.top(); q.pop();
        int v = hoge.v, s = hoge.s;
        ll x = hoge.x;
        if (dp[v][s] != x) continue;
        {
            int ns = min(s+c[v], MAX_S);
            push(v, ns, x+d[v]);
        }
        for (Edge e: g[v]) {
            push(e.to, s-e.a, x+e.b);
        }
    }
    for (int i = 1; i < n; i++) {
        ll ans = LINF;
        rep(j, MAX_S+5) {
            ans = min(ans, dp[i][j]);
        }
    	cout << ans << endl;
    }
	return 0;
}
