// https://atcoder.jp/contests/abc154/tasks/abc154_d
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
	int n, k;
	cin >> n >> k;
    vector<int> p(n), cum(n+1);
    rep(i,n) {
        cin >> p[i];
        cum[i+1] = cum[i] + p[i];
    }
    int sum = 0;
    rep(i,n-k+1) sum = max(sum, cum[i+k] - cum[i]);
    double ans = sum + k;
    ans /= 2;
    printf("%.10f\n", ans);
    // cout << ans << endl;
	return 0;
}
