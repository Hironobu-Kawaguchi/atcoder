// https://atcoder.jp/contests/abc151/tasks/abc151_c
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
	int n, m;
	cin >> n >> m;
    vector<int> ac(n), wa(n);
    rep(i,m) {
        int p;
        string s;
        cin >> p >> s;
        --p;
        if (ac[p]) continue;
        if (s == "AC") ac[p] = 1;
        else           wa[p]++;
    }
    int ac_cnt = 0, wa_cnt = 0;
    rep(i,n) {
        ac_cnt += ac[i];
        if (ac[i]) wa_cnt += wa[i];
    }
    printf("%d %d\n", ac_cnt, wa_cnt);
	// cout << ac_cnt << ' ' << wa_cnt << endl;
	return 0;
}
