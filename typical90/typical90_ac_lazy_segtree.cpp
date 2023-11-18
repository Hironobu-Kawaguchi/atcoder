// https://atcoder.jp/contests/typical90/tasks/typical90_ac
#include<iostream>
// #include<algorithm>
// #include<cmath>
// #include <ctime>
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

using S = int;  // モノイド（セグメントツリーが扱うデータ）の型
using F = int;  // 写像（更新操作）を表す型
S op(S x, S y) { return S{max(x, y)}; }     // データのマージ操作
S e() { return 0; }                         // データの初期値
S mapping(F f, S x) { return f == -1 ? x : (S)f; }  // データの更新操作 f:写像, x:更新対象
F composition(F f, F g) { return f == -1 ? g : f; } // 写像の合成（2つの更新操作f,gを組み合わせる方法）を定義
F id() { return -1; }   // 恒等写像（何も変更しない操作）を表す値

int main() {
    int w, n;
	cin >> w >> n;

    lazy_segtree<S, op, e, F, mapping, composition, id> seg(w);

    rep(i, n) {
		int l, r;
		cin >> l >> r;
		l--;
		int h = seg.prod(l, r) + 1;     // [l,r)の最大値+1
		seg.apply(l, r, h);             // [l,r)をhに更新
		cout << h << endl;
    }
    return 0;
}
