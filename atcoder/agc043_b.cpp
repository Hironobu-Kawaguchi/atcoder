// https://atcoder.jp/contests/agc043/tasks/agc043_b
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

int bit_count(int x) {
    int res = 0;
    while (x>0 && x%2==0) {
        res++;
        x /= 2;
    }
    return res;
}

int main() {
	int n;
	cin >> n;
    string s;
    cin >> s;
    vector<int> a(n);
    rep(i,n) a[i] = s[i] - '1';

    vector<int> comb_bit_count(n);
    comb_bit_count[0] = 0;
    rep(i,n-1) {
        comb_bit_count[i+1] = comb_bit_count[i] + bit_count(n-1-i) - bit_count(i+1);
        // cout << comb_bit_count[i+1] << endl;
    }

    int ans = 0;
    rep(i,n) {
        if (comb_bit_count[i]==0) {
            ans += a[i];
            ans %= 2;
        }
    }
    // 答えは0,1,2のどれか
    // 1なら1で確定
    if (ans==1) {
        cout << ans << endl;
        return 0;
    }
    // 入力に2(変換後1)が含まれていれば2にはならないので0
    rep(i,n) {
        if (a[i]==1) {
            cout << 0 << endl;
            return 0;
        }
    }
    // 1/2で0,2を判定、結果を2倍して出力
    ans = 0;
    rep(i,n) {
        if (comb_bit_count[i]==0) {
            ans += a[i]/2;
            ans %= 2;
        }
    }
	cout << ans*2 << endl;
	return 0;
}
