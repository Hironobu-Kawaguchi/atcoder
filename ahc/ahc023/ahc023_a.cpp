// https://atcoder.jp/contests/ahc023/tasks/asprocon10_a
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
#include <chrono>
using namespace std;
typedef long long ll;

// グローバル変数でテストケース、グリッドの次元、初期位置を定義
int T, K, H, W, i0;
vector<int> S, D;  // 各種の作物の植え付け日と収穫日を格納するベクトル
vector<vector<bool>> h, v;  // 水路の有無を格納する2次元ベクトル（横と縦）

// 入力を読み取る関数
void read_input() {
    // テストケース、グリッドの次元、初期位置を読み取る
    cin >> T >> H >> W >> i0;
    
    // 横方向の水路情報を読み取り、h に格納
    h.resize(H - 1, vector(W, false));
    for (int i = 0; i < H - 1; ++i) {
        string s; cin >> s;
        for (int j = 0; j < W; ++j) if (s[j] == '1') h[i][j] = true;
    }
    
    // 縦方向の水路情報を読み取り、v に格納
    v.resize(H, vector(W - 1, false));
    for (int i = 0; i < H; ++i) {
        string s; cin >> s;
        for (int j = 0; j < W - 1; ++j) if (s[j] == '1') v[i][j] = true;
    }
    
    // 作物の種類数と各作物の植え付け日、収穫日を読み取る
    cin >> K;
    S.resize(K);
    D.resize(K);
    for (int i = 0; i < K; ++i) cin >> S[i] >> D[i];
}

// 作業の情報を保持する構造体（作物の種類、位置、植え付け日）
struct Work {
    int k, i, j, s;
};

// 初期位置から特定のセルが到達可能かどうかをチェックする関数
bool reachable(int i, int j, const vector<vector<vector<pair<int, int>>>> &adj, const vector<vector<bool>> &used) {
    if (used[i][j] || used[i0][0]) {    // 目的地のセル(i, j)や初期位置(i0, 0)が既に使用されている場合、到達できない
        return false;
    } else if (i == i0 && j == 0) {    // 目的地が初期位置(i0, 0)の場合，到達できる
        return true;
    }
    // BFS（幅優先探索）を用いて到達可能かどうかを判定する
    queue<pair<int, int>> q;
    q.emplace(i0, 0);
    vector visited(H, vector(W, false));
    visited[i0][0] = true;
    while (!q.empty()) {
        const auto [i1, j1] = q.front();
        q.pop();
        for (const auto &[i2, j2] : adj[i1][j1]) {
            if (i2 == i && j2 == j) {   // 目的地のセル(i, j)に到達できた
                return true;
            } else if (!used[i2][j2] && !visited[i2][j2]) {
                visited[i2][j2] = true;
                q.emplace(i2, j2);
            }
        }
    }
    // 目的地のセル(i, j)に到達できなかった
    return false;
}

// 作業計画が可能かどうかを判定する関数
bool is_valid_plan(const vector<Work> &plan, const vector<vector<vector<pair<int, int>>>> &adj) {
    vector<vector<Work>> plant_list(T + 1), harvest_list(T + 1);
    for (const Work &w : plan) {
        plant_list[w.s].push_back(w);
        harvest_list[D[w.k]].push_back(w);
    }

    vector used(H, vector(W, false));   // 作業計画によって使用されるセルを保持する2次元ベクトル
    for (int t = 1; t <= T; ++t) {
        // planting phase
        for (const Work &w : plant_list[t]) {   // t日目に植え付ける作物が到達可能かどうかをチェック
            if (!reachable(w.i, w.j, adj, used)) {  // 作業計画によって使用されるセルが到達不可能な場合、作業計画は不可能
                return false;
            }
        }
        for (const Work &w : plant_list[t]) {   // t日目に植え付ける作物をusedに記録
            if (used[w.i][w.j]) {   // 作業計画によって使用されるセルが既に使用されている場合、作業計画は不可能
                return false;
            } else {    // 作業計画によって使用されるセルをusedに記録
                used[w.i][w.j] = true;
            }
        }

        // harvesting phase
        for (const Work &w : harvest_list[t]) { // t日目に収穫する作物をusedから削除
            used[w.i][w.j] = false;
        }
        for (const Work &w : harvest_list[t]) { // t日目に収穫する作物が到達可能かどうかをチェック
            if (!reachable(w.i, w.j, adj, used)) {
                return false;
            }
        }
    }

    return true;
}

