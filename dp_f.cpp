// https://atcoder.jp/contests/dp/tasks/dp_f
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
    string s, t;
	cin >> s >> t;

    vector<vector<int>> dp(3010, vector<int>(3010));
    rep(i, s.size()) rep(j, t.size()) {
        if (s[i] == t[j]) dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1);
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j]);
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1]);
    }

    string ans = "";
    int i = s.size(), j = t.size();
    while (i>0 && j>0) {
        if (dp[i][j] == dp[i-1][j]) i--;
        else if (dp[i][j] == dp[i][j-1]) j--;
        else {
            ans += s[i-1];
            i--, j--;
        }
    }
    
    reverse(all(ans));
	cout << ans << endl;
	return 0;
}
