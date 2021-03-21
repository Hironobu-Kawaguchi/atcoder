// https://atcoder.jp/contests/past202005-open/tasks/past202005_e
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
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, m ,q;
	cin >> n >> m >> q;
    vector<vector<int>> to(n);
    rep(i,m) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        to[u].push_back(v);
        to[v].push_back(u);
    }
    vector<int> c(n);
    rep(i,n) cin >> c[i];
    rep(i,q) {
        int t, x, y;
        cin >> t;
        if(t==1) {
            cin >> x;
            --x;
            cout << c[x] << endl;
            for (int v: to[x]) {
                c[v] = c[x];
            }            
        } else if(t==2) {
            cin >> x >> y;
            --x;
            cout << c[x] << endl;
            c[x] = y;
        }
    }
	return 0;
}
