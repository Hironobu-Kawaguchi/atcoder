// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// B - Grid Compression
// https://atcoder.jp/contests/abc107/tasks/abc107_b

#include <iostream>
#include <algorithm>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int H, W;
	cin >> H >> W;
	vector<bool> yck(H, false);
	vector<bool> xck(W, false);
	vector<vector<char>> a(H, vector<char>(W));
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			cin >> a.at(i).at(j);
			if (a.at(i).at(j) == '#') {
				yck.at(i) = true;
				xck.at(j) = true;
			}
		}
	}

	for (int i = 0; i < H; i++) {
		if (yck.at(i) == false) {
			continue;
		}
		for (int j = 0; j < W; j++) {
			if (xck.at(j) == false) {
				continue;
			}
			cout << a.at(i).at(j);
		}
		cout << endl;
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
