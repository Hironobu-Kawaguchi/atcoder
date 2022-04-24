// https://atcoder.jp/contests/abc241/tasks/abc241_d
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
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    multiset<ll> st;
	int q;
	cin >> q;
    rep(qi, q) {
        int t;
        cin >> t;
        if(t==1) {
            int x;
            cin >> x;
            st.insert(x);
        } else if (t==2) {
            int x, k;
            cin >> x >> k;
            auto iter = upper_bound(st.begin(), st.end(), x);
            if(distance(st.begin(), iter)<k) {
                cout << -1 << endl;
            } else {
                advance(iter, -k);
                // iter--;
                cout << *iter << endl;
            }
        } else {
            int x, k;
            cin >> x >> k;
            auto iter = lower_bound(st.begin(), st.end(), x);
            if(distance(iter, st.end())<k) {
                cout << -1 << endl;
            } else {
                advance(iter, k-1);
                cout << *iter << endl;
            }
        }
    }
	return 0;
}
