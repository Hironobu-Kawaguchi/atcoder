// https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_e
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
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

const int MX = 2005;
bool d[3][3][MX];

int main() {
    vector<string> s(3);
    rep(i,3) cin >> s[i];
    sort(s.begin(), s.end());
    int ans = MX*3;
    do {
        rep(i,3)rep(j,3)rep(k,s[i].size()) {
            if (i >= j) continue;
            bool ok = true;
            for (int ni = k; ni < s[i].size(); ni++) {
                int nj = ni - k;
                if (nj >= s[j].size()) break;
                if (s[i][ni] == '?' || s[j][nj] == '?') continue;
                if (s[i][ni] != s[j][nj]) ok = false;
            }
            d[i][j][k] = ok;
        }
        auto f = [&](int i, int j, int k) {
            if (k >= s[i].size()) return true;
            return d[i][j][k];
        };

        rep(x,MX)rep(y,MX) {
            if (!f(0,1,x)) continue;
            if (!f(1,2,y)) continue;
            if (!f(0,2,x+y)) continue;
            int now = 0;
            now = max<int>(now, s[0].size());
            now = max<int>(now, x+s[1].size());
            now = max<int>(now, x+y+s[2].size());
            ans = min(ans, now);
        }
    } while (next_permutation(s.begin(), s.end()));

    cout << ans << endl;
	return 0;
}
