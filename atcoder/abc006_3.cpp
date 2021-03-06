// https://atcoder.jp/contests/abc006/tasks/abc006_3
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

int main() {
	int N, M;
	cin >> N >> M;

    int a, b, c;

    if (M%2) {
        b = 1;
    } else {
        b = 0;
    }
    a = 2 * N - (M + b) / 2;
    c = N - a - b;

    if (a < 0 | c < 0) {
        a = -1; b = -1; c = -1;
    }

	cout << a << ' ' << b << ' ' << c << endl;
	return 0;
}
