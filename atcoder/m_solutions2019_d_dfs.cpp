// https://atcoder.jp/contests/m-solutions2019/tasks/m_solutions2019_d
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

const int MAX_N = 10000;
int n;
int cnt = 0;
vector<vector<int>> G(MAX_N);
vector<int> c(MAX_N), d(MAX_N);

int dfs(int now) {
    if(cnt>=n) return 0;
    d[now] = c[cnt];
    cnt++;
    for (int next: G[now]) {
        if (d[next]>0) continue;
        dfs(next);
    }
    return 0;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	cin >> n;
    rep(i,n-1) {
        int a, b;
        cin >> a >> b;
        --a, --b;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    rep(i,n) cin >> c[i];
    sort(c.rbegin(),c.rend());
    int m = 0;
    for (int i = 1; i < n; i++) m += c[i];
	cout << m << "\n";
    dfs(0);
    rep(i,n) cout << d[i] << ' ';
    cout << "\n";
	return 0;
}
