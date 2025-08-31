//! 2D Vector implementation in Rust
//! 
//! This module demonstrates Rust's operator overloading capabilities and
//! provides a high-performance 2D vector implementation with full mathematical
//! operations.

use serde::{Deserialize, Serialize};
use std::fmt;
use std::ops::{Add, Mul, Neg, Sub};
use thiserror::Error;

/// Error types for Vector operations
#[derive(Error, Debug, PartialEq)]
pub enum VectorError {
    #[error("Cannot normalize zero vector")]
    ZeroVectorNormalization,
    #[error("Invalid vector operation: {0}")]
    InvalidOperation(String),
}

/// A 2D vector with x and y components
#[derive(Debug, Clone, Copy, PartialEq, Serialize, Deserialize)]
pub struct Vector {
    pub x: f64,
    pub y: f64,
}

impl Vector {
    /// Create a new vector
    pub fn new(x: f64, y: f64) -> Self {
        Self { x, y }
    }

    /// Create a zero vector
    pub fn zero() -> Self {
        Self::new(0.0, 0.0)
    }

    /// Create a unit vector in the x direction
    pub fn unit_x() -> Self {
        Self::new(1.0, 0.0)
    }

    /// Create a unit vector in the y direction
    pub fn unit_y() -> Self {
        Self::new(0.0, 1.0)
    }

    /// Calculate the magnitude (length) of the vector
    pub fn magnitude(self) -> f64 {
        (self.x * self.x + self.y * self.y).sqrt()
    }

    /// Calculate the squared magnitude (avoiding sqrt for performance)
    pub fn magnitude_squared(self) -> f64 {
        self.x * self.x + self.y * self.y
    }

    /// Check if this is a zero vector
    pub fn is_zero(self) -> bool {
        self.x == 0.0 && self.y == 0.0
    }

    /// Normalize the vector to unit length
    pub fn normalized(self) -> Result<Vector, VectorError> {
        let mag = self.magnitude();
        if mag == 0.0 {
            Err(VectorError::ZeroVectorNormalization)
        } else {
            Ok(Vector::new(self.x / mag, self.y / mag))
        }
    }

    /// Calculate dot product with another vector
    pub fn dot(self, other: Vector) -> f64 {
        self.x * other.x + self.y * other.y
    }

    /// Calculate cross product (z-component only for 2D vectors)
    pub fn cross(self, other: Vector) -> f64 {
        self.x * other.y - self.y * other.x
    }

    /// Calculate distance to another vector
    pub fn distance_to(self, other: Vector) -> f64 {
        (other - self).magnitude()
    }

    /// Calculate squared distance to another vector
    pub fn distance_squared_to(self, other: Vector) -> f64 {
        (other - self).magnitude_squared()
    }

    /// Calculate angle with another vector in radians
    pub fn angle_with(self, other: Vector) -> Result<f64, VectorError> {
        let mag_product = self.magnitude() * other.magnitude();
        if mag_product == 0.0 {
            Err(VectorError::InvalidOperation(
                "Cannot calculate angle with zero vector".to_string(),
            ))
        } else {
            Ok((self.dot(other) / mag_product).acos())
        }
    }

    /// Rotate the vector by an angle in radians
    pub fn rotated(self, angle: f64) -> Vector {
        let cos_a = angle.cos();
        let sin_a = angle.sin();
        Vector::new(
            self.x * cos_a - self.y * sin_a,
            self.x * sin_a + self.y * cos_a,
        )
    }

    /// Project this vector onto another vector
    pub fn project_onto(self, other: Vector) -> Result<Vector, VectorError> {
        let other_mag_sq = other.magnitude_squared();
        if other_mag_sq == 0.0 {
            Err(VectorError::InvalidOperation(
                "Cannot project onto zero vector".to_string(),
            ))
        } else {
            let scalar = self.dot(other) / other_mag_sq;
            Ok(other * scalar)
        }
    }

