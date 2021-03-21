// https://atcoder.jp/contests/abc152/tasks/abc152_d
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

P f(int x) {
    int a = x%10;
    int b = 0;
    while (x) {
        b = x;
        x /= 10;
    }
    return P(a,b);
}

int main() {
	int N;
	cin >> N;
    map<P,int> freq;
    rep(i,N) {
        P p = f(i+1);
        freq[p]++;
    }
    ll ans = 0;
    rep(i,N) {
        P p = f(i+1);
        P q(p.second, p.first);
        ans += freq[q];
    }
	cout << ans << endl;
	return 0;
}
