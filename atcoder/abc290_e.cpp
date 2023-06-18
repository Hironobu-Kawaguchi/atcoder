// https://atcoder.jp/contests/abc290/tasks/abc290_e
// https://atcoder.jp/contests/abc290/submissions/39072481
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

ll c2(ll n) { return n*(n-1)/2;}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n;
	cin >> n;
    vector<int> a(n);
    rep(i,n) cin >> a[i];
    rep(i,n) a[i]--;
    vector<int> cnt(n);
    rep(i,n) cnt[a[i]]++;

    ll same = 0;
    rep(i,n) same += c2(cnt[i]);
    auto del = [&](int x) {
        same -= c2(cnt[x]);
        cnt[x]--;
        same += c2(cnt[x]);
    };

    ll ans = 0;
    rep(i,n) {
        int l = i, r = n-1-i;
        if (l >= r) break;
        ans += c2(r-l+1) - same;
        del(a[l]); del(a[r]);
    }
    cout << ans << endl;
	return 0;
}


// TLE
// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	int n;
// 	cin >> n;
//     vector<int> a(n);
//     rep(i,n) cin >> a[i];
//     ll ans = 0;
//     for (int k = 1; k < n; k++) {
//         rep(i, n-k) {
//             int cnt = min(i+1, n-(i+k));
//             if (a[i]!=a[i+k]) ans += cnt;
//         }
//     }
// 	cout << ans << "\n";
// 	return 0;
// }