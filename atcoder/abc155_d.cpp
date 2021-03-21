// https://atcoder.jp/contests/abc155/tasks/abc155_d
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
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const ll MOD = 1e9+7;

const ll INF = ll(1e18)+1;

int main() {
	ll n, k;
	cin >> n >> k;
    vector<ll> a(n);
    rep(i,n) cin >> a[i];
    sort(a.begin(), a.end());
    ll l = -INF, r = INF;
    while (l+1 < r) {
        ll x = (l+r)/2;
        bool ok = [&]{
            ll tot = 0;
            rep(i,n) {
                if (a[i] < 0) {
                    int l = -1, r = n;
                    while (l+1 < r) {
                        int c = (l+r)/2;
                        if (a[c]*a[i] < x) r = c;
                        else               l = c;
                    }
                    tot += n-r;
                } else {
                    int l = -1, r = n;
                    while (l+1 < r) {
                        int c = (l+r)/2;
                        if (a[c]*a[i] < x) l = c;
                        else               r = c;
                    }
                    tot += r;
                }
                if (a[i]*a[i] < x) tot--;
            }
            tot /= 2;
            return tot < k;
        }();
        if (ok) l = x;
        else    r = x;
    }
	cout << l << endl;
	return 0;
}
