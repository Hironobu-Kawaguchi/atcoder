// https://atcoder.jp/contests/abc159/tasks/abc159_f
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
const ll MOD = 998244353;

int main() {
	int n, s;
	cin >> n >> s;
	vector<int> a(n);
	rep(i,n) cin >> a[i];
	vector<vector<vector<ll>>> dp(n+1,vector<vector<ll>>(n+1, vector<ll>(s+1)));
	rep(i,n) dp[i][i][0] = 1;
	rep(i,n) for (int j = i; j < n; j++) rep(k,s+1) {
		if(dp[i][j][k] == 1) {
			dp[i][j+1][k] += dp[i][j][k];
			dp[i][j+1][k] %= MOD;
			if (k+a[j] <=s) {
				dp[i][j+1][k+a[j]] += dp[i][j][k];
				dp[i][j+1][k+a[j]] %= MOD;
			}
		}	
	}
	ll ans = 0;
	rep(i,n) for (int j = i; j < n; j++) {
		ans += dp[i][j+1][s];
		ans %= MOD;
		cout << ans << endl;
	}
	cout << ans << endl;
	return 0;
}
