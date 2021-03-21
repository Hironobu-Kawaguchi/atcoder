// https://atcoder.jp/contests/abc179/tasks/abc179_e
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
	ll n, x, m;
	cin >> n >> x >> m;
    vector<int> id(m, -1);
    vector<int> a;
    int len = 0;
    ll tot = 0;
    while (id[x] == -1) {
        a.push_back(x);
        id[x] = len;
        len++;
        tot += x;
        x = (x*x)%m;
    }

    int c = len - id[x];
    ll s = 0;
    for (int i = id[x]; i < len; ++i) s += a[i];

    ll ans = 0;
    if (n <= len) {
        rep(i,n) ans += a[i];
    } else {
        ans += tot;
        n -= len;
        ans += s*(n/c);
        n %= c;
        rep(i,n) ans += a[id[x]+i];
    }
    cout << ans << endl;
	return 0;
}

// WA
// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	ll n;
//     int x, m;
// 	cin >> n >> x >> m;
//     vector<ll> cum(m+1), num(m+1);
//     cum[0] = x;
//     num[x] = 1;
//     ll now = x;
//     int i = 1;
//     ll pre_num, cycle_num, pre_sum, cycle_sum;
//     while(1) {
//         now = (now*now)%m;
//         // cout << i << ' ' << now << endl;
//         if(num[now]!=0) {
//             pre_num = num[now]-1;
//             cycle_num = i - pre_num;
//             if(pre_num>0) pre_sum = cum[pre_num-1];
//             else          pre_sum = 0;
//             cycle_sum = cum[i-1] - pre_sum;
//             // cout << pre_num << ' ' << pre_sum << ' ' << cycle_num << ' ' << cycle_sum << ' ' << endl;
//             break;
//         }
//         num[now] = i+1;
//         cum[i] = cum[i-1] + now;
//         ++i;
//     }
//     ll ans = 0;
//     if(n<pre_num) {
//         ans = cum[n-n];
//     } else {
//         ans += pre_sum;
//         n -= pre_num;
//         ans += (n/cycle_num) * cycle_sum;
//         n %= cycle_num;
//         ans += cum[n + pre_num - 1] - pre_sum;
//     }
//     cout << ans << endl;
// 	return 0;
// }
