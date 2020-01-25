// https://atcoder.jp/contests/tenka1-2017/tasks/tenka1_2017_c
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
	ll N;
	cin >> N;
    ll h, n, w;
    for (int i = 1; i <= 3500; i++) {
        for (int j = 1; j <= 3500; j++) {
            if (((4*i*j-N*i-N*j)>0) && ((N*i*j)%(4*i*j-N*i-N*j)==0)) {
                w = (N*i*j)/(4*i*j-N*i-N*j);
                h = i;
                n = j;
                cout << h << ' ' << n << ' ' << w << endl;
                return 0;
            }
        }
    }
}
