// https://atcoder.jp/contests/abc079/tasks/abc079_d
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
	int h, w;
	cin >> h >> w;
    vector<vector<int>> c(10, vector<int>(10));
    rep(i,10) rep(j,10) cin >> c[i][j];
    rep(k,10) rep(i,10) rep(j,10) chmin(c[i][j], c[i][k] + c[k][j]);
    int ans = 0, A;
    rep(i,h) rep(j,w) {
        cin >> A;
        if (A>=0) ans += c[A][1];
    }
	cout << ans << endl;
	return 0;
}
