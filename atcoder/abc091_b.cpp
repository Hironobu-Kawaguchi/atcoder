// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// B - Two Colors Card Game
// https://atcoder.jp/contests/abc091/tasks/abc091_b

#include <iostream>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int N;
	cin >> N;
	vector<string> vecs(N);
	for (int i = 0; i < N; i++) {
		cin >> vecs.at(i);
	}
	int M;
	cin >> M;
	vector<string> vect(M);
	for (int j = 0; j < M; j++) {
		cin >> vect.at(j);
	}

	int ans = 0;
	for (int i = 0; i < N; i++) {
		int tmp = 0;
		for (int j = 0; j < N; j++) {
			if (vecs.at(i) == vecs.at(j)) {
				tmp++;
			}
		}
		for (int k = 0; k < M; k++) {
			if (vecs.at(i) == vect.at(k)) {
				tmp--;
			}
		}
		if (ans < tmp) {
			ans = tmp;
		}
	}
	cout << ans << endl;
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
