// https://codeforces.com/contest/1406/problem/C
// #include<iostream>
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

// #include<bits/stdc++.h>
// using namespace std;
// #define rep(i,n) for (int i = 0; i < (n); ++i)
// #define drep(i,n) for(int i = (n-1); i >= 0; i--)
// #define all(v) (v).begin(),(v).end()
// #define maxs(x,y) (x = max(x,y))
// #define mins(x,y) (x = min(x,y))
// template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
// template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
// template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
// template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
// typedef pair<int, int> P;
// typedef long long ll;
// const int INF = 1001001001;
// const ll LINF = 1001002003004005006ll;
// const ll MOD = 1e9+7;

// https://codeforces.com/contest/1406/submission/92671713
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int n, gsize[100005], fa[100005], minn=1e9, cent1, cent2;
vector<int> g[100005];

void dfs(int x,int f){
	fa[x] = f, gsize[x] = 1;
	int mx=0;
	for(int y:g[x]){
		if(y==f)continue;
		dfs(y,x);
		gsize[x] += gsize[y];
		mx = max(mx,gsize[y]);
	}
	mx = max(mx, n-gsize[x]);
	if(mx<minn) minn=mx, cent1=x, cent2=0;
	else if(mx==minn) cent2=x;
}

int S;

void dfs2(int x,int f){
	if(g[x].size()==1){
		S=x;
		return ;
	}
	for(int y:g[x]){
		if(y==f)continue;
		dfs2(y,x);
	}
}

int main(){
	int t;
	cin>>t;
	while(t--){
	cin>>n,cent1=cent2=0,minn=1e9;
	for(int i=1;i<=n;i++)g[i].clear(),fa[i]=0;
	for(int i=1;i<n;i++){
		int x,y;
		cin>>x>>y;
		g[x].push_back(y),g[y].push_back(x);
	}
	dfs(1,0);
	if(!cent2){
		printf("1 %d\n1 %d\n",g[1][0],g[1][0]);
		continue;
	}
	if(fa[cent1]!=cent2)swap(cent1,cent2);
	dfs2(cent1,cent2);
	printf("%d %d\n%d %d\n",S,fa[S],S,cent2);}
	return 0;
}