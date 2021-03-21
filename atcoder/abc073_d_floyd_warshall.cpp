// https://atcoder.jp/contests/abc073/tasks/abc073_d
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

int N, M, R;
int r[8];
int to[205][205];
int ans = INF;
bool used[8];

void dfs(int num, int pre, int dist) {
    if (num>=R) {
        if (ans>dist) ans = dist;
        return;
    }
    rep(i,R) {
        if(used[i]) continue;
        used[i] = true;
        if(pre==-1) dfs(num+1, i, 0);
        else        dfs(num+1, i, dist + to[r[pre]][r[i]]);
        used[i] = false;
    }
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	cin >> N >> M >> R;
    rep(i,R) {
        cin >> r[i];
        --r[i];
    }
    rep(i,R) used[i] = false;
    rep(i,N) rep(j,N) {
        if(i==j) to[i][j] = 0;
        else     to[i][j] = INF;
    }
    rep(i,M) {
        int a, b, c;
        cin >> a >> b >> c;
        to[a-1][b-1] = c;
        to[b-1][a-1] = c;
    }
    rep(k,N) rep(i,N) rep(j,N) mins(to[i][j], to[i][k] + to[k][j]);
    // rep(i,N) rep(j,N) cout << to[i][j];
    dfs(0, -1, 0);
	cout << ans << "\n";
	return 0;
}
