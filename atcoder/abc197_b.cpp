// https://atcoder.jp/contests/abc197/tasks/abc197_b
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
// #include <atcoder/all>
// using namespace atcoder;
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

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int h, w, x, y;
	cin >> h >> w >> x >> y;
	x--, y--;
	vector<string> s(h);
	rep(i,h) cin >> s[i];
    int ans = 1;  // (x.y)

	vector<int> vy{ 0, 0, -1, +1 };
	vector<int> vx{ -1, +1, 0, 0 };
	for (int k = 0; k < 4; k++) {
		int cnt = 0;
		int newx = x;
		int newy = y;
		while (true) {
			newx += vx[k];
			newy += vy[k];
			if (newx<0 || newx>=h) break;
			if (newy<0 || newy>=w) break;
			if (s[newx][newy]=='#') break;
			cnt++;
		}
		ans += cnt;
	}

	cout << ans << "\n";
	return 0;
}