// D-Sが大きい順に作物をソートする関数
vector<int> sort_plants_by_DS(const vector<int> &S, const vector<int> &D, const bool reverse = true) {
    vector<pair<int, int>> ds_pairs;
    for (int i = 0; i < S.size(); ++i) {
        ds_pairs.emplace_back(D[i] - S[i], i);  // D-Sと作物のインデックスをペアとして保存
    }
    if (reverse) {
        sort(ds_pairs.rbegin(), ds_pairs.rend());  // D-Sの大きい順にソート
    } else {
        sort(ds_pairs.begin(), ds_pairs.end());  // D-Sの小さい順にソート
    }

    vector<int> sorted_indexes;
    for (const auto &[ds, index] : ds_pairs) {
        sorted_indexes.push_back(index);  // ソートされた作物のインデックスを保存
    }
    return sorted_indexes;
}

int main() {
    auto start_time = std::chrono::high_resolution_clock::now();  // 計測開始
    read_input();  // 入力を読み取る

    // construct a graph
    // グラフを表す隣接リストを構築
    // adj[i][j]はセル(i, j)から到達可能なすべてのセルを保持
    vector adj(H, vector(W, vector<pair<int, int>>()));
    // 与えられた水路に基づいてadjを埋める
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (i + 1 < H && !h[i][j]) {
                // no waterway between (i, j) and (i + 1, j)
                adj[i][j].emplace_back(i + 1, j);
                adj[i + 1][j].emplace_back(i, j);
            }
            if (j + 1 < W && !v[i][j]) {
                // no waterway between (i, j) and (i, j + 1)
                adj[i][j].emplace_back(i, j + 1);
                adj[i][j + 1].emplace_back(i, j);
            }
        }
    }

    // BFSで入口からの距離が遠い順にセルを並べる
    vector<pair<int, int>> cells;
    queue<pair<int, int>> q;
    q.emplace(i0, 0);
    vector visited(H, vector(W, false));
    visited[i0][0] = true;
    while (!q.empty()) {
        const auto [i, j] = q.front();
        q.pop();
        cells.emplace_back(i, j);
        for (const auto &[i2, j2] : adj[i][j]) {
            if (!visited[i2][j2]) {
                visited[i2][j2] = true;
                q.emplace(i2, j2);
            }
        }
    }


    // 作業計画を作成
    vector<Work> plan;
    int l = cells.size() - 1;
    // for (int k = 0; k < min(K, 10); ++k) {
    // for (int k = 0; k < min(K, 200); ++k) {
    // for (int k = 0; k < K; ++k) {
    // D-Sが大きい順に作物をソート
    vector<int> sorted_plants_r = sort_plants_by_DS(S, D);
    for (int k : sorted_plants_r) {  // 変更後：D-Sが大きい順に作業計画を作成
        // try to plant crop k
        // 各作物について計画に追加できるか試す
        bool found = false;
        // cellsから遠い順に探索
        // for (int l = cells.size() - 1; l >= 0 && !found; --l) {
        if (l < 0) l = cells.size() - 1;
        while (l >= 0 && !found) {
            const auto [i, j] = cells[l];
            plan.push_back({k, i, j, S[k]});
            if (!is_valid_plan(plan, adj)) {
                plan.pop_back();
            } else {
                found = true;
            }
            --l;
        }
        auto current_time = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(current_time - start_time).count();
        if (duration >= 1500) break;  // 1.5秒 = 1500ミリ秒
    }
    // l = cells.size() - 1;
    // // l = 0;
    // vector<int> sorted_plants = sort_plants_by_DS(S, D, false);
    // for (int k : sorted_plants) {  // 変更後：D-Sが小さいに埋めていく
    //     // try to plant crop k
    //     // 各作物について計画に追加できるか試す
    //     bool found = false;
    //     // cellsから遠い順に探索
    //     // for (int l = cells.size() - 1; l >= 0 && !found; --l) {
    //     if (l < 0) l = cells.size() - 1;
    //     // if (l == cells.size()) l = 0;
    //     while (l < cells.size() && !found) {
    //         const auto [i, j] = cells[l];
    //         plan.push_back({k, i, j, S[k]});
    //         if (!is_valid_plan(plan, adj)) {
    //             plan.pop_back();
    //         } else {
    //             found = true;
    //         }
    //         --l;
    //         // ++l;
    //         auto current_time = std::chrono::high_resolution_clock::now();
    //         auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(current_time - start_time).count();
    //         if (duration >= 1500) break;  // 1.5秒 = 1500ミリ秒
    //     }
    //     auto current_time = std::chrono::high_resolution_clock::now();
    //     auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(current_time - start_time).count();
    //     if (duration >= 1500) break;  // 1.5秒 = 1500ミリ秒
    // }
    ll score = 0;
    for (const Work &w : plan) {
        score += (ll)D[w.k] - S[w.k] + 1;
    }
    score *= 1000000;
    score /= H * W * T;
    // error出力
    cerr << "score: " << score << '\n';

    // write output
    // 与えられた水路に基づいてadjを埋める
    cout << plan.size() << '\n';
    for (const Work &w : plan) {
        cout << w.k + 1 << ' ' << w.i << ' ' << w.j << ' ' << w.s << '\n';
    }
}
