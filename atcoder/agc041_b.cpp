// https://atcoder.jp/contests/agc041/tasks/agc041_b
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

const int MAXN = 100005;
int n, v, p;
ll m;
vector<ll> a(MAXN);

bool ok(int t) {
    if(t<=p) return true;               // すでに圏内
    if(a[p-1]>a[t-1]+m) return false;   // mを加えても逆転できない
    if(n-t+p >= v) return true;         // 加算する問題の種類がp-1位まで、自分、自分以降の数以下
    ll add = (v-(n-t+p)) * m;           // add: 追い抜く必要がある問題に加算されるスコア
    ll mxt = a[t-1] + m;
    ll tmp = 0;
    for (int i = p-1; i < t-1; i++) {
        tmp += mxt - a[i];
        if (tmp >= add) return true;    // add を全部足しても、追い越せる
    }
    return false;
}

int main() {
	cin >> n >> m >> v >> p;
    rep(i,n) cin >> a[i];
    sort(a.begin(), a.end(), greater<ll>());

    ll ans;
    ll start = 1, end = n+1;
    while (start + 1 < end) {           // 二分探索
        ans = (start + end) / 2;
        if (ok(ans)) start = ans;
        else         end   = ans;
    	// cout << start << ' ' << ans << ' ' << end << endl;
    }
    ans = (start + end) / 2;
    cout << ans << endl;
	return 0;
}
