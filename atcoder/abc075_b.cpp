// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// B - Minesweeper
// https://atcoder.jp/contests/abc075/tasks/abc075_b

#include <iostream>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int H, W;
	cin >> H >> W;

	vector<int> vy = {-1, -1, -1,  0, 0,  1, 1, 1};
	vector<int> vx = {-1,  0,  1, -1, 1, -1, 0, 1};

	vector<string> vecs(H + 2);
	string dummy = "dd";
	for (int j = 0; j < W; j++) {
		dummy += 'd';
	}
	vecs.at(0) = dummy;
	for (int i = 0; i < H; i++) {
		string s;
		cin >> s;
		vecs.at(i+1) = 'd' + s + 'd';
	}
	vecs.at(H+1) = dummy;

	for (int i = 0; i < H; i++) {
		string line = "";
		for (int j = 0; j < W; j++) {
			if (vecs.at(i + 1).at(j + 1) == '.') {
				//int cnt = 0;
				char cnt = '0';
				for (int k = 0; k < 8; k++) {
					if (vecs.at(i + 1 + vy.at(k)).at(j + 1 + vx.at(k)) == '#') {
						cnt++;
					}
				}
				//line += char(cnt + '0');	// intをcharに変換
				line += cnt;	// cntはchar型
			}
			else {
				line += vecs.at(i + 1).at(j + 1);
			}
		}
		cout << line << endl;
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
