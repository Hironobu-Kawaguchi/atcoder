// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// A - Good Integer
// https://atcoder.jp/contests/abc079/tasks/abc079_a

#include <iostream>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int N;
	cin >> N;

	int n1 = N / 1000;
	int n2 = (N - n1 * 1000) / 100;
	int n3 = (N - n1 * 1000 - n2 * 100) / 10;
	int n4 = N - n1 * 1000 - n2 * 100 - n3 * 10;

	if ((n1 == n2 && n2 == n3) || (n2 == n3 && n3 == n4)) {
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