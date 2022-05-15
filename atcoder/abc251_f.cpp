// https://atcoder.jp/contests/abc251/tasks/abc251_e
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

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> to(n);
    rep(i,m) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        to[u].push_back(v);
        to[v].push_back(u);
    }

    {
        vector<bool> visited(n);
        auto dfs = [&](auto dfs, int v) -> void {
            visited[v] = true;
            for (int u : to[v]) {
                if (visited[u]) continue;
                dfs(dfs, u);
                printf("%d %d\n", u+1, v+1);
            }
        };
        dfs(dfs, 0);
    }

    {
        vector<int> dist(n, INF);
        queue<int> q;
        dist[0] = 0;
        q.push(0);
        while (q.size()) {
            int v = q.front(); q.pop();
            for (int u : to[v]) {
                if (dist[u] != INF) continue;
                dist[u] = dist[v] + 1;
                q.push(u);
                printf("%d %d\n", u+1, v+1);
            }
        }                
    }

	return 0;
}