    /// Get the perpendicular vector (rotated 90 degrees counter-clockwise)
    pub fn perpendicular(self) -> Vector {
        Vector::new(-self.y, self.x)
    }

    /// Linear interpolation between this vector and another
    pub fn lerp(self, other: Vector, t: f64) -> Vector {
        self + (other - self) * t
    }

    /// Check if vectors are approximately equal (useful for floating point comparison)
    pub fn approx_eq(self, other: Vector, epsilon: f64) -> bool {
        (self.x - other.x).abs() < epsilon && (self.y - other.y).abs() < epsilon
    }
}

impl fmt::Display for Vector {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Vector({}, {})", self.x, self.y)
    }
}

// Operator overloading implementations

impl Add for Vector {
    type Output = Vector;

    fn add(self, rhs: Vector) -> Vector {
        Vector::new(self.x + rhs.x, self.y + rhs.y)
    }
}

impl Sub for Vector {
    type Output = Vector;

    fn sub(self, rhs: Vector) -> Vector {
        Vector::new(self.x - rhs.x, self.y - rhs.y)
    }
}

impl Mul<f64> for Vector {
    type Output = Vector;

    fn mul(self, scalar: f64) -> Vector {
        Vector::new(self.x * scalar, self.y * scalar)
    }
}

impl Mul<Vector> for f64 {
    type Output = Vector;

    fn mul(self, vector: Vector) -> Vector {
        Vector::new(vector.x * self, vector.y * self)
    }
}

impl Neg for Vector {
    type Output = Vector;

    fn neg(self) -> Vector {
        Vector::new(-self.x, -self.y)
    }
}

impl Default for Vector {
    fn default() -> Self {
        Self::zero()
    }
}

// Additional convenience methods
impl Vector {
    /// Component-wise multiplication (Hadamard product)
    pub fn component_mul(self, other: Vector) -> Vector {
        Vector::new(self.x * other.x, self.y * other.y)
    }

    /// Component-wise division
    pub fn component_div(self, other: Vector) -> Result<Vector, VectorError> {
        if other.x == 0.0 || other.y == 0.0 {
            Err(VectorError::InvalidOperation(
                "Division by zero component".to_string(),
            ))
        } else {
            Ok(Vector::new(self.x / other.x, self.y / other.y))
        }
    }

    /// Get the minimum components
    pub fn min_components(self, other: Vector) -> Vector {
        Vector::new(self.x.min(other.x), self.y.min(other.y))
    }

    /// Get the maximum components
    pub fn max_components(self, other: Vector) -> Vector {
        Vector::new(self.x.max(other.x), self.y.max(other.y))
    }

    /// Clamp vector components between min and max values
    pub fn clamp(self, min: f64, max: f64) -> Vector {
        Vector::new(self.x.clamp(min, max), self.y.clamp(min, max))
    }

    /// Get vector as tuple
    pub fn as_tuple(self) -> (f64, f64) {
        (self.x, self.y)
    }

