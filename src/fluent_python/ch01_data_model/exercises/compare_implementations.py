#!/usr/bin/env python3
"""
Comprehensive comparison of original vs. robust FrenchDeck implementations.

This script provides side-by-side analysis of the design differences,
performance characteristics, and type safety improvements.
"""

import sys
import timeit
from pathlib import Path

# Add the project root to Python path for imports
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root / "src"))

# Import both implementations  # noqa: E402
from fluent_python.ch01_data_model.original.french_deck import (  # noqa: E402
    Card as OriginalCard,
)
from fluent_python.ch01_data_model.original.french_deck import (  # noqa: E402
    FrenchDeck as OriginalDeck,
)
from fluent_python.ch01_data_model.robust.french_deck import (  # noqa: E402
    Card as RobustCard,
)
from fluent_python.ch01_data_model.robust.french_deck import FrenchDeck as RobustDeck  # noqa: E402
from fluent_python.ch01_data_model.robust.french_deck import (  # noqa: E402
    Rank,
    Suit,
    cards_by_suit,
    high_card,
)

# Rich for beautiful output
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table

    # from rich.columns import Columns  # Unused
    # from rich.pretty import pprint  # Unused
    console = Console()
    RICH_AVAILABLE = True
except ImportError:
    console = None
    RICH_AVAILABLE = False
    print("Install 'rich' for enhanced output: pip install rich")


def compare_card_implementations() -> None:
    """Compare Card implementations between original and robust versions."""
    if RICH_AVAILABLE:
        console.print(Panel.fit("🃏 Card Implementation Comparison", style="bold blue"))
    else:
        print("=== Card Implementation Comparison ===")

    # Create sample cards
    original_card = OriginalCard("A", "spades")
    robust_card = RobustCard(Rank.ACE, Suit.SPADES)

    breakpoint()  # 🔍 DEBUG POINT 1: Examine card structures

    # Comparison data
    comparisons = [
        ("Data Structure", "namedtuple", "@dataclass(frozen=True, order=True)"),
        ("Rank Type", "str", "Rank(Enum)"),
        ("Suit Type", "str", "Suit(Enum)"),
        ("Immutable", "✓ (namedtuple)", "✓ (@frozen)"),
        ("Ordered", "✗", "✓ (order=True)"),
        ("Type Safety", "Runtime only", "Development + Runtime"),
        (
            "Memory",
            f"{sys.getsizeof(original_card)} bytes",
            f"{sys.getsizeof(robust_card)} bytes",
        ),
        ("Fields Access", "card.rank, card[0]", "card.rank"),
        (
            "Comparison",
            "Not supported",
            f"ace > king: {robust_card > RobustCard(Rank.KING, Suit.HEARTS)}",
        ),
    ]

    if RICH_AVAILABLE:
        table = Table(title="Card Implementation Details")
        table.add_column("Feature", style="cyan")
        table.add_column("Original", style="magenta")
        table.add_column("Robust", style="green")

        for feature, original, robust in comparisons:
            table.add_row(feature, original, robust)
        console.print(table)
    else:
        print(f"{'Feature':<20} {'Original':<25} {'Robust':<30}")
        print("-" * 75)
        for feature, original, robust in comparisons:
            print(f"{feature:<20} {original:<25} {robust:<30}")

    # Test error handling
    print("\n=== Error Handling Comparison ===")
    breakpoint()  # 🔍 DEBUG POINT 2: Test error behavior

    # Original accepts any strings
    invalid_original = OriginalCard("invalid_rank", "invalid_suit")
    print(f"Original with invalid data: {invalid_original}")

    # Robust version would fail type checking (but let's show runtime behavior)
    try:
        # This would be caught by mypy at development time
        invalid_robust = RobustCard("invalid_rank", "invalid_suit")  # type: ignore
        print(f"Robust with invalid data: {invalid_robust}")
    except Exception as e:
        print(f"Robust version runtime error: {type(e).__name__}: {e}")


