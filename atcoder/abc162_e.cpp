// https://atcoder.jp/contests/abc162/tasks/abc162_e
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

ll mod_pow(ll n, ll p, ll mod=MOD) {
    if(p==0) return 1;
    ll res = mod_pow(n*n%mod, p/2, mod);
    if(p%2==1) res = res * n % mod;
    return res;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, k;
	cin >> n >> k;
    vector<ll> d(k+1);
    for (int i = 1; i <= k; i++) {
        d[i] = mod_pow(k/i, n, MOD);
    }
    for (int i = k; i > 0; i--) {
        for (int j = 2*i; j <= k; j+=i) {
            d[i] -= d[j];
            d[i] %= MOD;
        }        
    }
    ll ans = 0;
    for (int i = 1; i <= k; i++) {
        ans += d[i] * i;
        ans %= MOD;
    }
	cout << ans << "\n";
	return 0;
}

// int n, k;
// ll ans = 0;

// void dfs(int num, ll x) {
//     x %= MOD;
//     if (num==n) {
//         ans += x;
//         ans %= MOD;
//         return;
//     }
//     for (ll i = 1; i <= k; i++) {
//         dfs(num+1, gcd(x, i));
//     }   
//     return;
// }

// int main() {
// 	cin >> n >> k;
//     for (ll i = 1; i <= k; i++) {
//         dfs(1, i);
//     }   
// 	cout << ans << "\n";
// 	return 0;
// }
