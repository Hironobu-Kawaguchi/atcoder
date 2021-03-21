// https://atcoder.jp/contests/abc155/tasks/abc155_c
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
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define all(v) (v).begin(),(v).end()
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
    int n;
    cin >> n;
    string s;
    map<string, int> m;
    rep(i,n) {
        cin >> s;
        m[s]++;
    }
    int maxv = 0;
    for (auto x: m) {
        int v = x.second;
        if(v>maxv) maxv = v;
    }
    for (auto it = m.begin(); it != m.end(); it++) {
        if(it->second == maxv) cout << it->first << endl;
    }
    // for (auto x: m) {
    //     if(x.second == maxv) cout << x.first << endl;
    // }
	return 0;
}
