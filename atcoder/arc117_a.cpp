// https://atcoder.jp/contests/arc117/tasks/arc117_a
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
	int a, b;
	cin >> a >> b;
    vector<ll> e(a+b);
    rep(i,a-1) e[i] = i+1;
    rep(i,b-1) e[i+a] = -(i+1);
    if (a>b) {
        e[a-1] = a;
        e[a+b-1] = - (a*(a+1) - b*(b-1))/2;
    } else {
        e[a-1]   = (b*(b+1) - a*(a-1))/2;
        e[a+b-1] = - b;
    }
    rep(i,a+b) {
    	cout << e[i] << ' ';
    }
    cout << endl;
	return 0;
}
