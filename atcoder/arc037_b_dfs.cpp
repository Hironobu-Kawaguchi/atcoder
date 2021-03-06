// https://atcoder.jp/contests/arc037/tasks/arc037_b
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

const int MAX_N = 100;
bool done[MAX_N], ok;
vector<vector<int>> G(MAX_N);

int dfs(int now, int pre) {
    for (int next: G[now]) {
        if (next==pre) continue;
        if (done[next]) ok = false;
        else {
            done[next] = true;
            dfs(next,now);
        }
    }
    return 0;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, m;
	cin >> n >> m;
    rep(i,m) {
        int u, v;
        cin >> u >> v;
        --u, --v;
        G[u].push_back(v);
        G[v].push_back(u);
    }
    int ans = 0;
    rep(i,n) {
        if(done[i]) continue;
        ok = true;
        dfs(i,-1);
        if(ok) ans++;
    }
	cout << ans << "\n";
	return 0;
}
