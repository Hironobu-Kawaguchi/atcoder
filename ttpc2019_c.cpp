// https://atcoder.jp/contests/ttpc2019/tasks/ttpc2019_c
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
#define all(v) (v).begin(),(v).end()
#define chmin(x,y) x = min(x,y)
#define chmax(x,y) x = max(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
	int N, X;
	cin >> N >> X;
    vector<int> a(N);
    rep(i,N) cin >> a[i];
    vector<int> p;
    int s = X;
    rep(i,N) {
        if (a[i] == -1) p.push_back(i);
        else s ^= a[i];
    }
    for (int i: p) {
        a[i] = 0;
    }
    if (s != 0) {
        if (s > X) {
            if ((s^X) > X) {
                cout << -1 << endl;
                return 0;
            }
            if (p.size() < 2) {
                cout << -1 << endl;
                return 0;
            }
            a[p[0]] = X;
            a[p[1]] = X^s;
        } else {
            if (p.size() < 1) {
                cout << -1 << endl;
                return 0;
            }
            a[p[0]] = s;
        }
    }
    rep(i, N) {
        if(i) cout << ' ';
     	cout << a[i];
    }
    cout << endl;
	return 0;
}
