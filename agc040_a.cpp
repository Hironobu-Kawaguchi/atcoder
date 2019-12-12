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

int main() {
    string S;
	cin >> S;
    int N = S.size() + 1;
    vector<ll> Cnt;
    if (S[0] == '>') Cnt.push_back(0);
    ll num = 1;
    rep(i, N-2) {
        if (S[i] == S[i+1]) {
            num++;
        } else {
            Cnt.push_back(num);
            num = 1;
        }
    }
    Cnt.push_back(num);
    if (S[N-2] == '<') Cnt.push_back(0);

    ll ans = 0;
    rep(i, Cnt.size()/2) {
        if (Cnt[2*i]   > 1) ans += (Cnt[2*i]  -1)*(Cnt[2*i])  /2;
        if (Cnt[2*i+1] > 1) ans += (Cnt[2*i+1]-1)*(Cnt[2*i+1])/2;
        ans += max(Cnt[2*i], Cnt[2*i+1]);
    }
	cout << ans << endl;
	return 0;
}
