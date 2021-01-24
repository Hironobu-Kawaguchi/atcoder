// https://atcoder.jp/contests/abc189/tasks/abc189_c
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

// O(N)
vector<int> getLeft(vector<int> a) {
    int n = a.size();
    vector<int> res(n);
    stack<P> ps;
    ps.emplace(0,-1);
    rep(i,n) {
        while (ps.top().first >= a[i]) ps.pop();
        res[i] = ps.top().second;
        ps.emplace(a[i], i);
    }
    return res;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n;
	cin >> n;
    vector<int> a(n);
    rep(i,n) cin >> a[i];
    vector<vector<int>> d;
    rep(ri,2) {
        d.push_back(getLeft(a));
        reverse(a.begin(),a.end());
    }
    vector<int> ls = d[0];
    vector<int> rs = d[1];
    reverse(rs.begin(),rs.end());
    rep(i,n) rs[i] = n-1-rs[i];
    int ans = 0;
    rep(i,n) {
        int now = a[i] * (rs[i]-ls[i]-1);
        ans = max(ans, now);
    }
    cout << ans << endl;
	return 0;
}


// O(N^2)
// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	int n;
// 	cin >> n;
//     vector<int> a(n);
//     rep(i,n) cin >> a[i];
//     int ans = 0;
//     rep(l,n) {
//         int x = a[l];
//         for (int r = l; r < n; r++) {
//             x = min(x, a[r]);
//             ans = max(ans, x*(r-l+1));
//         }
        
//     }
// 	cout << ans << "\n";
// 	return 0;
// }


// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	int n;
// 	cin >> n;
//     vector<int> a(n);
//     rep(i,n) cin >> a[i];
//     vector<int> ord(n);
//     rep(i,n) ord[i] = i;
//     sort(ord.begin(), ord.end(), [&] (int x, int y) {
//         return a[x] > a[y];
//     });
//     vector<bool> ok(n);
//     int ans = 0;
//     for (auto i: ord) {
//         ok[i] = true;
//         int l = i;
//         while (l>=0 && ok[l]) --l;
//         int r = i;
//         while (r<n && ok[r]) ++r;
//         ans = max(ans, (r-l-1)*a[i]);
//     }
// 	cout << ans << "\n";
// 	return 0;
// }
