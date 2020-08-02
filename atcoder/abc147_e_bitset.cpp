// https://atcoder.jp/contests/abc147/tasks/abc147_e
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
#define chmax(x,y) x = max(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

const int D = 80*160+10;    // -80*160:0, 0:D, 80*160:2D
const int D2 = D*2;

int main() {
	int H, W;
	cin >> H >> W;
    vector<vector<int>> A(H, vector<int>(W));
    rep(i, H) rep(j, W) {
        int x;
        cin >> x;
        A[i][j] =x;
    }
    rep(i, H) rep(j, W) {
        int x;
        cin >> x;
        A[i][j] = abs(x - A[i][j]);
    }
    vector<vector<bitset<D2>>> dp(H, vector<bitset<D2>>(W));
    dp[0][0][D-A[0][0]] = 1;
    dp[0][0][D+A[0][0]] = 1;
    rep(i, H) rep(j, W) {
        if (i) {
            dp[i][j] |= dp[i-1][j] << A[i][j];
            dp[i][j] |= dp[i-1][j] >> A[i][j];
        }
        if (j) {
            dp[i][j] |= dp[i][j-1] << A[i][j];
            dp[i][j] |= dp[i][j-1] >> A[i][j];
        }
    }

    int ans = D2;
    rep(i,D2) if (dp[H-1][W-1][i]) {
        ans = min(ans, abs(i-D));
    }
	cout << ans << endl;
	return 0;
}
