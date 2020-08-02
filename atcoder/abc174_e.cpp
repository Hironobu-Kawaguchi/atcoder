// https://atcoder.jp/contests/abc174/tasks/abc174_e
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

int MAXN=200005;
int n, k;
vector<int> a(MAXN);

bool chk(int x) {
    int cnt = 0;
    rep(i,n) {
        cnt += (a[i]-1)/x;
    }
    if(cnt<=k) return true;
    return false;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	cin >> n >> k;
    rep(i,n) cin >> a[i];
    int l=1, r=1000000000, now;
    while (r>l) {
        now = (l+r)/2;
        if(chk(now)) {
            r = now;
        } else {
            l = now+1;
        }
    }
    cout << r << "\n";
	return 0;
}
