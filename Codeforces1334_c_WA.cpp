// https://codeforces.com/contest/1334/problem/C
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
#define drep(i,n) for(int i = (n-1); i >= 0; i--)
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

void solve() {
    int n;
    // cin >> n;
    scanf("%d", &n);
    vector<ll> a(n+1), b(n+1);
    // rep(i,n) cin >> a[i] >> b[i];
    rep(i,n) {
        scanf("%d", &a[i]);
        scanf("%d", &b[i]);
    }
    ll sum = 0, start = LINF;
    a[n] = a[0]; b[n] = b[0];
    rep(i,n) {
        if(a[i+1]>b[i]) {
            sum += a[i+1] - b[i];
            start = min(start, b[i]);
        } else {
            start = min(start, a[i+1]);
        }
    }
    // cout << sum + start << "\n";
    printf("%d\n", sum + start);
}

int main() {
	int t;
	// cin >> t;
    scanf("%d", &t);
    rep(i,t) solve();
	return 0;
}
