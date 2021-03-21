// https://codeforces.com/contest/1406/problem/C
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

// https://qiita.com/drken/items/4b4c3f1824339b090202
const int MAX_V = 100005;  // ツリーのサイズのありうる最大値

int N;  // ツリーのサイズ
vector<int> tree[MAX_V];  // ツリーを隣接リスト形式のグラフ構造で表したもの

int sizeSubtree[MAX_V];  // sizeSubtree[v] := v を根とする部分ツリーのサイズ
vector<int> centroids;  // 重心列挙の答えがここに入る

/* ツリーDP */
void SubFindCentroids(int v, int parent_of_v = -1) {
    sizeSubtree[v] = 1;
    bool isCentroid = true;
    for (auto ch : tree[v]) {
        if (ch == parent_of_v) continue;
        SubFindCentroids(ch, v);
        if (sizeSubtree[ch] > N / 2) isCentroid = false;
        sizeSubtree[v] += sizeSubtree[ch];
    }
    if (N - sizeSubtree[v] > N / 2) isCentroid = false;
    if (isCentroid) centroids.push_back(v);
}

void FindCentroids() {
    centroids.clear();
    SubFindCentroids(0, N); // これを呼び出すと centoroids に重心を列挙したものが入る
}

void solve() {
    cin >> N;
    rep(i,MAX_V) tree[i].clear();
    rep(i,N-1) {
        int x, y;
        cin >> x >> y;
        --x, --y;
        tree[x].push_back(y);
        tree[y].push_back(x);
    }
    FindCentroids();
    if(centroids.size()==1) {
        cout << 1 << ' ' << 2 << endl;
        cout << 1 << ' ' << 2 << endl;
        return;
    } else {
        int x = centroids[0];
        int y;
        for (int z: tree[x]) {
            if (z!=centroids[1]) {
                y = z;
                break;
            }
        }
        cout << x+1 << ' ' << y+1 << endl;
        x = centroids[1];
        cout << x+1 << ' ' << y+1 << endl;
    }
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int t;
	cin >> t;
    rep(i,t) solve();
	return 0;
}
