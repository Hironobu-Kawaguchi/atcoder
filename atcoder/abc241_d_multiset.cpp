// https://atcoder.jp/contests/abc241/tasks/abc241_d
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
// #include<map>
// #include<tuple>
#include<set>
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
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    multiset<ll> s;
	int q;
	cin >> q;
    rep(qi, q) {
        int type; ll x;
        cin >> type >> x;
        if(type==1) {
            s.insert(x);
        } else {
            int k;
            cin >> k;
            ll ans = -1;
            if (type==2) {
                auto it = s.upper_bound(x);
                bool ok = true;
                rep(i,k) {
                    if (it == s.begin()) { ok = false; break;}
                    --it;
                }
                if (ok) ans = *it;
            } else {
                auto it = s.lower_bound(x);
                bool ok = true;
                rep(i,k-1) {
                    if (it == s.end()) { ok = false; break;}
                    ++it;
                }
                if (ok && it != s.end()) ans = *it;
            }
            cout << ans << endl;
        }
    }
	return 0;
}
