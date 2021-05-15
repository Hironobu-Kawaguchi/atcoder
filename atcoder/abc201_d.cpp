// https://atcoder.jp/contests/abc201/tasks/abc201_d
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
	int h, w;
	cin >> h >> w;
    vector<string> a(h);
    rep(i,h) cin >> a[i];
    vector<vector<int>> point(h, vector<int>(w));
    rep(i,h) rep(j,w) {
        if (a[i][j]=='+') point[i][j] = 1;
        else              point[i][j] = -1;
    }
    // rep(i,h) {
    //     rep(j,w) {
    //         cout << point[i][j];
    //     }
    //     cout << endl;
    // }
    // vector<vector<int>> dp(h, vector<int>(w, -INF));
    vector<vector<int>> dp(h, vector<int>(w));
    rep(i,h) rep(j,w) {
        if ((i+j)%2) dp[i][j] = -INF;
        else         dp[i][j] = INF;
    }
    // dp[0][0] = 0;
    dp[h-1][w-1] = 0;
    // rep(i,h) rep(j,w) {
    for (int i = h-1; i >= 0; i--) for (int j = w-1; j >= 0; j--) {
        if (i>=1 & i<h) {
            if ((i+j)%2==0) dp[i-1][j] = max(dp[i-1][j], dp[i][j] + point[i][j]);
            else            dp[i-1][j] = min(dp[i-1][j], dp[i][j] - point[i][j]);
            // else         dp[i][j] = max(dp[i][j], dp[i-1][j] - point[i][j]);
        }
        if (j>=1 & j<w) {
            if ((i+j)%2==0) dp[i][j-1] = max(dp[i][j-1], dp[i][j] + point[i][j]);
            else            dp[i][j-1] = min(dp[i][j-1], dp[i][j] - point[i][j]);
            // else         dp[i][j] = max(dp[i][j], dp[i][j-1] - point[i][j]);
        }
    }
    // rep(i,h) {
    //     rep(j,w) {
    //         cout << dp[i][j];
    //     }
    //     cout << endl;
    // }
    // if (dp[h-1][w-1] > 0) {
    if (dp[0][0] < 0) {
    	cout << "Takahashi" << endl;
    // } else if (dp[h-1][w-1] == 0) {
    } else if (dp[0][0] == 0) {
    	cout << "Draw" << endl;
    } else {
    	cout << "Aoki" << endl;
    }
	return 0;
}
