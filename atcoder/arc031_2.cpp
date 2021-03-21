// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// B - 埋め立て
// https://atcoder.jp/contests/arc031/tasks/arc031_2

#include <iostream>
#include <algorithm>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

bool isReachableAll(vector<vector<char>> data, vector<vector<bool>> checked) {
	for (int i = 0; i < data.size(); i++) {
		for (int j = 0; j < data.at(0).size(); j++) {
			if (data.at(i).at(j) == 'o') {
				if (!checked.at(i).at(j)) return false;
			}
		}
	}
	return true;
}

void fillIsland(vector<vector<char>>& data, vector<vector<bool>>& checked, int x, int y) {
	if (data.at(x).at(y) != 'o') return;
	if (checked.at(x).at(y) == true) return;

	vector<int> dataX, dataY;
	checked.at(x).at(y) = true;
	if (x - 1 >= 0) {
		fillIsland(data, checked, x - 1, y);
	}
	if (x + 1 < data.size()) {
		fillIsland(data, checked, x + 1, y);
	}
	if (y - 1 >= 0) {
		fillIsland(data, checked, x, y - 1);
	}
	if (y + 1 < data.at(0).size()) {
		fillIsland(data, checked, x, y + 1);
	}
}

bool isOneIsland(vector<vector<char>> & data, vector<vector<bool>> & checked, int x, int y) {
	fillIsland(data, checked, x, y);
	return isReachableAll(data, checked);
}

int main() {
	int SIZE = 10;
	vector<vector<char>> data(SIZE, vector<char>(SIZE));
	for (int i = 0; i < SIZE; i++) {
		for (int j = 0; j < SIZE; j++) {
			cin >> data.at(i).at(j);
		}
	}
	int x, y;
	for (int i = 0; i < SIZE; i++) {
		for (int j = 0; j < SIZE; j++) {
			if (data.at(i).at(j) == 'o') {
				x = i;
				y = j;
			}
		}
	}

	vector<vector<bool>> checked(SIZE, vector<bool>(SIZE, false));
	if (isOneIsland(data, checked, x, y)) {
		cout << "YES" << endl;
		return 0;
	}

	for (int i = 0; i < SIZE; i++) {
		for (int j = 0; j < SIZE; j++) {
			if (data.at(i).at(j) != 'o') {
				data.at(i).at(j) = 'o';
				vector<vector<bool>> tmpChecked(SIZE, vector<bool>(SIZE, false));
				if (isOneIsland(data, tmpChecked, i, j)) {
					cout << "YES" << endl;
					return 0;
				}
				data.at(i).at(j) = 'x';
			}
		}
	}
	cout << "NO" << endl;
	return 0;
}

//#include <bits/stdc++.h>
//using namespace std;
//
//// (y, x)から到達出来るすべての陸地マスのcheckedをtrueにする
//void fill_island(vector<vector<char>> board, vector<vector<bool>>& checked, int y, int x) {
//	if (x < 0 || y < 0 || x>9 || y>9)
//		return;
//	if (checked.at(y).at(x))
//		return;
//	if (board.at(y).at(x) == 'x')
//		return;
//
//	checked.at(y).at(x) = true;
//
//	fill_island(board, checked, y + 1, x);
//	fill_island(board, checked, y - 1, x);
//	fill_island(board, checked, y, x + 1);
//	fill_island(board, checked, y, x - 1);
//
//	return;
//}
//
//bool check(vector<vector<char>> board, int y, int x) {
//	vector<vector<bool>> checked(10, vector<bool>(10, false));
//
//	/* 引数： 盤面, チェック二次元配列, y座標, x座標*/
//	fill_island(board, checked, y, x);  // (y, x)から到達出来るすべての陸地マスのcheckedをtrueにする
//
//	bool ok = true;
//	for (int i = 0; i < 10; i++) {
//		for (int j = 0; j < 10; j++) {
//			if (board.at(i).at(j) == 'o') {
//				if (!checked.at(i).at(j)) {
//					// 到達出来ていない陸地マスがある
//					ok = false;
//				}
//			}
//		}
//	}
//	// ok == true なら全ての陸地マスは繋がっている
//	return ok;
//}
//int main() {
//	// 入力をboardに格納
//	vector<vector<char>> board(10, vector<char>(10));
//	for (int i = 0; i < 10; i++) {
//		for (int j = 0; j < 10; j++) {
//			cin >> board.at(i).at(j);
//		}
//	}
//
//	// 海マスを探し、check()
//	int y, x;
//	bool result = false;
//	for (int i = 0; i < 10; i++) {
//		for (int j = 0; j < 10; j++) {
//			if (board.at(i).at(j) == 'x') {
//				y = i;
//				x = j;
//				result = check(board, y, x);
//				cout << "y:" << y << " x;" << x << " check:" << result << endl;
//				if (result) {
//					break;
//				}
//			}
//		}
//	}
//	if (result) {
//		cout << "YES" << endl;
//	}
//	else {
//		cout << "NO" << endl;
//	}
//}

// プログラムの実行: Ctrl + F5 または [デバッグ] > [デバッグなしで開始] メニュー
// プログラムのデバッグ: F5 または [デバッグ] > [デバッグの開始] メニュー

// 作業を開始するためのヒント: 
//    1. ソリューション エクスプローラー ウィンドウを使用してファイルを追加/管理します 
//   2. チーム エクスプローラー ウィンドウを使用してソース管理に接続します
//   3. 出力ウィンドウを使用して、ビルド出力とその他のメッセージを表示します
//   4. エラー一覧ウィンドウを使用してエラーを表示します
//   5. [プロジェクト] > [新しい項目の追加] と移動して新しいコード ファイルを作成するか、[プロジェクト] > [既存の項目の追加] と移動して既存のコード ファイルをプロジェクトに追加します
//   6. 後ほどこのプロジェクトを再び開く場合、[ファイル] > [開く] > [プロジェクト] と移動して .sln ファイルを選択します
