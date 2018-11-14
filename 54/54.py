import time
from enum import IntEnum


class PokerHand:
    cards = []
    general_score = 0
    higher_combination_figure_score = 0
    lower_combination_figure_score = 0
    sorted_cards_values = []

    def grade_hand(self):
        if self.has_royal_flush():
            self.general_score = Score.ROYAL_FLUSH
        elif self.has_straight_flush():
            self.general_score = Score.STRAIGHT_FLUSH
        elif self.has_four_of_a_kind():
            self.general_score = Score.FOUR_OF_A_KIND
        elif self.has_full_house():
            self.general_score = Score.FULL_HOUSE
        elif self.has_flush():
            self.general_score = Score.FLUSH
        elif self.has_straight():
            self.general_score = Score.STRAIGHT
        elif self.has_three_of_a_kind():
            self.general_score = Score.THREE_OF_A_KIND
        elif self.has_two_pairs():
            self.general_score = Score.TWO_PAIRS
        elif self.has_one_pair():
            self.general_score = Score.ONE_PAIR
        else:
            self.general_score = Score.HIGH_CARD

    def has_royal_flush(self):
        if not self.are_cards_of_same_suit():
            return False
        if not self.are_cards_consecutive():
            return False

        figures_set = self.get_figures_set()

        if not figures_set.__contains__('A'):
            return False
        if not figures_set.__contains__('T'):
            return False

        return True

    def get_number_of_distinct_figures(self):
        figures_set = self.get_figures_set()

        return len(figures_set)

    def get_figures_set(self):
        figures_set = set()

        for card in self.cards:
            figures_set.add(card[CardParts.FIGURE])

        return figures_set

    def are_cards_consecutive(self):
        figures_set = self.get_figures_set()

        if len(figures_set) < 5:
            return False

        self.count_sorted_card_values()

        for i in range(0, 4):
            if self.sorted_cards_values[i] - self.sorted_cards_values[i + 1] != 1:
                return False

        return True

    def get_smallest_card_value(self):
        smallest_card_value = 0

        for card in self.cards:
            smallest_card_value = min(smallest_card_value, self.get_card_value(card))

        return smallest_card_value

    @staticmethod
    def get_card_value(card):
        return PokerHand.get_figure_value(card[CardParts.FIGURE])

    @staticmethod
    def get_figure_value(figure):
        if figure == 'A':
            return 14
        if figure == 'K':
            return 13
        if figure == 'Q':
            return 12
        if figure == 'J':
            return 11
        if figure == 'T':
            return 10

        return int(figure)

    def are_cards_of_same_suit(self):
        suits_set = set()
        for card in self.cards:
            suits_set.add(card[CardParts.SUIT])
        return len(suits_set) < 2

    def has_straight_flush(self):
        if not self.are_cards_of_same_suit():
            return False
        if not self.are_cards_consecutive():
            return False

        if self.are_cards_consecutive():
            self.higher_combination_figure_score = self.count_max_card_value()

        return True

    def has_four_of_a_kind(self):
        if self.get_number_of_distinct_figures() != 2:
            return False

        figures = self.get_figures_list()

        if figures.count(figures[0]) == 4:
            self.higher_combination_figure_score = self.get_figure_value(figures[0])
            return True
        if figures.count(figures[1]) == 4:
            self.higher_combination_figure_score = self.get_figure_value(figures[1])
            return True

        return False

    def get_figures_list(self):
        figures = []

        for card in self.cards:
            figures.append(card[CardParts.FIGURE])

        return figures

    def has_full_house(self):
        if self.get_number_of_distinct_figures() != 2:
            return False

        distinct_figures = list(self.get_figures_set())
        figures = self.get_figures_list()
        has_three = False
        has_pair = False

        if figures.count(distinct_figures[0]) == 2 or figures.count(distinct_figures[1]) == 2:
            has_pair = True
        if figures.count(distinct_figures[0]) == 3 or figures.count(distinct_figures[1]) == 3:
            has_three = True

        if has_pair and has_three:
            if figures.count(distinct_figures[0]) == 3:
                self.higher_combination_figure_score = self.get_figure_value(distinct_figures[0])
                self.lower_combination_figure_score = self.get_figure_value(distinct_figures[1])
            else:
                self.higher_combination_figure_score = self.get_figure_value(distinct_figures[1])
                self.lower_combination_figure_score = self.get_figure_value(distinct_figures[0])

        return has_pair and has_three

    def has_flush(self):
        if self.are_cards_of_same_suit():
            self.higher_combination_figure_score = self.count_max_card_value()
        return self.are_cards_of_same_suit()

    def has_straight(self):
        if self.are_cards_consecutive():
            self.higher_combination_figure_score = self.count_max_card_value()
        return self.are_cards_consecutive()

    def has_three_of_a_kind(self):
        distinct_figures = list(self.get_figures_set())
        figures = self.get_figures_list()

        for figure in distinct_figures:
            if figures.count(figure) == 3:
                self.higher_combination_figure_score = PokerHand.get_figure_value(figure)
                return True

        return False

    def has_two_pairs(self):
        return self.get_pairs_count() == 2

    def get_pairs_count(self):
        distinct_figures = list(self.get_figures_set())
        figures = self.get_figures_list()

        pairs_count = 0
        pairs_figures_values = []

        for figure in distinct_figures:
            if figures.count(figure) == 2:
                pairs_figures_values.append(PokerHand.get_figure_value(figure))
                pairs_count += 1

        if pairs_count == 0:
            return 0

        self.higher_combination_figure_score = max(pairs_figures_values)

        if pairs_count == 2:
            self.lower_combination_figure_score = min(pairs_figures_values)

        return pairs_count

    def has_one_pair(self):
        return self.get_pairs_count() == 1

    def count_max_card_value(self):
        cards_values = []
        for card in self.cards:
            cards_values.append(self.get_card_value(card))
        return max(cards_values)

    def count_sorted_card_values(self):
        cards_values = []
        for card in self.cards:
            cards_values.append(self.get_card_value(card))
        cards_values.sort(reverse=True)
        self.sorted_cards_values =  cards_values


