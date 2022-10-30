// https://atcoder.jp/contests/abc270/tasks/abc270_e
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
	int n;
    ll k;
	cin >> n >> k;
    vector<ll> a(n);
    rep(i,n) cin >> a[i];
    auto e = a;  // 小さい順に見るためのコピー
    sort(e.begin(), e.end());
    ll pre = 0; // 回る回数
    rep(i,n) {
        ll r = n - i;
        ll num = r*(e[i]-pre);
        if (num <= k && i != n-1) {  // e[i]を使い切って1周できるか，最後はaを更新へ
            k -= num;
        } else {  // 最後に回答に使うaを更新
            pre += k/r;  // 回る回数
            rep(j,n) {
                a[j] -= pre;
                if (a[j] < 0) a[j] = 0;
            }
            k %= r;  // 最後，回りきれない端数
            rep(j,n) {
                if (k > 0 && a[j] > 0) {
                    a[j]--;
                    k--;
                }
            }
            break;
        }
        pre = e[i];
    }
    rep(i,n) cout << a[i] << ' ';
	return 0;
}
