// https://atcoder.jp/contests/abc179/tasks/abc179_d
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
// const ll MOD = 1e9+7;
const ll MOD = 998244353;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, k;
	cin >> n >> k;
    vector<int> l(k), r(k);
    rep(i,k) cin >> l[i] >> r[i];
    vector<ll> dp(n+1), dpsum(n+1);
    dp[1] = 1, dpsum[1] = 1;
    for (int i = 2; i <= n; ++i) {
        rep(j,k) {
            int li = i-r[j];
            int ri = i-l[j];
            if (ri < 0) continue;
            li = max(li, 1);
            dp[i] += dpsum[ri] - dpsum[li-1];
            dp[i] %= MOD;
        }
        dpsum[i] = dpsum[i-1] + dp[i];
    }
    cout << dp[n] << endl;
	return 0;
}

// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	int n, k;
// 	cin >> n >> k;
//     vector<P> s;
//     rep(i,k) {
//         int l, r;
//         cin >> l >> r;
//         s.push_back(make_pair(l,r));
//     }
//     vector<ll> dp(2*n);
//     dp[n] = 1;
//     ll cum = 0;
//     rep(i,n-1) {
//         for (P p: s) {
//             cum += dp[i+n+1-p.first];
//             cum -= dp[i+n+1-p.second-1];
//             cum += 2 * MOD;
//             cum %= MOD;
//         }
//         dp[i+n+1] = cum;
//     }
//     cout << dp[2*n-1] << endl;
// 	return 0;
// }

// TLE
// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	int n, k;
// 	cin >> n >> k;
//     vector<int> s;
//     rep(i,k) {
//         int l, r;
//         cin >> l >> r;
//         for (int d = l; d <= r; d++) {
//             s.push_back(d);
//         }
//     }
//     vector<ll> dp(n);
//     dp[0] = 1;
//     rep(i,n-1) {
//         for (int d: s) {
//             if(i+1>=d) {
//                 dp[i+1] += dp[i+1-d];
//                 dp[i+1] %= MOD;
//             }
//         }
//     }
//     cout << dp[n-1] << endl;
// 	return 0;
// }