class Player(IntEnum):
    ONE = 0
    TWO = 1


class Score(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9


class CardParts(IntEnum):
    FIGURE = 0
    SUIT = 1


def prepare_hands(hands_file):
    hands = [[], []]

    for line in poker_file:
        player_one_hand = PokerHand()
        player_one_hand.cards = line[:14].split(" ")
        player_one_hand.grade_hand()

        player_two_hand = PokerHand()
        player_two_hand.cards = line[15:-1].split(" ")
        player_two_hand.grade_hand()

        hands[Player.ONE].append(player_one_hand)
        hands[Player.TWO].append(player_two_hand)

    return hands


elapsed_time = time.time()

file_name = 'poker.txt'
poker_file = open(file_name, 'r')
player_hands = prepare_hands(poker_file)
poker_file.close()

number_of_hands = len(player_hands[Player.ONE])

p1wins = 0
p2wins = 0

for i in range(0, number_of_hands):

    if player_hands[Player.ONE][i].general_score > player_hands[Player.TWO][i].general_score:
        p1wins += 1
    if player_hands[Player.ONE][i].general_score < player_hands[Player.TWO][i].general_score:
        p2wins += 1
    if player_hands[Player.ONE][i].general_score == player_hands[Player.TWO][i].general_score:
        if player_hands[Player.ONE][i].higher_combination_figure_score > player_hands[Player.TWO][i].higher_combination_figure_score:
            p1wins += 1
        elif player_hands[Player.ONE][i].higher_combination_figure_score < player_hands[Player.TWO][i].higher_combination_figure_score:
            p2wins += 1
        else:
            if player_hands[Player.ONE][i].lower_combination_figure_score > player_hands[Player.TWO][i].lower_combination_figure_score:
                p1wins += 1
            elif player_hands[Player.ONE][i].lower_combination_figure_score < player_hands[Player.TWO][i].lower_combination_figure_score:
                p2wins += 1
            else:
                player_hands[Player.ONE][i].count_sorted_card_values()
                player_hands[Player.TWO][i].count_sorted_card_values()
                for j in range(0, 4):
                    if player_hands[Player.ONE][i].sorted_cards_values[j] > player_hands[Player.TWO][i].sorted_cards_values[j]:
                        p1wins += 1
                        break
                    if player_hands[Player.ONE][i].sorted_cards_values[j] < player_hands[Player.TWO][i].sorted_cards_values[j]:
                        p2wins += 1
                        break

elapsed_time = time.time() - elapsed_time

print(f'p1:{p1wins}, p2:{p2wins}, sum:{p1wins + p2wins}')
print('Time: ' + str(elapsed_time))
