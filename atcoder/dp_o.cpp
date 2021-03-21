// https://atcoder.jp/contests/dp/tasks/dp_o
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
    vector<vector<int>> a(N, vector<int>(N));
    rep(i,N) rep(j,N) cin >> a[i][j];

    vector<vector<ll>> dp(30, vector<ll>((1<<21)+10));
    dp[0][0] = 1;

    rep(i,N) rep(s,(1<<N)) {
        if (dp[i][s] != 0) rep(j, N) {
            if (!(s&(1<<j)) && a[i][j]) {
                dp[i+1][s|(1<<j)] = (dp[i+1][s|(1<<j)] + dp[i][s]) % MOD;
            } 
        }
    }
	cout << dp[N][(1<<N)-1] << endl;
	return 0;
}
