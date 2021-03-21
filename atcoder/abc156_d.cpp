// https://atcoder.jp/contests/abc156/tasks/abc156_d
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

// フェルマーの小定理
ll mod_pow(ll n, ll p, ll mod=MOD) {
    if(p==0) return 1;
    ll res = mod_pow(n*n%mod, p/2, mod);
    if(p%2==1) res = res * n % mod;
    return res;
}
ll nCr(ll n, ll r, ll mod=MOD) {
    r = min(r, n-r);
    ll numer = 1, denom = 1;
    rep(i,r) {
        numer *= n-i;
        numer %= mod;
        denom *= i+1;
        denom %= mod;
    }
    return numer * mod_pow(denom, mod-2, mod) % mod;
}

int main() {
	ll n, a, b;
	cin >> n >> a >> b;
    ll ans = mod_pow(2, n) - 1 -nCr(n,a) - nCr(n,b) + MOD * 2;
    ans %= MOD;
	cout << ans << endl;
	return 0;
}
