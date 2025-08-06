"""
Comprehensive tests for French Deck implementation

Tests cover:
- Basic functionality of Card and FrenchDeck
- Type safety and error handling
- Special methods behavior 
- Property-based testing with Hypothesis
- Performance characteristics
"""

import random
from typing import Any

import pytest
from hypothesis import given
from hypothesis import strategies as st

from fluent_python.ch01_data_model.french_deck import (
    Card,
    FrenchDeck,
    Rank,
    Suit,
    cards_by_suit,
    demonstrate_special_methods,
    high_card,
)


class TestCard:
    """Test cases for the Card class."""

    def test_card_creation(self) -> None:
        """Test basic card creation."""
        card = Card(Rank.ACE, Suit.SPADES)
        assert card.rank == Rank.ACE
        assert card.suit == Suit.SPADES

    def test_card_immutability(self) -> None:
        """Test that cards are immutable (frozen dataclass)."""
        card = Card(Rank.KING, Suit.HEARTS)
        with pytest.raises(AttributeError):
            card.rank = Rank.QUEEN  # type: ignore

    def test_card_equality(self) -> None:
        """Test card equality comparison."""
        card1 = Card(Rank.ACE, Suit.SPADES)
        card2 = Card(Rank.ACE, Suit.SPADES)
        card3 = Card(Rank.KING, Suit.SPADES)

        assert card1 == card2
        assert card1 != card3

    def test_card_ordering(self) -> None:
        """Test card ordering (rank first, then suit)."""
        ace_spades = Card(Rank.ACE, Suit.SPADES)
        king_spades = Card(Rank.KING, Suit.SPADES)
        ace_hearts = Card(Rank.ACE, Suit.HEARTS)

        # Ace > King regardless of suit
        assert ace_spades > king_spades
        assert ace_hearts > king_spades

        # Same rank: compare by suit (Spades < Hearts < Diamonds < Clubs)
        assert ace_spades < ace_hearts

    def test_card_str_representation(self) -> None:
        """Test human-readable string representation."""
        card = Card(Rank.ACE, Suit.SPADES)
        assert str(card) == "Ace of Spades"

        card = Card(Rank.TEN, Suit.HEARTS)
        assert str(card) == "10 of Hearts"

        card = Card(Rank.JACK, Suit.DIAMONDS)
        assert str(card) == "Jack of Diamonds"

    def test_card_repr(self) -> None:
        """Test developer-friendly representation."""
        card = Card(Rank.QUEEN, Suit.CLUBS)
        assert repr(card) == "Card(<Rank.QUEEN: 12>, <Suit.CLUBS: 4>)"

    @given(rank=st.sampled_from(Rank), suit=st.sampled_from(Suit))
    def test_card_property_roundtrip(self, rank: Rank, suit: Suit) -> None:
        """Property test: creating a card preserves rank and suit."""
        card = Card(rank, suit)
        assert card.rank == rank
        assert card.suit == suit


class TestFrenchDeck:
    """Test cases for the FrenchDeck class."""

    def test_deck_creation(self) -> None:
        """Test basic deck creation."""
        deck = FrenchDeck()
        assert len(deck) == 52

    def test_deck_contains_all_cards(self) -> None:
        """Test that deck contains exactly one of each card."""
        deck = FrenchDeck()
        expected_cards = {Card(rank, suit) for rank in Rank for suit in Suit}
        actual_cards = set(deck)
        assert actual_cards == expected_cards

    def test_deck_indexing(self) -> None:
        """Test deck indexing behavior."""
        deck = FrenchDeck()

        # Test positive indexing
        first_card = deck[0]
        assert isinstance(first_card, Card)

        # Test negative indexing
        last_card = deck[-1]
        assert isinstance(last_card, Card)

        # Test that first and last are different
        assert first_card != last_card

    def test_deck_slicing(self) -> None:
        """Test deck slicing behavior."""
        deck = FrenchDeck()

        # Test basic slicing
        first_three = deck[:3]
        assert isinstance(first_three, list)
        assert len(first_three) == 3
        assert all(isinstance(card, Card) for card in first_three)

        # Test slice with step
        every_other = deck[::2]
        assert isinstance(every_other, list)
        assert len(every_other) == 26

    def test_deck_invalid_indexing(self) -> None:
        """Test error handling for invalid indices."""
        deck = FrenchDeck()

        with pytest.raises(IndexError):
            _ = deck[100]  # Out of bounds

        with pytest.raises(TypeError):
            _ = deck["invalid"]  # type: ignore

    def test_deck_iteration(self) -> None:
        """Test deck iteration."""
        deck = FrenchDeck()
        cards = list(deck)
        assert len(cards) == 52
        assert all(isinstance(card, Card) for card in cards)

    def test_deck_reversed(self) -> None:
        """Test reversed iteration."""
        deck = FrenchDeck()
        forward = list(deck)
        backward = list(reversed(deck))
        assert forward == backward[::-1]

    def test_deck_membership(self) -> None:
        """Test membership testing."""
        deck = FrenchDeck()
        ace_of_spades = Card(Rank.ACE, Suit.SPADES)

        assert ace_of_spades in deck

        # Test with non-existent card (would need a custom Card)
        # Since our deck has all valid cards, we can't test False case easily
        # But we can test the __contains__ method works
        assert len([card for card in deck if card == ace_of_spades]) == 1

    def test_deck_shuffle(self) -> None:
        """Test deck shuffling."""
        deck1 = FrenchDeck()
        deck2 = FrenchDeck()
        _ = deck2  # Use the variable to prevent linter warning

        original_order = list(deck1)

        # Shuffle one deck
        deck1.shuffle()
        shuffled_order = list(deck1)

        # Should have same cards, likely different order
        assert set(original_order) == set(shuffled_order)

        # With 52 cards, extremely unlikely to have same order
        # (though theoretically possible)
        assert len(original_order) == len(shuffled_order) == 52

    def test_deck_sorting(self) -> None:
        """Test deck sorting."""
        deck = FrenchDeck()

        # Shuffle first to ensure we're actually sorting
        deck.shuffle()

        # Sort by rank (default)
        deck.sort()
        cards = list(deck)

        # Should be sorted by rank first
        for i in range(len(cards) - 1):
            current_rank = cards[i].rank.value
            next_rank = cards[i + 1].rank.value
            assert current_rank <= next_rank

    def test_deck_sort_by_suit(self) -> None:
        """Test deck sorting by suit."""
        deck = FrenchDeck()
        deck.shuffle()

        # Sort by suit first
        deck.sort(by_suit=True)
        cards = list(deck)

        # Should be sorted by suit first
        for i in range(len(cards) - 1):
            current_suit = cards[i].suit.value
            next_suit = cards[i + 1].suit.value
            assert current_suit <= next_suit

    def test_deck_repr(self) -> None:
        """Test deck string representations."""
        deck = FrenchDeck()
        assert repr(deck) == "FrenchDeck(52 cards)"
        assert str(deck) == "French deck with 52 cards"

    @given(st.integers(min_value=0, max_value=51))
    def test_deck_valid_indexing_property(self, index: int) -> None:
        """Property test: all valid indices return Cards."""
        deck = FrenchDeck()
        card = deck[index]
        assert isinstance(card, Card)

    @given(st.integers().filter(lambda x: x < -52 or x >= 52))
    def test_deck_invalid_indexing_property(self, index: int) -> None:
        """Property test: invalid indices raise IndexError."""
        deck = FrenchDeck()
        with pytest.raises(IndexError):
            _ = deck[index]


