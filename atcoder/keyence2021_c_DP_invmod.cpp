// https://atcoder.jp/contests/keyence2021/tasks/keyence2021_c
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
// const ll MOD = 1e9+7;
const ll MOD = 998244353;
using mint = modint998244353;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int h, w, k;
	cin >> h >> w >> k;
    vector<vector<int>> grid(h, vector<int>(w));
    map<char, int> mp={{'R',1}, {'D',2}, {'X',3}};
    rep(i,k) {
        int hh, ww;
        char c;
        cin >> hh >> ww >> c;
        hh--; ww--;
        grid[hh][ww] = mp[c];
    }

    vector<vector<mint>> dp(h, vector<mint>(w));
    dp[0][0] = pow_mod(3, h*w-k, MOD);
    ll invmod3 = inv_mod(3, MOD);
    rep(i,h) rep(j,w) {
        if (i<h-1) {
            if (grid[i][j]==0) dp[i+1][j] += dp[i][j] * 2 * invmod3;
            else if (grid[i][j]!=1) dp[i+1][j] += dp[i][j];
        }
        if (j<w-1) {
            if (grid[i][j]==0) dp[i][j+1] += dp[i][j] * 2 * invmod3;
            else if (grid[i][j]!=2) dp[i][j+1] += dp[i][j];
        }
    }
    // rep(i,h) rep(j,w) cout << dp[i][j].val() << ' ';
	cout << dp[h-1][w-1].val() << "\n";
	return 0;
}
