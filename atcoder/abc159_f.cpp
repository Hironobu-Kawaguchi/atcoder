// https://atcoder.jp/contests/abc159/tasks/abc159_f
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

// auto mod int
// https://youtu.be/L8grWxBlIZ4?t=9858
// https://youtu.be/ERZuLAxZffQ?t=4807 : optimize
// https://youtu.be/8uowVvQ_-Mo?t=1329 : division
const int mod = 998244353;
struct mint {
  ll x; // typedef long long ll;
  mint(ll x=0):x((x%mod+mod)%mod){}
  mint operator-() const { return mint(-x);}
  mint& operator+=(const mint a) {
    if ((x += a.x) >= mod) x -= mod;
    return *this;
  }
  mint& operator-=(const mint a) {
    if ((x += mod-a.x) >= mod) x -= mod;
    return *this;
  }
  mint& operator*=(const mint a) { (x *= a.x) %= mod; return *this;}
  mint operator+(const mint a) const { return mint(*this) += a;}
  mint operator-(const mint a) const { return mint(*this) -= a;}
  mint operator*(const mint a) const { return mint(*this) *= a;}
  mint pow(ll t) const {
    if (!t) return 1;
    mint a = pow(t>>1);
    a *= a;
    if (t&1) a *= *this;
    return a;
  }

  // for prime mod
  mint inv() const { return pow(mod-2);}
  mint& operator/=(const mint a) { return *this *= a.inv();}
  mint operator/(const mint a) const { return mint(*this) /= a;}
};
istream& operator>>(istream& is, const mint& a) { return is >> a.x;}
ostream& operator<<(ostream& os, const mint& a) { return os << a.x;}


int main() {
    int n, s;
    cin >> n >> s;
    vector<int> a(n);
    rep(i,n) cin >> a[i];
    vector<mint> dp(s+1);
    mint ans = 0;
    rep(i,n) {
        dp[0] += 1;     // Lがここからを足す
        vector<mint> dpNext(s+1);
        rep(j,s+1) {
            dpNext[j] += dp[j];                         // a[i]を選ばない
            if (j+a[i] <= s) dpNext[j+a[i]] += dp[j];   // a[i]を選ぶ
        }
        dp = dpNext;
        ans += dp[s];   // Rがここまでを足す
    }
    cout << ans << endl;
    return 0;
}

// int main() {
// 	int n, s;
// 	cin >> n >> s;
// 	vector<int> a(n);
// 	rep(i,n) cin >> a[i];
// 	vector<vector<vector<ll>>> dp(n+1,vector<vector<ll>>(s+1, vector<ll>(3)));
// 	// dp[0][0][0] = 1;
//     rep(i,n+1) dp[i][0][0] = 1;
// 	rep(i,n) rep(j,s+1) {
//         // a[i]を選ばない場合
//         // (dp[i+1][j][0] += dp[i][j][0]) %= MOD;
//         (dp[i+1][j][1] += dp[i][j][0] + dp[i][j][1]) %= MOD;
//         (dp[i+1][j][2] += dp[i][j][0] + dp[i][j][1] + dp[i][j][2]) %= MOD;
// 		if(j + a[i] <= s) { // a[i]を選ぶ場合
//             (dp[i+1][j+a[i]][1] += dp[i][j][0] + dp[i][j][1]) %= MOD;
//             (dp[i+1][j+a[i]][2] += dp[i][j][0] + dp[i][j][1]) %= MOD;
// 		}
// 	}
// 	cout << dp[n][s][2] << endl;
// 	return 0;
// }
