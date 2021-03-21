// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// EX15 - 三人兄弟へのプレゼント / 1.15
// https://atcoder.jp/contests/apg4b/tasks/APG4b_ch

#include <iostream>
#include <algorithm>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

// 1人のテストの点数を表す配列から合計点を計算して返す関数
// 引数 scores: scores.at(i)にi番目のテストの点数が入っている
// 返り値: 1人のテストの合計点
int sum(vector<int> scores) {
	// ここにプログラムを追記
	int res = 0;
	for (int i = 0; i < scores.size(); i++) {
		res += scores.at(i);
	}
	return res;
}

// 3人の合計点からプレゼントの予算を計算して出力する関数
// 引数 sum_a: A君のテストの合計点
// 引数 sum_b: B君のテストの合計点
// 引数 sum_c: C君のテストの合計点
// 返り値: なし
void output(int sum_a, int sum_b, int sum_c) {
	// ここにプログラムを追記
	cout << sum_a * sum_b * sum_c << endl;
}

// -------------------
// ここから先は変更しない
// -------------------

// N個の入力を受け取って配列に入れて返す関数
// 引数 N: 入力を受け取る個数
// 返り値: 受け取ったN個の入力の配列
vector<int> input(int N) {
	vector<int> vec(N);
	for (int i = 0; i < N; i++) {
		cin >> vec.at(i);
	}
	return vec;
}

int main() {
	// 科目の数Nを受け取る
	int N;
	cin >> N;

	// それぞれのテストの点数を受け取る
	vector<int> A, B, C;
	A = input(N);
	B = input(N);
	C = input(N);

	// プレゼントの予算を出力
	output(sum(A), sum(B), sum(C));
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
