// https://atcoder.jp/contests/abc313/tasks/abc313_d
#include<iostream>
// #include<algorithm>
// #include<cmath>
// #include <ctime>
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
	int n, k;
	cin >> n >> k;
    vector<int> a(n);

    auto f = [&](vector<int> x) {
        rep(i,k) x[i]++;
        cout << '?';
        rep(i,k) cout << ' ' << x[i];
        cout << endl;
        int res;
        cin >> res;
        return res;
    };

    vector<int> b(k+1);
    int t = 0;
    rep(i, k+1) {
        vector<int> x;
        rep(j, k+1) if(i != j) x.push_back(j);
        b[i] = f(x);
        t ^= b[i];
    }
    rep(i,k+1) a[i] = t^b[i];

    t = 0;
    rep(i,k-1) t ^= a[i];
    for (int i = k+1; i < n; i++) {
        vector<int> x;
        rep(j,k-1) x.push_back(j);
        x.push_back(i);
        a[i] = t^f(x);
    }

    cout << '!';
    rep(i,n) cout << ' ' << a[i];
    cout << endl;
	return 0;
}
