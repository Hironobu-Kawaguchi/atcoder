// https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_d
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
	int N, M;
	cin >> N >> M;

    vector<tuple<int, int, ll>> LRC(M);
    int l, r;
    ll c;
    rep(i, M) {
        cin >> l >> r >> c;
        --l, --r;
        LRC[i] = forward_as_tuple(l, r, c);
    }
    sort(all(LRC));

    vector<ll> dp(N, LINF);
    dp[0] = 0;

    rep(i, M) {
        tie(l, r, c) = LRC[i];
        // cout << l << r << c << endl;
        if (dp[l] == LINF) continue;
        for (int j = l+1; j <= r; j++) {
            dp[j] = min(dp[j], dp[l] + c);
        }       
    }

    // rep(j, N) cout << dp[j] << ' ';

    if (dp[N-1] == LINF) cout << -1 << endl;
    else cout << dp[N-1] << endl;
	return 0;
}
