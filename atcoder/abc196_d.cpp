// https://atcoder.jp/contests/abc196/tasks/abc196_d
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

int h, w;
bool used[16][16];

ll dfs(int i, int j, int a, int b) {
    if (a < 0 || b < 0) return 0;   // 条件外は0
    if (j == w) j = 0, ++i;         // 右端だったら1つ下の左端へ
    if (i == h) return 1;           // 下端で終了は1
    if (used[i][j]) return dfs(i, j+1, a, b);   // 既に使っていたら次へ
    ll res = 0;
    used[i][j] = true;
    res += dfs(i,j+1, a, b-1);      // B(1マス)で埋める
    if (j+1 < w && !used[i][j+1]) {
        used[i][j+1] = true;
        res += dfs(i, j+1, a-1, b); // A(横2マス)で埋める
        used[i][j+1] = false;
    }
    if (i+1 < h && !used[i+1][j]) {
        used[i+1][j] = true;
        res += dfs(i, j+1, a-1, b); // A(縦2マス)で埋める
        used[i+1][j] = false;
    }
    used[i][j] = false;
    return res;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int a, b;
	cin >> h >> w >> a >> b;
	cout << dfs(0,0,a,b) << "\n";
	return 0;
}
