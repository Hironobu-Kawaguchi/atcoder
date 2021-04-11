// https://atcoder.jp/contests/arc111/tasks/arc111_c
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

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n;
	cin >> n;
    vector<ll> a(n), b(n);
    vector<int> p(n);
    rep(i,n) cin >> a[i];
    rep(i,n) cin >> b[i];
    int cnt = 0;
    rep(i,n) {
        cin >> p[i];
        p[i]--;
        if (p[i]!=i) cnt++;
    }
    int ans;
    if (cnt>0) ans = cnt - 1;
    else       ans = cnt;
    vector<P> move;
    rep(i,n) {
        if (a[i] <= b[p[i]] && p[i]!=i) {
            cout << -1 << "\n";
            return 0;
        }
    }
    while(cnt>0) {
        bool no_change = true;
        rep(i,n) {
            if (p[i]==i) continue;
            rep(j,n) {
                if (p[j]==j) continue;
                if (p[i]==j && a[j]>b[i]) {
                    // swap(b[i], b[j]);
                    swap(p[i], p[j]);
                    // p[i] = j;
                    // p[j] = i;
                    cnt--;
                    if (p[i]==i) cnt--;
                    move.push_back(make_pair(i+1, j+1));
                    no_change = false;
                    continue;
                }
                if (p[j]==i && a[i]>b[j]) {
                    // swap(b[i], b[j]);
                    swap(p[i], p[j]);
                    // p[i] = j;
                    // p[j] = i;
                    cnt--;
                    move.push_back(make_pair(i+1, j+1));
                    if (p[j]==j) cnt--;
                    no_change = false;
                    continue;
                }
            }
        }
        if (no_change) {  // 全て変えられなかった
            ans = -1;
            break;
        }
    }
	cout << ans << "\n";
    if (ans>0) {
        for (P p : move) {
            cout << p.first << ' ' << p.second << "\n";
        }
        
    }
	return 0;
}
