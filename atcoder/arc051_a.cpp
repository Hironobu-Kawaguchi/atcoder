// https://atcoder.jp/contests/arc051/tasks/arc051_a
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

int main() {
	int x1, y1, r, x2, y2, x3, y3;
	cin >> x1 >> y1 >> r;
	x1 += 100, y1 += 100;
	cin >> x2 >> y2 >> x3 >> y3;
	x2 += 100, y2 += 100, x3 += 100, y3 += 100;
	vector<vector<int>> color(201, vector<int>(201, 0));
	rep(x, 201) rep(y, 201) {
		if ((x-x1)*(x-x1)+(y-y1)*(y-y1)<=r*r) color[x][y] += 1;
		if (x>=x2 and x<=x3 and y>=y2 and y<=y3) color[x][y] += 2;
	}
	string red="NO", blue="NO";
	rep(x, 201) rep(y, 201) {
		if (color[x][y] == 1) red = "YES";
		if (color[x][y] == 2) blue = "YES";
	}
	cout << red << endl;
	cout << blue << endl;
	return 0;
}
