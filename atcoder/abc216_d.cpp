// https://atcoder.jp/contests/abc216/tasks/abc216_d
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

const int MAX_N = 200005;
int n, m, k;
vector<queue<int>> stk(MAX_N);
set<int> top_set;
vector<int> top_idx(MAX_N, -1);

void check_top(int idx) {
    // cout << "run check_top" << endl;
    // for (int v: stk[idx]) cout << v << ' ';
    // for (int v: top_set) cout << v << ' ';
    if (stk[idx].empty()) return;
    int v = stk[idx].front();
    if (top_set.count(v)) {
        stk[idx].pop();
        top_set.erase(stk[top_idx[v]].front());
        stk[top_idx[v]].pop();
        check_top(idx);
        check_top(top_idx[v]);
    } else {
        top_set.emplace(v);
        top_idx[v] = idx;
    }
    return;
}


int main() {
    // cin.tie(nullptr);
    // ios::sync_with_stdio(false);
	cin >> n >> m;
    rep(i,m) {
        cin >> k;
        vector<int> a(k);
        rep(j,k) {
            cin >> a[j];
            stk[i].push(a[j]);
        }
        // reverse(a.begin(), a.end());
        check_top(i);
    }
    // rep(i,m) for (int v: stk[i]) cout << v << ' ';
    // for (int v: top_set) cout << v << ' ';
    

    if (top_set.empty()) cout << "Yes" << endl;
    else                 cout << "No"  << endl;
    // ll ans = 0;
	// cout << ans << "\n";
	return 0;
}
