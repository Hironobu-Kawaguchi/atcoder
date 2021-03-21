// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// EX13 - 平均との差 / 1.13
// https://atcoder.jp/contests/apg4b/tasks/APG4b_cj

#include <iostream>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int N;
	cin >> N;

	vector<int> vec(N);
	int sum = 0;
	for (int i = 0; i < N; i++) {
		int A;
		cin >> A;
		sum += A;
		vec.at(i) = A;
	}
	int avg = sum / N;	// 平均は切り捨てなのでint
	for (int i = 0; i < N; i++) {
		int tmp = vec.at(i) - avg;
		if (tmp >= 0) {
			cout << tmp << endl;
		}
		else {
			cout << -tmp << endl;
		}
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
