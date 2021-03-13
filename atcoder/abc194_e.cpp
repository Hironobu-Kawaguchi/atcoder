// https://atcoder.jp/contests/abc194/tasks/abc194_e
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
    vector<int> pre(n, -1);
    int ans = n;
    rep(i,n) {
        int a;
        cin >> a;
        if (i-pre[a]>m) ans = min(ans, a);
        pre[a] = i;
    }
    rep(i,n) if(n-pre[i]>m) ans = min(ans, i);
    cout << ans << endl;
	return 0;
}

// TLE
// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	int n, m;
//     cin >> n >> m;
//     vector<int> a(n);
//     rep(i,n) cin >> a[i];
//     vector<int> cnt(n+1);
//     rep(i,m) cnt[a[i]]++;
//     int ans=0;
//     while(cnt[ans]>0) ans++;
//     rep(i,n-m) {
//         cnt[a[i]]--;
//         cnt[a[i+m]]++;
//         int tmp=0;
//         while(cnt[tmp]>0) tmp++;
//         ans = min(ans,tmp);
//     }
//     cout << ans << endl;
// 	return 0;
// }
