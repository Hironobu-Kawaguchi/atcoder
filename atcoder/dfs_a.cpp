// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// A - 深さ優先探索
// https://atcoder.jp/contests/atc001/tasks/dfs_a

#include <iostream>
#include <algorithm>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

int W, H; // 横幅と縦幅
int MAX_W = 500, MAX_H = 500;
vector<vector<char>> maze(MAX_H, vector<char>(MAX_W));
vector<vector<bool>> reached(MAX_H, vector<bool>(MAX_W));
int sx, sy, gx, gy;

void dfs(int x, int y) {
	// 迷路の外側か壁の場合は何もしない
	if (x < 0 || W <= x || y < 0 || H <= y || maze.at(y).at(x) == '#') return;
	// 以前に到達していたら何もしない
	if (reached.at(y).at(x)) return;
	reached.at(y).at(x) = true; // 到達したよ
	// 4 方向を試す
	dfs(x + 1, y); // 右
	dfs(x - 1, y); // 左
	dfs(x, y + 1); // 下
	dfs(x, y - 1); // 上
}

int main() {
	cin >> H >> W;

	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			cin >> maze.at(i).at(j);
			if (maze.at(i).at(j) == 's') {
				sy = i;
				sx = j;
			}
			else if (maze.at(i).at(j) == 'g') {
				gy = i;
				gx = j;
			}
		}
	}

	dfs(sx, sy);

	if (reached.at(gy).at(gx)) {
		cout << "Yes" << endl;
	}
	else {
		cout << "No" << endl;
	}
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
