// https://atcoder.jp/contests/abc199/tasks/abc199_c
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
	cin >> n;
    string s;
    cin >> s;
    vector<vector<char>> ss(2, vector<char>(n));
    rep(i,n*2) ss[i/n][i%n] = s[i];
    // rep(i,2) rep(j,n) cout << ss[i][j];
    int q;
    cin >> q;
    int cnt_t2 = 0;
    rep(i,q) {
        int t, a, b;
        cin >> t >> a >> b;
        a--; b--;
        if (t==2) cnt_t2++;
        else {
            if (cnt_t2%2) swap(ss[1-a/n][a%n], ss[1-b/n][b%n]);
            else swap(ss[a/n][a%n], ss[b/n][b%n]);
        }
    }
    string ans;
    if (cnt_t2%2) for (int i=1; i>=0; i--) rep(j,n) ans += ss[i][j];
    else rep(i,2) rep(j,n) ans += ss[i][j];
    cout << ans << endl;
	return 0;
}
