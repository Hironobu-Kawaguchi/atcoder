from dataclasses import dataclass
from enum import Enum
import sys

MAX_INVEST_LEVEL = 20


@dataclass
class Project:
    """
    Project クラス: プロジェクトの情報を管理
    h: 残務量
    v: 価値
    """
    h: int
    v: int

# enum.Enum を使用し CardType 列挙型 カードの種類を表す定数を定義
class CardType(Enum):
    WORK_SINGLE = 0     # 通常労働カード
    WORK_ALL = 1        # 全力労働カード
    CANCEL_SINGLE = 2   # キャンセルカード
    CANCEL_ALL = 3      # 業務転換カード
    INVEST = 4          # 増資カード

@dataclass
class Card:
    """
    Card クラス: 方針カードの情報を管理
    t: 方針カードの種類
    w: 労働力
    p: コスト
    """
    t: CardType
    w: int
    p: int

class Judge:
    """
    Judge クラス: ゲームの入出力を管理
    n: 手札に持つ方針カードの枚数 2<=N<=7
    m: 会社が管理するプロジェクトの数 2<=M<=8
    k: 手札に補充する方針カードの提示枚数 2<=K<=5
    """

    def __init__(self, n: int, m: int, k: int):
        self.n = n
        self.m = m
        self.k = k

    def read_initial_cards(self) -> list[Card]:
        """
        開始時点の手札の方針カードの情報を読み込む
        """
        cards = []
        for _ in range(self.n):
            t, w = map(int, input().split())
            cards.append(Card(CardType(t), w, 0))
        return cards

    def read_projects(self) -> list[Project]:
        """
        プロジェクトの情報を読み込む
        """
        projects = []
        for _ in range(self.m):
            h, v = map(int, input().split())
            projects.append(Project(h, v))
        return projects

    def use_card(self, c: int, m: int) -> None:
        """
        方針カードを使用する
        c: 手札のうち何番目の方針カードを使用するか
        m: カードの効果を適用するプロジェクトの番号
        """
        print(f"{c} {m}", flush=True)

    def read_money(self) -> int:
        """
        現在の所持金の情報を標準入力から受け取る
        """
        return int(input())

    def read_next_cards(self) -> list[Card]:
        """
        手札に補充する方針カードの候補の情報を標準入力から受け取る
        """
        cards = []
        for _ in range(self.k):
            t, w, p = map(int, input().split())
            cards.append(Card(CardType(t), w, p))
        return cards

    def select_card(self, r: int) -> None:
        """
        K枚の方針カード候補のうち何番目のカードを手札に加えるかの情報を標準出力へ出力
        r: 手札に補充する方針カードの候補の中から何番目のカードを選ぶか
        """
        print(r, flush=True)

    def comment(self, message: str) -> None:
        """
        コメントを出力する
        message: コメントの内容
        """
        print(f"# {message}")


class Solver:
    """
    Solver クラス: ゲームの進行を管理
    n: 手札に持つ方針カードの枚数 2<=N<=7
    m: 会社が管理するプロジェクトの数 2<=M<=8
    k: 手札に補充する方針カードの提示枚数 2<=K<=5
    t: ゲームのターン数 T==1000
    """

    def __init__(self, n: int, m: int, k: int, t: int):
        self.n = n
        self.m = m
        self.k = k
        self.t = t
        self.judge = Judge(n, m, k)

    def solve(self) -> int:
        """
        ゲームを進行する
        """
        self.turn = 0
        self.money = 0
        self.invest_level = 0
        self.cards = self.judge.read_initial_cards()
        self.projects = self.judge.read_projects()

        for _ in range(self.t):
            use_card_i, use_target = self._select_action()
            if self.cards[use_card_i].t == CardType.INVEST:
                self.invest_level += 1
            # example for comments
            self.judge.comment(f"used {self.cards[use_card_i]} to target {use_target}")
            self.judge.use_card(use_card_i, use_target)
            assert self.invest_level <= MAX_INVEST_LEVEL

            self.projects = self.judge.read_projects()
            self.money = self.judge.read_money()

            next_cards = self.judge.read_next_cards()
            select_card_i = self._select_next_card(next_cards)
            self.cards[use_card_i] = next_cards[select_card_i]
            self.judge.select_card(select_card_i)
            self.money -= next_cards[select_card_i].p
            assert self.money >= 0

            self.turn += 1

        return self.money

    def _select_action(self) -> tuple[int, int]:
        """
        手札から使用する方針カードとプロジェクトを決める戦略
        (c, m): c番目の方針カードをm番目のプロジェクトに使用する
        c: 手札のうち何番目の方針カードを使用するか
        m: カードの効果を適用するプロジェクトの番号
        """
        # TODO: implement your strategy
        # 増資カードがあり，self.invest_level が MAX_INVEST_LEVEL 未満の場合は増資カードを使用する
        if self.invest_level < MAX_INVEST_LEVEL:
            for i, card in enumerate(self.cards):
                if card.t == CardType.INVEST:
                    return (i, 0)
        # WORKカードの労働力が最大のものを選ぶ
        work_cards = []
        for i, card in enumerate(self.cards):
            if card.t == CardType.WORK_SINGLE:
                work_cards.append((card.w, i, card))
            elif card.t == CardType.WORK_ALL:
                work_cards.append((card.w * self.n, i, card))
        work_cards.sort(reverse=True)
        if len(work_cards) == 0:    # WORKカードがない場合は0番目のカードを選ぶ
            c = 0
        else:
            c = work_cards[0][1]
        # 選んだカードが全力労働カード, 業務転換カード, 増資カードのいずれかの場合は m=0 を満たす必要がある
        if self.cards[c].t in [CardType.WORK_ALL, CardType.CANCEL_ALL, CardType.INVEST]:
            m = 0
            return (c, m)
        elif self.cards[c].t == CardType.CANCEL_SINGLE: # キャンセルカードの場合
            m = 0
            return (c, m)
        else: # WORK_SINGLEの場合
            # 残務量が選択したカードの労働力以下で価値が最大のプロジェクトを選ぶ
            # ただし, 該当プロジェクトがない場合は，費用対効果(v/h)が最大のプロジェクトを選ぶ
            best_vh = 0.0
            best_vh_m = 0
            finish_best_v = 0
            finish_best_v_m = -1
            for m, project in enumerate(self.projects):
                if project.v / project.h > best_vh:
                    best_vh = project.v / project.h
                    best_vh_m = m
                if project.h <= self.cards[c].w:
                    if project.v > finish_best_v:
                        finish_best_v = project.v
                        finish_best_v_m = m
            if finish_best_v_m != -1:
                m = finish_best_v_m
            else:
                m = best_vh_m
            return (c, m)

    def _select_next_card(self, next_cards: list[Card]) -> int:
        """
        手札に補充する方針カードの候補から次の手札を決める戦略
        r: 手札に補充する方針カードの候補の中から何番目のカードを選ぶか
        """
        # TODO: implement your strategy
        return 0


def main():
    n, m, k, t = map(int, input().split())
    solver = Solver(n, m, k, t)
    score = solver.solve()
    print(f"score:{score}", file=sys.stderr)


if __name__ == "__main__":
    main()
