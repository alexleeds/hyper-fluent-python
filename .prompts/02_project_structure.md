# Fluent Python Project Structure

Date: 2025-01-08

## Directory Organization

This project follows a systematic structure that scales across all chapters of Fluent Python:

```
hyper-fluent-python/
├── .prompts/                    # Learning plans and project documentation
│   ├── 00_fluent_python_learning_plan.md
│   ├── 02_project_structure.md  # This file
│   └── 03_debugging_guide.md    # Debugging methodology
├── src/fluent_python/
│   ├── ch01_data_model/
│   │   ├── original/            # Classic Fluent Python implementations
│   │   ├── robust/              # Enhanced with Robust Python typing
│   │   ├── exercises/           # Debugging and exploration scripts
│   │   ├── extensions/          # AI-generated creative extensions
│   │   └── comparison.py        # Side-by-side analysis
│   ├── ch02_sequences/          # Chapter 2: Data Structures
│   ├── ch03_dictionaries/       # Chapter 3: Dictionaries and Sets
│   └── ...                     # Pattern continues for all chapters
├── tests/                       # Comprehensive test suite
├── notebooks/                   # Jupyter notebooks for exploration
├── rust/                        # Rust implementations for comparison
├── benchmarks/                  # Performance analysis scripts
└── docs/                        # Documentation and insights
```

## Chapter Structure Pattern

Each chapter follows this consistent pattern:

### Source Code Organization
```
src/fluent_python/chXX_topic/
├── __init__.py                  # Public API exports
├── original/                    # Original Fluent Python code
│   ├── __init__.py
│   ├── example1.py              # Direct from book
│   └── example2.py
├── robust/                      # Enhanced implementations
│   ├── __init__.py
│   ├── example1.py              # With full typing
│   └── example2.py
├── exercises/                   # Interactive debugging scripts
│   ├── __init__.py
│   ├── debug_example1.py        # Step-through debugging
│   ├── debug_example2.py
│   └── compare_implementations.py
├── extensions/                  # Creative AI-generated extensions
│   ├── __init__.py
│   ├── advanced_example1.py     # Push boundaries of concepts
│   └── edge_cases.py            # Corner cases and stress tests
└── comparison.py                # Chapter-level analysis
```

### Debugging Scripts Location
- **exercises/** directory contains all interactive debugging scripts
- **Naming convention**: `debug_{example_name}.py`
- Each script focuses on one core concept
- Scripts include comprehensive breakpoints and exploration points

### Benefits of This Structure

1. **Scalability**: Easy to add new chapters following the same pattern
2. **Clarity**: Clear separation between original, enhanced, and extension code
3. **Debugging Focus**: Dedicated exercises/ directory for learning scripts
4. **AI Integration**: Designated space for AI-generated extensions
5. **Testing**: Parallel test structure mirrors source organization
6. **Performance**: Rust comparisons organized by chapter

## File Naming Conventions

### Debugging Scripts
- `debug_{concept}.py` - Interactive debugging for core concepts
- `explore_{feature}.py` - Deep dives into specific features  
- `compare_{aspect}.py` - Side-by-side comparisons

### Implementation Files
- Original: Keep names from Fluent Python book
- Robust: Same names with enhanced typing
- Extensions: Descriptive names indicating the enhancement

### Test Files
- `test_{implementation_file}.py` - Standard tests
- `test_original_{concept}.py` - Tests for original implementations
- `bench_{concept}.py` - Performance benchmarks

## Documentation Strategy

### .prompts/ Directory
- Learning methodology and reflection
- Project evolution notes
- AI prompt logs for reproducibility

### notebooks/ Directory  
- Interactive exploration notebooks
- Chapter walkthroughs with rich output
- Comparison analyses with visualizations

### docs/ Directory
- Generated documentation
- Performance comparison reports
- Insights and learnings summary
