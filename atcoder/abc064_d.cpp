// https://atcoder.jp/contests/abc064/tasks/abc064_d
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
#define all(v) (v).begin(),(v).end()
#define chmin(x,y) x = min(x,y)
#define chmax(x,y) x = max(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;
ll gcd(ll a, ll b) { return b?gcd(b,a%b):a;}
ll lcm(ll a, ll b) { return a/gcd(a,b)*b;}

int main() {
	int N;
	cin >> N;
    string S;
    cin >> S;
    int l = 0, r = 0, lp = 0, rp = 0;
    rep(i,N) {
        if (S[i] == '(') l++;
        else             r++;
        lp = max(lp, r-l);
    }
    rp = lp + l - r;
    string ans = string(lp, '(') + S + string(rp, ')');
	cout << ans << endl;
	return 0;
}
