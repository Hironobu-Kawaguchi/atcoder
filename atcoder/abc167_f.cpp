// https://atcoder.jp/contests/abc167/tasks/abc167_f
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

bool check(vector<P> s) {
    int h = 0;
    for (P p : s) {
        int b = h + p.first;
        if (b < 0) return false;
        h += p.second;
    }
    return true;
}
int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n;
	cin >> n;
    vector<P> ls, rs;
    int total = 0;
    rep(i,n) {
        string s;
        cin >> s;
        int h = 0, b = 0;
        for (char c: s) {
            if (c == '(') ++h; else --h;
            b = min(b, h);
        }
        if (h > 0) ls.emplace_back(b, h);   // 増減+ はb:最下点, h:増減を取る
        else rs.emplace_back(b-h, -h);      // 増減- は、上下左右逆さに考え、b:右から見た最下点、h:増減のマイナスを取る
        total += h;
    }
    sort(ls.rbegin(), ls.rend());
    sort(rs.rbegin(), rs.rend());  // 増減-は右から見るので、大きい順にsort

    if(check(ls) && check(rs) && total==0) {
	    cout << "Yes" << "\n";
    } else {
        cout << "No"  << "\n";
    }
	return 0;
}
