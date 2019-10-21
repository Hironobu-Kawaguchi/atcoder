// https://atcoder.jp/contests/abc080/tasks/abc080_c
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
	int N;
	cin >> N;
    vector<vector<int>> F(N, vector<int>(10));
    rep(i,N)rep(j,10) cin >> F[i][j];
    vector<vector<int>> P(N, vector<int>(11));
    rep(i,N)rep(j,11) cin >> P[i][j];

    int ans = -(1<<30);
    for (int b = 1; b < (1<<10); b++) {
        int tmp = 0;
        rep(i,N) {
            int cnt = 0;
            rep(j,10) {
                if((b>>j&1)&&F[i][j]) {
                    cnt++;
                }
            }
            tmp += P[i][cnt];
        }
        ans = max(ans, tmp);
    }
    
	cout << ans << endl;
	return 0;
}
