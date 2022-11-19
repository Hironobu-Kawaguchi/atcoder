// https://atcoder.jp/contests/abc275/tasks/abc275_e
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
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;

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
	int n, m, k;
	cin >> n >> m >> k;
    vector dp(k+1, vector(n+1, mint(0)));
    mint m_inv = mint(1) / m;
    dp[0][0] = 1;
    rep(i, k) rep(j, n+1) {
        if (j==n) {
            dp[i+1][j] += dp[i][j];
            continue;
        }
        rep(l, m) {
            int nx = j + l + 1;
            if (nx>n) nx = n*2 - nx;
            dp[i+1][nx] += dp[i][j] * m_inv;
        }
    }
	cout << dp[k][n].val() << "\n";
	return 0;
}
