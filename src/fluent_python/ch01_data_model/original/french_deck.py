"""
French Deck implementation - Original Fluent Python style.

This is the classic implementation from Fluent Python Chapter 1, 
demonstrating the Python data model with minimal type hints.

Based on: https://github.com/fluentpython/example-code-2e/blob/master/01-data-model/frenchdeck.py
"""

import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# Utility function for card ranking (Bridge-style)
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
