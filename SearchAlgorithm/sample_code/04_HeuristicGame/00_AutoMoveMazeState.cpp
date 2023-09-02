// Copyright [2022] <Copyright Eita Aoki (Thunder) >
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <utility>
#include <random>
#include <assert.h>
#include <math.h>
#include <chrono>
#include <queue>
#include <algorithm>
#include <iostream>
#include <functional>

std::mt19937 mt_for_action(0);

constexpr const int H = 5;     // 迷路の高さ
constexpr const int W = 5;     // 迷路の幅
constexpr int END_TURN = 5;    // ゲーム終了ターン
constexpr int CHARACTER_N = 3; // キャラクターの数

using ScoreType = int64_t;
constexpr const ScoreType INF = 1000000000LL;

// 座標を保持する
struct Coord
{
    int y_;
    int x_;
    Coord(const int y = 0, const int x = 0) : y_(y), x_(x) {}
};

// 自動一人ゲームの例
// キャラクターは1マス先の最もポイントが高い床に自動で移動する。
// 合法手の中でスコアが同値のものがある場合、右、左、下、上の順で行動が優先される。
// 1ターンに上下左右四方向のいずれかに壁のない場所に1マスずつ進む。
// 床にあるポイントを踏むと自身のスコアとなり、床のポイントが消える。
// END_TURNの時点のスコアを高くすることを目的とし、
// ゲームに介入できる要素として、初期状態でのキャラクターをどこに配置するかを選択できる。
// どのようにキャラクターを配置すると最終スコアが高くなるかを考えるゲーム。
class AutoMoveMazeState
{
private:
    static constexpr const int dx[4] = {1, -1, 0, 0};
    static constexpr const int dy[4] = {0, 0, 1, -1};

    int points_[H][W] = {};              // 床のポイントを1~9で表現する
    int turn_;                           // 現在のターン
    Coord characters_[CHARACTER_N] = {}; // CHARACTER_N体のキャラクター

    // 指定キャラクターを移動させる。
    void movePlayer(const int character_id)
    {
        Coord &character = this->characters_[character_id];
        int best_point = -INF;
        int best_action_index = 0;
        for (int action = 0; action < 4; action++)
        {
            int ty = character.y_ + dy[action];
            int tx = character.x_ + dx[action];
            if (ty >= 0 && ty < H && tx >= 0 && tx < W)
            {
                auto point = this->points_[ty][tx];
                if (point > best_point)
                {
                    best_point = point;
                    best_action_index = action;
                }
            }
        }

        character.y_ += dy[best_action_index];
        character.x_ += dx[best_action_index];
    }

    // ゲームを1ターン進める。
    void advance()
    {
        for (int character_id = 0; character_id < CHARACTER_N; character_id++)
        {
            movePlayer(character_id);
        }
        for (auto &character : this->characters_)
        {
            auto &point = this->points_[character.y_][character.x_];
            this->game_score_ += point;
            point = 0;
        }
        ++this->turn_;
    }

public:
    int game_score_;            // ゲーム上で実際に得たスコア
    ScoreType evaluated_score_; // 探索上で評価したスコア

    // h*wの迷路を生成する。
    AutoMoveMazeState(const int seed) : turn_(0),
                                        game_score_(0),
                                        evaluated_score_(0)
    {

        auto mt_for_construct = std::mt19937(seed);
        for (int y = 0; y < H; y++)
        {
            for (int x = 0; x < W; x++)
            {
                points_[y][x] = mt_for_construct() % 9 + 1;
            }
        }
    }

    // 指定位置に指定キャラクターを配置する。
    void setCharacter(const int character_id, const int y, const int x)
    {
        this->characters_[character_id].y_ = y;
        this->characters_[character_id].x_ = x;
    }

    // [どのゲームでも実装する] : ゲームの終了判定
    bool isDone() const
    {
        return this->turn_ == END_TURN;
    }

    // [実装しなくてもよいが実装すると便利] : 現在のゲーム状況を文字列にする
    std::string toString() const
    {
        std::stringstream ss;
        ss << "turn:\t" << this->turn_ << "\n";
        ss << "score:\t" << this->game_score_ << "\n";
        auto board_chars = std::vector<std::vector<char>>(H, std::vector<char>(W, '.'));
        for (int h = 0; h < H; h++)
        {
            for (int w = 0; w < W; w++)
            {
                bool is_written = false; // この座標に書く文字が決定したか

                for (const auto &character : this->characters_)
                {
                    if (character.y_ == h && character.x_ == w)
                    {
                        ss << "@";
                        is_written = true;
                        break;
                    }
                    board_chars[character.y_][character.x_] = '@';
                }
                if (!is_written)
                {
                    if (this->points_[h][w] > 0)
                    {
                        ss << points_[h][w];
                    }
                    else
                    {
                        ss << '.';
                    }
                }
            }
            ss << '\n';
        }

        return ss.str();
    }

    // [どのゲームでも実装する] : スコア計算をする。(toStringを実装しない場合は引数is_printとそれの不随する処理は不要)
    ScoreType getScore(bool is_print = false) const
    {
        auto tmp_state = *this;
        // キャラクターの位置にあるポイントを消す。
        for (auto &character : this->characters_)
        {
            auto &point = tmp_state.points_[character.y_][character.x_];
            point = 0;
        }
        // 終了するまでキャラクターの移動を繰り返す。
        while (!tmp_state.isDone())
        {
            tmp_state.advance();
            if (is_print)
                std::cout << tmp_state.toString() << std::endl;
        }
        return tmp_state.game_score_;
    }
};

using State = AutoMoveMazeState;

State randomAction(const State &state)
{
    State now_state = state;
    for (int character_id = 0; character_id < CHARACTER_N; character_id++)
    {
        int y = mt_for_action() % H;
        int x = mt_for_action() % W;

        now_state.setCharacter(character_id, y, x);
    }
    return now_state;
}

using AIFunction = std::function<State(const State &)>;

using StringAIPair = std::pair<std::string, AIFunction>;

// ゲームを1回プレイしてゲーム状況を表示する
void playGame(const StringAIPair &ai, const int seed)
{
    using std::cout;
    using std::endl;
    auto state = State(seed);
    state = ai.second(state);
    cout << state.toString() << endl;
    auto score = state.getScore(true);
    cout << "Score of " << ai.first << ": " << score << endl;
}

int main()
{
    const auto &ai = StringAIPair("randomAction", [&](const State &state)
                                  { return randomAction(state); });
    playGame(ai, 0); // 盤面生成シードを0に設定してプレイする。
    return 0;
}