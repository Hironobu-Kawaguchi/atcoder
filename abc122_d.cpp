// D - We Like AGC
// https://atcoder.jp/contests/abc122/tasks/abc122_d

#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;


// int dp[101][4][4][4];
vector<vector<vector<vector<int>>>> dp(101, vector<vector<vector<int>>>(4, vector<vector<int>>(4, vector<int>(4))));

int main() {
	int N;
	cin >> N;

	//長さ0の文字列は1である。
	//0,1,2に関する制約しかないので、
	//Sは、333Sと考えても問題がない。
	dp[0][3][3][3] = 1;

	int mod = 1'000'000'007;

	//文字列の文字数
	for (int len = 0; len < N; len++)
	{
		//最後から1文字目の文字
		for (int c1 = 0; c1 < 4; c1++)
		{
			//最後から2文字目の文字
			for (int c2 = 0; c2 < 4; c2++)
			{
				//最後から3文字目の文字
				for (int c3 = 0; c3 < 4; c3++)
				{
					//条件に当てはまるものがない場合はcontinue;
					if (dp[len][c1][c2][c3] == 0) continue;

					//新しく追加する文字
					for (int a = 0; a < 4; a++)
					{
						//ダメな5つの条件をカットする
						if (a == 2 && c1 == 1 && c2 == 0) continue;
						if (a == 2 && c1 == 0 && c2 == 1) continue;
						if (a == 1 && c1 == 2 && c2 == 0) continue;
						if (a == 2 && c1 == 1 && c3 == 0) continue;
						if (a == 2 && c2 == 1 && c3 == 0) continue;

						//ダメな条件を抜けたら、aを足した文字列が作れる

						// S = ...... c3 c2 c1
						// nextS = ...... c2 c1 a

						dp[len + 1][a][c1][c2] += dp[len][c1][c2][c3];
						dp[len + 1][a][c1][c2] %= mod;
					}
				}
			}
		}
	}

	int ans = 0;

	//長さNの全部の答えを纏める
	//最後から1文字目の文字
	for (int c1 = 0; c1 < 4; c1++)
	{
		//最後から2文字目の文字
		for (int c2 = 0; c2 < 4; c2++)
		{
			//最後から3文字目の文字
			for (int c3 = 0; c3 < 4; c3++)
			{
				ans += dp[N][c1][c2][c3];
				ans %= mod;
			}
		}
	}

	cout << ans << endl;
}

