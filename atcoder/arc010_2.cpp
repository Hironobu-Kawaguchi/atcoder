// https://atcoder.jp/contests/arc010/tasks/arc010_2
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
#define rrep(i,n) for (int i = 1; i <= n; i++)
#define all(v) (v).begin(),(v).end()
#define chmin(x,y) x = min(x,y)
#define chmax(x,y) x = max(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

const int ds[13] = {0,31,29,31,30,31,30,31,31,30,31,30,31};
int s[13][32];

int main() {
	int N;
	cin >> N;

    int x, y, ans = 0;
    x = 0;
    rrep(i,12){
        rrep(j,ds[i]){
            if(x%7==0 || x%7==6) s[i][j] = 1;
            x++;
        }
    }
    rep(i,N){
        scanf("%d/%d", &x, &y);
        s[x][y]++;
    }

    x = 0; y = 0;
    rrep(i,12){
        rrep(j,ds[i]){
            x += s[i][j];
            if(x){x--; y++;} else y = 0;
            ans = max(ans, y);
        }
    }

	cout << ans << endl;
	return 0;
}
