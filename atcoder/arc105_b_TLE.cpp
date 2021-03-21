// https://atcoder.jp/contests/arc105/tasks/arc105_b
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

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    int n;
    ll ans = LINF;
    cin >> n;
    vector<ll> a(n);
    priority_queue<ll> q;
    set<ll> s;
	rep(i,n) {
        cin >> a[i];
        if(a[i]<ans) ans = a[i];
        if(s.count(a[i])==0) {
            s.insert(a[i]);
            q.push(a[i]);
        }
    }
    while(q.size()>0) {
        ll now = q.top(); q.pop();
        if(now==ans) break;
        ll dif = now - ans;
        if(s.count(dif)==0) {
            s.insert(dif);
            q.push(dif);
        }
        if(dif < ans) ans = dif;
    }
	cout << ans << "\n";
	return 0;
}