    /// Create vector from tuple
    pub fn from_tuple(tuple: (f64, f64)) -> Vector {
        Vector::new(tuple.0, tuple.1)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const EPSILON: f64 = 1e-10;

    #[test]
    fn test_vector_creation() {
        let v = Vector::new(3.0, 4.0);
        assert_eq!(v.x, 3.0);
        assert_eq!(v.y, 4.0);
        assert_eq!(v.to_string(), "Vector(3, 4)");
    }

    #[test]
    fn test_vector_magnitude() {
        let v = Vector::new(3.0, 4.0);
        assert_eq!(v.magnitude(), 5.0);
        assert_eq!(v.magnitude_squared(), 25.0);
        
        let zero = Vector::zero();
        assert_eq!(zero.magnitude(), 0.0);
        assert!(zero.is_zero());
    }

    #[test]
    fn test_vector_arithmetic() {
        let v1 = Vector::new(1.0, 2.0);
        let v2 = Vector::new(3.0, 4.0);
        
        assert_eq!(v1 + v2, Vector::new(4.0, 6.0));
        assert_eq!(v2 - v1, Vector::new(2.0, 2.0));
        assert_eq!(v1 * 2.0, Vector::new(2.0, 4.0));
        assert_eq!(2.0 * v1, Vector::new(2.0, 4.0));
        assert_eq!(-v1, Vector::new(-1.0, -2.0));
    }

    #[test]
    fn test_vector_normalization() {
        let v = Vector::new(3.0, 4.0);
        let normalized = v.normalized().unwrap();
        assert!(normalized.magnitude().abs() - 1.0 < EPSILON);
        
        let zero = Vector::zero();
        assert!(zero.normalized().is_err());
    }

    #[test]
    fn test_dot_and_cross_product() {
        let v1 = Vector::new(1.0, 2.0);
        let v2 = Vector::new(3.0, 4.0);
        
        assert_eq!(v1.dot(v2), 11.0); // 1*3 + 2*4 = 11
        assert_eq!(v1.cross(v2), -2.0); // 1*4 - 2*3 = -2
    }

    #[test]
    fn test_distance() {
        let v1 = Vector::new(0.0, 0.0);
        let v2 = Vector::new(3.0, 4.0);
        
        assert_eq!(v1.distance_to(v2), 5.0);
        assert_eq!(v1.distance_squared_to(v2), 25.0);
    }

    #[test]
    fn test_rotation() {
        let v = Vector::new(1.0, 0.0);
        let rotated = v.rotated(std::f64::consts::PI / 2.0); // 90 degrees
        
        assert!(rotated.approx_eq(Vector::new(0.0, 1.0), EPSILON));
    }

    #[test]
    fn test_projection() {
        let v1 = Vector::new(2.0, 3.0);
        let v2 = Vector::new(1.0, 0.0); // Unit vector in x direction
        
        let projected = v1.project_onto(v2).unwrap();
        assert_eq!(projected, Vector::new(2.0, 0.0));
    }

    #[test]
    fn test_perpendicular() {
        let v = Vector::new(1.0, 2.0);
        let perp = v.perpendicular();
        
        assert_eq!(perp, Vector::new(-2.0, 1.0));
        assert_eq!(v.dot(perp), 0.0); // Should be orthogonal
    }

    #[test]
    fn test_lerp() {
        let v1 = Vector::new(0.0, 0.0);
        let v2 = Vector::new(10.0, 20.0);
        
        assert_eq!(v1.lerp(v2, 0.0), v1);
        assert_eq!(v1.lerp(v2, 1.0), v2);
        assert_eq!(v1.lerp(v2, 0.5), Vector::new(5.0, 10.0));
    }

    #[test]
    fn test_component_operations() {
        let v1 = Vector::new(2.0, 3.0);
        let v2 = Vector::new(4.0, 5.0);
        
        assert_eq!(v1.component_mul(v2), Vector::new(8.0, 15.0));
        assert_eq!(v1.component_div(v2).unwrap(), Vector::new(0.5, 0.6));
        
        assert_eq!(v1.min_components(v2), Vector::new(2.0, 3.0));
        assert_eq!(v1.max_components(v2), Vector::new(4.0, 5.0));
    }

    #[test]
    fn test_special_vectors() {
        assert_eq!(Vector::zero(), Vector::new(0.0, 0.0));
        assert_eq!(Vector::unit_x(), Vector::new(1.0, 0.0));
        assert_eq!(Vector::unit_y(), Vector::new(0.0, 1.0));
    }

    #[test]
    fn test_error_cases() {
        let zero = Vector::zero();
        let v = Vector::new(1.0, 2.0);
        
        assert!(zero.normalized().is_err());
        assert!(v.angle_with(zero).is_err());
        assert!(v.project_onto(zero).is_err());
        
        let div_by_zero = Vector::new(1.0, 0.0);
        assert!(v.component_div(div_by_zero).is_err());
    }
}
