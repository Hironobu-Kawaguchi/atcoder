// https://atcoder.jp/contests/abc150/tasks/abc150_c
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
    vector<int> P(N);
    rep(i,N) cin >> P[i];
    vector<int> Q(N);
    rep(i,N) cin >> Q[i];

    vector<int> a(N);
    rep(i,N) a[i] = i+1;
    
    map<vector<int>, int> mp;
    do {
        mp[a] = mp.size();
    } while (next_permutation(a.begin(), a.end()));

    int ans = abs(mp[P] - mp[Q]);
	cout << ans << endl;
	return 0;
}
