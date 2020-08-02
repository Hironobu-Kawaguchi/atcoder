// https://atcoder.jp/contests/arc018/tasks/arc018_2
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

vector<vector<ll>> XY(100, vector<ll>(2)); 

bool chk(int i, int j, int k) {
    ll x;
    x = (XY[j][0]-XY[i][0]) * (XY[k][1]-XY[i][1]) - (XY[j][1]-XY[i][1]) * (XY[k][0]-XY[i][0]);
    // cout << x << i << j << k << endl;
    return (x != 0) and (x%2 == 0);
}

int main() {
	int N;
	cin >> N;
    rep(i,N) cin >> XY[i][0] >> XY[i][1];
    ll ans = 0;
    for (int i = 0; i < N-2; i++) {
        for (int j = i+1; j < N-1; j++) {
            for (int k = j+1; k < N; k++) {
                if(chk(i,j,k)) ans++;
            }            
        }        
    }
	cout << ans << endl;
	return 0;
}
