// https://atcoder.jp/contests/abc146/tasks/abc146_e
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
#include<map>
// #include<tuple>
// #include<set>
#include<queue>
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
	int n, k;
	cin >> n >> k;
    vector<int> a(n);
    rep(i,n) cin >> a[i];
    rep(i,n) a[i]--;
    vector<int> s(n+1);
    rep(i,n) {
        s[i+1] = (s[i]+a[i])%k; // 累積和
    }
    map<int,int> mp;    // 連想配列
    ll ans = 0;
    queue<int> q;
    rep(j,n+1) {
        ans += mp[s[j]];
        mp[s[j]]++;
        q.push(s[j]);
        if (q.size() == k) {
            mp[q.front()]--;
            q.pop();
        }
    }
	cout << ans << endl;
	return 0;
}
