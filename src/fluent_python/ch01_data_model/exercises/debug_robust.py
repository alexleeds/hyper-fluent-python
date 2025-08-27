#!/usr/bin/env python3
"""
Interactive debugging script for the robust FrenchDeck implementation.

Run this script and use the debugger to step through the enhanced, fully-typed version.
"""

import sys
from pathlib import Path

# Add the project root to Python path for imports
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root / "src"))

from fluent_python.ch01_data_model.robust.french_deck import (  # noqa: E402
    Card,
    FrenchDeck,
    Rank,
    Suit,
    cards_by_suit,
    high_card,
)


def debug_robust_french_deck() -> None:
    """
    Step through the robust FrenchDeck implementation with the debugger.

    This function demonstrates the enhanced features:
    - Enum-based type safety for ranks and suits
    - Dataclass with frozen/ordered behavior
    - Full type annotations and overloads
    - Protocol compliance with Sequence[Card]
    - Enhanced error handling
    """
    print("=== Debugging Robust FrenchDeck Implementation ===")

    # Set a breakpoint here to start debugging
    breakpoint()  # 🔍 DEBUG POINT 1: Start here

    # Explore the enum types first
    print("Examining enum types...")
    print(f"Rank.ACE: {Rank.ACE}")
    print(f"Rank.ACE.value: {Rank.ACE.value}")
    print(f"Suit.SPADES: {Suit.SPADES}")
    print(f"All ranks: {list(Rank)}")

    breakpoint()  # 🔍 DEBUG POINT 2: Examine enum behavior

    # Create individual cards - step into Card creation
    ace_of_spades = Card(Rank.ACE, Suit.SPADES)
    king_of_hearts = Card(Rank.KING, Suit.HEARTS)

    print(f"Ace of spades: {ace_of_spades}")
    print(f"String representation: {str(ace_of_spades)}")
    print(f"Repr: {repr(ace_of_spades)}")

    breakpoint()  # 🔍 DEBUG POINT 3: Explore Card dataclass features

    # Test card comparison (thanks to dataclass order=True)
    print(f"Ace > King: {ace_of_spades > king_of_hearts}")
    print(f"Cards are frozen: {ace_of_spades.__dataclass_fields__}")

    # Try to modify (should fail)
    try:
        ace_of_spades.rank = Rank.KING  # This will raise an error
    except Exception as e:
        print(f"Immutability works: {e}")

    breakpoint()  # 🔍 DEBUG POINT 4: Test immutability and ordering

    # Create a deck - step into enhanced __init__
    print("Creating robust deck...")
    deck = FrenchDeck()

    print(f"Deck length: {len(deck)}")
    print(f"Deck type: {type(deck)}")
    print(
        f"Deck is a Sequence: {isinstance(deck, list) or hasattr(deck, '__getitem__')}"
    )

    breakpoint()  # 🔍 DEBUG POINT 5: Examine deck structure

    # Test overloaded __getitem__ behavior
    single_card = deck[0]  # Returns Card
    multiple_cards = deck[:3]  # Returns list[Card]

    print(f"Single card type: {type(single_card)}")
    print(f"Multiple cards type: {type(multiple_cards)}")
    print(f"Single card: {single_card}")
    print(f"Multiple cards: {multiple_cards}")

    breakpoint()  # 🔍 DEBUG POINT 6: Examine type system behavior

    # Test enhanced methods
    print("Testing enhanced deck methods...")

    # Get all spades
    spades = cards_by_suit(deck, Suit.SPADES)
    print(f"Number of spades: {len(spades)}")
    print(f"First few spades: {spades[:3]}")

    # Find highest card
    sample_cards = [deck[0], deck[13], deck[26], deck[39]]
    highest = high_card(sample_cards)
    print(f"Highest card from sample: {highest}")

    breakpoint()  # 🔍 DEBUG POINT 7: Explore utility functions

    # Test deck mutation methods
    original_first_card = deck[0]
    deck.shuffle()
    new_first_card = deck[0]

    print(f"Before shuffle: {original_first_card}")
    print(f"After shuffle: {new_first_card}")
    print(f"Shuffled: {original_first_card != new_first_card}")

    # Test sorting
    deck.sort(by_suit=True)
    print(f"After sort by suit: {deck[:4]}")

    deck.sort(by_suit=False)
    print(f"After sort by rank: {deck[:4]}")

    breakpoint()  # 🔍 DEBUG POINT 8: Examine mutation methods

    # Test error handling
    print("Testing error handling...")
    try:
        high_card([])  # Empty sequence
    except ValueError as e:
        print(f"Error handling works: {e}")

    try:
        deck["invalid"]  # Wrong index type
    except TypeError as e:
        print(f"Type checking works: {e}")

    print("\n=== Key Enhancements to Observe ===")
    print("1. Enum types provide better type safety and debugging")
    print("2. Dataclass gives us immutability and comparison for free")
    print("3. Type annotations help catch errors at development time")
    print("4. Overloads provide precise typing for different use cases")
    print("5. Protocol compliance makes deck work with generic functions")
    print("6. Enhanced error messages improve debugging experience")


def compare_implementations() -> None:
    """
    Side-by-side comparison of key differences.
    """
    print("\n=== IMPLEMENTATION COMPARISON ===")

    breakpoint()  # 🔍 DEBUG POINT 9: Compare implementations

    # Import both
    from fluent_python.ch01_data_model.original.french_deck import Card as OriginalCard
    from fluent_python.ch01_data_model.original.french_deck import (
        FrenchDeck as OriginalDeck,
    )

    # Create instances
    original_deck = OriginalDeck()
    robust_deck = FrenchDeck()

    original_card = original_deck[0]
    robust_card = robust_deck[0]

    print("=== Card Comparison ===")
    print(f"Original card: {original_card} (type: {type(original_card)})")
    print(f"Robust card: {robust_card} (type: {type(robust_card)})")
    print(f"Original fields: {original_card._fields}")
    print(f"Robust fields: {robust_card.__dataclass_fields__.keys()}")

    print("\n=== Behavior Comparison ===")
    print(f"Original supports < comparison: {hasattr(original_card, '__lt__')}")
    print(f"Robust supports < comparison: {hasattr(robust_card, '__lt__')}")

    # Test what happens with invalid data
    print(f"Original with strings: {OriginalCard('invalid', 'data')}")
    # Robust version would fail type checking at development time


if __name__ == "__main__":
    print(
        """
    🐛 DEBUGGING INSTRUCTIONS:
    
    This script explores the enhanced implementation with these debugging tips:
    
    🔍 At each breakpoint, try:
    - p Rank.ACE.__dict__
    - p ace_of_spades.__dataclass_fields__
    - p type(deck[0]) vs type(deck[:1])
    - pp [card for card in deck[:3]]
    
    🎯 Key things to observe:
    1. How enums provide better debugging info than strings
    2. How dataclass generates methods automatically
    3. How type annotations affect IDE behavior
    4. How overloads provide different return types
    5. How protocol compliance enables generic functions
    """
    )

    debug_robust_french_deck()
    compare_implementations()
