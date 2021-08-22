// https://atcoder.jp/contests/abc215/tasks/abc215_c
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

set<string> st;

void dfs(string s, string cs) {
    if (cs == "") {
        st.insert(s);
        return;
    }
    rep(i, cs.size()) {
        string ncs = cs;
        ncs.erase(ncs.begin()+i);
        dfs(s+cs[i], ncs);
    }
}

int main() {
    string s;
    int k;
    cin >> s >> k;
    dfs("", s);
    vector<string> ss;
    for (string t : st) ss.push_back(t);
    sort(ss.begin(), ss.end());
    cout << ss[k-1] << endl;
	return 0;
}


// int main() {
//     string s;
//     int k;
//     cin >> s >> k;
//     sort(s.begin(), s.end());
//     rep(i, k-1) next_permutation(s.begin(), s.end());
//     cout << s << endl;
// 	return 0;
// }
