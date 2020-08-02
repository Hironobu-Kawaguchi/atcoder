// https://atcoder.jp/contests/arc098/tasks/arc098_b
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
	int N;
	cin >> N;
    vector<ll> A(N+1), S(N+1);
    rep (i, N) {
        ll x;
        cin >> x;
        A[i+1] = A[i] ^ x;
        S[i+1] = S[i] + x;
    }
    ll ans = 0;
    int l = 1;
    for (int r = 1; r <= N; r++) {
        while ((S[r]-S[l-1]) != (A[r]^A[l-1])) {
            l++;
        }
        ans += r-l+1;        
    }
	cout << ans << endl;
	return 0;
}
