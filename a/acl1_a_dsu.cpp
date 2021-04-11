// https://atcoder.jp/contests/practice2/tasks/practice2_a
#include<bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define drep(i,n) for(int i = (n-1); i >= 0; i--)
#define all(v) (v).begin(),(v).end()
#define maxs(x,y) (x = max(x,y))
#define mins(x,y) (x = min(x,y))
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n;
	cin >> n;
	vector<int> x(n), y(n);
	rep(i,n) {
		int _x, _y;
		cin >> _x >> _y;
		_x--, _y--;
		x[i] = _x;
		y[_x] = _y;
	}
	dsu d(n);
	set<pair<int,int>> s;   // (y, x) yが小さい順に格納、一番小さいもを除き1度mergeしたらerase
	rep(i,n){
		if(s.size()>0 && (s.begin()->first)<y[i]){
			pair<int,int> Keep = *s.begin();    // 1番yが小さいものは残す
			s.erase(s.begin());
			while(s.size()>0 && s.begin()->first < y[i]){
				d.merge(s.begin()->second, i);
				s.erase(s.begin());
			}
			d.merge(Keep.second, i);
			s.insert(Keep);
		}
		else{
			s.insert(make_pair(y[i], i));
		}
	}
	rep(i,n) cout << d.size(x[i]) << "\n";
	return 0;
}

// // https://atcoder.jp/contests/acl1/tasks/acl1_a
// // https://atcoder.github.io/ac-library/production/document_ja/dsu.html
// #include <bits/stdc++.h>
// // #include <atcoder/all>
// #include <atcoder/dsu>
// using namespace std;
// using namespace atcoder;
// using ll = long long;
// using P = pair<int,int>;
// #define rep(i,n) for (int i = 0; i < (n); ++i)
// #define Inf 1000000001

// int main(){
	
// 	int N;
// 	cin>>N;
	
// 	vector<vector<int>> X(N);
	
// 	rep(i,N){
// 		int x,y;
// 		scanf("%d %d",&x,&y);
// 		X[i] = {x,y,i};
// 	}
	
// 	sort(X.begin(),X.end());
// 	dsu D(N);
// 	set<pair<int,int>> S;
	
// 	rep(i,N){
// 		if(S.size()>0 && (S.begin()->first)<X[i][1]){
// 			pair<int,int> Keep = *S.begin();
// 			S.erase(S.begin());
// 			while(S.size()>0 && S.begin()->first < X[i][1]){
// 				D.merge(S.begin()->second,X[i][2]);
// 				S.erase(S.begin());
// 			}
// 			D.merge(Keep.second,X[i][2]);
// 			S.insert(Keep);
// 		}
// 		else{
// 			S.insert(make_pair(X[i][1],X[i][2]));
// 		}
// 	}
	
// 	rep(i,N){
// 		cout<<D.size(i)<<endl;
// 	}
	
// 	return 0;
// }
 