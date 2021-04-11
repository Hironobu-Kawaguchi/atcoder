#include <iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
#include<vector>
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
// #include<bits/stdc++.h>

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
    int t, n;
    cin >> t;
    for (int x = 1; x <= t; ++x) {
        cin >> n;
        vector<vector<int>> m(n, vector<int>(n));
        rep(i,n) rep(j,n) cin >> m[i][j];
        int k = 0, r = 0, c = 0;
        rep(i,n) {
            k += m[i][i];
            vector<int> rows(n), cols(n);
            rep(j,n) {
                rows[m[i][j]-1] += 1;
                cols[m[j][i]-1] += 1;
            }
            rep(j,n) if(rows[j]!=1) {
                r++;
                break;
            }
            rep(j,n) if(cols[j]!=1) {
                c++; 
                break;
            }
        }
        cout << "Case #" << x << ": " << k << " " << r << " " << c << endl;
    }
    return 0;
}
