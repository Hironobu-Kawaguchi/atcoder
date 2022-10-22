// https://atcoder.jp/contests/abc274/tasks/abc274_d
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

bool f(int x, vector<int> a) {
    unordered_set<int> s;
    s.insert(0);
    for (int na: a) {
        unordered_set<int> p;
        swap(p, s);
        for (int nx: p) {
            s.insert(nx-na);
            s.insert(nx+na);
        }
    }
    return s.count(x);
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    int n, x, y;
    cin >> n >> x >> y;
    vector<int> a(n);
    rep(i,n) cin >> a[i];
    x -= a[0];
    vector<int> xa, ya;
    for (int i = 1; i < n; i++) {
        if (i%2==1) ya.push_back(a[i]);
        else        xa.push_back(a[i]);
    }
    if (f(x, xa) && f(y, ya)) cout << "Yes" << endl;
    else                    cout << "No" << endl;
	return 0;
}
