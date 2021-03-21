// D - Cake 123
// https://atcoder.jp/contests/abc123/tasks/abc123_d

#include<iostream>
#include<string>
#include<map>
#include<algorithm>
#include<vector>
using namespace std;


int main() {
	int X, Y, Z;
	int K;
	cin >> X >> Y >> Z;
	cin >> K;
	vector<long long> A(X), B(Y), C(Z);

	for (int i = 0; i < X; i++) cin >> A[i];
	for (int i = 0; i < Y; i++) cin >> B[i];
	for (int i = 0; i < Z; i++) cin >> C[i];

	sort(A.begin(), A.end());
	reverse(A.begin(), A.end());
	sort(B.begin(), B.end());
	reverse(B.begin(), B.end());
	sort(C.begin(), C.end());
	reverse(C.begin(), C.end());

	vector<long long> ABC;
	for (int a = 0; a < X; a++)
	{
		for (int b = 0; b < Y; b++)
		{
			if ((a + 1) * (b + 1) > K) break;

			for (int c = 0; c < Z; c++)
			{
				if ((a + 1) * (b + 1) * (c + 1) > K) break;

				ABC.push_back(A[a] + B[b] + C[c]);
			}
		}
	}


	sort(ABC.begin(), ABC.end());
	reverse(ABC.begin(), ABC.end());

	for (int i = 0; i < K; i++)
	{
		cout << ABC[i] << endl;
	}

}



// #include<iostream>
// #include<string>
// #include<map>
// #include<algorithm>
// #include<vector>
// using namespace std;


// int main() {
// 	int X, Y, Z;
// 	int K;
// 	cin >> X >> Y >> Z;
// 	cin >> K;
// 	vector<long long> A(X), B(Y), C(Z);

// 	for (int i = 0; i < X; i++) cin >> A[i];
// 	for (int i = 0; i < Y; i++) cin >> B[i];
// 	for (int i = 0; i < Z; i++) cin >> C[i];

// 	vector<long long> AB;
// 	for (int i = 0; i < X; i++)
// 	{
// 		for (int j = 0; j < Y; j++)
// 		{
// 			AB.push_back(A[i] + B[j]);
// 		}
// 	}
// 	sort(AB.begin(), AB.end());
// 	reverse(AB.begin(), AB.end());

// 	vector<long long> ABC;

// 	for (int i = 0; i < min(K, (int)AB.size()); i++)
// 	{
// 		for (int j = 0; j < Z; j++)
// 		{
// 			ABC.push_back(AB[i] + C[j]);
// 		}
// 	}

// 	sort(ABC.begin(), ABC.end());
// 	reverse(ABC.begin(), ABC.end());

// 	for (int i = 0; i < K; i++)
// 	{
// 		cout << ABC[i] << endl;
// 	}

// }



// #include<iostream>
// #include<string>
// #include<map>
// #include<algorithm>
// #include<vector>
// #include<queue>
// #include<set>
// using namespace std;

// class Nums {
// public:
// 	int a, b, c;

// 	Nums(int _a, int _b, int _c) {
// 		a = _a;
// 		b = _b;
// 		c = _c;
// 	}

// 	bool operator<(const Nums& other) const {
// 		return a < other.a;
// 	}
// };

// //           a * 1000 * 1000 + b * 1000 + c;
// //bool isUsed[1000][1000][1000]; // <- 10億要素あるからダメ
// //set<int> UsedNumbers // 使った値だけを入れてあげる

// int main() {
// 	int X, Y, Z;
// 	int K;
// 	cin >> X >> Y >> Z;
// 	cin >> K;
// 	vector<long long> A(X), B(Y), C(Z);
// 	for (int i = 0; i < X; i++) cin >> A[i];
// 	for (int i = 0; i < Y; i++) cin >> B[i];
// 	for (int i = 0; i < Z; i++) cin >> C[i];
// 	A.push_back((long long)-1e17);
// 	B.push_back((long long)-1e17);
// 	C.push_back((long long)-1e17);

// 	sort(A.begin(), A.end());
// 	reverse(A.begin(), A.end());
// 	sort(B.begin(), B.end());
// 	reverse(B.begin(), B.end());
// 	sort(C.begin(), C.end());
// 	reverse(C.begin(), C.end());

// 	priority_queue<pair<long long, Nums>> pq;
// 	pq.push(make_pair(A[0] + B[0] + C[0], Nums(0, 0, 0)));
// 	//PriorityQueueに入れたかどうかを管理する
// 	set<int> s;
// 	s.insert(0);

// 	vector<long long> ans;

// 	while (ans.size() < K) {
// 		auto v = pq.top(); pq.pop();
// 		ans.push_back(v.first);

// 		for (int i = 0; i < 3; i++)
// 		{
// 			int a = v.second.a;
// 			int b = v.second.b;
// 			int c = v.second.c;
// 			if (i == 0) a++;
// 			if (i == 1) b++;
// 			if (i == 2) c++;
// 			//hashを作る
// 			int hash = (a << 20) + (b << 10) + c;
// 			if (s.find(hash) == s.end()) {
// 				s.insert(hash);
// 				pq.push(make_pair(A[a] + B[b] + C[c], Nums(a, b, c)));
// 			}
// 		}
// 	}

// 	for (int i = 0; i < K; i++)
// 	{
// 		cout << ans[i] << endl;
// 	}

// }
