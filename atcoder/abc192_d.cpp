// https://atcoder.jp/contests/abc192/tasks/abc192_d
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
    string x;
	ll m;
	cin >> x >> m;
    if (x.size() == 1) {
        if (stoi(x) <= m) cout << 1 << endl;
        else              cout << 0 << endl;
        return 0;
    }
 
    int d = 0;
    for (char c: x) d = max(d, int(c-'0'));
    ll ac = d, wa = m+1;
    while (wa - ac > 1) {
        ll wj = (ac+wa)/2;
        ll v = 0;
        for (char c : x) {
            if (v > m/wj) {
                v = m+1;
                break;
            }
            v = v*wj + (c-'0');
        }
        if (v <= m) ac = wj;
        else        wa = wj;
    }
    cout << ac - d << endl;
	return 0;
}


// WA
// bool check(ll n, string x, ll m) {
//     ll tmp=0;
//     ll now = 1;
//     for (int i = x.size()-1; i >= 0; i--) {
//         if(now>m) {
//             tmp = LINF;
//             break;
//         }
//         tmp += now * (x[i]-'0');
//         now *= n;
//     }
//     // cout << n << ' ' << tmp << endl;
//     if(tmp>m) return false;
//     else      return true;
// }

// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
//     string x;
// 	ll m;
// 	cin >> x >> m;
//     int d=0;
//     for (char c: x) {
//         d = max(d, c-'0');
//     }
//     if(x.size()==1) {
//         if(check(1,x,m)) cout << 1 << endl;
//         else             cout << 0 << endl;
//         return 0;
//     }
//     // cout << d << endl;
//     ll max_n = m + 10;
//     // ll max_n = d+1;
//     // while(true) {
//     //     if(!check(max_n,x,m)) break;
//     //     max_n *=2;
//     // }
//     // ll min_n = max_n / 2;
//     ll min_n = d+1;
//     ll n = (max_n + min_n) / 2;
//     // cout << max_n << ' ' << min_n << endl;
//     while(true) {
//         if(!check(n,x,m)) max_n = n;
//         else {
//             if(n==max_n-1) {
//                 if(check(max_n,x,m)) n = max_n;
//                 break;
//             }
//             if(n==min_n) break;
//             min_n = n;
//         }
//         n = (max_n + min_n) / 2;
//     }    
//     ll ans = n - d;
//     cout << ans << "\n";
// 	return 0;
// }
