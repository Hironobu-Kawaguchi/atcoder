// https://atcoder.jp/contests/abc278/tasks/abc278_c
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

bool f(int h, int m) {
    int h2 = (h/10)*10 + m/10;
    int m2 = (h%10)*10 + m%10;
    return h2 <= 23 && m2 <= 59;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, q;
	cin >> n >> q;
    set<P> st;
    rep(qi, q) {
        int t, a, b;
        cin >> t >> a >> b;
        if (t == 1) st.emplace(a,b);
        if (t == 2) st.erase(P(a,b));
        if (t == 3) {
            if (st.count(P(a,b)) && st.count(P(b,a))) {
                cout << "Yes" << endl;
            } else {
                cout << "No" << endl;
            }
        }
    }
	return 0;
}
