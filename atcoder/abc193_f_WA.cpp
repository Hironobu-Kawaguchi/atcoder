// https://atcoder.jp/contests/abc193/tasks/abc193_f
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

int n;
char color[100][100];
bool done[100][100];
int di[4]={ 1, 0,-1, 0}; // y軸方向への変位
int dj[4]={ 0, 1, 0,-1}; // x軸方向への変位

int dfs_test(int i, int j, char c) {
    done[i][j] = true;
    int cnt = 0;
    char nc;
    if (c=='B') nc = 'W';
    else        nc = 'B';
    rep(k, 4) {
        int ni = i + di[k], nj = j + dj[k];
        if (ni<0) continue;
        if (ni>=n) continue;
        if (nj<0) continue;
        if (nj>=n) continue;
        if (done[ni][nj]==true) continue;
        if (color[ni][nj]==nc) cnt++;
        if (color[ni][nj]=='?') cnt += dfs_test(ni, nj, nc);
    }
    return cnt;
}

void dfs_color(int i, int j, char c) {
    color[i][j] = c;
    char nc;
    if (c=='B') nc = 'W';
    else        nc = 'B';
    rep(k, 4) {
        int ni = i + di[k], nj = j + dj[k];
        if (ni<0) continue;
        if (ni>=n) continue;
        if (nj<0) continue;
        if (nj>=n) continue;
        if (color[ni][nj]!='?') continue;
        dfs_color(ni, nj, nc);
    }
    return;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	cin >> n;
    rep(i,n) {
        string s;
        cin >> s;
        rep(j,n) color[i][j] = s[j];
    }
    rep(i,n) rep(j,n) {
        if (color[i][j]!='?') continue;
        rep(ii,n) rep(jj,n) done[ii][jj] = false;
        int cntb = dfs_test(i,j,'B');
        rep(ii,n) rep(jj,n) done[ii][jj] = false;
        int cntw = dfs_test(i,j,'W');
        if (cntb>cntw) dfs_color(i,j,'B');
        else           dfs_color(i,j,'W');
    }
    int ans = 0;
    rep(i,n) {
        rep(j,n) cout << color[i][j];
        cout << endl;
    }
    rep(i,n) rep(j,n-1) if(color[i][j]!=color[i][j+1]) ans++;
    rep(i,n-1) rep(j,n) if(color[i][j]!=color[i+1][j]) ans++;
	cout << ans << "\n";
	return 0;
}
