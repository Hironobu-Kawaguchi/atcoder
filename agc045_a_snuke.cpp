// https://atcoder.jp/contests/agc045/tasks/agc045_a
// https://atcoder.jp/contests/agc045/submissions/14091514
#include <bits/stdc++.h>
#define fi first
#define se second
#define rep(i,n) for(int i = 0; i < (n); ++i)
#define rrep(i,n) for(int i = 1; i <= (n); ++i)
#define drep(i,n) for(int i = (n)-1; i >= 0; --i)
#define srep(i,s,t) for (int i = s; i < t; ++i)
#define rng(a) a.begin(),a.end()
#define rrng(a) a.rbegin(),a.rend()
#define maxs(x,y) (x = max(x,y))
#define mins(x,y) (x = min(x,y))
#define isin(x,l,r) ((l) <= (x) && (x) < (r))
#define pb push_back
#define eb emplace_back
#define sz(x) (int)(x).size()
#define pcnt __builtin_popcountll
#define uni(x) x.erase(unique(rng(x)),x.end())
#define snuke srand((unsigned)clock()+(unsigned)time(NULL));
#define show(x) cout<<#x<<" = "<<x<<endl;
#define PQ(T) priority_queue<T,v(T),greater<T> >
#define bn(x) ((1<<x)-1)
#define dup(x,y) (((x)+(y)-1)/(y))
#define newline puts("")
#define v(T) vector<T>
#define vv(T) v(v(T))
using namespace std;
typedef long long int ll;
typedef unsigned uint;
typedef unsigned long long ull;
typedef pair<int,int> P;
typedef tuple<int,int,int> T;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<P> vp;
typedef vector<T> vt;
inline int getInt() { int x; scanf("%d",&x); return x;}
template<typename T>inline istream& operator>>(istream&i,v(T)&v)
{rep(j,sz(v))i>>v[j];return i;}
template<typename T>string join(const v(T)&v)
{stringstream s;rep(i,sz(v))s<<' '<<v[i];return s.str().substr(1);}
template<typename T>inline ostream& operator<<(ostream&o,const v(T)&v)
{if(sz(v))o<<join(v);return o;}
template<typename T1,typename T2>inline istream& operator>>(istream&i,pair<T1,T2>&v)
{return i>>v.fi>>v.se;}
template<typename T1,typename T2>inline ostream& operator<<(ostream&o,const pair<T1,T2>&v)
{return o<<v.fi<<","<<v.se;}
template<typename T>inline ll suma(const v(T)& a) { ll res(0); for (auto&& x : a) res += x; return res;}
const double eps = 1e-10;
const ll LINF = 1001002003004005006ll;
const int INF = 1001001001;
#define dame { puts("1"); return;}
#define yn {puts("Yes");}else{puts("No");}
const int MX = 200005;

inline int bsr(ll x) { return 63^__builtin_clzll(x);}
struct BB {
  const int n = 60;
  vl d;
  BB(): d(n) {}
  void add(ll x) {
    x = tomin(x);
    if (!x) return;
    int p = bsr(x);
    rep(i,n) if (d[i]>>p&1) d[i] ^= x;
    d[p] = x;
  };
  ll& operator[] (int i) { return d[i];}
  inline ll tomin(ll x) {
    drep(i,n) if (x>>i&1) x ^= d[i];
    return x;
  }
  inline ll tomax(ll x) {
    drep(i,n) if (~x>>i&1) x ^= d[i];
    return x;
  }
};


void solve() {
  int n;
  scanf("%d",&n);
  vl a(n);
  cin>>a;
  string s;
  cin>>s;
  BB b;
  drep(i,n) {
    if (s[i] == '0') {
      b.add(a[i]);
    } else {
      if (b.tomin(a[i])) dame;
    }
  }
  cout<<0<<endl;
}

int main() {
  int ts;
  scanf("%d",&ts);
  rep(ti,ts) solve();
  return 0;
}
