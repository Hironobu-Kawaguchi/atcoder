// https://atcoder.jp/contests/abc183/tasks/abc183_e
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
	int h, w;
	cin >> h >> w;
    vector<string> s(h);
    rep(i,h) cin >> s[i];
    vector<vector<ll>> dp(h, vector<ll>(w));
    dp[0][0] = 1;
    int ii, jj;
    rep(i,h) rep(j,w) {
        if (s[i][j]=='#') continue;
        ii = i;
        jj = j;
        while (s[ii][jj]=='.') {
            ii++;
            if (ii>=h) break;
            dp[ii][jj] += dp[i][j];
            dp[ii][jj] %= MOD;
        }
        ii = i;
        jj = j;
        while (s[i][jj]=='.') {
            jj++;
            if (jj>=w) break;
            dp[ii][jj] += dp[i][j];
            dp[ii][jj] %= MOD;
        }
        ii = i;
        jj = j;
        while (s[ii][jj]=='.') {
            ii++;
            if (ii>=h) break;
            jj++;
            if (jj>=w) break;
            dp[ii][jj] += dp[i][j];
            dp[ii][jj] %= MOD;
        }
    }

	cout << dp[h-1][w-1]%MOD << "\n";
	return 0;
}
