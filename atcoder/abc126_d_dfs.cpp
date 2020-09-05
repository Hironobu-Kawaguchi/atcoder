// https://atcoder.jp/contests/abc126/tasks/abc126_d
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

const int MAX_N = 100005;
vector<vector<P>> to(MAX_N);
vector<int> ans(MAX_N, -1);

void dfs(int now, int c) {
    ans[now] = c;
    for (P p: to[now]) {
        if(ans[p.first]!=-1) continue;
        dfs(p.first, (c+p.second)%2);
    }
    return;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n;
	cin >> n;
    rep(i,n-1) {
        int u, v, w;
        cin >> u >> v >> w;
        --u, --v;
        to[u].push_back(make_pair(v,w));
        to[v].push_back(make_pair(u,w));
    }
    // ans[0] = 0;
    dfs(0,0);
    rep(i,n) cout << ans[i] << "\n";
	return 0;
}
