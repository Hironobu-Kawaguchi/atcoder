// https://atcoder.jp/contests/arc023/tasks/arc023_2
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

int R, C, D;
vector<vector<int>> A(1010, vector<int>(1010));
// vector<vector<bool>> eat(1010, vector<bool>(1010));
// vector<vector<bool>> nxt(1010, vector<bool>(1010));

// void dfs(int n) {
//     if (n == D) return;
//     rep(i,R)rep(j,C) nxt[i][j] = 0;
//     rep(i,R)rep(j,C) {
//         if(eat[i][j]) {
//             if(i>0)   nxt[i-1][j] = 1;
//             if(i<R-1) nxt[i+1][j] = 1;
//             if(j>0)   nxt[i][j-1] = 1;
//             if(j<C-1) nxt[i][j+1] = 1;
//         } 
//     }
//     rep(i,R)rep(j,C) eat[i][j] = nxt[i][j];
//     dfs(n+1);
// }

int main() {
	cin >> R >> C >> D;
    rep(i,R)rep(j,C) cin >> A[i][j];
    // eat[0][0] = 1;
    // dfs(0);
    int ans = 0;
    // rep(i,R)rep(j,C) if(eat[i][j]) ans = max(ans, A[i][j]);
    rep(i,R)rep(j,C) {
        if (((i+j)%2 == D%2) and ((i+j) <= D)) ans = max(ans, A[i][j]);
    }
	cout << ans << endl;
	return 0;
}
