"""
Tests for original Vector implementation.

These tests verify the basic functionality of the original Fluent Python vector example.
"""

from fluent_python.ch01_data_model.original.vector import Vector


class TestOriginalVector:
    """Test cases for the original Vector class."""

    def test_vector_creation(self) -> None:
        """Test basic vector creation."""
        v = Vector(3, 4)
        assert v.x == 3
        assert v.y == 4

        # Test default values
        zero = Vector()
        assert zero.x == 0
        assert zero.y == 0

    def test_vector_repr(self) -> None:
        """Test vector representation."""
        v = Vector(3, 4)
        assert repr(v) == "Vector(3, 4)"

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

        assert result.x == 4
        assert result.y == 5
        assert isinstance(result, Vector)

    def test_vector_multiplication(self) -> None:
        """Test vector scalar multiplication."""
        v = Vector(3, 4)
        result = v * 2

        assert result.x == 6
        assert result.y == 8

        # Test with float
        result_float = v * 2.5
        assert result_float.x == 7.5
        assert result_float.y == 10.0
