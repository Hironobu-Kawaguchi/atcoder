// https://atcoder.jp/contests/abc215/tasks/abc215_d
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
    int n, m;
    cin >> n >> m;
    const int L = 100001;
    vector<bool> x(L);
    rep(i,n) {
        int a;
        cin >> a;
        x[a] = true;
    }

    vector<int> d; // Prime factorization
    for (int i = 2; i < L; i++) {
        bool flag = false;
        for (int j = i; j < L; j += i) {
            if (x[j]) flag = true; // if a%i==0
        }
        if (flag) d.push_back(i);
    }

    vector<bool> ok(m+1, true);
    for (int i :d) {
        for (int j = i; j <= m; j += i){
            ok[j] = false;
        }
    }
    int cnt = 0;
    for (int i = 1; i <= m; ++i) if (ok[i]) cnt++;
    cout << cnt << endl;
    for (int i = 1; i <= m; ++i) if (ok[i]) cout << i << endl;
	return 0;
}
