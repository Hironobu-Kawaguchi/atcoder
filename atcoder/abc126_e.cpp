// https://atcoder.jp/contests/abc126/tasks/abc126_e
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
#include<vector>
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
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

const ll MAXN = 100010;
ll N, M;
vector<vector<ll>> g(MAXN);
vector<bool> vis(MAXN);

void dfs(ll x) {
    if (vis[x]) return;
    vis[x] = 1;
    for (ll y:g[x]) dfs(y);
}

int main() {
	cin >> N >> M;
    rep (i, M) {
        ll X, Y, Z;
        cin >> X >> Y >> Z;
        --X;
        --Y;
        g[X].push_back(Y);
        g[Y].push_back(X);
    }

    ll ans = 0;
    rep (i, N) vis[i] = 0;
    rep (i, N) {
        if (vis[i] == 0) {
            dfs(i);
            ++ans;
        }
    }

	cout << ans << endl;
	return 0;
}
