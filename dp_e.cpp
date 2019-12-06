// https://atcoder.jp/contests/dp/tasks/dp_e
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
#define all(v) (v).begin(),(v).end()
#define chmin(x,y) x = min(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;


int main() {
	int N, W;
	cin >> N >> W;
    vector<int> w(N), v(N);
    rep(i, N) cin >> w[i] >> v[i];

    vector<vector<ll>> dp(110, vector<ll>(101010));
    int maxV = N*1000;
    rep(i, N+1) rep(j, maxV+1) dp[i][j] = LINF;
    dp[0][0] = 0;

    rep(i, N) rep(j, maxV+1) {
        dp[i+1][j] = min(dp[i+1][j], dp[i][j]);
        dp[i+1][j+v[i]] = min(dp[i+1][j+v[i]], dp[i][j]+w[i]);
    }

    ll ans = 0;
    rep(j, maxV+1) {
        if (dp[N][j] <= W) ans = j;
    }
	cout << ans << endl;
	return 0;
}
