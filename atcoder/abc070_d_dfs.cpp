// https://atcoder.jp/contests/abc070/tasks/abc070_d
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
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n;
	cin >> n;
    vector<vector<ll>> g(n, vector<ll>(n, LINF));
    // rep(i,n) rep(j,n) g[i][j] = LINF;
    rep(i,n-1) {
        int a, b, c;
        cin >> a >> b >> c;
        --a, --b;
        g[a][b] = c;
        g[b][a] = c;
    }
    rep(k,n) rep(i,n) rep(j,n) mins(g[i][j], g[i][k] + g[k][j]);
    int q, K;
    cin >> q >> K;
    --K;
    rep(i,q) {
        int x, y;
        cin >> x >> y;
        --x, --y;
        ll ans = g[x][K] + g[K][y];
    	cout << ans << "\n";
    }
	return 0;
}
