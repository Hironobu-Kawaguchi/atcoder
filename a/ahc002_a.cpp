// https://atcoder.jp/contests/ahc002/tasks/ahc002_a
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

const int MAX_I = 50;
// const int POINT_THRESHHOLD = 1000;
// const int POINT_THRESHHOLD = 500;
// const int POINT_THRESHHOLD = 300;
vector<vector<int>> t(MAX_I, vector<int>(MAX_I)), p(MAX_I, vector<int>(MAX_I));
vector<bool> gone(MAX_I*MAX_I);
vector<char> vc{'L','D','R','U'};
vector<int>  vi{ 0, +1,  0, -1 };
vector<int>  vj{ -1, 0, +1,  0 };
int max_point = 0;
string ans = "";
clock_t start = clock();

void dfs(int nowi, int nowj, string route, int point) {
    if (1000.0 * (clock() - start) / CLOCKS_PER_SEC > 1900) {
    // if (1000.0 * (clock() - start) / CLOCKS_PER_SEC > 10000) {
	 	// cout << 1000.0 * (clock() - start) / CLOCKS_PER_SEC << endl;
      	return;
    }
    if (point>max_point) {
        max_point = point;
        ans = route;
        // cout << max_point << endl;
        // cout << ans << endl;
    }
    vector<P> k_p;
    for (int k = 0; k < 4; k++) {
        int newi = nowi + vi[k];
        int newj = nowj + vj[k];
        if (newi < 0) continue;
        if (newi >= MAX_I) continue;
        if (newj < 0) continue;
        if (newj >= MAX_I) continue;
        if (gone[t[newi][newj]]) continue;
        k_p.push_back(make_pair(t[newi][newj], k));
    }
    sort(k_p.rbegin(), k_p.rend());
    int i = 0;
    for (P kp: k_p) {
        i++;
        if (point >= 15000) {
            if (i>1) break;    // top 1 direction only
        }else if (point >= 1000) {
            if (i>2) break;    // top 2 direction only
        }
        int newi = nowi + vi[kp.second];
        int newj = nowj + vj[kp.second];
        gone[t[newi][newj]] = true;
        dfs(newi, newj, route + vc[kp.second], point + p[newi][newj]);
        gone[t[newi][newj]] = false;
    }
    return;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int si, sj;
	cin >> si >> sj;
    rep(i,MAX_I) rep(j,MAX_I) cin >> t[i][j];
    rep(i,MAX_I) rep(j,MAX_I) cin >> p[i][j];
    gone[t[si][sj]] = true;
    dfs(si, sj, "", p[si][sj]);
    // cout << 1000.0 * (clock() - start) / CLOCKS_PER_SEC << endl;
    // cout << max_point << endl;
	cout << ans << "\n";
	return 0;
}
