// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// EX20 - 報告書の枚数 / 2.05
// https://atcoder.jp/contests/apg4b/tasks/APG4b_cc

#include <iostream>
#include <algorithm>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

// x番の組織が親組織に提出する枚数を返す
// childrenは組織の関係を表す2次元配列(参照渡し)
int count_report_num(vector<vector<int>>& children, int x) {
	vector<int> children_of_x = children.at(x);

	if (children_of_x.size() == 0) {
		return 1;
	}
	else {
		int report_num = 1;
		for (int x : children_of_x) {
			report_num += count_report_num(children, x);
		}
		return report_num;
	}
}
// これ以降の行は変更しなくてよい
int main() {
	int N;
	cin >> N;

	vector<int> p(N);  // 各組織の親組織を示す配列
	p.at(0) = -1;  // 0番組織の親組織は存在しないので-1を入れておく
	for (int i = 1; i < N; i++) {
		cin >> p.at(i);
	}

	// 組織の関係から2次元配列を作る
	vector<vector<int>> children(N);  // ある組織の子組織の番号一覧
	for (int i = 1; i < N; i++) {
		int parent = p.at(i);  // i番の親組織の番号
		children.at(parent).push_back(i);  // parentの子組織一覧にi番を追加
	}

	// 各組織について、答えを出力
	for (int i = 0; i < N; i++) {
		cout << count_report_num(children, i) << endl;
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
