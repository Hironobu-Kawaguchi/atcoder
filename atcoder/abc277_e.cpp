// https://atcoder.jp/contests/abc277/tasks/abc277_d
// 
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
#include <atcoder/all>
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

struct Edge {
    int to, cost;
};

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, m, k;
	cin >> n >> m >> k;
    int n2 = n*2;
    vector<vector<Edge>> g(n2);
    rep(i,m) {
        int u, v, a;
        cin >> u >> v >> a;
        --u; --v;
        if (a==1) {
            g[u].push_back((Edge{v,1}));
            g[v].push_back((Edge{u,1}));
        } else {
            g[n+u].push_back((Edge{n+v,1}));
            g[n+v].push_back((Edge{n+u,1}));
        }
    }
    rep(i,k) {
        int s;
        cin >> s;
        --s;
        g[s].push_back((Edge{n+s,0}));
        g[n+s].push_back((Edge{s,0}));
    }

    vector<int> dist(n2, INF);
    deque<P> q;
    dist[0] = 0;
    q.emplace_back(0,0);
    while (q.size()) {
        auto [d, v] = q.front(); q.pop_front();
        if (dist[v] != d) continue;
        for (Edge e: g[v]) {
            int nd = d + e.cost;
            if (nd >= dist[e.to]) continue;
            dist[e.to] = nd;
            if (e.cost) q.emplace_back(nd, e.to);
            else       q.emplace_front(nd, e.to);
        }
    }
    int ans = min(dist[n-1], dist[n2-1]);
    if (ans == INF) ans = -1;
	cout << ans << "\n";
	return 0;
}
