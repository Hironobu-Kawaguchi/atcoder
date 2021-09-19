// https://atcoder.jp/contests/arc126/tasks/arc126_b
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
#include <atcoder/all>
using namespace atcoder;
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

int op(int a, int b) {
    return max(a, b);
}
int e() {
    return (int)(0);
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> ab(n+1);
    segtree<int, op, e> segt(n+1);
    rep(i,m) {
        int a, b;
        cin >> a >> b;
        ab[a].push_back(b);
    }
    rep(i,n+1) sort(ab[i].rbegin(), ab[i].rend());
    rep(i, n+1) {
        for (int b: ab[i]) {
            int maxk = segt.prod(0,b);
            // cout << i << ' ' << b << ' ' << segt.get(b) << ' ' << maxk+1 << endl;
            if (segt.get(b)<maxk+1) {
                segt.set(b, maxk+1);
            }        
        }        
    }
    
    int ans = segt.all_prod();
    cout << ans << endl;
	return 0;
}

