// https://atcoder.jp/contests/abc208/tasks/abc208_d
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
	// cout << "check" << "\n";
	int n, m;
	cin >> n >> m;
    vector<vector<vector<int>>> d(n, vector<vector<int>>(n, vector<int>(n, INF)));
    // int d[400][400][400];
    // rep(x,400) rep(i,400) rep(j,400) d[x][i][j] = INF;
	// cout << "check" << "\n";
    rep(i,m) {
        int a, b, c;
        cin >> a >> b >> c;
        // rep(x, n) d[x][a-1][b-1] = c;
        d[0][a-1][b-1] = c;
    }
	// cout << "check" << "\n";
    rep(k,n) {
        // if (k>x) break;
        if(k!=0) rep(i,n) rep(j,n) d[k][i][j] = d[k-1][i][j];
        rep(i,n) rep(j,n) {
            d[k][i][j] = min(d[k][i][j], d[k][i][k] + d[k][k][j]);
        }
    }
    ll ans = 0;
	// cout << "check" << "\n";
    rep(i,n) rep(j,n) {
        if (i==j) continue;
        if (d[n-1][i][j]==INF) continue;
        rep(x,n) {
            if (d[x][i][j]==INF) continue;
            ans += d[x][i][j];
        }
    }
	cout << ans << "\n";
	return 0;
}
