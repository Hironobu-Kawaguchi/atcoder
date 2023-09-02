// https://atcoder.jp/contests/abc315/tasks/abc315_d
#include<iostream>
// #include<algorithm>
// #include<cmath>
// #include <ctime>
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

#include <iostream>
#include <vector>
#include <set>
#include <string>

using namespace std;

int main() {
    int h, w;
    cin >> h >> w;
    vector<string> c(h);
    rep(i, h) cin >> c[i];
    vector a(h, vector<int>(w));
    rep(i, h) rep(j, w) a[i][j] = c[i][j] - 'a';

    const int m = 26;
    vector row(h, vector<int>(m));
    vector col(w, vector<int>(m));
    rep(i,h) rep(j,w) {
        row[i][a[i][j]]++;
        col[j][a[i][j]]++;
    }
    vector<bool> row_del(h), col_del(w);

    auto toDelete = [&](vector<int> x) {
        int total = 0, k = 0;
        rep(i, m) {
            total += x[i];
            if (x[i]) k++;
        }
        return total >= 2 && k == 1;
    };

    auto del = [&](int i, int j) {
        if (row_del[i] || col_del[j]) return;
        row[i][a[i][j]]--;
        col[j][a[i][j]]--;
    };

    bool update = true;
    while (update) {
        update = false;
        vector<int> del_row, del_col;
        rep(i, h) {
            if (row_del[i]) continue;
            if (toDelete(row[i])) del_row.push_back(i);
        }
        rep(j, w) {
            if (col_del[j]) continue;
            if (toDelete(col[j])) del_col.push_back(j);
        }
        for (int i : del_row) {
            rep(j, w) del(i, j);
            row_del[i] = true;
            update = true;
        }
        for (int j : del_col) {
            rep(i, h) del(i, j);
            col_del[j] = true;
            update = true;
        }
    }

    int ans = 0;
    rep(i, h) rep(j, w) {
        if (row_del[i] || col_del[j]) continue;
        ans++;
    }
    cout << ans << endl;
    return 0;
}
