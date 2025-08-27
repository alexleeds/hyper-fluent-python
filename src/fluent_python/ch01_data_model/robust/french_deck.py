"""
French Deck of Cards - Enhanced Implementation

This module demonstrates the Python data model through Card and FrenchDeck examples,
enhanced with comprehensive type annotations following Robust Python methodology.

This closely follows the classic FrenchDeck example from Fluent Python Chapter 1,
but with added type safety, documentation, and error handling.
"""

from __future__ import annotations

import random
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Final, Union, overload


class Suit(Enum):
    """Card suit enumeration with explicit ordering for comparison operations."""

    SPADES = auto()
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()

    def __lt__(self, other: Any) -> bool:
        """Enable suit comparison for sorting. Spades > Hearts > Diamonds > Clubs."""
        if not isinstance(other, Suit):
            return NotImplemented
        return self.value < other.value


class Rank(Enum):
    """Card rank enumeration with poker-style ordering."""

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __lt__(self, other: Any) -> bool:
        """Enable rank comparison for sorting."""
        if not isinstance(other, Rank):
            return NotImplemented
        return self.value < other.value


# Type alias for cleaner type hints
IndexType = Union[int, slice]


@dataclass(frozen=True, order=True)
class Card:
    """
    A playing card with rank and suit.

    This implementation uses frozen dataclass for immutability and automatic
    comparison methods. The order is defined by rank first, then suit.

    Examples:
        >>> card = Card(Rank.ACE, Suit.SPADES)
        >>> card.rank
        <Rank.ACE: 14>
        >>> card.suit
        <Suit.SPADES: 1>
        >>> str(card)
        'Ace of Spades'
    """

    rank: Rank
    suit: Suit

    def __str__(self) -> str:
        """Return human-readable card representation."""
        rank_names: Final[dict[Rank, str]] = {
            Rank.TWO: "2",
            Rank.THREE: "3",
            Rank.FOUR: "4",
            Rank.FIVE: "5",
            Rank.SIX: "6",
            Rank.SEVEN: "7",
            Rank.EIGHT: "8",
            Rank.NINE: "9",
            Rank.TEN: "10",
            Rank.JACK: "Jack",
            Rank.QUEEN: "Queen",
            Rank.KING: "King",
            Rank.ACE: "Ace",
        }

        suit_names: Final[dict[Suit, str]] = {
            Suit.SPADES: "Spades",
            Suit.HEARTS: "Hearts",
            Suit.DIAMONDS: "Diamonds",
            Suit.CLUBS: "Clubs",
        }

        return f"{rank_names[self.rank]} of {suit_names[self.suit]}"

    def __repr__(self) -> str:
        """Return developer-friendly representation."""
        return f"Card({self.rank!r}, {self.suit!r})"


class FrenchDeck(Sequence[Card]):
    """
    A deck of 52 French playing cards.

    This implementation demonstrates the Python data model by implementing
    special methods that allow the deck to behave like a built-in sequence.

    The deck supports:
    - len() - returns number of cards
    - indexing with deck[index]
    - iteration with for card in deck
    - membership testing with card in deck
    - slicing with deck[start:end]

    Examples:
        >>> deck = FrenchDeck()
        >>> len(deck)
        52
        >>> deck[0]
        Card(Rank.TWO, Suit.SPADES)
        >>> deck[-1]
        Card(Rank.ACE, Suit.CLUBS)
        >>> Card(Rank.ACE, Suit.SPADES) in deck
        True
    """

    def __init__(self) -> None:
        """Initialize a complete deck of 52 cards."""
        self._cards: list[Card] = [Card(rank, suit) for suit in Suit for rank in Rank]

    def __len__(self) -> int:
        """Return the number of cards in the deck."""
        return len(self._cards)

    @overload
    def __getitem__(self, position: int) -> Card: ...

    @overload
    def __getitem__(self, position: slice) -> list[Card]: ...

    def __getitem__(self, position: IndexType) -> Union[Card, list[Card]]:
        """
        Get card(s) at position.

        Args:
            position: Integer index or slice object

        Returns:
            Single Card for integer index, list of Cards for slice

        Raises:
            IndexError: If position is out of bounds
            TypeError: If position is not int or slice
        """
        if isinstance(position, int):
            return self._cards[position]
        elif isinstance(position, slice):
            return self._cards[position]
        else:
            raise TypeError(
                f"indices must be integers or slices, not {type(position).__name__}"
            )

    def __iter__(self) -> Iterator[Card]:
        """Return iterator over cards in the deck."""
        return iter(self._cards)

    def __reversed__(self) -> Iterator[Card]:
        """Return iterator over cards in reverse order."""
        return reversed(self._cards)

    def __contains__(self, card: object) -> bool:
        """Check if card is in the deck."""
        return card in self._cards

    def __repr__(self) -> str:
        """Return developer-friendly representation."""
        return f"FrenchDeck({len(self)} cards)"

    def __str__(self) -> str:
        """Return human-readable representation."""
        return f"French deck with {len(self)} cards"

    def shuffle(self) -> None:
        """
        Shuffle the deck in place.

        Note: This method mutates the deck state. Consider using
        random.sample() for functional-style shuffling.
        """
        random.shuffle(self._cards)

    def sort(self, *, by_suit: bool = False) -> None:
        """
        Sort the deck in place.

        Args:
            by_suit: If True, sort by suit first, then rank.
                    If False, sort by rank first, then suit.
        """
        if by_suit:
            self._cards.sort(key=lambda card: (card.suit, card.rank))
        else:
            self._cards.sort(key=lambda card: (card.rank, card.suit))