def compare_deck_implementations() -> None:
    """Compare FrenchDeck implementations."""
    if RICH_AVAILABLE:
        console.print(
            Panel.fit("🎴 Deck Implementation Comparison", style="bold green")
        )
    else:
        print("\n=== Deck Implementation Comparison ===")

    # Create decks
    original_deck = OriginalDeck()
    robust_deck = RobustDeck()

    breakpoint()  # 🔍 DEBUG POINT 3: Examine deck structures

    # Basic functionality comparison
    print("=== Basic Functionality ===")
    print(f"Original deck length: {len(original_deck)}")
    print(f"Robust deck length: {len(robust_deck)}")
    print(f"Original first card: {original_deck[0]}")
    print(f"Robust first card: {robust_deck[0]}")

    # Slicing behavior
    original_slice = original_deck[:3]
    robust_slice = robust_deck[:3]

    print("\nSlicing returns:")
    print(f"Original: {type(original_slice)} = {original_slice}")
    print(f"Robust: {type(robust_slice)} = {robust_slice}")

    breakpoint()  # 🔍 DEBUG POINT 4: Compare slicing behavior

    # Enhanced methods available only in robust version
    print("\n=== Enhanced Methods (Robust Only) ===")
    try:
        spades = cards_by_suit(robust_deck, Suit.SPADES)
        print(f"Spades in deck: {len(spades)}")

        sample_cards = [robust_deck[0], robust_deck[13], robust_deck[26]]
        highest = high_card(sample_cards)
        print(f"Highest card from sample: {highest}")

        # Deck manipulation
        robust_deck.shuffle()
        print("Deck shuffled successfully")

        robust_deck.sort(by_suit=True)
        print("Deck sorted by suit")

    except Exception as e:
        print(f"Error in enhanced methods: {e}")


def performance_comparison() -> None:
    """Compare performance characteristics."""
    if RICH_AVAILABLE:
        console.print(Panel.fit("🏃 Performance Comparison", style="bold yellow"))
    else:
        print("\n=== Performance Comparison ===")

    breakpoint()  # 🔍 DEBUG POINT 5: Performance analysis

    # Deck creation time
    original_time = timeit.timeit(lambda: OriginalDeck(), number=1000)
    robust_time = timeit.timeit(lambda: RobustDeck(), number=1000)

    # Card creation time
    original_card_time = timeit.timeit(
        lambda: OriginalCard("A", "spades"), number=10000
    )
    robust_card_time = timeit.timeit(
        lambda: RobustCard(Rank.ACE, Suit.SPADES), number=10000
    )

    # Card access time
    orig_deck = OriginalDeck()
    rob_deck = RobustDeck()

    orig_access_time = timeit.timeit(lambda: orig_deck[25], number=100000)
    rob_access_time = timeit.timeit(lambda: rob_deck[25], number=100000)

    # Memory usage
    import sys

    orig_deck_memory = sys.getsizeof(orig_deck._cards) + sum(
        sys.getsizeof(card) for card in orig_deck._cards
    )
    rob_deck_memory = sys.getsizeof(rob_deck._cards) + sum(
        sys.getsizeof(card) for card in rob_deck._cards
    )

    if RICH_AVAILABLE:
        perf_table = Table(title="Performance Metrics")
        perf_table.add_column("Operation", style="cyan")
        perf_table.add_column("Original", style="magenta")
        perf_table.add_column("Robust", style="green")
        perf_table.add_column("Overhead", style="red")

        operations = [
            (
                "Deck creation (1k)",
                f"{original_time:.4f}s",
                f"{robust_time:.4f}s",
                f"{((robust_time - original_time) / original_time * 100):+.1f}%",
            ),
            (
                "Card creation (10k)",
                f"{original_card_time:.4f}s",
                f"{robust_card_time:.4f}s",
                f"{((robust_card_time - original_card_time) / original_card_time * 100):+.1f}%",
            ),
            (
                "Card access (100k)",
                f"{orig_access_time:.4f}s",
                f"{rob_access_time:.4f}s",
                f"{((rob_access_time - orig_access_time) / orig_access_time * 100):+.1f}%",
            ),
            (
                "Memory usage",
                f"{orig_deck_memory:,} bytes",
                f"{rob_deck_memory:,} bytes",
                f"{((rob_deck_memory - orig_deck_memory) / orig_deck_memory * 100):+.1f}%",
            ),
        ]

        for op, orig, robust, overhead in operations:
            perf_table.add_row(op, orig, robust, overhead)
        console.print(perf_table)
    else:
        print(f"{'Operation':<20} {'Original':<15} {'Robust':<15} {'Overhead':<10}")
        print("-" * 65)
        operations = [
            (
                "Deck creation (1k)",
                f"{original_time:.4f}s",
                f"{robust_time:.4f}s",
                f"{((robust_time - original_time) / original_time * 100):+.1f}%",
            ),
            (
                "Card creation (10k)",
                f"{original_card_time:.4f}s",
                f"{robust_card_time:.4f}s",
                f"{((robust_card_time - original_card_time) / original_card_time * 100):+.1f}%",
            ),
            (
                "Card access (100k)",
                f"{orig_access_time:.4f}s",
                f"{rob_access_time:.4f}s",
                f"{((rob_access_time - orig_access_time) / orig_access_time * 100):+.1f}%",
            ),
            (
                "Memory usage",
                f"{orig_deck_memory:,} bytes",
                f"{rob_deck_memory:,} bytes",
                f"{((rob_deck_memory - orig_deck_memory) / orig_deck_memory * 100):+.1f}%",
            ),
        ]
        for op, orig, robust, overhead in operations:
            print(f"{op:<20} {orig:<15} {robust:<15} {overhead:<10}")


