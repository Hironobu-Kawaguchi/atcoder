// https://atcoder.jp/contests/agc039/tasks/agc039_a
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
    string s;
    ll k;
	cin >> s >> k;
    int n = s.size();
    vector<int> chrs;
    int num = 1;
    rep(i,s.size()) {
        if(i) {
            if(s[i-1]==s[i]) {
                num++;
            } else {
                chrs.push_back(num);
                num = 1;
            }
        }
    }
    chrs.push_back(num);
    int chrs_n = chrs.size();
    ll cnt = 0; // sの最初と最後の文字種を除いたs内の操作回数
    rep(i,chrs_n-2) cnt += chrs[i+1] / 2;

    ll ans = 0;
    if (chrs.size() == 1) {     // 全結合
        ans = (k * s.size()) / 2;
    } else if (s[0] == s[n-1]) { // 結合あり
        ans = cnt * k + chrs[0]/2 + chrs[chrs_n-1]/2 + ((chrs[0]+chrs[chrs_n-1])/2)*(k-1);
    } else {                    // 結合なし
        ans = (cnt + chrs[0]/2 + chrs[chrs_n-1]/2) * k;
    }

	cout << ans << endl;
	return 0;
}
