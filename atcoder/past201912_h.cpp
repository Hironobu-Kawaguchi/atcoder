// https://atcoder.jp/contests/past201912-open/tasks/past201912_h
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
    vector<ll> c(n);
    ll minall = INF, minodd = INF;
    rep(i,n) {
        cin >> c[i];
        minall = min(minall, c[i]);
        if(i%2==0) minodd = min(minodd, c[i]);
    }
    ll sellall = 0, sellodd = 0;
    vector<ll> sell(n,0);
    int q, type;
    ll x, a;
    cin >> q;
    rep(i,q) {
        cin >> type;
        if(type==1) {
            cin >> x >> a;
            if(c[x-1]-sell[x-1]-sellall-sellodd*(x%2) >= a) {
                sell[x-1] += a;
                minall = min(minall, c[x-1]-sell[x-1]-sellall-sellodd*(x%2));
                if(x%2) minodd = min(minodd, c[x-1]-sell[x-1]-sellall-sellodd);
            }
        } else if (type==2) {
            cin >> a;
            if(minodd >= a) {
                sellodd += a;
                minodd -= a;
                minall = min(minall, minodd);
            }
        } else {
            cin >> a;
            if(minall >= a) {
                sellall += a;
                minall -= a;
                minodd -= a;
            }
        }
    }
    ll ans = sellall * n + sellodd * ((n+1)/2);
    rep(i,n) ans += sell[i];
	cout << ans << endl;
	return 0;
}
