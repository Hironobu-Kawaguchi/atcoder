// A - Double Helix
// https://atcoder.jp/contests/abc122/tasks/abc122_a

#include<iostream>
#include<string>
#include<map>
using namespace std;

int main() {
	//入力
	string S;
	cin >> S;

	//処理
	// A <-> T C <-> G

	map<char, char> m;
	m['A'] = 'T';
	m['T'] = 'A';
	m['C'] = 'G';
	m['G'] = 'C';

	char ans = m[S[0]];

	//出力
	cout << ans << endl;
}



// #include<iostream>
// #include<string>
// #include<map>
// using namespace std;

// int main() {
// 	//入力
// 	string S;
// 	cin >> S;

// 	//処理
// 	// A <-> T C <-> G

// 	string before = "ATCG";
// 	string after = "TAGC";
// 	map<char, char> m;

// 	for (int i = 0; i < before.size(); i++)
// 	{
// 		m[before[i]] = after[i];
// 	}

// 	char ans = m[S[0]];

// 	//出力
// 	cout << ans << endl;
// }



// #include<iostream>
// #include<string>
// using namespace std;

// int main() {
// 	//入力
// 	string S;
// 	cin >> S;

// 	//処理
// 	// A <-> T C <-> G

// 	string before = "ATCG";
// 	string after = "TAGC";

// 	char ans = 'A';

// 	for (int i = 0; i < before.size(); i++)
// 	{
// 		if (S[0] == before[i]) ans = after[i];
// 	}

// 	//出力
// 	cout << ans << endl;
// }



// #include<iostream>
// #include<string>
// using namespace std;

// int main() {
// 	//入力
// 	string S;
// 	cin >> S;

// 	//処理
// 	// A <-> T C <-> G
// 	char ans = 'A';

// 	if (S[0] == 'A') ans = 'T';
// 	else if (S[0] == 'T') ans = 'A';
// 	else if (S[0] == 'C') ans = 'G';
// 	else if (S[0] == 'G') ans = 'C';

// 	//出力
// 	cout << ans << endl;
// }

