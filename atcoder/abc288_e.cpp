// https://atcoder.jp/contests/abc288/tasks/abc288_e
// https://atcoder.jp/contests/abc288/submissions/38628169
#include<iostream>
// #include<algorithm>
// #include<cmath>
// #include <ctime>
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
	int n, m;
	cin >> n >> m;
    vector<int> a(n), c(n);
    rep(i,n) cin >> a[i];
    rep(i,n) cin >> c[i];

    vector mc(n, vector<int>(n));
    rep(l, n) {
        int now = INF;
        for (int r = l; r < n; r++) {
            now = min(now, c[r]);
            mc[l][r] = now;
        }
    }

    vector<bool> must(n);
    rep(i,m) {
        int x;
        cin >> x;
        must[x-1] = true;
    }
    vector<ll> dp(1);
    rep(i,n) {
        vector<ll> p(dp.size()+1, LINF);
        swap(dp,p);
        rep(j,p.size()) {
            if (!must[i]) dp[j] = min(dp[j], p[j]);
            dp[j+1] = min(dp[j+1], p[j] + a[i] + mc[i-j][i]);
        }
    }

    ll ans = *min_element(dp.begin(), dp.end());
    cout << ans << endl;
	return 0;
}
