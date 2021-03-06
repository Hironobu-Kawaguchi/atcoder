// https://atcoder.jp/contests/arc033/tasks/arc033_2
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
// #include<map>
// #include<tuple>
#include<set>
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
ll gcd(ll a, ll b) { return b?gcd(b,a%b):a;}
ll lcm(ll a, ll b) { return a/gcd(a,b)*b;}

int main() {
	int NA, NB;
	cin >> NA >> NB;
    int a, b;
    vector<int> A(NA), B(NB);
    set<int> s;
    rep(i, NA) {
        cin >> A[i];
        s.insert(A[i]);
    } 
    rep(i, NB) {
        cin >> B[i];
        s.insert(B[i]);
    }
	cout << setprecision(10) << double(A.size() + B.size() - s.size()) / s.size() << endl;
	return 0;
}
