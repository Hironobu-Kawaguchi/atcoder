// https://atcoder.jp/contests/past201912-open/tasks/past201912_d
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
	cin >> n;
    vector<int> a(n), c(n,0);
    rep(i,n) {
        cin >> a[i];
        c[a[i]-1]++;
    }
    int x = 0, y = 0;
    rep(i,n) {
        if (c[i] == 0)     x = i+1;
        else if (c[i] > 1) y = i+1;
    }
    if (x==0) cout << "Correct" << endl;
    else      cout << y << ' ' << x << endl;
	return 0;
}
