// https://atcoder.jp/contests/abc165/tasks/abc165_e
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
	int n, m;
	cin >> n >> m;
    vector<P> ans;
    if (n%2) {
        for (int l = 1, r = n-1; l < r; l++, r--) {
            ans.emplace_back(l,r);
        }
    } else {
        bool flag = false;
        for (int l = 1, r = n-1; l < r; l++, r--) {
            if (!flag && r-l <= n/2) {
                --r;
                flag = true;
            }
            ans.emplace_back(l,r);
        }
    }
    rep(i,m) printf("%d %d\n", ans[i].first, ans[i].second);
	return 0;
}
