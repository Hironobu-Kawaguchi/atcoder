// https://atcoder.jp/contests/arc080/tasks/arc080_b
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
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;
ll gcd(ll a, ll b) { return b?gcd(b,a%b):a;}
ll lcm(ll a, ll b) { return a/gcd(a,b)*b;}

int main() {
	int h, w;
	cin >> h >> w;
    int n;
    cin >> n;
    vector<int> a(n);
    rep(i,n) cin >> a[i];
    vector<vector<int>> ans(h, vector<int>(w));
    int num = 0;
    rep(x, n) rep(y, a[x]) {
        int i = num/w;
        int j = num%w;
        if (i%2) j = w-1-j;
        ans[i][j] = x+1;
        num++;
    }
	rep(i,h) {
        rep(j,w) {
            cout << ans[i][j];
            if(j!=w-1) cout << ' ';
        }
        cout << endl;
    } 
	return 0;
}
