// https://atcoder.jp/contests/abc224/tasks/abc224_e
// https://atcoder.jp/contests/abc224/editorial/2814
#include <iostream>
#include <vector>
#include <map>
using namespace std;

int h, w, n;
int r[200005], c[200005], a[200005];
int rmax[200005], cmax[200005];
int dp[200005];
map<int, vector<int> > mp;

int main(void)
{
  cin >> h >> w >> n;
  for(int i = 1; i <= n; i++){
    cin >> r[i] >> c[i] >> a[i];
    mp[a[i]].push_back(i);
  }

  for(auto it = mp.rbegin(); it != mp.rend(); it++){
    for(auto i : it->second) dp[i] = max(rmax[r[i]], cmax[c[i]]);
    for(auto i : it->second){
      rmax[r[i]] = max(rmax[r[i]], dp[i] + 1);
      cmax[c[i]] = max(cmax[c[i]], dp[i] + 1);
    }
  }

  for(int i = 1; i <= n; i++) cout << dp[i] << endl;

  return 0;
}
