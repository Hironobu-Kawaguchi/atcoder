// https://atcoder.jp/contests/abc120/tasks/abc120_d   碧黴本
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
#include<iomanip>
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

struct UnionFind {
    vector<int> data;
    UnionFind(int size) : data(size, -1) {}

    // 集合をマージする
    // 既に同じ集合なら false が返る
    bool merge(int x, int y) {
        x = root(x); y = root(y);
        if (x == y) return false;
        // 要素数の少ない方を多い方に繋げる
        if (data[y] < data[x]) swap(x, y);
        data[x] += data[y];
        data[y] = x;
        return true;
    }
    // ある要素がどの集合に属しているかを答える
    int root(int x) {
        // 根に直接つなぎ直す
        return data[x] < 0 ? x : (data[x]=root(data[x]));
    }
    // ある集合の大きさを答える
    int size(int x) {
        return -data[root(x)];
    }
};

int main() {
    ll N, M;
    cin >> N >> M;
    vector<ll> a(M);
    vector<ll> b(M);
    rep(i, M) {
        cin >> a[i] >> b[i];
        a[i]--; b[i]--;
    }
    UnionFind UF(N);
    vector<ll> ans(M, 0);
    // 不便さ
    ans[M-1] = N*(N-1)/2;

    for (int i = M-1; i > 0; i--) {
        if(UF.root(a[i]) == UF.root(b[i])) {
            ans[i-1] = ans[i];
            continue;
        }
        // 新たに行き来できるようになった頂点のペアの数だけ不便さが減る
        // オーバーフローに注意
        ans[i-1] = ans[i] - 1ll*UF.size(a[i])*UF.size(b[i]);
        UF.merge(a[i], b[i]);
    }
	rep(i, M) cout << ans[i] << endl;
	return 0;
}
