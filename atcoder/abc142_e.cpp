// https://atcoder.jp/contests/abc142/tasks/abc142_e
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
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
	int N, M;
	cin >> N >> M;
    vector<pair<int, int>> key;
    rep (i, M) {
        int a, b;
        cin >> a >> b;
        int s = 0;
        rep (j, b) {
            int c;
            cin >> c;
            --c;
            s |= 1<<c;
        }
        key.emplace_back(s, a);
    }

    vector<int> dp(1<<N, INF);
    dp[0] = 0;
    rep (s, 1<<N) {
        rep (i, M) {
            int t = s | key[i].first;
            int cost = dp[s] + key[i].second;
            dp[t] = min(dp[t], cost);
        }
    }

    int ans = dp.back();
    if (ans == INF) ans = -1;
	cout << ans << endl;
	return 0;
}
