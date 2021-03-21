// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// B - Harshad Number
// https://atcoder.jp/contests/abc080/tasks/abc080_b

#include <iostream>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int N;
	cin >> N;
	int tmp = N;
	int sum = 0;
	while (tmp > 0) {
		sum += tmp % 10;
		tmp /= 10;
	}
	if (N % sum == 0) {
		cout << "Yes" << endl;
	}
	else {
		cout << "No" << endl;
	}
}

/* log10()とpow()関数を使ったやり方（不要だった）
int main() {
	int N;
	cin >> N;
	int digit = log10(N) + 1;
	int sum = 0;
	for (int i = 0; i < digit; i++) {
		sum += int(N / pow(10, i)) % 10;
		//cout << sum << ":" << int(N / pow(10, i)) % 10 << " " << pow(10, i) << endl;
	}
	if (N % sum == 0) {
		cout << "Yes" << endl;
	}
	else {
		cout << "No" << endl;
	}
}
*/

// プログラムの実行: Ctrl + F5 または [デバッグ] > [デバッグなしで開始] メニュー
// プログラムのデバッグ: F5 または [デバッグ] > [デバッグの開始] メニュー

// 作業を開始するためのヒント: 
//    1. ソリューション エクスプローラー ウィンドウを使用してファイルを追加/管理します 
//   2. チーム エクスプローラー ウィンドウを使用してソース管理に接続します
//   3. 出力ウィンドウを使用して、ビルド出力とその他のメッセージを表示します
//   4. エラー一覧ウィンドウを使用してエラーを表示します
//   5. [プロジェクト] > [新しい項目の追加] と移動して新しいコード ファイルを作成するか、[プロジェクト] > [既存の項目の追加] と移動して既存のコード ファイルをプロジェクトに追加します
//   6. 後ほどこのプロジェクトを再び開く場合、[ファイル] > [開く] > [プロジェクト] と移動して .sln ファイルを選択します
