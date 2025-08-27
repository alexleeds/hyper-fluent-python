"""
Tests for original French Deck implementation.

These tests verify the basic functionality of the original Fluent Python examples.
"""

import random

from fluent_python.ch01_data_model.original.french_deck import (
    Card,
    FrenchDeck,
    spades_high,
)


class TestOriginalCard:
    """Test cases for the original Card namedtuple."""

    def test_card_creation(self) -> None:
        """Test basic card creation."""
        card = Card("A", "spades")
        assert card.rank == "A"
        assert card.suit == "spades"

    def test_card_equality(self) -> None:
        """Test card equality."""
        card1 = Card("A", "spades")
        card2 = Card("A", "spades")
        card3 = Card("K", "spades")

        assert card1 == card2
        assert card1 != card3

    def test_card_str_representation(self) -> None:
        """Test card string representation."""
        card = Card("A", "spades")
        assert str(card) == "Card(rank='A', suit='spades')"


class TestOriginalFrenchDeck:
    """Test cases for the original FrenchDeck class."""

    def test_deck_creation(self) -> None:
        """Test basic deck creation."""
        deck = FrenchDeck()
        assert len(deck) == 52

    def test_deck_contains_expected_cards(self) -> None:
        """Test that deck contains expected cards."""
        deck = FrenchDeck()

        # Check first few cards
        first_card = deck[0]
        assert first_card.rank in FrenchDeck.ranks
        assert first_card.suit in FrenchDeck.suits

    def test_deck_indexing(self) -> None:
        """Test deck indexing behavior."""
        deck = FrenchDeck()

        # Test positive indexing
        first_card = deck[0]
        assert isinstance(first_card, Card)

        # Test negative indexing
        last_card = deck[-1]
        assert isinstance(last_card, Card)

    def test_deck_slicing(self) -> None:
        """Test deck slicing behavior."""
        deck = FrenchDeck()

        # Test basic slicing
        first_three = deck[:3]
        assert isinstance(first_three, list)
        assert len(first_three) == 3
        assert all(isinstance(card, Card) for card in first_three)

    def test_deck_iteration(self) -> None:
        """Test deck iteration."""
        deck = FrenchDeck()
        cards = list(deck)
        assert len(cards) == 52
        assert all(isinstance(card, Card) for card in cards)

    def test_random_choice_works(self) -> None:
        """Test that random.choice works with our deck."""
        deck = FrenchDeck()
        card = random.choice(deck)
        assert isinstance(card, Card)

    def test_builtin_functions_work(self) -> None:
        """Test that built-in functions work with our deck."""
        deck = FrenchDeck()

        # len() should work
        assert len(deck) == 52

        # max() should work with key function
        highest_card = max(deck, key=spades_high)
        assert isinstance(highest_card, Card)

        # min() should work
        lowest_card = min(deck, key=spades_high)
        assert isinstance(lowest_card, Card)

        # sorted() should work
        sorted_cards = sorted(deck, key=spades_high)
        assert len(sorted_cards) == 52


class TestSpadesHigh:
    """Test the spades_high utility function."""

    def test_spades_high_ordering(self) -> None:
        """Test that spades_high provides correct ordering."""
        ace_spades = Card("A", "spades")
        king_hearts = Card("K", "hearts")

        # Ace should be higher than King
        assert spades_high(ace_spades) > spades_high(king_hearts)

        # Spades should be higher than other suits for same rank
        ace_hearts = Card("A", "hearts")
        assert spades_high(ace_spades) > spades_high(ace_hearts)
