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

const int MAX_N = 2005;
int n;
vector<pair<ll, int>> A(MAX_N);
vector<vector<ll>> dp(MAX_N, vector<ll>(MAX_N));

// void dfs(int x, int l) {
//     if (x==n) return;
//     dp[x+1][l+1] = max(dp[x+1][l+1], dp[x][l] + A[x].first * abs(A[x].second - l));
//     dfs(x+1, l+1);
//     dp[x+1][l]   = max(dp[x+1][l], dp[x][l] + A[x].first * abs(A[x].second - (n-1-(x-l))));
//     dfs(x+1, l);
// }

int main() {
	cin >> n;
    rep(i,n) {
        ll a;
        cin >> a;
        A[i] = make_pair(a, i);
    }
    sort(A.begin(),A.end());
    reverse(A.begin(),A.end());

    // dfs(0, 0);
    rep(x,n) rep(l,x+1) {
        dp[x+1][l+1] = max(dp[x+1][l+1], dp[x][l] + A[x].first * abs(A[x].second - l));
        dp[x+1][l]   = max(dp[x+1][l], dp[x][l] + A[x].first * abs(A[x].second - (n-1-(x-l))));
    }
    ll ans = 0;
    // rep(i,n) {
    //     cout << dp[1][i] << endl;
    // }
    rep(i,n) {
        ans = max(ans, dp[n][i]);
        // cout << dp[n][i] << endl;
    }
	cout << ans << "\n";
	return 0;
}
