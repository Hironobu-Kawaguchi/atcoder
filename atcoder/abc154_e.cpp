// https://atcoder.jp/contests/abc154/tasks/abc154_e
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

ll solve(string n, ll k){
    ll size = n.size();
    if(size < k) return 0;
    if(k == 0) return 1;
    ll ans = 0;
    // n より桁数が少ないもの
    if(size > k) ans += nCr(size-1, k) * pow(9LL, k);
    // n と桁数が同じで、最上位が n[0] より小さいもの
    ans += (n[0] - '1') * nCr(size-1, k-1) * pow(9LL, k-1);
    // n と桁数が同じで、最上位が n[0] と同じもの
    ll at = 1;
    while(n[at] == '0') at++;
    ans += solve(n.substr(at, size - at), k-1);
    return ans;
}

int main() {
	string n;
    ll k;
	cin >> n >> k;
	cout << solve(n, k) << endl;
	return 0;
}
