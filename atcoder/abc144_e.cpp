// https://atcoder.jp/contests/abc144/tasks/abc144_e
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
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
	int N;
    ll K;
	cin >> N >> K;
    vector<int> A(N), F(N);
    rep(i, N) cin >> A[i];
    rep(i, N) cin >> F[i];
    sort(all(A));
    // sort(all(F));
    // reverse(all(F));
    sort(F.rbegin(), F.rend());
    ll start = -1, end = 1e12;
    while (start + 1 < end) {
        ll now = (start + end) / 2;
        bool ok = [&] {
            ll s = 0;
            rep(i, N) {
                s += max(0ll, A[i]-now/F[i]);
            }
            return s <= K;
        } ();
        if (ok) end = now; else start = now;
    }
    cout << end << endl;
    return 0;
}
