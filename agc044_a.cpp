// https://atcoder.jp/contests/agc044/tasks/agc044_a
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define maxs(x,y) (x = max(x,y))
#define mins(x,y) (x = min(x,y))
typedef long long int ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int a,b,c,d;

map<ll,ll> mem;
ll f(ll x) {
  if (!x) return 0;
  if (mem.count(x)) return mem[x];
  ll res = LINF;
  if (LINF/d > x) res = x*d;
  auto f2 = [&](ll y) {
    if (y >= x) return LINF;
    return f(y);
  };
  {
    ll l = x/2*2, r = l+2;
    mins(res, f2(l/2)+a+(x-l)*d);
    mins(res, f2(r/2)+a+(r-x)*d);
  }
  {
    ll l = x/3*3, r = l+3;
    mins(res, f2(l/3)+b+(x-l)*d);
    mins(res, f2(r/3)+b+(r-x)*d);
  }
  {
    ll l = x/5*5, r = l+5;
    mins(res, f2(l/5)+c+(x-l)*d);
    mins(res, f2(r/5)+c+(r-x)*d);
  }
  return mem[x] = res;
}

void solve() {
  ll n;
  cin>>n;
  scanf("%d%d%d%d",&a,&b,&c,&d);
  mem = map<ll,ll>();
  cout<<f(n)<<endl;
}

int main() {
  int ts;
  scanf("%d",&ts);
  rep(ti,ts) solve();
  return 0;
}
