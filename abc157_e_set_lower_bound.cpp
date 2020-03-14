// https://atcoder.jp/contests/abc157/tasks/abc157_e
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
// #include<map>
// #include<tuple>
#include<set>
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
	int n, q;
    string s;
	cin >> n >> s >> q;
    vector<set<int>> sv(26);
    rep(i,n) sv[s[i]-'a'].insert(i);
    rep(qi, q) {
        int type;
        cin >> type;
        if (type == 1) {
            int i;
            char c;
            cin >> i >> c;
            i--;
            sv[s[i]-'a'].erase(i);
            s[i] = c;
            sv[s[i]-'a'].insert(i);
        } else {
            int l, r;
            cin >> l >> r;
            l--;
            int ans = 0;
            rep(i,26) {
                auto it = sv[i].lower_bound(l);
                if (it != sv[i].end() && *it < r) ans++;
            }
            cout << ans << endl;
        }
    }
	return 0;
}
