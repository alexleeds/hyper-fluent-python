# Getting Started with Fluent Python Debugging

## Quick Overview

This project implements a systematic approach to learning Fluent Python with enhanced typing and interactive debugging. Every concept is explored through three lenses:

1. **Original Implementation** - Classic Fluent Python code
2. **Robust Implementation** - Enhanced with strong typing
3. **Interactive Debugging** - Step-through exploration with strategic breakpoints

## Project Structure

```
hyper-fluent-python/
├── .prompts/                           # Learning methodology & guides
│   ├── 00_fluent_python_learning_plan.md   # Overall learning strategy  
│   ├── 02_project_structure.md             # Directory organization
│   ├── debugging_complete_guide.md         # Complete debugging reference
│   └── getting_started.md                  # This file
├── src/fluent_python/
│   └── ch01_data_model/
│       ├── original/                       # Classic Fluent Python
│       ├── robust/                         # Enhanced with typing
│       └── exercises/                      # Interactive debugging scripts
├── tests/                                  # Comprehensive test suite
├── notebooks/                              # Jupyter explorations
└── rust/                                   # Rust comparisons
```

## Getting Started - Chapter 1

### 1. Understand the Concepts
Read about Python's data model in Fluent Python Chapter 1, focusing on how `__len__` and `__getitem__` make objects sequence-like.

### 2. Explore the Implementations

#### Original Implementation
```bash
# Look at the classic code
cat src/fluent_python/ch01_data_model/original/french_deck.py
```

#### Robust Implementation  
```bash
# See the enhanced version
cat src/fluent_python/ch01_data_model/robust/french_deck.py
```

### 3. Interactive Debugging

#### Step Through Original Implementation
```bash
cd /path/to/hyper-fluent-python
python -m fluent_python.ch01_data_model.exercises.debug_original
```

**At each breakpoint, try:**
- `p deck` - See the deck object
- `p deck._cards[:3]` - Look at the first few cards
- `type(deck[0])` - Check card type
- `dir(deck)` - See available methods

#### Explore Robust Implementation
```bash
python -m fluent_python.ch01_data_model.exercises.debug_robust
```

**Focus on:**
- Enum types: `p Rank.ACE`, `p Suit.SPADES`
- Dataclass features: `p card.__dataclass_fields__`
- Type safety: Try creating invalid cards
- Enhanced methods: `deck.shuffle()`, `deck.sort()`

#### Compare Side-by-Side
```bash
python -m fluent_python.ch01_data_model.exercises.compare_implementations
```

**Observe:**
- Performance differences
- Error handling improvements
- Type safety benefits
- Memory usage

### 4. Run Tests
```bash
python -m pytest tests/ch01_data_model/ -v
```

### 5. Explore in Jupyter
```bash
jupyter lab notebooks/ch01_french_deck_debugging.ipynb
```

## Essential Debugging Commands

| Command | Purpose |
|---------|---------|
| `l` | List current code |
| `n` | Next line |
| `s` | Step into function |
| `c` | Continue to next breakpoint |
| `p var` | Print variable |
| `pp var` | Pretty print |
| `dir(obj)` | Show object methods |
| `q` | Quit debugger |

## Key Learning Points

### Original Implementation
- How Python's data model works
- namedtuple capabilities
- Sequence protocol basics
- Minimal but powerful design

### Robust Implementation  
- Type safety with enums and dataclasses
- Enhanced error messages
- Protocol compliance
- Better maintainability

### Comparative Analysis
- Performance trade-offs
- Development experience improvements
- Long-term maintenance benefits

## Next Steps

1. **Master Chapter 1** using the debugging scripts
2. **Create extensions** - try building your own card games
3. **Explore Rust** implementations for performance comparison
4. **Move to Chapter 2** following the same methodology

## Getting Help

- **Complete debugging guide**: `.prompts/debugging_guide.md`
- **Project structure**: `.prompts/02_project_structure.md`
- **Learning plan**: `.prompts/00_fluent_python_learning_plan.md`

## Quick Troubleshooting

**Import errors?**
```bash
# Ensure you're in project root
cd /path/to/hyper-fluent-python

# Run as module
python -m fluent_python.ch01_data_model.exercises.debug_original
```

**Debugger not starting?**
- Check that `breakpoint()` calls are uncommented
- Ensure you're in an interactive terminal

**Missing dependencies?**
```bash
pip install -e ".[dev]"
pip install rich ipython  # For enhanced output
```

---

Happy debugging! The goal is to understand Python deeply through systematic exploration of both classic and modern implementations.
