// https://atcoder.jp/contests/abc170/tasks/abc170_e
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
    vector<int> a(n), b(n);
    vector<multiset<int>> s(200005);
    multiset<int> maxs;
    auto getMax = [&](int i) {
        if (s[i].size()==0) return -1;
        return *s[i].rbegin();
    };
    auto addYochien = [&](int i) {
        int x = getMax(i);
        if (x == -1) return;
        maxs.insert(x);
    };
    auto delYochien = [&](int i) {
        int x = getMax(i);
        if (x == -1) return;
        maxs.erase(maxs.find(x));
    };
    auto addEnji = [&](int i, int x) {
        delYochien(i);
        s[i].insert(x);
        addYochien(i);
    };
    auto delEnji = [&](int i, int x) {
        delYochien(i);
        s[i].erase(s[i].find(x));
        addYochien(i);
    };
    rep(i,n) {
        cin >> a[i] >> b[i];
        addEnji(b[i], a[i]);
    }
    rep(i,q) {
        int c, d;
        cin >> c >> d;
        --c;
        delEnji(b[c], a[c]);
        b[c] = d;
        addEnji(b[c], a[c]);
        int ans = *maxs.begin();
        printf("%d\n", ans);
    }
	return 0;
}
