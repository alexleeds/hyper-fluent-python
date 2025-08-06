"""
Vector - Enhanced Implementation

This module demonstrates a simple 2D vector class that shows how special methods
make custom objects behave like built-in types.

This follows the Vector example from Fluent Python Chapter 1, enhanced with
robust typing and comprehensive documentation.
"""

from __future__ import annotations

import math
from typing import Any


class Vector:
    """
    A simple 2D vector class demonstrating special methods.

    This implementation shows how to make custom objects work naturally
    with Python operators and built-in functions through special methods.

    Examples:
        >>> v1 = Vector(2, 4)
        >>> v2 = Vector(2, 1)
        >>> v1 + v2
        Vector(4, 5)
        >>> abs(v1)
        4.47213595499958
        >>> v1 * 3
        Vector(6, 12)
        >>> bool(Vector(0, 0))
        False
        >>> bool(v1)
        True
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initialize a 2D vector.

        Args:
            x: X coordinate (default: 0)
            y: Y coordinate (default: 0)
        """
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        """Return developer-friendly representation."""
        return f"Vector({self.x!r}, {self.y!r})"

    def __str__(self) -> str:
        """Return human-readable representation."""
        return f"({self.x}, {self.y})"

    def __abs__(self) -> float:
        """
        Return the magnitude (length) of the vector.

        This enables abs(vector) to work naturally.
        """
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        """
        Return True if vector is non-zero.

        This enables truthiness testing: if vector: ...
        """
        return bool(abs(self))

    def __add__(self, other: Any) -> Vector:
        """
        Add two vectors.

        Args:
            other: Another Vector object

        Returns:
            New Vector with component-wise addition

        Raises:
            TypeError: If other is not a Vector
        """
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: Any) -> Vector:
        """
        Multiply vector by a scalar.

        Args:
            scalar: Numeric scalar value

        Returns:
            New Vector scaled by the scalar

        Raises:
            TypeError: If scalar is not numeric
        """
        if not isinstance(scalar, (int, float)):
            return NotImplemented

        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: Any) -> Vector:
        """
        Right multiplication (scalar * vector).

        This enables expressions like: 3 * vector
        """
        result = self.__mul__(scalar)
        if result is NotImplemented:
            return NotImplemented  # type: ignore[return-value]
        return result

    def __eq__(self, other: Any) -> bool:
        """
        Test equality with another vector.

        Args:
            other: Object to compare with

        Returns:
            True if both components are equal
        """
        if not isinstance(other, Vector):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Any) -> bool:
        """Test inequality with another vector."""
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __hash__(self) -> int:
        """
        Make Vector hashable so it can be used in sets and as dict keys.

        Returns:
            Hash based on both coordinates
        """
        return hash((self.x, self.y))

    # Additional useful methods beyond the basic Fluent Python example

    def dot(self, other: Vector) -> float:
        """
        Calculate dot product with another vector.

        Args:
            other: Another Vector

        Returns:
            Dot product (scalar)
        """
        return self.x * other.x + self.y * other.y

    def angle(self) -> float:
        """
        Return the angle of the vector in radians.

        Returns:
            Angle from positive x-axis in radians
        """
        return math.atan2(self.y, self.x)

    def normalized(self) -> Vector:
        """
        Return a unit vector in the same direction.

        Returns:
            New Vector with magnitude 1

        Raises:
            ValueError: If vector is zero (cannot normalize)
        """
        magnitude = abs(self)
        if magnitude == 0:
            raise ValueError("Cannot normalize zero vector")

        return Vector(self.x / magnitude, self.y / magnitude)

    def distance_to(self, other: Vector) -> float:
        """
        Calculate distance to another vector.

        Args:
            other: Another Vector

        Returns:
            Euclidean distance between vectors
        """
        return abs(self - other)

    def __sub__(self, other: Vector) -> Vector:
        """
        Subtract two vectors.

        Args:
            other: Another Vector

        Returns:
            New Vector with component-wise subtraction
        """
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self) -> Vector:
        """Return negated vector (-self)."""
        return Vector(-self.x, -self.y)

    def __pos__(self) -> Vector:
        """Return positive vector (+self)."""
        return Vector(+self.x, +self.y)


def demonstrate_vector_operations() -> None:
    """Demonstrate various vector operations and special methods."""
    print("=== Vector Operations Demo ===")

    # Create vectors
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    zero = Vector()

    print(f"v1 = {v1!r}")
    print(f"v2 = {v2!r}")
    print(f"zero = {zero!r}")

    # Arithmetic operations
    print("\nArithmetic:")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 3 = {v1 * 3}")
    print(f"3 * v1 = {3 * v1}")

    # Magnitude and normalization
    print("\nMagnitude and normalization:")
    print(f"abs(v1) = {abs(v1)}")
    print(f"v1.normalized() = {v1.normalized()}")
    print(f"abs(v1.normalized()) = {abs(v1.normalized())}")

    # Boolean conversion
    print("\nBoolean conversion:")
    print(f"bool(v1) = {bool(v1)}")
    print(f"bool(zero) = {bool(zero)}")

    # Dot product and angle
    print("\nGeometric operations:")
    print(f"v1.dot(v2) = {v1.dot(v2)}")
    print(f"v1.angle() = {v1.angle():.3f} radians")
    print(f"v1.distance_to(v2) = {v1.distance_to(v2):.3f}")

    # Set operations (thanks to __hash__)
    print("\nSet operations:")
    vectors = {v1, v2, Vector(2, 4), zero}  # Note: Vector(2, 4) == v1
    print(f"Unique vectors: {vectors}")
    print(f"v1 in vectors: {v1 in vectors}")


if __name__ == "__main__":
    # Add debugger breakpoint for interactive exploration
    # breakpoint()  # Uncomment to debug interactively

    demonstrate_vector_operations()
