// https://atcoder.jp/contests/arc042/tasks/arc042_a
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
	int N, M;
	cin >> N >> M;
    vector<int> b(N+M), u(N);
    rep(i, N) b[i] = N - i;
    rep(i, M) cin >> b[N+i];
    for (int i = N+M-1; i >= 0; i--) {
        if (u[b[i]-1] == 0) {
            cout << b[i] << endl;
            u[b[i]-1] = 1;
        }
    }
    
	return 0;
}
