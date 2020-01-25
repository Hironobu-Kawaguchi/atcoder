// https://atcoder.jp/contests/atc001/tasks/dfs_a
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
#define all(v) (v).begin(),(v).end()
#define chmin(x,y) x = min(x,y)
#define chmax(x,y) x = max(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;
ll gcd(ll a, ll b) { return b?gcd(b,a%b):a;}
ll lcm(ll a, ll b) { return a/gcd(a,b)*b;}

int H, W;
int MAXH = 500, MAXW = 500;
int si, sj, gi, gj;
vector<vector<char>> c(MAXH, vector<char>(MAXW));
vector<vector<bool>> reached(MAXH, vector<bool>(MAXW));
const vector<int> di = {-1, 0, 1, 0};
const vector<int> dj = { 0,-1, 0, 1};

void dfs(int x, int y) {
    if (x<0 || W<=x || y<0 || H<=y || c[y][x] == '#') return;
    if (reached[y][x]) return;
    reached[y][x] = true;
    rep(i,4) {
        dfs(x+di[i], y+dj[i]);
    }
}

int main() {
	cin >> H >> W;
    // vector<vector<char>> c(H, vector<char>(W));
    // vector<vector<bool>> reached(H, vector<bool>(W, false));
    rep(i,H) rep(j,W) {
        cin >> c[i][j];
        if (c[i][j] == 's') {
            si = i;
            sj = j;
        }
        if (c[i][j] == 'g') {
            gi = i;
            gj = j;
        }
    }
    dfs(sj, si);
    if (reached[gi][gj]) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

	return 0;
}
