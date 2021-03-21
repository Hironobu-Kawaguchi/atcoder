// https://atcoder.jp/contests/caddi2018/tasks/caddi2018_a
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

map<ll, int> prime_factor(ll n) {
    map<ll, int> ret;
    for (ll i=2; i*i <= n; i++) {
        while (n%i==0) {
            ret[i]++;
            n /= i;
        }
    }
    if (n != 1) ret[n] = 1;
    return ret;
}

int main() {
	ll n, p;
	cin >> n >> p;
    ll ans = 1;
    for (auto a : prime_factor(p)) {
        if (a.second >= n) {
            ans *= pow(a.first, a.second/n);
        }
    }
	cout << ans << endl;
	return 0;
}