class TestUtilityFunctions:
    """Test utility functions."""

    def test_high_card(self) -> None:
        """Test high card function."""
        cards = [
            Card(Rank.KING, Suit.HEARTS),
            Card(Rank.ACE, Suit.SPADES),
            Card(Rank.QUEEN, Suit.DIAMONDS),
        ]

        highest = high_card(cards)
        assert highest.rank == Rank.ACE

    def test_high_card_empty_sequence(self) -> None:
        """Test high card with empty sequence."""
        with pytest.raises(ValueError, match="Cannot find high card in empty sequence"):
            high_card([])

    def test_cards_by_suit(self) -> None:
        """Test filtering cards by suit."""
        deck = FrenchDeck()
        spades = cards_by_suit(deck, Suit.SPADES)

        assert len(spades) == 13
        assert all(card.suit == Suit.SPADES for card in spades)

        # Should have all ranks
        ranks_in_spades = {card.rank for card in spades}
        assert ranks_in_spades == set(Rank)


class TestSpecialMethods:
    """Test special methods integration."""

    def test_random_choice_works(self) -> None:
        """Test that random.choice works with our deck."""
        deck = FrenchDeck()
        card = random.choice(deck)
        assert isinstance(card, Card)
        assert card in deck

    def test_builtin_functions_work(self) -> None:
        """Test that built-in functions work with our deck."""
        deck = FrenchDeck()

        # len() should work
        assert len(deck) == 52

        # max() should work with key function
        highest_card = max(deck, key=lambda c: c.rank.value)
        assert highest_card.rank == Rank.ACE

        # min() should work
        lowest_card = min(deck, key=lambda c: c.rank.value)
        assert lowest_card.rank == Rank.TWO

        # sorted() should work
        sorted_cards = sorted(deck, key=lambda c: c.rank.value)
        assert len(sorted_cards) == 52
        assert sorted_cards[0].rank == Rank.TWO
        assert sorted_cards[-1].rank == Rank.ACE


class TestDemonstration:
    """Test the demonstration function."""

    def test_demonstrate_special_methods_runs(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Test that the demonstration function runs without error."""
        demonstrate_special_methods()

        captured = capsys.readouterr()
        assert "Demonstrating Python Data Model" in captured.out
        assert "Type Safety Demonstration" in captured.out


# Benchmarking tests (optional, for performance insights)
class TestPerformance:
    """Performance-related tests."""

    def test_deck_creation_performance(self, benchmark: Any) -> None:
        """Benchmark deck creation."""
        try:
            benchmark(FrenchDeck)
        except NameError:
            # pytest-benchmark not installed, skip
            pytest.skip("pytest-benchmark not available")

    def test_deck_iteration_performance(self, benchmark: Any) -> None:
        """Benchmark deck iteration."""
        try:
            deck = FrenchDeck()
            benchmark(list, deck)
        except NameError:
            # pytest-benchmark not installed, skip
            pytest.skip("pytest-benchmark not available")
