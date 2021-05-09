// https://atcoder.jp/contests/abc200/tasks/abc200_e
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

    auto c2 = [&](ll s) {
        if (s < 0) return 0ll;
        return s*(s-1)/2;
    };

    auto f = [&](ll s) {
        ll res = c2(s-1);
        res -= c2(s-1-n)*3;
        res += c2(s-1-n*2)*3;
        res -= c2(s-1-n*3);
        return res;
    };

    auto f2 = [&](int s) {
        int l = max(1, s-n);
        int r = min(n, s-1);
        if (l > r) return 0;
        return r-l+1;
    };

    for (int s = 3; s <= n*3; ++s) {
        ll x = f(s);
        if (k > x) {
            k -= x;
        } else {
            for (int a = 1; a <= n; ++a) {
                x = f2(s-a);
                if (k > x) {
                    k -= x;
                } else {
                    for (int b = 1; b <= n; ++b) {
                        int c = s-a-b;
                        if (c <= 0 || c > n) continue;
                        if (k > 1) {
                            --k;
                        } else {
                            printf("%d %d %d\n", a, b, c);
                            return 0;
                        }
                    }
                }
            }

        }
    }
    return 0;
}
