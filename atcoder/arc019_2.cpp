// https://atcoder.jp/contests/arc019/tasks/arc019_2
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
#define all(v) (v).begin(),(v).end()
#define chmin(x,y) x = min(x,y)
#define chmax(x,y) x = max(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
	string A;
	cin >> A;
    int L = A.size();
    int dif= 0 ;
    rep(i,L) if(A[i]!=A[L-i-1]) dif++;
    int x;
    if(L%2) {
        if(dif==0)      x = 25;
        else if(dif==2) x = 2;
        else            x = 0;
    } else {
        if(dif==2)      x = 2;
        else            x = 0;
    }
    int ans = L*25 - x;
	cout << ans << endl;
	return 0;
}
