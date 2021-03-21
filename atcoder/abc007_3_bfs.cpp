// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// A - 幅優先探索
// https://atcoder.jp/contests/atc002/tasks/abc007_3

#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <tuple>
// #include <bits/stdc++.h>
using namespace std;
int main()
{
	int R, C;
	cin >> R >> C;
	int sy, sx, gy, gx;
	cin >> sy >> sx >> gy >> gx;
	sy--, sx--, gy--, gx--;
	vector<string> S(R);
	for (auto& s : S) {
		cin >> s;
	}
	queue<tuple<int, int, int>> Q;
	vector<vector<bool>> visited(R, vector<bool>(C));
	Q.emplace(sy, sx, 0);

	while (!Q.empty()) {
		int y, x, d;
		tie(y, x, d) = Q.front();
		Q.pop();
		if (visited.at(y).at(x)) continue;
		visited.at(y).at(x) = true;
		if (y == gy && x == gx) {
			cout << d << endl;
			break;
		}
		vector<int> vy{ 0, 0, -1, +1 };
		vector<int> vx{ -1, +1, 0, 0 };
		for (int i = 0; i < 4; i++) {
			int newx = x + vx.at(i);
			int newy = y + vy.at(i);
			if (0 <= newx && newx < C && 0 <= newy && newy < R && S.at(newy).at(newx) != '#') {
				Q.emplace(newy, newx, d + 1);
			}
		}
	}
	return 0;
}

// プログラムの実行: Ctrl + F5 または [デバッグ] > [デバッグなしで開始] メニュー
// プログラムのデバッグ: F5 または [デバッグ] > [デバッグの開始] メニュー

// 作業を開始するためのヒント: 
//    1. ソリューション エクスプローラー ウィンドウを使用してファイルを追加/管理します 
//   2. チーム エクスプローラー ウィンドウを使用してソース管理に接続します
//   3. 出力ウィンドウを使用して、ビルド出力とその他のメッセージを表示します
//   4. エラー一覧ウィンドウを使用してエラーを表示します
//   5. [プロジェクト] > [新しい項目の追加] と移動して新しいコード ファイルを作成するか、[プロジェクト] > [既存の項目の追加] と移動して既存のコード ファイルをプロジェクトに追加します
//   6. 後ほどこのプロジェクトを再び開く場合、[ファイル] > [開く] > [プロジェクト] と移動して .sln ファイルを選択します
