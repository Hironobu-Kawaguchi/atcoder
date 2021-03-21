// https://atcoder.jp/contests/abc159/tasks/abc159_d
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
    int MAXN = 200000;
    int n;
	cin >> n;
    vector<int> a(n);
    rep(i,n) cin >> a[i];
    vector<ll> cnt(MAXN);
    rep(i,n) cnt[a[i]-1]++;
    ll ans = 0;
    rep(i,MAXN) {
        if (cnt[i] >= 2) {
            ans += (ll)cnt[i]*(cnt[i]-1)/2;
        }
    }
    rep(i,n) {
        cout << ans - (cnt[a[i]-1]-1) << endl;
    }
	return 0;
}
