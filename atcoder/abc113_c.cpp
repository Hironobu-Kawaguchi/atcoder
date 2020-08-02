// https://atcoder.jp/contests/abc113/tasks/abc113_c
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
    vector<int> P(M), Y(M);
    vector<vector<int>> yd(N+1);
    rep(i,M) {
        cin >> P[i] >> Y[i];
        yd[P[i]].push_back(Y[i]);
    }
    rep(i,N) sort(yd[i+1].begin(), yd[i+1].end());
    rep(i,M) {
        printf("%012lld\n", ll(P[i])*1000000 + int(lower_bound(yd[P[i]].begin(),yd[P[i]].end(), Y[i]) - yd[P[i]].begin()) +1);
    }
	return 0;
}
