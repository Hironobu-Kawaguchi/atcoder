// https://atcoder.jp/contests/dp/tasks/dp_c
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
	int N;
	cin >> N;
    vector<vector<int>> a(101010, vector<int>(3));
    rep(i, N) rep(j, 3) cin >> a[i][j];

    vector<vector<int>> dp(100010, vector<int>(3));
    rep(j, 3) dp[0][j] = 0;

    rep(i, N) rep(j, 3) rep(k, 3) {
        if (j == k) continue;
        dp[i+1][k] = max(dp[i+1][k], dp[i][j] + a[i][k]);
    }

    int ans = 0;
    rep(j, 3) ans = max(ans, dp[N][j]);
	cout << ans << endl;
	return 0;
}
