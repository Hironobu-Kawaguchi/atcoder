// https://atcoder.jp/contests/abc184/tasks/abc184_c
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

int solve(int x, int y) {
    if (x == 0 && y == 0) return 0;

    if (x+y == 0) return 1;
    if (x-y == 0) return 1;
    if (abs(x)+abs(y) <= 3) return 1;

    if ((x+y)%2 == 0) return 2;
    if (abs(x)+abs(y) <= 6) return 2;
    if (abs(x+y) <=3) return 2;
    if (abs(x-y) <=3) return 2;

    else return 3;
}

int main() {
	int x1,y1,x2,y2;
	cin >> x1 >> y1 >> x2 >> y2;
	cout << solve(x2-x1, y2-y1) << "\n";
	return 0;
}
