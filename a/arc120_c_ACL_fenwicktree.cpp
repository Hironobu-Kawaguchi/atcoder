// https://atcoder.jp/contests/arc120/tasks/arc120_c
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
#include <atcoder/all>
using namespace atcoder;
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

using vl=vector<ll>;

int main() {
    int N; cin>>N;
    vl A(N), B(N);
    for (int i = 0; i < N; i++)cin>>A[i];
    for (int i = 0; i < N; i++)cin>>B[i];

    fenwick_tree<int> fw(N);
    for (int i = 0; i < N; i++)A[i] += i;
    map<ll, queue<int>> pos;
    for (int i = 0; i < N; i++){
        pos[A[i]].push(i);
    }

    ll ans = 0;
    for (int i = 0; i < N; i++){
        ll target = B[i] + i;
        if(pos[target].empty()){
            cout << -1 << endl;
            return 0;
        }
        int d = pos[target].front();
        pos[target].pop();
        fw.add(d, 1);
        ans += d -fw.sum(0, d);
    }

    cout << ans << endl;
}

// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	int n;
// 	cin >> n;
//     vector<ll> a(n), b(n);
//     rep(i,n) cin >> a[i];
//     rep(i,n) cin >> b[i];
//     map<ll, vector<int>> amap, bmap;
//     rep(i,n) amap[a[i]+i].push_back(i);
//     rep(i,n) bmap[b[i]+i].push_back(i);
//     vector<int> to(n);
//     for (auto [k, ls]: amap) {
//         if (bmap.count(k)==0) {
//             cout << -1 << endl;
//             return 0;
//         } else if (ls.size() != bmap[k].size()) {
//             cout << -1 << endl;
//             return 0;
//         }
//         for (int i=0; i<ls.size(); ++i) to[ls[i]] = bmap[k][i];
//     }
//     rep(i,n) cout << to[i] << endl;
//     int ans = 0;
//     set<int> st;
//     rep(i,n) st.insert(i);
//     rep(i,n) {
//         // int idx = int(lower_bound(st.begin(), st.end(), to[i]) - st.begin());
//         auto idx = st.lower_bound(to[i]);
//         auto idx_b = st.begin();
//         ans += *idx - *idx_b;
//         cout << ans << ' ' << st.size() << endl;
//         st.erase(*idx);
//     }
// 	cout << ans << "\n";
// 	return 0;
// }
