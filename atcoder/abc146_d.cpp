// https://atcoder.jp/contests/abc146/tasks/abc146_d
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
#define all(v) (v).begin(),(v).end()
#define chmin(x,y) x = min(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

struct Edge {int to, id;};

vector<vector<Edge>> g;
vector<int> ans;

void dfs(int v, int c=-1, int p=-1) {
    int k = 1;
    rep(i, g[v].size()) {
        int u = g[v][i].to, ei = g[v][i].id;
        if (u == p) continue;
        if (k == c) ++k;
        ans[ei] = k; ++k;
        dfs(u, ans[ei], v);
    }
}

int main() {
	int n;
    cin >>n;
    g.resize(n);
    ans = vector<int>(n-1);
    rep(i, n-1) {
        int a, b;
        cin >> a >> b;
        --a; --b;
        g[a].push_back((Edge){b,i});
        g[b].push_back((Edge){a,i});
    }
    dfs(0);
    int mx = 0;
    rep(i, n) mx = max(mx, int(g[i].size()));
    cout << mx << endl;
    rep(i, n-1) {
    	cout << ans[i] << endl;
    }
	return 0;
}
