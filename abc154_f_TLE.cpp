// https://atcoder.jp/contests/abc154/tasks/abc154_f
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
#define all(v) (v).begin(),(v).end()
#define chmin(x,y) x = min(x,y)
#define chmax(x,y) x = max(x,y)
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
	ll r1, c1, r2, c2;
	cin >> r1 >> c1 >> r2 >> c2;
    ll ans = 0;
    for (ll i = r1; i <= r2; i++) {
        for (ll j = c1; j <= c2; j++) {
            ans += nCr(i+j, i);
            ans %= MOD;
        }        
    }
    
	cout << ans << endl;
	return 0;
}
