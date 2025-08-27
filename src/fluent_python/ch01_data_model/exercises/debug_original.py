#!/usr/bin/env python3
"""
Interactive debugging script for the original FrenchDeck implementation.

Run this script and use the debugger to step through the classic Fluent Python code.
"""

import sys
from pathlib import Path

# Add the project root to Python path for imports
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root / "src"))

from fluent_python.ch01_data_model.original.french_deck import (  # noqa: E402
    Card,
    FrenchDeck,
    spades_high,
)


def debug_original_french_deck() -> None:
    """
    Step through the original FrenchDeck implementation with the debugger.

    This function demonstrates all the key concepts from Fluent Python Chapter 1:
    - How __len__ and __getitem__ make an object sequence-like
    - How Python's data model provides rich functionality for free
    - The power of namedtuples for simple data structures
    """
    print("=== Debugging Original FrenchDeck Implementation ===")

    # Set a breakpoint here to start debugging
    breakpoint()  # 🔍 DEBUG POINT 1: Start here

    # Create a deck - step into __init__ to see how cards are created
    print("Creating deck...")
    deck = FrenchDeck()

    breakpoint()  # 🔍 DEBUG POINT 2: Examine the deck object

    # Examine the structure
    print(f"Deck length: {len(deck)}")  # Calls __len__
    print(f"Type of deck._cards: {type(deck._cards)}")
    print(f"First few cards: {deck._cards[:3]}")

    breakpoint()  # 🔍 DEBUG POINT 3: Look at card structure

    # Get individual cards - this calls __getitem__
    first_card = deck[0]
    last_card = deck[-1]

    print(f"First card: {first_card}")
    print(f"Last card: {last_card}")
    print(f"Card type: {type(first_card)}")
    print(f"Card fields: {first_card._fields}")

    breakpoint()  # 🔍 DEBUG POINT 4: Explore card properties

    # Test slicing - also calls __getitem__
    first_three = deck[:3]
    print(f"First three cards: {first_three}")

    # Test iteration - Python calls __getitem__ repeatedly since no __iter__
    print("Iterating through first 5 cards:")
    for i, card in enumerate(deck):  # type: ignore
        if i >= 5:
            break
        print(f"  {i}: {card}")

    breakpoint()  # 🔍 DEBUG POINT 5: See how iteration works without __iter__

    # Test membership - Python iterates through since no __contains__
    ace_of_spades = Card("A", "spades")
    print(f"Ace of spades in deck: {ace_of_spades in deck}")  # type: ignore

    # Test the ranking function
    some_cards = [deck[0], deck[13], deck[26], deck[39]]  # One from each suit
    print(f"Sample cards: {some_cards}")

    breakpoint()  # 🔍 DEBUG POINT 6: Examine ranking

    # Sort cards using spades_high function
    sorted_cards = sorted(some_cards, key=spades_high)
    print(f"Sorted by spades_high: {sorted_cards}")

    print("\n=== Key Insights to Observe ===")
    print("1. How namedtuple creates Card with ._fields and indexing")
    print("2. How __len__ and __getitem__ provide sequence protocol")
    print("3. How Python falls back to __getitem__ for iteration")
    print("4. How list comprehension creates the full deck")
    print("5. How the ranking function works with card attributes")


if __name__ == "__main__":
    # Instructions for debugging
    print(
        """
    🐛 DEBUGGING INSTRUCTIONS:
    
    This script has multiple breakpoint() calls. At each one:
    
    1. Use 'l' (list) to see current code
    2. Use 'p variable_name' to print variables
    3. Use 'pp variable_name' for pretty printing
    4. Use 'n' (next) to go to next line
    5. Use 's' (step) to step into function calls
    6. Use 'c' (continue) to go to next breakpoint
    7. Use 'q' (quit) to exit debugger
    
    Try these commands at each breakpoint:
    - p deck
    - p deck._cards[:5]
    - p first_card.rank, first_card.suit
    - pp vars()
    """
    )

    debug_original_french_deck()
