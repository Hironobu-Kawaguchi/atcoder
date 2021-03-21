// https://atcoder.jp/contests/abc117/tasks/abc117_d
// https://atcoder.jp/contests/abc117/submissions/4155836
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<iomanip>
#include<math.h>
#include<complex>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<bitset>
#include<functional>
#include<assert.h>
#include<numeric>
using namespace std;
#define REP(i,m,n) for(int i=(int)m ; i < (int) n ; ++i )
#define rep(i,n) REP(i,0,n)
typedef long long ll;
typedef pair<int,int> pint;
typedef pair<ll,int> pli;
const int inf=1e9+7;
const ll longinf=1LL<<60 ;
const ll mod=1e9+7;

int main(){
    ll n;
    cin>>n;
    ll k;cin>>k;
    ll a[n];
    rep(i,n)cin>>a[i];
    ll ans=0;
    ll ret=0;
    for(int i=40;i>=0;--i){
        ll mask=1LL<<i;
        ll cnt=0;
        rep(j,n){
            if(a[j]&mask)++cnt;
        }
        if(cnt>=n-cnt){
            ans+=mask*cnt;
        }
        else {
            if(mask+ret<=k){
                ans+=(n-cnt)*mask;
                ret+=mask;
            }
            else ans+=mask*cnt;
        }
    }
    cout<<ans<<endl;
    return 0;
}
