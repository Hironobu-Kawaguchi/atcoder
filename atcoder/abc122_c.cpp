// C - GeT AC
// https://atcoder.jp/contests/abc122/tasks/abc122_c

#include<iostream>
#include<string>
#include<map>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	int N, Q;
	string S;

	cin >> N >> Q;
	cin >> S;

	vector<int> l(Q), r(Q);
	for (int i = 0; i < Q; i++)
	{
		cin >> l[i] >> r[i];
	}


	vector<int> sum(N + 1, 0);

	//ACが出る可能性があるのは2文字目から(0-indexedで1から)
	for (int i = 0; i < N - 1; i++)
	{
		sum[i + 1] = sum[i];
		if (S[i] == 'A' && S[i + 1] == 'C') {
			sum[i + 1]++;
		}
	}

	//0 1 2 3 4 5 6
	// A C A C A C
	// 1 2 3 4 5 6

	for (int i = 0; i < Q; i++)
	{
		int ans = sum[r[i] - 1] - sum[l[i] - 1];
		cout << ans << endl;
	}
}



//#include<iostream>
//#include<string>
//#include<map>
//#include<algorithm>
//#include<vector>
//using namespace std;
//
//int main() {
//	int N, Q;
//	string S;
//
//	cin >> N >> Q;
//	cin >> S;
//
//	vector<int> l(Q), r(Q);
//	for (int i = 0; i < Q; i++)
//	{
//		cin >> l[i] >> r[i];
//	}
//
//
//	vector<int> sum(N + 1, 0);
//
//	//ACが出る可能性があるのは2文字目から(0-indexedで1から)
//	for (int i = 1; i < N; i++)
//	{
//		sum[i + 1] = sum[i];
//		if (S[i - 1] == 'A' && S[i] == 'C') {
//			sum[i + 1]++;
//		}
//	}
//
//	//0 1 2 3 4 5 6
//	// A C A C A C
//	// 1 2 3 4 5 6
//
//	for (int i = 0; i < Q; i++)
//	{
//		int ans = sum[r[i]] - sum[l[i]];
//		cout << ans << endl;
//	}
//}
//
