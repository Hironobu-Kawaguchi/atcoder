// https://atcoder.jp/contests/agc041/tasks/agc041_a
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

int main() {
	ll N, A, B;
	cin >> N >> A >> B;
    ll ans = 0;
    if ((B-A)%2) ans = (B-A)/2 + min(A-1, N-B) + 1;
    else         ans = (B-A)/2;
	cout << ans << endl;
	return 0;
}

// vurtual traial

// #include<bits/stdc++.h>
// using namespace std;
// #define rep(i,n) for (int i = 0; i < (n); ++i)
// #define drep(i,n) for(int i = (n-1); i >= 0; i--)
// #define all(v) (v).begin(),(v).end()
// template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
// template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
// template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
// template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
// typedef pair<int, int> P;
// typedef long long ll;
// const int INF = 1001001001;
// const ll LINF = 1001002003004005006ll;
// const ll MOD = 1e9+7;

// int main() {
// 	ll n, a, b;
// 	cin >> n >> a >> b;
//     ll ans;
//     if ((b-a)%2) {
//         ans = min((b-a+1)/2+(a-1), ((b-a+1)/2+(n-b)));
//     } else {
//         ans = (b-a)/2;
//     }
// 	cout << ans << endl;
// 	return 0;
// }
