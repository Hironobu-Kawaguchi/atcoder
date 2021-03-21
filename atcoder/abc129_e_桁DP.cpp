// https://atcoder.jp/contests/abc129/tasks/abc129_e
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
    string L;
    cin >> L;
    int n = L.size();
    vector<vector<ll>> dp(2, vector<ll>(n+1));    // 0: イコール, 1: 未満
    dp[0][0] = 1;
    rep(i,n) {
        if(L[i]=='1') {
            dp[0][i+1] = (dp[0][i] * 2) % MOD;
            dp[1][i+1] = (dp[0][i] + dp[1][i] * 3) % MOD;
        } else {
            dp[0][i+1] = dp[0][i];
            dp[1][i+1] = (dp[1][i] * 3) % MOD;
        }
    }
	cout << (dp[0][n] + dp[1][n]) % MOD << endl;
	return 0;
}
