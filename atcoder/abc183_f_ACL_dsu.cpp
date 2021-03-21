// https://atcoder.jp/contests/abc183/tasks/abc183_f
// https://atcoder.jp/contests/abc183/submissions/18111496
#include <iostream>
#include <vector>
#include <map>
#include <atcoder/dsu>
using namespace std;
using namespace atcoder;

int main() {
	int n,q;
	cin >> n >> q;
	vector<map<int,int>> cnt(n);
	for(int i=0; i<n; i++) {
		int c;
		cin >> c;
		c--;
		cnt[i][c] = 1;
	}
	
	dsu d(n);
	while(q--) {
		int t,x,y;
		cin >> t >> x >> y;
		x--,y--;
		if(t==1){
			x = d.leader(x);
			y = d.leader(y);
			if(x!=y){
				int r = d.merge(x,y);
				if(r!=x) swap(x,y);  // yをxに統合する
				for(auto temp:cnt[y]) cnt[x][temp.first] += temp.second;
			}
		} else {
			cout << cnt[d.leader(x)][y] << endl;
		}
	}
}
