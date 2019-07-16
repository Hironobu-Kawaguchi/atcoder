// https://atcoder.jp/contests/arc012/tasks/arc012_3
// https://atcoder.jp/contests/arc012/submissions/6018140
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<string>
#include<vector>
//#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
using namespace std;

int N = 19;
vector<string> board;

bool isInside(int y, int x) {
	return y >= 0 && x >= 0 && y < N && x < N;
}

int countPiece(char c) {
	int ans = 0;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			if (board[i][j] == c) ans++;
	return ans;
}

vector<int> dx = { 1,1,0,-1 };
vector<int> dy = { 0,1,1,1 };
bool checkBoard(char c) {
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (board[i][j] == '.') continue;
			for (int k = 0; k < dx.size(); k++)
			{
				if (!isInside(i + dy[k] * 4, j + dx[k] * 4)) continue;
				int cntPiece = 1;
				for (int p = 1; p <= 4; p++)
				{
					if (board[i][j] == board[i + dy[k] * p][j + dx[k] * p]) cntPiece++;
				}
				if (cntPiece == 5) return false;
			}
		}
	}
	return true;
}


bool calc() {
	int CountO = countPiece('o');
	int CountX = countPiece('x');
	char lastMove;
	if (CountO == CountX + 1) lastMove = 'o';
	else if (CountO == CountX) lastMove = 'x';
	else return false;

	if (CountO == 0) return true;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (board[i][j] == lastMove) {
				board[i][j] = '.';
				if (checkBoard(lastMove)) return true;
				board[i][j] = lastMove;
			}
		}
	}
	return false;
}

int main() {
	board = vector<string>(N);
	for (int i = 0; i < N; i++)  cin >> board[i];
	if (calc()) cout << "YES" << endl;
	else cout << "NO" << endl;
}
