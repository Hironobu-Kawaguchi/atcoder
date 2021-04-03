// https://codeforces.com/contest/1504/problem/B
// #include<iostream>
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
    int n;
    cin >> n;
    string a, b;
    cin >> a >> b;
    vector<int> pos;
    pos.push_back(-1);
    int zeros = 0, ones = 0;
    rep(i,a.size()) {
        if (a[i]=='0') zeros++;
        else           ones++;
        if (zeros==ones) pos.push_back(i);
    }
    reverse(pos.begin(), pos.end());
    bool flg = true;
    for (int i = 0; i < pos.size(); i++) {
        // cout << i << endl;
        if (i==0) {
            for (int j = pos[i]+1; j < a.size(); j++) {
                if (a[j]!=b[j]) {
                    flg = false;
                    break;
                }
            }
        } else {
            bool dif_flag;
            for (int j = pos[i]+1; j <= pos[i-1]; j++) {
                if (j==pos[i]+1) {
                    if (a[j]==b[j]) dif_flag = true;
                    else dif_flag = false;
                } else {
                    if (a[j]==b[j] ^ dif_flag) {
                        flg = false;
                        break;
                    }
                }
            }
        }
        if (!flg) break;
    }
    if (flg) cout << "YES" << endl;
    else     cout << "NO"  << endl;
    return;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int t;
	cin >> t;
    rep(i,t) solve();
	return 0;
}
