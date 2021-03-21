// https://atcoder.jp/contests/past201912-open/tasks/past201912_e
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
// #include<map>
// #include<tuple>
#include<set>
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

int main() {
	int n, q;
	cin >> n >> q;
    vector<vector<int>> f(n, vector<int>(n, 0));
    int type, from, to;
    rep(i,q) {
        cin >> type;
        if (type==1) {
            cin >> from >> to;
            from--; to--;
            f[from][to] = 1;
        } else if (type==2) {
            cin >> from;
            from--;
            rep(j,n) if(f[j][from] && from != j) f[from][j] = 1;
        } else {
            cin >> from;
            from--;
            vector<int> v;
            rep(j,n) if(f[from][j]) v.push_back(j);
            for(auto j : v)  rep(k,n) if(f[j][k] && from != k) f[from][k] = 1;
        }
    }
    rep(i,n) {
        rep(j,n) {
            if (f[i][j]) cout << 'Y';
            else         cout << 'N';
        }
        cout << endl;
    }
	return 0;
}
