// https://atcoder.jp/contests/typical90/tasks/typical90_z
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

const int MAX_N = 100005;
vector<int> col;
vector<vector<int>> to;

void dfs(int pos, int color) {
    // cout << "dfs" << endl;
    col[pos] = color;
    for (int nxt: to[pos]) {
        if (col[nxt]==-1) dfs(nxt, 1-color);
    }
    return;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n;
	cin >> n;
    col = vector<int>(n, -1);
    to.resize(n);
    // cout << "check0" << endl;
    rep(i, n-1) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        to[a].push_back(b);
        to[b].push_back(a);
    }
    // cout << "check1" << endl;
    // for (int nxt: to[0]) cout << nxt << endl;
    dfs(0, 0);
    // rep(i,n) cout << col[i] << endl;

    // cout << "check2" << endl;
    int zeros = 0, ones = 0;
    rep(i, n) {
        if (col[i]==0) zeros++;
        else           ones++;
    }
    int c = 1;
    if (zeros*2>=n) c = 0;
    int cnt = 0;
    rep(i, n) {
        if (col[i]==c) {
            cout << i+1 << ' ';
            cnt++;
        }
        if (cnt*2>=n) break;
    }
	return 0;
}
