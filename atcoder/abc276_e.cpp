// https://atcoder.jp/contests/abc276/tasks/abc276_e
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
#include <atcoder/all>
using namespace atcoder;
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

const int di[] = {-1, 0, 1, 0};
const int dj[] = { 0,-1, 0, 1};

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    int h, w;
	cin >> h >> w;
    vector<string> c(h);
    rep(i,h) cin >> c[i];
    int n = h*w;
    dsu uf(n);
    rep(v,n) {
        int i = v/w, j = v%w;
        if (c[i][j]!='.') continue;
        if (i+1<h && c[i+1][j]=='.') uf.merge(v, v+w);
        if (j+1<w && c[i][j+1]=='.') uf.merge(v, v+1);
    }
    set<int> st;
    int cnt = 0;
    rep(i,h) rep(j,w) if(c[i][j]=='S') {
        rep(v, 4) {
            int ni = i + di[v], nj = j + dj[v];
            if (ni<0 || ni>=h) continue;
            if (nj<0 || nj>=w) continue;
            if (c[ni][nj]!='.') continue;
            st.insert(uf.leader(ni*w+nj));
            cnt++;
        }
    }

    if (st.size()!=cnt) {
    	cout << "Yes" << "\n";
    } else {
        cout << "No" << "\n";
    }
	return 0;
}



// const int MAX_H = 1000005;
// vector<string> c(MAX_H);
// vector<bool> gone(MAX_H);
// bool ans = false;
// int h, w;
// int si, sj;
// vector<int> vi{ 0, 0, -1, +1 };
// vector<int> vj{ -1, +1, 0, 0 };

// void dfs(int i, int j, int n) {
//     // cout << i << ' ' << j << endl;
//     if (i==si && j==sj && n>=4) {
//         ans = true;
//         return;
//     }
//     // cout << i << ' ' << j << endl;
//     rep(idx, 4) {
//         int ni = i + vi[idx];
//         // cout << i << ' ' << ni << ' ' << vi[idx] << endl;
//         if (ni<0 || ni>=h) continue;
//         int nj = j + vj[idx];
//         // cout << j << ' ' << nj << ' ' << vj[idx] << endl;
//         if (nj<0 || nj>=w) continue;
//         // cout << 'c' << endl;
//         // cout << c[ni][nj] << endl;
//         if (c[ni][nj]=='#') continue;
//         if (gone[ni*w+nj]) continue;
//         gone[ni*w+nj] = true;
//         // cout << gone[ni*w+nj] << endl;
//         dfs(ni, nj, n+1);
//         gone[ni*w+nj] = false;
//     }
//     return;
// }

// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	cin >> h >> w;
//     // cout << h << ' ' << w << endl;
//     // vector<string> c(h);
//     rep(i,h) cin >> c[i];
//     // cout << c[0] << endl;
//     vector<bool> gone(h*w, false);
//     // cout << gone[0][0] << endl;
//     rep(i,h) rep(j,w) if(c[i][j]=='S') {
//         si = i, sj = j;
//         break;
//     }
//     // cout << si << ' ' << sj << endl;
//     dfs(si, sj, 0);
//     if (ans) {
//     	cout << "Yes" << "\n";
//     } else {
//         cout << "No" << "\n";
//     }
// 	return 0;
// }
