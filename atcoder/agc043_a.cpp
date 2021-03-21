// https://atcoder.jp/contests/agc043/tasks/agc043_a
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
	int h, w;
	cin >> h >> w;
    vector<string> s(h);
    rep(i,h) cin >> s[i];
    vector<vector<int>> dp(h, vector<int>(w, INF));
    if(s[0][0]=='#') dp[0][0] = 1;
    else             dp[0][0] = 0;
    rep(i,h) rep(j,w) {
        if (i) {
            if (s[i][j]=='#' && s[i-1][j]=='.') dp[i][j] = min(dp[i][j], dp[i-1][j] + 1);
            else                                dp[i][j] = min(dp[i][j], dp[i-1][j]);
        }
        if (j) {
            if (s[i][j]=='#' && s[i][j-1]=='.') dp[i][j] = min(dp[i][j], dp[i][j-1] + 1);
            else                                dp[i][j] = min(dp[i][j], dp[i][j-1]);
        }
    }
	cout << dp[h-1][w-1] << endl;
	return 0;
}
