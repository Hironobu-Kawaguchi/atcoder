// B - Five Dishes
// https://atcoder.jp/contests/abc123/tasks/abc123_b

#include<iostream>
#include<string>
#include<map>
#include<algorithm>
#include<vector>
using namespace std;


int main() {
	int a, b, c, d, e;
	cin >> a >> b >> c >> d >> e;
	int N = 5;

	//注文してから届くまでの時間
	vector<int> Time = { a, b, c, d, e };

	//順番の並び替え
	vector<int> index = { 0,1,2,3,4 };


	int BestTime = (int)1e9; //←10の9乗(double)

	//next_permutationでindexの中身が
	//0,1,2,3,4
	//0,1,2,4,3
	//:
	//4,3,2,1,0
	//の全探索が出来る！(当然DFSとかで探索して求めてもOK)
	do {
		int NowTime = 0;
		for (int i = 0; i < N; i++)
		{
			//10で割り切れるようになるまで1を足し続ける
			while (NowTime % 10 != 0) NowTime++;
			NowTime += Time[index[i]];
		}
		BestTime = min(NowTime, BestTime);
		
	} while (next_permutation(index.begin(), index.end()));
	
	cout << BestTime << endl;
}



// #include<iostream>
// #include<string>
// #include<map>
// #include<algorithm>
// #include<vector>
// using namespace std;


// int main() {
// 	int a, b, c, d, e;
// 	cin >> a >> b >> c >> d >> e;
// 	int N = 5;

// 	//注文してから届くまでの時間
// 	vector<int> Time = { a, b, c, d, e };
// 	//注文してから次に注文出来るまでの時間
// 	vector<int> nextTime(N);
// 	for (int i = 0; i < N; i++)
// 	{
// 		if (Time[i] % 10 == 0) nextTime[i] = Time[i];
// 		else nextTime[i] = Time[i] - Time[i] % 10 + 10;

// 		// nextTime[i] = (Time[i] + 9) / 10 * 10;
// 	}

// 	int BestTime = 999999999; //大きい値を適当に入れる
// 	//最後に注文するものを全通り計算
// 	for (int i = 0; i < N; i++)
// 	{
// 		int SumTime = 0;
// 		for (int j = 0; j < N; j++)
// 		{
// 			if (i == j) {
// 				//最後の処理
// 				SumTime += Time[j];
// 			}
// 			else {
// 				//最後以外の処理
// 				SumTime += nextTime[j];
// 			}
// 		}
// 		BestTime = min(BestTime, SumTime);
// 		//if (BestTime > SumTime) BestTime = SumTime;
// 	}

// 	cout << BestTime << endl;
// }

