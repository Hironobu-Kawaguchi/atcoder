// https://atcoder.jp/contests/arc032/tasks/arc032_2
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

// Union-Find木の実装（ランクあり）
struct UnionFind {
    vector<int> parent, rank;
    UnionFind(int n) : 
        parent(n, -1),  // parent 親
        rank(n, 0)      // rank 深さ
        {}

    // 木の根を求める
    int root(int x) {
        if (parent[x] < 0) return x;        // xが根
        else {
            parent[x] = root(parent[x]);    // 経路圧縮
            return parent[x];
        }
    }

    // xとyが同じ集合に属するか否か
    int same(int x, int y) {
        return root(x) == root(y);
    }

    // xとyの属する集合を併合   // 既に同じ集合なら false が返る
    bool unite(int x, int y) {
        x = root(x); y = root(y);
        if (x == y) return false;
        // 要素数の少ない方を多い方に繋げる
        if (rank[x] < rank[y]) {
            parent[x] = y;
        } else {
            parent[y] = x;
            if (rank[x] == rank[y]) rank[x]++;
        }
        return true;
    }
};

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, m;
	cin >> n >> m;
    UnionFind uf(n);
    int a, b;
    rep(i,m) {
        cin >> a >> b;
        --a, --b;
        uf.unite(a, b);
    }
    int ans = -1;
    rep(i,n) if(i==uf.root(i)) ans++;
	cout << ans << "\n";
	return 0;
}
