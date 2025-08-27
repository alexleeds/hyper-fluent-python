"""
Chapter 1: Python Data Model

This module provides both the original Fluent Python examples and robust,
type-safe implementations demonstrating the Python data model.

Use:
- fluent_python.ch01_data_model.original - Original book examples
- fluent_python.ch01_data_model.robust - Enhanced, typed implementations
"""

# Re-export robust implementations as the default
from .robust.french_deck import Card, FrenchDeck, Rank, Suit
from .robust.vector import Vector

__all__ = [
    "Card",
    "FrenchDeck",
    "Rank",
    "Suit",
    "Vector",
]
