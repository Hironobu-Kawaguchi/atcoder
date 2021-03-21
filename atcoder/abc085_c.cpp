// https://atcoder.jp/contests/abc085/tasks/abc085_c
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
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
	int n, y;
	cin >> n >> y;

    rep(i, min(n+1, y/10000+1)) {
        rep(j, min(n+1-i, (y-10000*i)/5000+1)) {
            int k = n - (i+j);
            if (10000*i + 5000*j + 1000*k == y) {
                cout << i << " " << j << " " << k << endl;
                return 0;
            }
        }
    }
	cout << "-1 -1 -1" << endl;
	return 0;
}
