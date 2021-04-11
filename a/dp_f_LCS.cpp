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
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define drep(i,n) for(int i = (n-1); i >= 0; i--)
#define all(v) (v).begin(),(v).end()
#define maxs(x,y) (x = max(x,y))
#define mins(x,y) (x = min(x,y))
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	string s, t;
	cin >> s >> t;
    vector<vector<int>> dp(1+s.size(), vector<int>(1+t.size(), 0));
    rep(i,s.size()) rep(j,t.size()) {
        if (s[i]==t[j]) dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1);
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j]);
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1]);
    }

    string ans = "";
    int i = s.size(), j = t.size();
    while (i>0 && j>0) {
        if (dp[i][j]==dp[i-1][j]) i--;
        else if (dp[i][j]==dp[i][j-1]) j--;
        else {
            ans += s[i-1];
            i--; j--;
        }
    }
    reverse(ans.begin(), ans.end());

	cout << ans << "\n";
	return 0;
}
