// https://codeforces.com/contest/1406/problem/B
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

void solve() {
    int n;
    cin >> n;
    vector<int> a(n), apos, aneg;
    int pos = 0, neg = 0;
    rep(i,n) {
        cin >> a[i];
        if(a[i]>0) {
            ++pos;
            apos.push_back(a[i]);
        }
        if(a[i]<0) {
            ++neg;
            aneg.push_back(a[i]);
        }
    }
    sort(a.begin(),a.end(), [](int i, int j) -> bool {
        return abs(i) < abs(j);
        });
    sort(apos.rbegin(), apos.rend());
    sort(aneg.begin(), aneg.end());
    // rep(i,n) cout << a[i];
    // cout << endl;
    ll ans = (ll) a[0]*a[1]*a[2]*a[3]*a[4];
    ll tmp;
    if(pos>=5) {
        tmp = (ll) apos[0]*apos[1]*apos[2]*apos[3]*apos[4];
        maxs(ans, tmp);
    }   
    if(pos>=3 && neg>=2) {
        tmp = (ll) apos[0]*apos[1]*apos[2]*aneg[0]*aneg[1];
        maxs(ans, tmp);
    }
    if(pos>=1 && neg>=4) {
        tmp = (ll) apos[0]*aneg[0]*aneg[1]*aneg[2]*aneg[3];
        maxs(ans, tmp);
    }
    cout << ans << endl;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int t;
	cin >> t;
    rep(i,t) solve();
	return 0;
}
