// https://atcoder.jp/contests/practice2/tasks/practice2_k
// https://atcoder.github.io/ac-library/production/document_ja/lazysegtree.html
#include <atcoder/lazysegtree>
#include <atcoder/modint>
#include <cstdio>

using namespace std;
using namespace atcoder;

using mint = modint998244353;

// モノイド（セグメントツリーが扱うデータ）の型
struct S {
    mint a;
    int size;
};

// 写像（更新操作）を表す型
struct F {
    mint b, c;
};

S op(S l, S r) { return S{l.a + r.a, l.size + r.size}; }    // データのマージ操作

S e() { return S{0, 0}; }                                   // データの初期値

// データの更新操作 f:写像, x:更新対象  sum(a) * b + c * sum(size)
S mapping(F f, S x) { return S{x.a * f.b + x.size * f.c, x.size}; }

// 写像の合成（2つの更新操作f,gを組み合わせる方法）を定義
F composition(F f, F g) { return F{g.b * f.b, g.c * f.b + f.c}; }

F id() { return F{1, 0}; }  // 恒等写像（何も変更しない操作）を表す値   a * 1 + 0

int main() {
    int n, q;
    scanf("%d %d", &n, &q);

    vector<S> a(n);
    for (int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        a[i] = S{x, 1};
    }

    lazy_segtree<S, op, e, F, mapping, composition, id> seg(a);

    for (int i = 0; i < q; i++) {
        int t;
        scanf("%d", &t);
        if (t == 0) {
            int l, r;
            int c, d;
            scanf("%d %d %d %d", &l, &r, &c, &d);
            seg.apply(l, r, F{c, d});
            // for (int i = 0; i < n; i++) {
            //     printf("%d%c", seg.get(i).a.val(), i == n - 1 ? '\n' : ' ');
            // }
        } else {
            int l, r;
            scanf("%d %d", &l, &r);
            printf("%d\n", seg.prod(l, r).a.val());
        }
    }
}