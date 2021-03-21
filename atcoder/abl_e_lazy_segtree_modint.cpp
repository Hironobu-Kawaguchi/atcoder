// https://atcoder.jp/contests/abl/tasks/abl_e
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

using mint = modint998244353;
const mint inv9 = mint(1)/9;  // 逆元

struct S {
    mint x, w;
    S(mint x=0, mint w=1):x(x),w(w) {}  // コンストラクタ
};

S op(S a, S b) { return S(a.x*b.w + b.x, a.w*b.w);}
S e() { return S();}
S mapping(int f, S a) {
    if(f==0) return a;
    // return S((a.w-1)/9 * f,a.w);
    return S((a.w-1)*inv9 * f,a.w);
}
int composition(int f, int g) {
    if(f==0) return g;
    return f;
}
int id() { return 0;}

int main() {
    int n, q;
    cin >> n >> q;
    lazy_segtree<S,op,e,int,mapping,composition,id> t(n);
    rep(i,n) t.set(i, S(1,10));
    rep(qi,q) {
        int l, r, d;
        cin >> l >> r >> d;
        --l;
        t.apply(l,r,d);
        S ans = t.all_prod();
        // cout << ans.x.val() << endl;
        printf("%d\n", ans.x.val());
    }
    return 0;
}
