"""
Comparison between original and robust implementations.

This module demonstrates the differences between the original Fluent Python
examples and the enhanced robust versions.
"""

from typing import Any

# Import both implementations
from .original import french_deck as original_deck
from .original import vector as original_vector
from .robust import french_deck as robust_deck
from .robust import vector as robust_vector


def demonstrate_french_deck_differences() -> None:
    """Demonstrate differences between original and robust French deck implementations."""
    print("=" * 60)
    print("FRENCH DECK IMPLEMENTATION COMPARISON")
    print("=" * 60)

    # Original implementation
    print("\n--- ORIGINAL IMPLEMENTATION ---")
    original = original_deck.FrenchDeck()
    print(f"Deck length: {len(original)}")
    print(f"First card: {original[0]}")
    print(f"Card type: {type(original[0])}")
    print(f"Available ranks: {original.ranks}")
    print(f"Available suits: {original.suits}")

    # Robust implementation
    print("\n--- ROBUST IMPLEMENTATION ---")
    robust = robust_deck.FrenchDeck()
    print(f"Deck length: {len(robust)}")
    print(f"First card: {robust[0]}")
    print(f"Card type: {type(robust[0])}")
    print(f"Card string representation: {robust[0]}")
    print(f"Available ranks: {[rank.name for rank in robust_deck.Rank]}")
    print(f"Available suits: {[suit.name for suit in robust_deck.Suit]}")

    # Demonstrate type safety differences
    print("\n--- TYPE SAFETY COMPARISON ---")

    # Original - can create invalid cards
    print("Original: Can create invalid cards")
    try:
        invalid_original = original_deck.Card("invalid_rank", "invalid_suit")
        print(f"Invalid card created: {invalid_original}")
    except Exception as e:
        print(f"Error: {e}")

    # Robust - type system prevents invalid cards (at development time)
    print("\nRobust: Type system prevents invalid cards")
    print("(This would be caught by mypy/type checker before runtime)")
    try:
        # This creates a runtime error for demonstration
        # In practice, the type checker would catch this
        invalid_robust = robust_deck.Card("invalid_rank", "invalid_suit")  # type: ignore
        print(f"Invalid card created: {invalid_robust}")
    except Exception as e:
        print(f"Runtime error: {e}")

    # Demonstrate additional functionality in robust version
    print("\n--- ADDITIONAL ROBUST FEATURES ---")
    robust_card = robust_deck.Card(robust_deck.Rank.ACE, robust_deck.Suit.SPADES)
    print(f"Rich card representation: {robust_card}")
    print("Card is immutable: attempting to modify rank...")

    try:
        robust_card.rank = robust_deck.Rank.KING  # type: ignore
    except AttributeError as e:
        print(f"✓ Immutability protected: {e}")

    # Sorting capabilities
    print("\nSorting capabilities:")
    print("Shuffling deck...")
    robust.shuffle()
    print("Sorting by rank...")
    robust.sort()
    print(f"Now first card: {robust[0]}")


def demonstrate_vector_differences() -> None:
    """Demonstrate differences between original and robust vector implementations."""
    print("\n\n" + "=" * 60)
    print("VECTOR IMPLEMENTATION COMPARISON")
    print("=" * 60)

    # Original implementation
    print("\n--- ORIGINAL IMPLEMENTATION ---")
    original_v1 = original_vector.Vector(3, 4)
    original_v2 = original_vector.Vector(2, 1)

    print(f"Vector 1: {original_v1}")
    print(f"Vector 2: {original_v2}")
    print(f"Addition: {original_v1 + original_v2}")
    print(f"Multiplication: {original_v1 * 2}")
    print(f"Magnitude: {abs(original_v1)}")
    print(f"Truthiness: {bool(original_v1)}")

    # Robust implementation
    print("\n--- ROBUST IMPLEMENTATION ---")
    robust_v1 = robust_vector.Vector(3, 4)
    robust_v2 = robust_vector.Vector(2, 1)

    print(f"Vector 1: {robust_v1}")
    print(f"Vector 2: {robust_v2}")
    print(f"Addition: {robust_v1 + robust_v2}")
    print(f"Subtraction: {robust_v1 - robust_v2}")
    print(f"Multiplication: {robust_v1 * 2}")
    print(f"Reverse multiplication: {2 * robust_v1}")
    print(f"Magnitude: {abs(robust_v1)}")
    print(f"Truthiness: {bool(robust_v1)}")

    # Additional robust features
    print("\n--- ADDITIONAL ROBUST FEATURES ---")
    print(f"Dot product: {robust_v1.dot(robust_v2)}")
    print(f"Angle (radians): {robust_v1.angle():.3f}")
    print(f"Distance between vectors: {robust_v1.distance_to(robust_v2):.3f}")
    print(f"Normalized vector: {robust_v1.normalized()}")
    print(f"Normalized magnitude: {abs(robust_v1.normalized()):.6f}")

    # Hash support
    print("\nHash support (can be used in sets):")
    vector_set = {robust_v1, robust_v2, robust_vector.Vector(3, 4)}
    print(f"Set of vectors: {vector_set}")
    print(f"Set length (Vector(3,4) == robust_v1): {len(vector_set)}")

    # Error handling
    print("\nError handling:")
    try:
        _ = robust_v1 + "invalid"  # type: ignore
    except TypeError as e:
        print(f"✓ Type error caught: {e}")

    try:
        zero = robust_vector.Vector(0, 0)
        zero.normalized()
    except ValueError as e:
        print(f"✓ Zero vector normalization error: {e}")


def demonstrate_type_annotations() -> None:
    """Demonstrate the value of type annotations in the robust implementation."""
    print("\n\n" + "=" * 60)
    print("TYPE ANNOTATION BENEFITS")
    print("=" * 60)

    print("\nOriginal implementation type hints:")
    print("- Minimal type information")
    print("- Runtime errors for type mismatches")
    print("- No IDE support for autocompletion")
    print("- Hard to reason about interfaces")

    print("\nRobust implementation type hints:")
    print("- Complete type information with generics")
    print("- Compile-time error detection with mypy")
    print("- Rich IDE support and autocompletion")
    print("- Clear contracts and interfaces")
    print("- Protocol compliance (e.g., Sequence)")

    # Demonstrate protocol compliance
    def process_sequence(seq: Any) -> None:
        """Function that works with sequence-like objects."""
        print(f"Processing {type(seq).__name__} with {len(seq)} items")

    print("\nProtocol compliance:")
    print("Both implementations work as sequences:")

    original = original_deck.FrenchDeck()
    robust = robust_deck.FrenchDeck()

    process_sequence(original)
    process_sequence(robust)
    process_sequence([1, 2, 3])  # Regular list
    process_sequence("hello")  # String


if __name__ == "__main__":
    """Run all demonstrations."""
    demonstrate_french_deck_differences()
    demonstrate_vector_differences()
    demonstrate_type_annotations()

    print("\n\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("\nOriginal implementations:")
    print("✓ Faithful to Fluent Python examples")
    print("✓ Demonstrate core Python data model concepts")
    print("✓ Minimal, focused code")

    print("\nRobust implementations:")
    print("✓ Comprehensive type safety with mypy support")
    print("✓ Enhanced error handling and validation")
    print("✓ Additional utility methods and functionality")
    print("✓ Immutable data structures where appropriate")
    print("✓ Rich documentation and examples")
    print("✓ Protocol compliance for better interoperability")
    print("✓ Property-based testing support")

    print("\nUse original for: Learning concepts, understanding basics")
    print("Use robust for: Production code, type-safe applications")
