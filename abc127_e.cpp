// https://atcoder.jp/contests/abc127/tasks/abc127_e
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
	int N, M, K;
	cin >> N >> M >> K;
    ll ans = 0;
    // 2点の差がxになる組み合わせは同じ行でM-x通り、2点の行の組み合わせはN*N通り
    rep(x, M) ans += (ll)x * (M-x) * N*N;
    rep(y, N) ans += (ll)y * (N-y) * M*M;
    ans %= MOD;
    // 2点以外(K-2)をN*M-2のマスに配置する組み合わせはnCr(N*M-2, K-2)通り
    ans *= nCr(N*M-2, K-2, MOD);
    ans %= MOD;

	cout << ans << endl;
	return 0;
}
