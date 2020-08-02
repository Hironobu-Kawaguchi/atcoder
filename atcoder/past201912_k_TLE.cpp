// https://atcoder.jp/contests/past201912-open/tasks/past201912_k
// LCA 最小共通祖先 or 行きがけ順
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
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

vector<int> od(150005, 0), d(150005, 0);
vector<vector<int>> sub(150005);
int ranking = 1;

int dfs(int member, int depth) {
    od[member] = ranking;
    d[member] = depth;
    for (int m : sub[member]) {
        if(od[m]) continue;    // 既に順番が確定
        ranking++;
        dfs(m, depth+1);
    }
    return 0;
}

vector<int> v(150005, 0);
int dir = 0;
int dfs2(int root, vector<int> v) {
    for (int m : sub[root]) {
        if (v[m]) continue;
        v[m] = 1;
        dir++;
        dfs2(m, v);
    }
    return 0;
}

int main() {
	int n;
	cin >> n;
    vector<int> p(n);
    int boss;
    rep(i, n) {
        cin >> p[i];
        if (p[i] == -1) boss = i;
        else sub[p[i]-1].emplace_back(i);
    }
    dfs(boss, 0);
    // rep(i,n) cout << od[i] << ' ';
    // cout << endl;
    // rep(i,n) cout << d[i] << ' ';
    // cout << endl;
    int q;
    cin >> q;
    int a, b;
    rep(i,q) {
        cin >> a >> b;
        a--; b--;
        // cout << od[a] << ' ' << od[b] << endl;
        if ((od[a] > od[b]) && (d[a] > d[b])) {
            rep(i,n) v[i] = 0;
            dir = 0;
            dfs2(b, v);
            // cout << dir << ' ' << od[a] << ' ' <<  od[b] << endl;
            if (od[a] <= od[b] + dir) {
                cout << "Yes" << endl;
            } else cout << "No"  << endl;
        } else cout << "No"  << endl;
    }
	return 0;
}
