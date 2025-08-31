//! Demo of the Rust implementations
//! 
//! Run with: cargo run --example demo

use fluent_python_rs::*;

fn main() {
    println!("🦀 Rust Implementation of Fluent Python Chapter 1\n");
    
    demo_french_deck();
    println!();
    demo_vector();
}

fn demo_french_deck() {
    println!("=== French Deck Demo ===");
    
    // Create a new deck
    let mut deck = FrenchDeck::new();
    println!("Created deck with {} cards", deck.len());
    
    // Show first few cards
    println!("First 5 cards:");
    for i in 0..5 {
        println!("  {}: {}", i, deck[i]);
    }
    
    // Test slicing
    let first_three = deck.slice(0..3);
    println!("\nFirst 3 cards: {:?}", first_three);
    
    // Find highest card
    if let Some(highest) = deck.highest_card() {
        println!("Highest card: {}", highest);
    }
    
    // Get all spades
    let spades = deck.cards_by_suit(Suit::Spades);
    println!("Number of spades: {}", spades.len());
    println!("First spade: {}", spades[0]);
    println!("Last spade: {}", spades[spades.len() - 1]);
    
    // Shuffle and show effect
    println!("\nBefore shuffle: {} {}", deck[0], deck[1]);
    deck.shuffle();
    println!("After shuffle:  {} {}", deck[0], deck[1]);
    
    // Test spades-high ranking
    let ace_spades = Card::new(Rank::Ace, Suit::Spades);
    let ace_clubs = Card::new(Rank::Ace, Suit::Clubs);
    let spades_rank = spades_high_rank(&ace_spades);
    let clubs_rank = spades_high_rank(&ace_clubs);
    
    println!("\nSpades-high ranking:");
    println!("  {} rank: {:?}", ace_spades, spades_rank);
    println!("  {} rank: {:?}", ace_clubs, clubs_rank);
    println!("  Spades higher: {}", spades_rank > clubs_rank);
}

fn demo_vector() {
    println!("=== Vector Demo ===");
    
    // Create vectors
    let v1 = Vector::new(3.0, 4.0);
    let v2 = Vector::new(1.0, 2.0);
    
    println!("v1 = {}", v1);
    println!("v2 = {}", v2);
    
    // Basic arithmetic
    println!("\nArithmetic:");
    println!("v1 + v2 = {}", v1 + v2);
    println!("v1 - v2 = {}", v1 - v2);
    println!("v1 * 2.0 = {}", v1 * 2.0);
    println!("-v1 = {}", -v1);
    
    // Magnitude and normalization
    println!("\nMagnitude and normalization:");
    println!("||v1|| = {}", v1.magnitude());
    if let Ok(normalized) = v1.normalized() {
        println!("v1 normalized = {}", normalized);
        println!("||normalized|| = {:.6}", normalized.magnitude());
    }
    
    // Dot and cross products
    println!("\nProducts:");
    println!("v1 · v2 = {}", v1.dot(v2));
    println!("v1 × v2 = {}", v1.cross(v2));
    
    // Distance
    println!("\nDistance:");
    println!("distance(v1, v2) = {}", v1.distance_to(v2));
    
    // Advanced operations
    println!("\nAdvanced operations:");
    println!("v1 perpendicular = {}", v1.perpendicular());
    
    if let Ok(angle) = v1.angle_with(v2) {
        println!("angle between v1 and v2 = {:.3} radians", angle);
    }
    
    if let Ok(projection) = v1.project_onto(Vector::unit_x()) {
        println!("v1 projected onto x-axis = {}", projection);
    }
    
    // Lerp
    let lerped = v1.lerp(v2, 0.5);
    println!("lerp(v1, v2, 0.5) = {}", lerped);
    
    // Component operations
    println!("\nComponent operations:");
    println!("v1 ⊙ v2 (component mul) = {}", v1.component_mul(v2));
    println!("min(v1, v2) = {}", v1.min_components(v2));
    println!("max(v1, v2) = {}", v1.max_components(v2));
    
    // Error handling demo
    println!("\nError handling:");
    let zero = Vector::zero();
    match zero.normalized() {
        Ok(_) => println!("Zero vector normalized (shouldn't happen)"),
        Err(e) => println!("Zero vector normalization error: {}", e),
    }
}
