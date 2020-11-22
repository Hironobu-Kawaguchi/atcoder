// https://atcoder.jp/contests/abc184/tasks/abc184_f
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
#define drep(i,n) for(int i = (n-1); i >= 0; i--)
#define all(v) (v).begin(),(v).end()
#define maxs(x,y) (x = max(x,y))
#define mins(x,y) (x = min(x,y))
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
    int n, T;
    cin >> n >> T;
    vector<int> a(n);
    rep(i,n) cin >> a[i];
    vector<ll> s, t;
    s = t = {0};
    rep(i,n) {
        for (int j = s.size()-1; j >= 0; --j) {
            s.push_back(s[j]+a[i]);
        }
        swap(s,t);
    }
    sort(s.begin(),s.end());
    ll ans = 0;
    for (ll x: t) {
        if (x > T) continue;
        int si = upper_bound(s.begin(),s.end(), T-x) - s.begin();
        ans = max(ans, x + s[si-1]);
    }
    cout << ans << endl;
	return 0;
}
