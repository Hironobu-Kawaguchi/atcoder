// https://atcoder.jp/contests/abc176/tasks/abc178_f
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
	int n;
    cin >> n;
    vector<int> a(n), b(n), cnta(n), cntb(n), cuma(n+1), cumb(n+1);
    rep(i,n) {
        cin >> a[i];
        cnta[a[i]-1]++;
    }
    rep(i,n) {
        cin >> b[i];
        cntb[b[i]-1]++;
    }
    rep(i,n) if(cnta[i]+cntb[i]>n) {
        cout << "No" << endl;
        return 0;
    }
    rep(i,n) {
        cuma[i+1] = cuma[i] + cnta[i];
        cumb[i+1] = cumb[i] + cntb[i];
    }

    int x = 0;
    rep(i,n) {
        x = max(x, cuma[i+1] - cumb[i]);
    }
    // cout << x << endl;
    cout << "Yes" << endl;
    rep(i,n) cout << b[(i+n-x)%n] << ' ';
    cout << endl;
	return 0;
}


// WA
// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	int n;
//     cin >> n;
//     vector<int> a(n), b(n), cnta(n), cntb(n), posa(n), posb(n);
//     rep(i,n) {
//         cin >> a[i];
//         --a[i];
//         cnta[a[i]]++;
//         posa[a[i]] = i;
//     }
//     rep(i,n) {
//         cin >> b[i];
//         --b[i];
//         cntb[b[i]]++;
//         posb[b[i]] = i;
//     }
//     int maxi, maxcnt = 0;
//     rep(i,n) {
//         if(cnta[i]+cntb[i]>maxcnt) {
//             maxcnt = cnta[i]+cntb[i];
//             maxi = i;
//         }
//         if(cnta[i]+cntb[i]>n) {
//             cout << "No" << endl;
//             return 0;
//         }
//     }
//     cout << "Yes" << endl;
//     int slide = posa[maxi] - posb[maxi] + cntb[maxi];
//     rep(i,n) {
//         cout << b[(i+slide)%n]+1 << ' ';
//     }

//     cout << endl;
// 	return 0;
// }
