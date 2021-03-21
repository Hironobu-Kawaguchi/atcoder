// https://atcoder.jp/contests/arc035/tasks/arc035_b
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
ll gcd(ll a, ll b) { return b?gcd(b,a%b):a;}
ll lcm(ll a, ll b) { return a/gcd(a,b)*b;}

int main() {
	int n;
	cin >> n;
    vector<int> T(n);
    rep(i,n) cin >> T[i];
    sort(T.begin(), T.end());

    vector<ll> f(10001);
    f[0] = 1;
    rep(i,10000) f[i+1] = f[i]*(i+1)%MOD;

    ll ans1 = 0, cum = 0;
    rep(i,n) {
        cum += T[i];
        ans1 += cum;
    }
	cout << ans1 << endl;

    ll ans2 = 1;
    vector<int> cnt(10001, 0);
    rep(i,n) cnt[T[i]]++;
    rep(i,10001) {
        if (cnt[i]) {
            ans2 *= f[cnt[i]];
            ans2 %= MOD;
        }
    }
	cout << ans2 << endl;
	return 0;
}
