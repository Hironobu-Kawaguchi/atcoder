// https://atcoder.jp/contests/abc203/tasks/abc203_e
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
// #include <atcoder/all>
// using namespace atcoder;
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
    // cin.tie(nullptr);
    // ios::sync_with_stdio(false);
	int n, m;
	cin >> n >> m;
    vector<ll> x(m), y(m);
    rep(i,m) cin >> x[i] >> y[i];
    map<ll, vector<ll>> mp;
    rep(i,m) {
        mp[x[i]].push_back(y[i]);
    }
    // sort(mp.begin(), mp.end());  // compile error
    set<ll> now;
    now.insert(n);
    for (auto z: mp) {
        ll x = z.first;
        vector<ll> ys = z.second;
        set<ll> adds, rems;
        for (ll y: ys) {
            if (now.count(y)) rems.insert(y);
        }
        for (ll y: ys) {
            if (now.count(y-1)) adds.insert(y);
            if (now.count(y+1)) adds.insert(y);
        }
        for (ll y: rems) now.erase(y);
        for (ll y: adds) now.insert(y);
        // now = next;
    }
	cout << now.size() << "\n";
	return 0;
}
