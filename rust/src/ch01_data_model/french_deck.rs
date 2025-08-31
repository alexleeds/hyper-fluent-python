//! French Deck implementation in Rust
//! 
//! This module demonstrates Rust's powerful enum system and trait implementations
//! to create a type-safe, memory-efficient playing card deck.

use rand::seq::SliceRandom;
use rand::thread_rng;
use serde::{Deserialize, Serialize};
use std::fmt;

/// Card suits with explicit ordering for comparison
#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Serialize, Deserialize)]
pub enum Suit {
    Spades = 1,
    Hearts = 2,
    Diamonds = 3,
    Clubs = 4,
}

impl Suit {
    /// Iterator over all suits in order
    pub fn all() -> impl Iterator<Item = Suit> {
        [Suit::Spades, Suit::Hearts, Suit::Diamonds, Suit::Clubs]
            .iter()
            .copied()
    }
}

impl fmt::Display for Suit {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Suit::Spades => write!(f, "Spades"),
            Suit::Hearts => write!(f, "Hearts"), 
            Suit::Diamonds => write!(f, "Diamonds"),
            Suit::Clubs => write!(f, "Clubs"),
        }
    }
}

/// Card ranks with values for comparison and high/low Ace support
#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Serialize, Deserialize)]
pub enum Rank {
    Two = 2,
    Three = 3,
    Four = 4,
    Five = 5,
    Six = 6,
    Seven = 7,
    Eight = 8,
    Nine = 9,
    Ten = 10,
    Jack = 11,
    Queen = 12,
    King = 13,
    Ace = 14,
}

impl Rank {
    /// Iterator over all ranks in order
    pub fn all() -> impl Iterator<Item = Rank> {
        [
            Rank::Two, Rank::Three, Rank::Four, Rank::Five,
            Rank::Six, Rank::Seven, Rank::Eight, Rank::Nine,
            Rank::Ten, Rank::Jack, Rank::Queen, Rank::King, Rank::Ace,
        ]
        .iter()
        .copied()
    }

    /// Get numeric value for the rank
    pub fn value(self) -> u8 {
        self as u8
    }
}

impl fmt::Display for Rank {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Rank::Two => write!(f, "2"),
            Rank::Three => write!(f, "3"),
            Rank::Four => write!(f, "4"),
            Rank::Five => write!(f, "5"),
            Rank::Six => write!(f, "6"),
            Rank::Seven => write!(f, "7"),
            Rank::Eight => write!(f, "8"),
            Rank::Nine => write!(f, "9"),
            Rank::Ten => write!(f, "10"),
            Rank::Jack => write!(f, "Jack"),
            Rank::Queen => write!(f, "Queen"),
            Rank::King => write!(f, "King"),
            Rank::Ace => write!(f, "Ace"),
        }
    }
}

/// A playing card with rank and suit
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub struct Card {
    pub rank: Rank,
    pub suit: Suit,
}

impl Card {
    /// Create a new card
    pub fn new(rank: Rank, suit: Suit) -> Self {
        Self { rank, suit }
    }

    /// Get the card's rank value for comparison
    pub fn rank_value(self) -> u8 {
        self.rank.value()
    }

    /// Get the card's suit value for comparison  
    pub fn suit_value(self) -> u8 {
        self.suit as u8
    }
}

impl fmt::Display for Card {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{} of {}", self.rank, self.suit)
    }
}

impl PartialOrd for Card {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Card {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        // Compare by rank first, then by suit
        self.rank.cmp(&other.rank).then(self.suit.cmp(&other.suit))
    }
}

/// A French deck of 52 playing cards
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct FrenchDeck {
    cards: Vec<Card>,
}

impl FrenchDeck {
    /// Create a new deck of 52 cards in standard order
    pub fn new() -> Self {
        let mut cards = Vec::with_capacity(52);
        
        for suit in Suit::all() {
            for rank in Rank::all() {
                cards.push(Card::new(rank, suit));
            }
        }
        
        Self { cards }
    }

    /// Get the number of cards in the deck
    pub fn len(&self) -> usize {
        self.cards.len()
    }

    /// Check if the deck is empty
    pub fn is_empty(&self) -> bool {
        self.cards.is_empty()
    }

    /// Get a card by index
    pub fn get(&self, index: usize) -> Option<&Card> {
        self.cards.get(index)
    }

    /// Get a slice of cards
    pub fn slice(&self, range: std::ops::Range<usize>) -> &[Card] {
        &self.cards[range]
    }

    /// Shuffle the deck in place
    pub fn shuffle(&mut self) {
        let mut rng = thread_rng();
        self.cards.shuffle(&mut rng);
    }

    /// Get all cards of a specific suit
    pub fn cards_by_suit(&self, suit: Suit) -> Vec<&Card> {
        self.cards.iter().filter(|card| card.suit == suit).collect()
    }

    /// Find the highest card by rank
    pub fn highest_card(&self) -> Option<&Card> {
        self.cards.iter().max_by_key(|card| card.rank_value())
    }

