// https://atcoder.jp/contests/agc002/tasks/agc002_b
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
    vector<int> num(n, 1);
    vector<int> red(n, 0); red[0] = 1;

    int x, y;
    rep(i,m) {
        cin >> x >> y; --x; --y;
        if (red[x]) red[y] = 1;
        num[x]--; num[y]++;
        if (num[x] == 0) red[x] = 0;
    }

    int ans = 0;
    rep(i,n) {
        if (red[i]) ans++;
    }
	cout << ans << endl;
	return 0;
}
