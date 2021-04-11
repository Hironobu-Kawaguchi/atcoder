// https://atcoder.jp/contests/arc116/tasks/arc116_c
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

using mint = modint998244353;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, m;
	cin >> n >> m;

    // DPによるTLE解法
    vector<vector<mint>> dp(n, vector<mint>(m+1));
    rep(i,m) dp[0][i+1] = 1;
    // rep(i,m) cout << dp[0][i+1].val();
    rep(i,n-1) {
        rep(j,m) {
            for (int k = j+1; k <= m; k+=(j+1)) {
                dp[i+1][k] += dp[i][j+1];
            }
        }
    }
    rep(i,n) {
        mint ansx = 0;
        rep(j,m) ansx += dp[i][j+1];
        cout << ansx.val() << ' ';
    }
    cout << endl;

    mint div1 = 0, div2 = 0;  // div1:1以外の約数の数, div2:自分以外の約数の数
    for (int i = 2; i <= m; i++) {
        div1 += m / i;
        int j = i;
        while (j<=m) {
            div2 += m / j - 1;
            j *= i;
        }
    }
    mint ans = m;
    rep(i,n-1) {
        cout << ans.val() << ' ';
        if (i>0) {
            mint div3 = div2 + i - 1;
            div1 += div3;
        }
        ans += div1;
    }
    cout << ans.val() << endl;
    cout << div1.val() << ' ' << div2.val() << endl;
	return 0;
}
