// https://atcoder.jp/contests/abc131/tasks/abc131_c
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
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

// 最大公約数	最小公倍数 LCM=a*b/gcd
ll gcd(ll a, ll b) {
	if (b == 0) return a;
	else return gcd(b, a%b);
}

int main() {
	ll A, B, C, D;
	cin >> A >> B >> C >> D;
	ll l = C*D/gcd(C, D);
	ll ans = B - (B/C + B/D - B/l);
	ans -= (A-1) - ((A-1)/C + (A-1)/D - (A-1)/l);
	cout << ans << endl;
	return 0;
}