def type_safety_demonstration() -> None:
    """Demonstrate type safety improvements."""
    if RICH_AVAILABLE:
        console.print(Panel.fit("🛡️ Type Safety Demonstration", style="bold red"))
    else:
        print("\n=== Type Safety Demonstration ===")

    breakpoint()  # 🔍 DEBUG POINT 6: Type safety analysis

    print("=== IDE and MyPy Benefits ===")
    print("The robust implementation provides:")
    print("1. Autocomplete for enum values: Rank.ACE, Suit.SPADES")
    print("2. Type checking catches errors before runtime")
    print("3. Better error messages with specific types")
    print("4. Protocol compliance verification")

    print("\n=== Error Quality Comparison ===")

    # Demonstrate error message quality
    try:
        # This works in original but shouldn't
        original_bad = OriginalCard(123, None)  # type: ignore
        print(f"Original accepts invalid types: {original_bad}")
    except Exception as e:
        print(f"Original error: {e}")

    try:
        # This fails appropriately in robust version
        robust_bad = RobustCard(123, None)  # type: ignore
        print(f"Robust unexpectedly accepted: {robust_bad}")
    except Exception as e:
        print(f"Robust error (better): {type(e).__name__}: {e}")


def main() -> None:
    """Run comprehensive comparison of implementations."""
    if RICH_AVAILABLE:
        console.print(
            Panel.fit(
                "Fluent Python Chapter 1: Implementation Comparison\n"
                "Original vs. Robust French Deck Analysis",
                style="bold blue",
            )
        )
    else:
        print("=== Fluent Python Chapter 1: Implementation Comparison ===")
        print("Original vs. Robust French Deck Analysis")

    print(
        """
    🐛 DEBUGGING INSTRUCTIONS:
    
    This script has 6 debug points for systematic exploration:
    
    1. Card structure comparison
    2. Error handling differences  
    3. Deck implementation details
    4. Slicing and method behavior
    5. Performance characteristics
    6. Type safety demonstrations
    
    At each breakpoint, explore:
    - Variable values with 'p' and 'pp'
    - Object attributes with 'dir(obj)'
    - Type information with 'type(obj)'
    - Help with 'help(obj)'
    """
    )

    try:
        compare_card_implementations()
        compare_deck_implementations()
        performance_comparison()
        type_safety_demonstration()

        print("\n=== Summary of Key Differences ===")
        print("✅ Robust implementation provides:")
        print("  - Type safety at development time")
        print("  - Better error messages")
        print("  - Enhanced functionality")
        print("  - Protocol compliance")
        print("  - Immutability guarantees")
        print("  - Ordering support")

        print("\n⚖️ Trade-offs:")
        print("  - Slightly higher memory usage")
        print("  - Minor performance overhead")
        print("  - More complex code structure")
        print("  - Better long-term maintainability")

    except KeyboardInterrupt:
        print("\n\nDebugging session interrupted.")
    except Exception as e:
        print(f"\nUnexpected error: {type(e).__name__}: {e}")
        if RICH_AVAILABLE:
            console.print_exception()


if __name__ == "__main__":
    main()
