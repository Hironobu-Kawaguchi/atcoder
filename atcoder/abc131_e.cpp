// https://atcoder.jp/contests/abc131/tasks/abc131_e
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
    int n, k;
    cin >> n >> k;
    int mx = (n-1)*(n-2)/2;
    if (mx < k) {
        cout << -1 << endl;
        return 0;
    }
    vector<P> ans;
    rep(i,n-1) {
        ans.push_back(P(i+1,n));    // star graph
    }
    int add = mx - k;
    vector<P> edge;
    rep(i,n-1) rep(j,i) edge.push_back(P(i+1,j+1)); // complete graph
    rep(i,add) ans.push_back(edge[i]);  // add本のedgeを追加
	cout << ans.size() << endl;
    rep(i, ans.size()) {
        cout << ans[i].first << ' ' << ans[i].second << endl;
    }
	return 0;
}
