// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// P - 1.15.関数
// https://atcoder.jp/contests/apg4b/tasks/APG4b_p

#include <iostream>
#include <algorithm>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

// 関数定義
int my_min(int x, int y) {
	if (x < y) {
		return x;
	}
	else {
		return y;
	}
}
// 返り値が無いのでvoidを指定
void hello(string text) {
	cout << "Hello, " << text << endl;
	return;
}
// 引数なし // 整数の入力を受け取って返す関数
int input() {
	int x;
	cin >> x;
	return x;
}
int main() {
	int answer = my_min(10, 5);
	cout << answer << endl;

	hello("Tom");
	hello("C++");

	int num = input(); // 引数なし
	cout << num + 5 << endl;
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
