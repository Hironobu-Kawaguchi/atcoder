// https://atcoder.jp/contests/abc075/tasks/abc075_c
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

const int MAX_N = 50;
int n, m;
int a[MAX_N], b[MAX_N];
bool G[MAX_N][MAX_N];
bool visited[MAX_N];

void dfs(int v) {
    visited[v] = true;
    rep(v2, n) {
        if(G[v][v2]==false) continue;
        if(visited[v2]==true) continue;
        dfs(v2);
    }
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	cin >> n >> m;
    rep(i,m) {
        cin >> a[i] >> b[i];
        --a[i], --b[i];
        G[a[i]][b[i]] = G[b[i]][a[i]] = true;
    }
    int ans = 0;
    rep(i,m) {
        G[a[i]][b[i]] = G[b[i]][a[i]] = false;
        rep(j,n) visited[j] = false;
        dfs(0);
        bool bridge = false;
        rep(j,n) if(visited[j]==false) bridge = true;
        if(bridge) ++ans;
        G[a[i]][b[i]] = G[b[i]][a[i]] = true;
    }
	cout << ans << "\n";
	return 0;
}


// #include<bits/stdc++.h>
// using namespace std;
// #define rep(i,n) for (int i = 0; i < (n); ++i)
// #define all(v) (v).begin(),(v).end()
// #define chmin(x,y) x = min(x,y)
// typedef pair<int, int> P;
// typedef long long ll;
// const int INF = 1001001001;
// const ll LINF = 1001002003004005006ll;
// const ll MOD = 1e9+7;

// const int MAXN = 50;
// int N, M;
// vector<int> a(MAXN), b(MAXN);
// vector<vector<bool>> graph(MAXN, vector<bool>(MAXN));
// vector<bool> visited(MAXN);

// void dfs(int v) {
//     visited[v] = true;
//     rep(v2, N) {
//         if (graph[v][v2] == false) continue;
//         if (visited[v2] == true) continue;
//         dfs(v2);
//     }
// }

// int main() {
// 	cin >> N >> M;
//     rep(i, M) {
//         cin >> a[i] >> b[i];
//         a[i]--, b[i]--;
//         graph[a[i]][b[i]] = graph[b[i]][a[i]] = true;
//     }

//     int ans = 0;

//     rep(i, M) {
//         graph[a[i]][b[i]] = graph[b[i]][a[i]] = false;
//         rep(j, N) visited[j] = false;
//         dfs(0);
//         bool bridge = false;
//         rep(j, N) if(visited[j] == false) bridge = true;
//         if(bridge) ans++;
//         graph[a[i]][b[i]] = graph[b[i]][a[i]] = true;
//     }

// 	cout << ans << endl;
// 	return 0;
// }