    /// Sort cards by rank (high to low by default, or custom function)
    pub fn sort_by_rank(&mut self, reverse: bool) {
        if reverse {
            self.cards.sort_by(|a, b| b.rank.cmp(&a.rank));
        } else {
            self.cards.sort_by(|a, b| a.rank.cmp(&b.rank));
        }
    }

    /// Get an iterator over the cards
    pub fn iter(&self) -> std::slice::Iter<'_, Card> {
        self.cards.iter()
    }

    /// Get a mutable iterator over the cards
    pub fn iter_mut(&mut self) -> std::slice::IterMut<'_, Card> {
        self.cards.iter_mut()
    }

    /// Convert to vector (consumes the deck)
    pub fn into_vec(self) -> Vec<Card> {
        self.cards
    }
}

impl Default for FrenchDeck {
    fn default() -> Self {
        Self::new()
    }
}

/// Index access for deck[index]
impl std::ops::Index<usize> for FrenchDeck {
    type Output = Card;

    fn index(&self, index: usize) -> &Self::Output {
        &self.cards[index]
    }
}

/// Iteration support
impl IntoIterator for FrenchDeck {
    type Item = Card;
    type IntoIter = std::vec::IntoIter<Card>;

    fn into_iter(self) -> Self::IntoIter {
        self.cards.into_iter()
    }
}

impl<'a> IntoIterator for &'a FrenchDeck {
    type Item = &'a Card;
    type IntoIter = std::slice::Iter<'a, Card>;

    fn into_iter(self) -> Self::IntoIter {
        self.cards.iter()
    }
}

impl<'a> IntoIterator for &'a mut FrenchDeck {
    type Item = &'a mut Card;
    type IntoIter = std::slice::IterMut<'a, Card>;

    fn into_iter(self) -> Self::IntoIter {
        self.cards.iter_mut()
    }
}

/// Ranking function for spades-high ordering (like in the Python example)
pub fn spades_high_rank(card: &Card) -> (u8, u8) {
    // Return (rank_value, suit_priority) where spades = highest priority
    let suit_priority = match card.suit {
        Suit::Spades => 4,
        Suit::Hearts => 3,
        Suit::Diamonds => 2,
        Suit::Clubs => 1,
    };
    (card.rank_value(), suit_priority)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_card_creation() {
        let card = Card::new(Rank::Ace, Suit::Spades);
        assert_eq!(card.rank, Rank::Ace);
        assert_eq!(card.suit, Suit::Spades);
        assert_eq!(card.to_string(), "Ace of Spades");
    }

    #[test]
    fn test_card_comparison() {
        let ace_spades = Card::new(Rank::Ace, Suit::Spades);
        let king_hearts = Card::new(Rank::King, Suit::Hearts);
        
        assert!(ace_spades > king_hearts);
        assert_eq!(ace_spades.rank_value(), 14);
        assert_eq!(king_hearts.rank_value(), 13);
    }

    #[test]
    fn test_deck_creation() {
        let deck = FrenchDeck::new();
        assert_eq!(deck.len(), 52);
        assert!(!deck.is_empty());
        
        // First card should be 2 of Spades
        assert_eq!(deck[0], Card::new(Rank::Two, Suit::Spades));
        
        // Last card should be Ace of Clubs
        assert_eq!(deck[51], Card::new(Rank::Ace, Suit::Clubs));
    }

    #[test]
    fn test_deck_indexing() {
        let deck = FrenchDeck::new();
        let first_card = deck.get(0).unwrap();
        assert_eq!(*first_card, Card::new(Rank::Two, Suit::Spades));
        
        assert!(deck.get(52).is_none()); // Out of bounds
    }

    #[test]
    fn test_deck_iteration() {
        let deck = FrenchDeck::new();
        let mut count = 0;
        
        for _card in &deck {
            count += 1;
        }
        
        assert_eq!(count, 52);
    }

    #[test]
    fn test_cards_by_suit() {
        let deck = FrenchDeck::new();
        let spades = deck.cards_by_suit(Suit::Spades);
        assert_eq!(spades.len(), 13);
        
        for card in spades {
            assert_eq!(card.suit, Suit::Spades);
        }
    }

    #[test]
    fn test_shuffle() {
        let mut deck1 = FrenchDeck::new();
        let deck2 = deck1.clone();
        
        deck1.shuffle();
        
        // Very unlikely (but not impossible) that shuffle produces same order
        // This test might occasionally fail, but demonstrates shuffle works
        assert_ne!(deck1.cards, deck2.cards);
    }

    #[test]
    fn test_spades_high_ranking() {
        let ace_spades = Card::new(Rank::Ace, Suit::Spades);
        let ace_clubs = Card::new(Rank::Ace, Suit::Clubs);
        
        let spades_rank = spades_high_rank(&ace_spades);
        let clubs_rank = spades_high_rank(&ace_clubs);
        
        assert!(spades_rank > clubs_rank);
        assert_eq!(spades_rank.0, clubs_rank.0); // Same rank value
        assert!(spades_rank.1 > clubs_rank.1);   // Different suit priority
    }
}
