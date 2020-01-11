// https://atcoder.jp/contests/abc150/tasks/abc150_d
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

int f(int x) {
    int res = 0;
    while (x%2 == 0) {
        x /= 2;
        res++;
    }
    return res;
}

int main() {
	int n, m;
	cin >> n >> m;
    vector<int> a(n);
    rep(i,n) cin >> a[i];
    rep(i,n) {
        if (a[i]%2 ==1) {
            cout << 0 << endl;
            return 0;
        }
        a[i] /= 2;
    }

    int t = f(a[0]);
    rep(i,n) {
        if (f(a[i]) != t) {
            cout << 0 << endl;
            return 0;
        }
        a[i] >>= t; // a[i] /= 2^t
    }
    m >>=t;

    ll l = 1;
    rep(i,n) {
        l = lcm(l, a[i]);
        if (l > m) {
            cout << 0 << endl;
            return 0;
        }
    }
    m /= l;
    int ans = (m+1)/2;
	cout << ans << endl;
	return 0;
}
