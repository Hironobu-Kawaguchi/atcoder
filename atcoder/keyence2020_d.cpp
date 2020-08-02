// https://atcoder.jp/contests/keyence2020/tasks/keyence2020_d
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
ll gcd(ll a, ll b) { return b?gcd(b,a%b):a;}
ll lcm(ll a, ll b) { return a/gcd(a,b)*b;}

int main() {
	int N;
	cin >> N;
    vector<int> A(N), B(N);
    rep(i,N) cin >> A[i];
    rep(i,N) cin >> B[i];
    vector<P> v(N);
    stack<int> s;
    int ans = 500, tmp, p, q;
    rep(i,1<<N) {  // bit探索
        tmp = 0;
        rep(j,N) {
            if ((i>>j)&1) v[j] = P(B[j], j);
            else          v[j] = P(A[j], j);
        }
        rep(j,N) {
            p = j;
            while (p && v[p].first < v[p-1].first) {
                swap(v[p], v[p-1]);
                tmp++;
                p--;
            }
        }
        rep(j,N) {
            int idx = v[j].second;
            if (((i>>idx)+idx-j)&1) s.push(v[j].first*500+j);
        }
        if (s.size()&1) {
            tmp = 500;
            s.pop();
        }
        while (s.size()) {
            p = s.top(); s.pop();
            q = s.top(); s.pop();
            if ((p-q)&1) tmp += p-q;
            else         tmp += 500;
        }
        ans = min(ans, tmp);
    }
    if (ans < 500) cout << ans << endl;
    else       	   cout << -1  << endl;
	return 0;
}
