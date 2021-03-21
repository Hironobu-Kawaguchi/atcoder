// https://atcoder.jp/contests/abc129/tasks/abc129_c
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
#define drep(i,n) for(int i = (n-1); i >= 0; i--)
#define all(v) (v).begin(),(v).end()
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
	int n, m;
	cin >> n >> m;
    vector<int> a(m), dp(n+2);
    dp[0] = 0, dp[1] = 1;
    rep(i,m) {
        cin >> a[i];
        if (i && a[i] == a[i-1] + 1) {
            cout << 0 << endl;
            return 0;
        }
        dp[a[i]+1] = -1;
    }
    rep(i,n) {
        if (dp[i+2] != -1) {
            dp[i+2] = max(dp[i+1],0) + max(dp[i],0);
            dp[i+2] %= MOD;
        }
    }
	cout << dp[n+1] << endl;
	return 0;
}
