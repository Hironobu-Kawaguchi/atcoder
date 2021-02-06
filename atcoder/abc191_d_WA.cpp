// https://atcoder.jp/contests/abc191/tasks/abc191_d
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

const ll MAX_R = 100005;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    double x, y, r;
    cin >> x >> y >> r;
    vector<int> ur(MAX_R), ul(MAX_R), dl(MAX_R), dr(MAX_R);
    int sx = ceil(x), sy = ceil(y);
    int nx, ny;

    // 右上
    nx = x + sqrt(r*r - (sy-y)*(sy-y));
    ny = sy;
    // cout << nx << ' ' << ny << endl;
    while (nx>=x) {
        if ((nx-x)*(nx-x)+(ny-y)*(ny-y) <= r*r) {
            ur[ny-sy] = nx;
            // cout << ny-sy << ' ' << nx << endl;
            ny++;
        } else {
            nx--;
        }
    }

    // 左上
    nx = sx;
    ny = y + sqrt(r*r - (sx-x)*(sx-x));
    // cout << nx << ' ' << ny << endl;
    while (ny>=y) {
        if ((nx-x)*(nx-x)+(ny-y)*(ny-y) <= r*r) {
            ul[ny-sy] = nx-1;
            // cout << ny-sy << ' ' << nx-1 << endl;
            nx--;
        } else {
            ny--;
        }
    }

    // 左下
    nx = ceil(x - sqrt(r*r - (sy-1-y)*(sy-1-y)));
    ny = sy-1;
    // cout << nx << ' ' << ny << endl;
    while (nx<=x) {
        if ((nx-x)*(nx-x)+(ny-y)*(ny-y) <= r*r) {
            dl[sy-ny] = nx-1;
            // cout << sy-ny << ' ' << nx-1 << endl;
            ny--;
        } else {
            nx++;
        }
    }

    // 右下
    nx = sx;
    ny = ceil(y - sqrt(r*r - (sx-x)*(sx-x)));
    // cout << nx << ' ' << ny << endl;
    while (ny<y) {
        if ((nx-x)*(nx-x)+(ny-y)*(ny-y) <= r*r) {
            dr[sy-ny] = nx;
            // cout << sy-ny << ' ' << nx << endl;
            nx++;
        } else {
            ny++;
        }
    }

    ll ans = 0;
    rep(i,MAX_R) {
        ans += ur[i] - ul[i];
        ans += dr[i] - dl[i];
    }
    cout << ans << "\n";
	return 0;
}
