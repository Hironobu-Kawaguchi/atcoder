// https://atcoder.jp/contests/arc115/tasks/arc115_a
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

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, m;
	cin >> n >> m;
    vector<string> s(n);
    rep(i,n) cin >> s[i];
    int odd = 0, even = 0;
    rep(i,n) {
        int cnt = 0;
        rep(j,m) if(s[i][j]=='1') cnt++;
        if (cnt%2) odd++;
        else      even++;
    }
    ll ans = (ll) odd * even;
	cout << ans << "\n";
	return 0;
}

// 誤読
// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	int n, m;
// 	cin >> n >> m;
//     vector<string> s(n);
//     rep(i,n) cin >> s[i];
//     ll ans = 0;
//     rep(k,1<<m) {
//         vector<int> seikai(m+1);
//         rep(i,n) {
//             int cnt = 0;
//             rep(j,m) {
//                 if (('0'+(k>>j&&1))==s[i][j]) cnt++;
//             }
//             seikai[cnt]++;
//         }
//         bool flg = true;
//         rep(j, m+1) if(seikai[j]>=2) flg = false;
//         if(flg) ans++;
//     }
// 	cout << ans << "\n";
// 	return 0;
// }
