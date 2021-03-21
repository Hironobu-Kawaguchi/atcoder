// https://atcoder.jp/contests/aising2020/tasks/aising2020_d
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

int pcnt(int x) {
    return __builtin_popcount(x);
}

int f(int x) {
    if (x == 0) return 0;
    return f(x%pcnt(x))+1;
}
int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n;
	cin >> n;
    string s;
    cin >> s;
    vector<int> x(n);
    rep(i,n) x[i] = s[i]-'0';
    int pc = 0;
    rep(i,n) pc += x[i];
    vector<int> ans(n);
    rep(b,2) {
        int npc = pc;
        if (b==0) npc++; else npc--;
        if (npc <= 0) continue;
        int r0 = 0;
        rep(i,n) {
            r0 = (r0*2)%npc;
            r0 += x[i];
        }
        int k = 1;
        for (int i = n-1; i >= 0; i--) {
            if (x[i] == b) {
                int r = r0;
                if (b == 0) r = (r+k)%npc;
                else r = (r-k+npc)%npc;
                ans[i] = f(r)+1;
            }
            k = (k*2)%npc;
        }
    }
    
    rep(i,n) cout << ans[i] << "\n";
	return 0;
}
