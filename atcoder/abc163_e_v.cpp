// https://atcoder.jp/contests/abc163/tasks/abc163_e
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
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n;
	cin >> n;
    vector<pair<ll, ll>> ap(n);
    ll a;
    rep(i,n) {
        cin >> a;
        ap[i] = make_pair(a, i);
    }
    sort(ap.begin(), ap.end());
    reverse(ap.begin(), ap.end());
    vector<vector<ll>> dp(n+1, vector<ll>(n+1));
    rep(i,n) rep(j,i+1) {
        dp[i+1][j]   = max(dp[i+1][j],   dp[i][j] + ap[i].first * abs(n-1 - (i-j) - ap[i].second));
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + ap[i].first * abs(ap[i].second - j));
    }
    ll ans = 0;
    rep(i,n+1) ans = max(ans, dp[n][i]);
    cout << ans << endl;
	return 0;
}