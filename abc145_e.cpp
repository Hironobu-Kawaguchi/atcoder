// https://atcoder.jp/contests/abc145/tasks/abc145_e
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

vector<vector<int>> dp(3005, vector<int>(3005));

int main() {
	int N, T;
	cin >> N >> T;
    vector<P> p(N);
    rep(i,N) cin >> p[i].first >> p[i].second;
    sort(all(p));

    int ans = 0;
    rep(i,N) {
        rep(j, T) {
            chmax(dp[i+1][j], dp[i][j]);
            int nj = j + p[i].first;
            if (nj<T) chmax(dp[i+1][nj], dp[i][j]+p[i].second);
        }
        int now = dp[i][T-1] + p[i].second;
        chmax(ans, now);
    } 

	cout << ans << endl;
	return 0;
}
