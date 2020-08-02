// https://atcoder.jp/contests/arc002/tasks/arc002_3
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

int main() {
	int n;
    string s;
	cin >> n >> s;
    vector<char> c = {'A', 'B', 'X', 'Y'}, r(4);
    int ans = INF, x, j;
    rep(i,256) {
        rep(k,4) r[k] = c[(i>>(k*2))&3];
        x = 0;
        j = 0;
        while (j<n-1) {
            if ((s[j]==r[0] && s[j+1]==r[1]) || (s[j]==r[2] && s[j+1]==r[3])) {
                x++;
                j += 2;
            } else {
                x++;
                j++;
            }
        }
        if (j==n-1) x++;
        ans = min(ans, x);
    }

	cout << ans << endl;
	return 0;
}
