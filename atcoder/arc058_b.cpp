// https://atcoder.jp/contests/abc042/tasks/arc058_b
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
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

vector<ll> fact(200010), invfact(200010);

ll extgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    ll g = extgcd(b, a%b, x, y);
    ll nextx = y, nexty = x-(a/b)*y;
    x = nextx, y = nexty;
    return g;
}

ll nCr(int n, int r) {
    ll ret = fact[n];
    ret = ret * invfact[n-r] % MOD;
    ret = ret * invfact[r] % MOD;
    return ret;
}

int main() {
	int H, W, A, B;
	cin >> H >> W >> A >> B;
    fact[0] = 1;
    for (int i = 1; i <=200000; i++) {
        fact[i] = (fact[i-1] * i) % MOD;
    }
    for (int i = 0; i <=200000; i++) {
        ll x, y;
        ll g = extgcd(fact[i], MOD, x, y);
        while (x < 0) x += MOD;
        x %= MOD;
        invfact[i] = x;
    }
    ll ans = 0;
    for (int i = B; i < W; i++) {
        ll tmp = nCr((H-A-1)+i, H-A-1);
        tmp = tmp * nCr((A-1)+(W-i-1), A-1) % MOD;
        ans = (ans + tmp) % MOD;
    }
    
	cout << ans << endl;
	return 0;
}
