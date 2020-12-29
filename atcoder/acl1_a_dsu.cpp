// https://atcoder.jp/contests/acl1/tasks/acl1_a
// https://atcoder.github.io/ac-library/production/document_ja/dsu.html
#include <bits/stdc++.h>
// #include <atcoder/all>
#include <atcoder/dsu>
using namespace std;
using namespace atcoder;
using ll = long long;
using P = pair<int,int>;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define Inf 1000000001

int main(){
	
	int N;
	cin>>N;
	
	vector<vector<int>> X(N);
	
	rep(i,N){
		int x,y;
		scanf("%d %d",&x,&y);
		X[i] = {x,y,i};
	}
	
	sort(X.begin(),X.end());
	dsu D(N);
	set<pair<int,int>> S;
	
	rep(i,N){
		if(S.size()>0 && (S.begin()->first)<X[i][1]){
			pair<int,int> Keep = *S.begin();
			S.erase(S.begin());
			while(S.size()>0 && S.begin()->first < X[i][1]){
				D.merge(S.begin()->second,X[i][2]);
				S.erase(S.begin());
			}
			D.merge(Keep.second,X[i][2]);
			S.insert(Keep);
		}
		else{
			S.insert(make_pair(X[i][1],X[i][2]));
		}
	}
	
	rep(i,N){
		cout<<D.size(i)<<endl;
	}
	
	return 0;
}
 