// https://atcoder.jp/contests/abc096/tasks/abc096_d
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
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

bool isprime(int p) {
    if (p==1) return false;
    for (int i = 2; i < p; i++) {
        if (p%i == 0) return false;
    }
    return true;
}
int main() {
	int n;
	cin >> n;
    for (int i = 11; i <= 55555; i += 10) {
        if (isprime(i)) {
            if (i != 11) cout << ' ';
            cout << i;
            n--;
        }
        if (n == 0) break;
    }
	cout << endl;
	return 0;
}
