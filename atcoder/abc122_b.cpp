// B - ATCoder
// https://atcoder.jp/contests/abc122/tasks/abc122_b

#include<iostream>
#include<string>
#include<map>
#include<algorithm>
using namespace std;

int main() {
	//入力
	string S;
	cin >> S;

	//処理
	string T = "ATCG";

	int ans = 0;
	for (int i = 0; i < S.size(); i++)
	{
		//i は開始地点
		int now = 0;
		for (int j = i; j < S.size(); j++)
		{
			//j 文字目まではATCGであるかチェック
			bool ok = false;
			for (int k = 0; k < T.size(); k++)
			{
				if (S[j] == T[k]) ok = true;
			}

			if (ok) {
				//j文字目がATCG文字なら、i文字目からj文字目までがATCG文字列である。
				now++;
				ans = max(ans, now);
			}
			else {
				//j文字目がATCG文字ではないなら、
				//これ以上i文字目から始まるATCG文字列は作れない。
				break;
			}
		}
	}

	cout << ans << endl;
}



// #include<iostream>
// #include<string>
// #include<map>
// #include<algorithm>
// using namespace std;

// int main() {
// 	//入力
// 	string S;
// 	cin >> S;

// 	//処理
// 	string T = "ATCG";

// 	int ans = 0; //ATCG文字列の最大長
// 	int now = 0; //今見ている文字を末尾とするATCG文字列の最大長
// 	for (int i = 0; i < S.size(); i++)
// 	{
// 		bool isATCG = false;
// 		for (int j = 0; j < T.size(); j++)
// 		{
// 			if (S[i] == T[j]) isATCG = true;
// 		}

// 		if (!isATCG) {
// 			//違う場合は0にする
// 			now = 0;
// 		}
// 		else {
// 			//ATCG文字の場合は、前の文字列に1つ文字を足せる
// 			now++;
// 			//最大値を更新する
// 			ans = max(now, ans);
// 			// if(now > ans) ans = now; も同じ
// 		}
// 	}

// 	cout << ans << endl;
// }

