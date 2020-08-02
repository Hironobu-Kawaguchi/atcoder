// https://atcoder.jp/contests/abc025/tasks/abc025_c
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

vector<vector<int>> b(2, vector<int>(3));
vector<vector<int>> c(3, vector<int>(2));
vector<vector<int>> m(3, vector<int>(3));

int min_max(int t) {
    if (t == 9) {
        int S = 0;
        rep(i, 2) rep(j, 3) {
            if (m[i][j] == m[i+1][j]) {
                S += b[i][j];
            }
        }
        rep(i, 3) rep(j, 2) {
            if (m[i][j] == m[i][j+1]) {
                S += c[i][j];
            }
        }
        return S;
    } else {
        int maxv = -INF, minv = INF;
        rep(i, 3) rep(j, 3) {
            if (m[i][j] != 0) continue;
            if (t%2 == 0) m[i][j] = 1;  // 直大
            else          m[i][j] = 2;  // 直子
            int Sum = min_max(t+1);
            if (t%2 == 0) maxv = max(maxv, Sum);
            else          minv = min(minv, Sum);
            m[i][j] = 0;
        }
        if (t%2 == 0) return maxv;
        else          return minv;
    }
}

int main() {
	int S = 0;
    rep(i, 2) rep(j, 3) cin >> b[i][j], S += b[i][j];
    rep(i, 3) rep(j, 2) cin >> c[i][j], S += c[i][j];

    int ans = min_max(0);
	cout << ans << endl;
	cout << S - ans << endl;
	return 0;
}
