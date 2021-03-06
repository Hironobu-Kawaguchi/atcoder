// https://atcoder.jp/contests/abc194/tasks/abc194_b
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
    vector<P> ap, bp;
    rep(i,n) {
        int a, b;
    	cin >> a >> b;
        ap.push_back(make_pair(a,i));
        bp.push_back(make_pair(b,i));
    }
    sort(ap.begin(), ap.end());
    sort(bp.begin(), bp.end());
    int ans;
    if (ap[0].second != bp[0].second) ans = max(ap[0].first ,bp[0].first);
    else {
        ans = ap[0].first + bp[0].first;
        ans = min(ans, max(ap[0].first, bp[1].first));
        ans = min(ans, max(ap[1].first, bp[0].first));
    }
    cout << ans << endl;
	return 0;
}
