// https://atcoder.jp/contests/agc040/tasks/agc040_a
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

int N;
string S;
vector<int> a;

int dfs(int i) {
    if (a[i] != -1) return a[i];
    a[i] = 0;
    if (i && S[i-1] == '<') {
        chmax(a[i], dfs(i-1)+1);
    }
    if (i+1 < N && S[i] == '>') {
        chmax(a[i], dfs(i+1)+1);
    }
    return a[i];
}

int main() {
	cin >> S;
    N = S.size() + 1;
    a = vector<int>(N, -1);
    rep(i,N) dfs(i);
    ll ans = 0;
    for (ll x: a) ans += x;
	cout << ans << endl;
	return 0;
}
