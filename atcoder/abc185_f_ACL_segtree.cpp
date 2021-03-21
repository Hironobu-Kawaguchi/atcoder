// https://atcoder.jp/contests/abc185/tasks/abc185_f

#include <bits/stdc++.h>
#include <atcoder/segtree>
using namespace std;
using namespace atcoder;

#define rep(i,n) for(int i=0; i<n;i++)
typedef long long ll;
typedef pair<int, int> P;

int op(int x, int y) { return x^y;}
int e() { return 0;}

int main() {
    int n, q, a, typ, x, y;
    scanf("%d%d", &n, &q);
    segtree<int,op,e> t(n);
    rep(i,n) {
        scanf("%d", &a);
        t.set(i,a);
    }
    rep(qi,q) {
        scanf("%d%d%d", &typ, &x, &y);
        --x;
        if(typ==1) {
            t.set(x, op(t.get(x),y));
        } else {
            printf("%d\n", t.prod(x,y));
        }
    }
    return 0;
}



// // https://atcoder.jp/contests/abc185/submissions/18768850
// #include <iostream>
// #include <bits/stdc++.h>
// using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
// #define rep(i,n) for (int i = 0; i < (n); ++i)
// using ll = long long;
// using P = pair<int,int>;

// int op(int x, int y) { return x^y;}
// int e() { return 0;}

// int main() {
//   int n, q;
//   cin >> n >> q;
//   segtree<int,op,e> t(n);
//   rep(i,n) {
//     int a;
//     cin >> a;
//     t.set(i,a);
//   }
//   rep(qi,q) {
//     int type, x, y;
//     cin >> type >> x >> y;
//     --x;
//     if (type == 1) {
//       t.set(x, t.get(x)^y);
//     } else {
//       int ans = t.prod(x,y);
//       cout << ans << endl;
//     }
//   }
//   return 0;
// }