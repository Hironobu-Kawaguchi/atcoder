// https://atcoder.jp/contests/abc161/tasks/abc161_e
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

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, k ,c;
	cin >> n >> k >> c;
    string s;
    cin >> s;
    auto getPositions = [&]() {
        vector<int> res;
        for (int i = 0; i < n && res.size() < k;) {
            if (s[i]=='o') {
                res.push_back(i);
                i += c+1;
            } else {
                ++i;
            }
        }
        return res;
    };
    vector<int> l, r;
    l = getPositions();
    reverse(s.begin(), s.end());
    r = getPositions();
    rep(i,k) r[i] = n-1-r[i];
    reverse(s.begin(), s.end());

    rep(i,k) {
        if (l[i]==r[k-1-i]) cout << l[i]+1 << endl;
    }
 
	return 0;
}
