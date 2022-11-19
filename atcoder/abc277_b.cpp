// https://atcoder.jp/contests/abc277/tasks/abc277_b
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
// #include<regex>

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

bool solve() {
	int n;
	cin >> n;
    vector<string> s(n);
    rep(i,n) cin >> s[i];
    const string cs1 = "HDCS";
    const string cs2 = "A23456789TJQK";
    // rep(i,n) {
    //     if (cs1.find(s[i][0]) == string::npos) return false;
    //     if (cs2.find(s[i][1]) == string::npos) return false;
    // }
    regex re("[HDCS][ATJQK2-9]");
    rep(i,n) {
        if (!regex_match(s[i], re)) return false;
    }
    // rep(i,n) rep(j,n) {
    //     if (i==j) continue;
    //     if (s[i] == s[j]) return false;
    // }
    set<string> st;
    rep(i,n) st.insert(s[i]);
    if (st.size() != n) return false;
    return true;
}

int main() {
    if (solve()) cout << "Yes" << endl;
	else cout << "No" << endl;
	return 0;
}
