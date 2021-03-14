// https://atcoder.jp/contests/arc114/tasks/arc114_a
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
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define drep(i,n) for(int i = (n-1); i >= 0; i--)
#define all(v) (v).begin(),(v).end()
#define maxs(x,y) (x = max(x,y))
#define mins(x,y) (x = min(x,y))
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

const int MAX_X = 51;
const int MAX_PRIME = 15;
// const int MAX_PRIME = 2;
const int bit_n = 1<<MAX_PRIME;
const vector<int> p = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
// const vector<int> p = {2,3};
vector<vector<bool>> divisors(MAX_X, vector<bool>(MAX_PRIME));

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n;
	cin >> n;
    vector<int> x(n);
    rep(i,n) {
        cin >> x[i];
        rep(j,MAX_PRIME) {
        // for (int j: p) {
            if(x[i] % p[j]==0) {
                divisors[i][j] = true;
                // cout << i << ' ' << j << endl;
            }
        }        
    }
    // rep(i,n) cout << x[i]; cout << endl;
    // rep(i,n) rep(j,MAX_PRIME) cout << divisors[i][j]; cout << endl;
    ll ans = LINF;
    rep(i,bit_n) {
        vector<bool> done(n);
        ll tmp = 1;
        rep(j,MAX_PRIME){
            if(i>>j&1) continue;
            // cout << i << ' ' << j << endl;
            rep(k,n) if(divisors[k][j]==true) done[k] = true;
            tmp *= p[j];
        }
        bool flg = true;
        rep(i,n) if(done[i]==false) flg = false;
        if(flg) {
            ans = min(ans, tmp);
        }
    }

	cout << ans << "\n";
	return 0;
}


// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	int n;
// 	cin >> n;
//     vector<int> x(n);
//     rep(i,n) cin >> x[i];
//     int y = 3;
//     while(true) {
//         bool flg = true;
//         rep(i,n) {
//             int gcdxy = gcd(x[i], y);
//             if(gcdxy==1) flg = false;
//         }
//         if(flg) break;
//         y++;
//     }
// 	cout << y << "\n";
// 	return 0;
// }
