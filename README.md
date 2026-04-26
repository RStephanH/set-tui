# Set-TUI 🎯

**A Terminal User Interface for Interactive Set Theory & Mathematical Learning**

Set-TUI is an educational mathematics application designed to teach and practice **set theory**, **functions**, and **discrete mathematics concepts** through an interactive terminal-based interface. It's built with Python and leverages the Textual framework for a rich TUI experience.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Mathematical Concepts](#mathematical-concepts)
- [Core Operations](#core-operations)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Interactive Set Operations**: Perform basic and advanced set operations (union, intersection, difference, symmetric difference, cartesian product)
- **Set Comprehension**: Build sets using mathematical predicates (e.g., "x % 2 == 0" for even numbers)
- **Functions & Applications**: Construct functions `f: A → B` and analyze their properties
  - Test **injectivity** (one-to-one)
  - Test **surjectivity** (onto)
  - Test **bijectivity** (one-to-one and onto)
- **Advanced Set Theory**: Compute power sets, complements, direct/inverse images
- **Data Persistence**: Save and load your work with JSON-based storage
- **Educational Interface**: Clean TUI designed for learning mathematics concepts
- **Mathematical Notation**: Display results using proper mathematical symbols (∪, ∩, ⊆, etc.)

## 📦 Installation

### Requirements
- Python ≥ 3.14
- `textual` ≥ 8.1.1

### Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd set-tui
   ```

2. **Install dependencies** (using `uv` package manager)
   ```bash
   uv sync
   ```

   Or with pip:
   ```bash
   pip install textual>=8.1.1
   ```

## 🚀 Quick Start

Run the application:
```bash
python main.py
```

This launches the interactive TUI where you can:
1. Define sets A and B
2. Perform operations between sets
3. Define and analyze functions
4. View operation results with mathematical notation
5. Save your work to `data.json`

## 📂 Project Structure

```
set-tui/
├── main.py                 # Entry point
├── pyproject.toml         # Project configuration & dependencies
├── data.json              # Persistent storage (sets & history)
├── README.md              # This file
├── core/
│   ├── models.py          # Data models (not yet implemented)
│   └── operations.py      # All set theory & function operations
├── ui/
│   └── app.py             # Textual TUI application
├── storage/
│   └── json_store.py      # JSON persistence layer
└── docs/                  # Mathematical documentation (multilingual)
    ├── en/                # English documentation
    │   ├── SET_THEORY.md      # Foundations of set theory
    │   ├── FUNCTIONS.md       # Function theory & properties
    │   ├── OPERATIONS.md      # Set operations guide
    │   └── LEARNING_GUIDE.md  # How to use for learning
    └── fr/                # French documentation (Français)
        ├── SET_THEORY.md      # Fondements de la théorie des ensembles
        ├── FUNCTIONS.md       # Théorie des fonctions et propriétés
        ├── OPERATIONS.md      # Guide des opérations sur les ensembles
        └── LEARNING_GUIDE.md  # Guide d'apprentissage
```

## 🧮 Mathematical Concepts

Set-TUI implements core concepts from discrete mathematics and set theory:

### Set Operations
- **Union** (A ∪ B): All elements in A or B
- **Intersection** (A ∩ B): Common elements
- **Difference** (A \ B): Elements in A but not B
- **Symmetric Difference** (A △ B): Elements in either but not both
- **Cartesian Product** (A × B): All ordered pairs
- **Complement** (Ā): Elements not in A

### Function Analysis
- **Injectivity**: Each output maps to exactly one input (one-to-one)
- **Surjectivity**: Every element in codomain is mapped to (onto)
- **Bijectivity**: Both injective and surjective (perfect correspondence)
- **Image & Preimage**: Direct and inverse mappings

### Set Theory Foundations
- **Cardinality**: Counting elements in a set
- **Subset Relations**: ⊆, ⊂, ⊃
- **Power Set**: P(A) = all subsets of A
- **Set Comprehension**: {x ∈ E | P(x)} - building sets by conditions
- **Disjoint Sets**: Sets with no common elements

For detailed explanations, see the [docs/](docs/) folder.

## 🔧 Core Operations

All operations are implemented in `core/operations.py`:

### Basic Operations
```python
from core.operations import union, intersection, difference

A = {1, 2, 3}
B = {3, 4, 5}

union(A, B)              # {1, 2, 3, 4, 5}
intersection(A, B)       # {3}
difference(A, B)         # {1, 2}
```

### Functions
```python
from core.operations import build_function, is_injective, is_bijective

f = build_function({1, 2, 3}, "x ** 2")  # f(x) = x²
is_injective(f)
is_bijective(f, {1, 4, 9})
```

### Set Comprehension
```python
from core.operations import build_set_by_comprehension, build_universe

universe = build_universe(1, 20)
evens = build_set_by_comprehension(universe, "x % 2 == 0")
# evens = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
```

## 📚 Documentation

Comprehensive mathematical documentation is available in the `docs/` folder in multiple languages:

### English (English)
- **[SET_THEORY.md](docs/en/SET_THEORY.md)** - Foundations, axioms, and basic definitions
- **[FUNCTIONS.md](docs/en/FUNCTIONS.md)** - Function theory, properties, and classifications
- **[OPERATIONS.md](docs/en/OPERATIONS.md)** - Detailed guide to all set operations
- **[LEARNING_GUIDE.md](docs/en/LEARNING_GUIDE.md)** - How to use this project for learning

### Français (French)
- **[SET_THEORY.md](docs/fr/SET_THEORY.md)** - Fondements, axiomes et définitions de base
- **[FUNCTIONS.md](docs/fr/FUNCTIONS.md)** - Théorie des fonctions, propriétés et classifications
- **[OPERATIONS.md](docs/fr/OPERATIONS.md)** - Guide détaillé de toutes les opérations sur les ensembles
- **[LEARNING_GUIDE.md](docs/fr/LEARNING_GUIDE.md)** - Comment utiliser ce projet pour apprendre

## 🤝 Contributing

Contributions are welcome! Here are some areas for improvement:

- Additional function properties (monotonicity, periodicity, etc.)
- More advanced set operations (quotient sets, partitions)
- Graphical representations of functions and sets
- Enhanced TUI with more visualization options
- Unit tests and benchmarks

## 📄 License

This project is open source. See LICENSE file for details.

---

**Built for mathematical learning and AI education** 🧠✨
