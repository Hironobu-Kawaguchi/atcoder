// https://atcoder.jp/contests/abc175/tasks/abc175_e
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

int a[3005][3005];
ll dp[3005][3005][4];

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	ll r, c, k;
	cin >> r >> c >> k;
    rep(i,k) {
        int _r, _c, _v;
        cin >> _r >> _c >> _v;
        a[_r-1][_c-1] = _v;
    }
    rep(i,r) rep(j,c) {
        for (int k = 2; k >= 0; k--) {    // i,j にあるアイテムを選ぶ
            chmax(dp[i][j][k+1], dp[i][j][k] + a[i][j]);
        }
        rep(k,4) {    // 次に移動する、この時点ではアイテムは選ばない
            chmax(dp[i+1][j][0], dp[i][j][k]);
            chmax(dp[i][j+1][k], dp[i][j][k]);
        }        
    }
    ll ans = 0;
    rep(k,4) chmax(ans, dp[r-1][c-1][k]);
    cout << ans << "\n";
	return 0;
}
