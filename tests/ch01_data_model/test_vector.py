"""
Tests for Vector implementation from Chapter 1.

Tests cover:
- Vector arithmetic operations
- Special methods behavior
- Geometric operations
- Type safety
"""

import math

import pytest
from hypothesis import given
from hypothesis import strategies as st

from fluent_python.ch01_data_model.robust.vector import (
    Vector,
    demonstrate_vector_operations,
)


class TestVector:
    """Test cases for the Vector class."""

    def test_vector_creation(self) -> None:
        """Test basic vector creation."""
        v = Vector(3, 4)
        assert v.x == 3.0
        assert v.y == 4.0

        # Test default values
        zero = Vector()
        assert zero.x == 0.0
        assert zero.y == 0.0

    def test_vector_repr(self) -> None:
        """Test vector representation."""
        v = Vector(3, 4)
        assert repr(v) == "Vector(3.0, 4.0)"

    def test_vector_str(self) -> None:
        """Test vector string representation."""
        v = Vector(3, 4)
        assert str(v) == "(3.0, 4.0)"

    def test_vector_abs(self) -> None:
        """Test vector magnitude calculation."""
        v = Vector(3, 4)
        assert abs(v) == 5.0

        v = Vector(0, 0)
        assert abs(v) == 0.0

    def test_vector_bool(self) -> None:
        """Test vector truthiness."""
        v = Vector(3, 4)
        assert bool(v) is True

        zero = Vector(0, 0)
        assert bool(zero) is False

    def test_vector_addition(self) -> None:
        """Test vector addition."""
        v1 = Vector(2, 4)
        v2 = Vector(2, 1)
        result = v1 + v2

        assert result.x == 4.0
        assert result.y == 5.0
        assert isinstance(result, Vector)

    def test_vector_addition_type_error(self) -> None:
        """Test vector addition with invalid type."""
        v = Vector(1, 2)
        with pytest.raises(TypeError):
            v + "invalid"

    def test_vector_subtraction(self) -> None:
        """Test vector subtraction."""
        v1 = Vector(5, 7)
        v2 = Vector(2, 3)
        result = v1 - v2

        assert result.x == 3.0
        assert result.y == 4.0

    def test_vector_multiplication(self) -> None:
        """Test vector scalar multiplication."""
        v = Vector(3, 4)
        result = v * 2

        assert result.x == 6.0
        assert result.y == 8.0

        # Test with float
        result_float = v * 2.5
        assert result_float.x == 7.5
        assert result_float.y == 10.0

    def test_vector_rmul(self) -> None:
        """Test right multiplication (scalar * vector)."""
        v = Vector(3, 4)
        result = 2 * v

        assert result.x == 6.0
        assert result.y == 8.0

    def test_vector_multiplication_type_error(self) -> None:
        """Test vector multiplication with invalid type."""
        v = Vector(1, 2)
        with pytest.raises(TypeError):
            v * "invalid"

    def test_vector_equality(self) -> None:
        """Test vector equality."""
        v1 = Vector(3, 4)
        v2 = Vector(3, 4)
        v3 = Vector(1, 2)

        assert v1 == v2
        assert v1 != v3
        assert not (v1 != v2)

    def test_vector_equality_with_different_type(self) -> None:
        """Test vector equality with different type."""
        v = Vector(1, 2)
        result = v == "not a vector"
        assert result is False

    def test_vector_hash(self) -> None:
        """Test vector hashing."""
        v1 = Vector(3, 4)
        v2 = Vector(3, 4)
        v3 = Vector(1, 2)

        # Equal vectors have same hash
        assert hash(v1) == hash(v2)

        # Can be used in sets
        vector_set = {v1, v2, v3}
        assert len(vector_set) == 2  # v1 and v2 are the same
        assert v1 in vector_set

    def test_vector_negation(self) -> None:
        """Test vector negation."""
        v = Vector(3, 4)
        neg_v = -v

        assert neg_v.x == -3.0
        assert neg_v.y == -4.0

    def test_vector_positive(self) -> None:
        """Test unary positive."""
        v = Vector(3, 4)
        pos_v = +v

        assert pos_v.x == 3.0
        assert pos_v.y == 4.0
        assert pos_v is not v  # Should be a new instance

    def test_vector_dot_product(self) -> None:
        """Test dot product calculation."""
        v1 = Vector(3, 4)
        v2 = Vector(2, 1)

        result = v1.dot(v2)
        assert result == 10.0  # 3*2 + 4*1

    def test_vector_angle(self) -> None:
        """Test angle calculation."""
        v = Vector(1, 0)  # Points along positive x-axis
        assert v.angle() == 0.0

        v = Vector(0, 1)  # Points along positive y-axis
        assert abs(v.angle() - math.pi / 2) < 1e-10

        v = Vector(-1, 0)  # Points along negative x-axis
        assert abs(abs(v.angle()) - math.pi) < 1e-10

    def test_vector_normalization(self) -> None:
        """Test vector normalization."""
        v = Vector(3, 4)
        normalized = v.normalized()

        # Should have magnitude 1
        assert abs(abs(normalized) - 1.0) < 1e-10

        # Should point in same direction
        assert abs(normalized.x - 0.6) < 1e-10
        assert abs(normalized.y - 0.8) < 1e-10

    def test_vector_normalization_zero_vector(self) -> None:
        """Test normalization of zero vector raises error."""
        zero = Vector(0, 0)
        with pytest.raises(ValueError, match="Cannot normalize zero vector"):
            zero.normalized()

    def test_vector_distance(self) -> None:
        """Test distance calculation between vectors."""
        v1 = Vector(0, 0)
        v2 = Vector(3, 4)

        distance = v1.distance_to(v2)
        assert distance == 5.0

        # Distance should be symmetric
        assert v2.distance_to(v1) == distance

    @given(
        x1=st.floats(
            min_value=-100, max_value=100, allow_nan=False, allow_infinity=False
        ),
        y1=st.floats(
            min_value=-100, max_value=100, allow_nan=False, allow_infinity=False
        ),
        x2=st.floats(
            min_value=-100, max_value=100, allow_nan=False, allow_infinity=False
        ),
        y2=st.floats(
            min_value=-100, max_value=100, allow_nan=False, allow_infinity=False
        ),
    )
    def test_vector_addition_commutative(
        self, x1: float, y1: float, x2: float, y2: float
    ) -> None:
        """Property test: vector addition is commutative."""
        v1 = Vector(x1, y1)
        v2 = Vector(x2, y2)

        assert v1 + v2 == v2 + v1

    @given(
        x=st.floats(
            min_value=-100, max_value=100, allow_nan=False, allow_infinity=False
        ),
        y=st.floats(
            min_value=-100, max_value=100, allow_nan=False, allow_infinity=False
        ),
        scalar=st.floats(
            min_value=-10, max_value=10, allow_nan=False, allow_infinity=False
        ),
    )
    def test_vector_multiplication_properties(
        self, x: float, y: float, scalar: float
    ) -> None:
        """Property test: scalar multiplication properties."""
        v = Vector(x, y)

        # Multiplication by 1 gives same vector
        assert v * 1 == v

        # Multiplication is commutative
        assert v * scalar == scalar * v

        # Multiplication by 0 gives zero vector
        zero_result = v * 0
        assert zero_result == Vector(0, 0)

    @given(
        x=st.floats(
            min_value=0.1, max_value=100, allow_nan=False, allow_infinity=False
        ),
        y=st.floats(
            min_value=0.1, max_value=100, allow_nan=False, allow_infinity=False
        ),
    )
    def test_vector_normalization_property(self, x: float, y: float) -> None:
        """Property test: normalization produces unit vector."""
        v = Vector(x, y)
        normalized = v.normalized()

        # Magnitude should be 1 (within floating point precision)
        assert abs(abs(normalized) - 1.0) < 1e-10


class TestVectorEdgeCases:
    """Test edge cases and error conditions."""

    def test_very_small_vectors(self) -> None:
        """Test vectors with very small components."""
        v = Vector(1e-10, 1e-10)
        assert v.x == 1e-10
        assert v.y == 1e-10
        assert abs(v) > 0

    def test_vector_operations_preserve_type(self) -> None:
        """Test that operations return Vector instances."""
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)

        assert isinstance(v1 + v2, Vector)
        assert isinstance(v1 - v2, Vector)
        assert isinstance(v1 * 2, Vector)
        assert isinstance(2 * v1, Vector)
        assert isinstance(-v1, Vector)
        assert isinstance(+v1, Vector)


class TestDemonstration:
    """Test the demonstration function."""

    def test_demonstrate_vector_operations_runs(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Test that the demonstration function runs without error."""
        demonstrate_vector_operations()

        captured = capsys.readouterr()
        assert "Vector Operations Demo" in captured.out
        assert "Arithmetic:" in captured.out
        assert "Magnitude and normalization:" in captured.out
