// https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f00
#include <iostream>
#include<algorithm>
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
    int t;
    cin >> t;
    for (int x = 1; x <= t; ++x) {
        int n, k;
        cin >> n >> k;
        vector<int> p(n);
        rep(i,n) cin >> p[i];
        sort(p.begin(), p.end());
        vector<int> ys;
        ys.push_back(p[0]-1);
        ys.push_back(k-p.back());
        rep(i,n-1) ys.push_back((p[i+1]-p[i])/2);
        sort(ys.rbegin(), ys.rend());
        double y = ys[0]+ys[1];
        cout << "Case #" << x << ": " << y/k << endl;
    }
    return 0;
}
