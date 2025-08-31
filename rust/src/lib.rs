//! Rust ports of Fluent Python exercises.
//! 
//! This crate provides high-performance Rust implementations of the data structures
//! and algorithms from Luciano Ramalho's "Fluent Python" book.

pub mod ch01_data_model;

pub use ch01_data_model::*;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn test_basic_integration() {
        let deck = FrenchDeck::new();
        assert_eq!(deck.len(), 52);
        
        let v1 = Vector::new(3.0, 4.0);
        let v2 = Vector::new(1.0, 2.0);
        let sum = v1 + v2;
        assert_eq!(sum, Vector::new(4.0, 6.0));
    }
}