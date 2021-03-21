// https://atcoder.jp/contests/agc014/tasks/agc014_b
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
	int n, m;
	cin >> n >> m;
    vector<int> d(n);
    rep(i,m) {
        int a, b;
        cin >> a >> b; a--; b--;
        d[a] ^= 1;
        d[b] ^= 1;
    }
    int ans = 0;
    rep(i,n) ans += d[i];
	if (ans > 0) {
        cout << "NO" << endl;
    } else {
        cout << "YES" << endl;
    }

	return 0;
}
