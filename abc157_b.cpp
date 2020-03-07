// https://atcoder.jp/contests/abc157/tasks/abc157_b
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
    vector<vector<int>> a(3, vector<int>(3));
    rep(i,3) rep(j,3) cin >> a[i][j];
	int n;
	cin >> n;
    vector<vector<int>> d(3, vector<int>(3));
    rep(i,n) {
        int x;
        cin >> x;
        rep(i,3)rep(j,3) if(a[i][j]==x) d[i][j] = 1;
    }
    bool ans = false;
    rep(i,3) {
        int cnt = 0;
        rep(j,3) cnt += d[i][j];
        if(cnt==3) ans = true;
    }
    rep(i,3) {
        int cnt = 0;
        rep(j,3) cnt += d[j][i];
        if(cnt==3) ans = true;
    }
    {
        int cnt = 0;
        rep(j,3) cnt += d[j][j];
        if(cnt==3) ans = true;
    }
    {
        int cnt = 0;
        rep(j,3) cnt += d[j][2-j];
        if(cnt==3) ans = true;
    }
	if (ans) cout << "Yes" << endl;
    else     cout << "No"  << endl;
	return 0;
}
