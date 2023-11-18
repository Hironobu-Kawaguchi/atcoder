// https://atcoder.jp/contests/abc329/tasks/abc329_f
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
	int n, q;
	cin >> n >> q;
    // cout << n << ' ' << q << endl;
    vector<set<int>> box(n, set<int>());
    rep(i,n) {
        int c;
        cin >> c;
        box[i].insert(c);
    }

    rep(i,q) {
        int a, b;
        cin >> a >> b;
        --a, --b;
        // cout << a << ' ' << b << endl;
        if (box[a].size() < box[b].size()) {
            for (int x: box[a]) box[b].insert(x);
        } else {
            for (int x: box[b]) box[a].insert(x);
            swap(box[a],box[b]);
        }
        box[a].clear();
        cout << box[b].size() << endl;
    }

	return 0;
}
