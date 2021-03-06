// https://codeforces.com/contest/1398/problem/B
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

void solve() {
    string s;
    cin >> s;
    s += '0';
    vector<int> a;
    int now = 0;
    bool flg = false;
    rep(i,s.size()) {
        if(s[i]=='1') {
            now++;
            flg = true;
        } else {
            if(flg) a.push_back(now);
            now = 0;
        }
    }
    sort(a.rbegin(), a.rend());
    now = 1;
    int ans = 0;
    for (int num: a) {
        if(now%2) ans += num;
        now++;
    }
    cout << ans << endl;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int t;
	cin >> t;
    rep(i,t) solve();
	return 0;
}
