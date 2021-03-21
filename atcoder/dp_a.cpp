// https://atcoder.jp/contests/dp/tasks/dp_a
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
    vector<int> h(N);
    rep(i, N) cin >> h[i];
    vector<int> dp(100010);
    dp[0] = 0;
    for (int i = 1; i < N; i++) {
        if (i == 1) dp[i] = dp[0] + abs(h[0] - h[1]);
        else {
            dp[i] = min(dp[i-1] + abs(h[i-1]-h[i]), 
                        dp[i-2] + abs(h[i-2]-h[i]));
        }
    }   

	cout << dp[N-1] << endl;
	return 0;
}
