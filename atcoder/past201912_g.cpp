// https://atcoder.jp/contests/past201912-open/tasks/past201912_g
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
    vector<vector<ll>> a(n, vector<ll>(n));
    ll tmp;
    rep(i,n-1) rep(j,n-1-i) {
        cin >> tmp;
        a[i][i+j+1] = tmp;
        a[i+j+1][i] = tmp;
    }
    ll ans = -INF;
    ll cmb = pow(3,n);
    for (ll i = 0; i < cmb; i++) {
        vector<vector<ll>> grp(3);
        ll tmp = i;
        rep(j,n) {
            ll flg = tmp%3;
            tmp /= 3;
            if (flg==0) {
                grp[0].push_back(j);
            } else if (flg==1) {
                grp[1].push_back(j);
            } else {
                grp[2].push_back(j);
            }
        }
        ll score = 0;
        rep(i,3) {
            rep(j, grp[i].size()) {
                for (int k = j+1; k < grp[i].size(); k++) {
                    score += a[grp[i][j]][grp[i][k]];
                }
            }
        }
        ans = max(ans, score);
    }
	cout << ans << endl;
	return 0;
}