# Utility functions demonstrating different ways to work with the deck
def high_card(cards: Sequence[Card]) -> Card:
    """
    Return the highest card from a sequence of cards.

    Args:
        cards: Sequence of cards to evaluate

    Returns:
        The card with the highest rank (Ace high)

    Raises:
        ValueError: If cards sequence is empty

    Examples:
        >>> cards = [Card(Rank.KING, Suit.HEARTS), Card(Rank.ACE, Suit.SPADES)]
        >>> high_card(cards)
        Card(Rank.ACE, Suit.SPADES)
    """
    if not cards:
        raise ValueError("Cannot find high card in empty sequence")

    return max(cards, key=lambda card: card.rank.value)


def cards_by_suit(deck: FrenchDeck, suit: Suit) -> list[Card]:
    """
    Extract all cards of a given suit from the deck.

    Args:
        deck: The deck to search
        suit: The suit to filter by

    Returns:
        List of cards matching the suit

    Examples:
        >>> deck = FrenchDeck()
        >>> spades = cards_by_suit(deck, Suit.SPADES)
        >>> len(spades)
        13
    """
    return [card for card in deck if card.suit == suit]


def demonstrate_special_methods() -> None:
    """
    Demonstrate the power of Python's data model through special methods.

    This function shows how implementing __len__ and __getitem__ gives us
    many behaviors for free through the Python data model.
    """
    print("=== Demonstrating Python Data Model ===")

    # Create a deck
    deck = FrenchDeck()

    # len() calls __len__
    print(f"Deck length: {len(deck)}")

    # Indexing calls __getitem__
    print(f"First card: {deck[0]}")
    print(f"Last card: {deck[-1]}")

    # Slicing also calls __getitem__
    print(f"First 3 cards: {deck[:3]}")

    # Iteration calls __iter__ (which we implemented)
    # or falls back to __getitem__ + __len__
    print("First 5 cards via iteration:")
    for i, card in enumerate(deck):
        if i >= 5:
            break
        print(f"  {card}")

    # random.choice works because deck supports indexing and len
    random_card = random.choice(deck)
    print(f"Random card: {random_card}")

    # 'in' operator uses __contains__ (which we implemented)
    # or falls back to iteration
    ace_of_spades = Card(Rank.ACE, Suit.SPADES)
    print(f"Ace of Spades in deck: {ace_of_spades in deck}")

    # Sorting works with any iterable
    sorted_by_rank = sorted(deck, key=lambda card: card.rank.value)
    print(f"Lowest card: {sorted_by_rank[0]}")
    print(f"Highest card: {sorted_by_rank[-1]}")

    print("\n=== Type Safety Demonstration ===")

    # The type system helps catch errors at development time
    try:
        # This would be caught by a type checker
        Card("invalid", "suit")  # type: ignore
    except Exception as e:
        print(f"Runtime error caught: {e}")

    # Demonstrate protocol usage
    def process_sequence(seq: Sequence[Any]) -> None:
        """Function that works with any sequence-like object."""
        print(f"Processing sequence with {len(seq)} items")
        if len(seq) > 0:
            print(f"First item: {seq[0]}")

    process_sequence(deck)
    process_sequence([1, 2, 3])
    process_sequence("hello")


if __name__ == "__main__":
    # Add debugger breakpoint for interactive exploration
    # breakpoint()  # Uncomment to debug interactively

    demonstrate_special_methods()
