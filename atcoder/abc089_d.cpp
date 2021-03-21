// https://atcoder.jp/contests/abc089/tasks/abc089_d
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
ll gcd(ll a, ll b) { return b?gcd(b,a%b):a;}
ll lcm(ll a, ll b) { return a/gcd(a,b)*b;}

int H, W, D, A;
int Q, L, R;
vector<int> px(90001), py(90001), d(90001);

int main() {
	cin >> H >> W >> D;
    rep(i,H) rep(j,W) {
        cin >> A;
        px[A] = i;
        py[A] = j;
    }
    for (int i = D+1; i <= H*W; i++) {
        d[i] = d[i-D] + abs(px[i]-px[i-D]) + abs(py[i]-py[i-D]);
    }
    cin >> Q;
    rep(i,Q) {
        cin >> L >> R;
        cout << d[R]-d[L] << endl;
    }   
	return 0;
}
