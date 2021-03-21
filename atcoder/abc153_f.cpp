// https://atcoder.jp/contests/abc153/tasks/abc153_f
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
    ll d, a;
	cin >> n >> d >> a;
    vector<P> p(n);
    rep(i,n) cin >> p[i].first >> p[i].second;
    sort(all(p));
    d *= 2;
    ll tot = 0;
    queue<pair<ll, ll>> q;
    ll ans = 0;
    rep(i,n) {
        ll x = p[i].first;
        ll h = p[i].second;
        while (q.size() && q.front().first < x) {
            tot -= q.front().second;
            q.pop();
        }
        h -= tot;
        if (h>0) {
            ll num = (h+a-1)/a;
            ans += num;
            ll damage = num*a;
            tot += damage;
            q.emplace(x+d, damage);
        }
    }
	cout << ans << endl;
	return 0;
}
