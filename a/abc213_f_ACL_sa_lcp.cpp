// https://atcoder.jp/contests/abc213/tasks/abc213_f
// https://atcoder.jp/contests/abc213/submissions/24850592
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
#include <atcoder/all>
using namespace atcoder;
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
	int n;
	cin >> n;
    string s;
    cin >> s;
    auto sa = suffix_array(s);
    auto lcp = lcp_array(s, sa);
    vector<ll> ans(n);
    rep(i,n) ans[i] = n-i;

    rep(ri,2) {
        stack<P> st;
        ll now = 0;
        rep(i,n-1) {
            int len = 1;
            while (st.size() && st.top().first >= lcp[i]) {
                len += st.top().second;
                now -= (ll)st.top().first * st.top().second;
                st.pop();
            }
            now += (ll)lcp[i]*len;
            st.emplace(lcp[i], len);
            ans[sa[i+1]] += now;
        }
        reverse(lcp.begin(), lcp.end());
        reverse(sa.begin(), sa.end());
    }
    rep(i,n) cout << ans[i] << endl;
	return 0;
}
