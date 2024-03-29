// https://atcoder.jp/contests/abc278/tasks/abc278_f
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
#include<map>
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
    vector<string> S(n);
    rep(i,n) cin >> S[i];
    int n2 = 1<<n;

    vector mem(n2, vector<bool>(n));
    vector val(n2, vector<bool>(n));
    auto f = [&](auto f, int s, int p) -> bool {
        if (mem[s][p]) return val[s][p];
        bool res = false;
        rep(i,n) {
            if (s>>i&1) continue;
            if (s && S[i][0] != S[p].back()) continue;
            res |= !f(f,s|1<<i,i);
        }
        mem[s][p] = true; val[s][p] = res;
        return res;
    };

    if (f(f,0,0)) cout << "First" << endl;
    else cout << "Second" << endl;
	return 0;
}
