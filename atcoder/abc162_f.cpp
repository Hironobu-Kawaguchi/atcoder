// https://atcoder.jp/contests/abc162/tasks/abc162_f
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

int MAXN = 200005;
vector<vector<ll>> dp(MAXN, vector<ll>(3));

int main() {
    int n;
	cin >> n;
    vector<ll> a(n);
    rep(i,n) cin >> a[i];
    bool odd_flg = false;
    if (n%2) odd_flg = true;
    // rep(j,3) dp[0][j] = 0;
    rep(i,n/2) {
        dp[i+1][0] = dp[i][0] + a[i*2];
        dp[i+1][1] = max(dp[i][0]+a[i*2+1], dp[i][1]+a[i*2+1]);
        if(odd_flg) {
            dp[i+1][2] = max(max(dp[i][0]+a[i*2+2], dp[i][1]+a[i*2+2]), dp[i][2]+a[i*2+2]);
        }

    }
    ll ans = max(dp[n/2][0], dp[n/2][1]);
    if(odd_flg) ans = max(ans, dp[n/2][2]);
	cout << ans << "\n";
	return 0;
}
