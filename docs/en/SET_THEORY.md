# Set Theory Foundations

**A comprehensive guide to the mathematical foundations of Set-TUI**

## Table of Contents

1. [What is a Set?](#what-is-a-set)
2. [Set Notation](#set-notation)
3. [Basic Definitions](#basic-definitions)
4. [Set Relations](#set-relations)
5. [Fundamental Properties](#fundamental-properties)
6. [Empty Set & Universal Set](#empty-set--universal-set)

---

## What is a Set?

A **set** is a well-defined collection of distinct objects (called **elements** or **members**).

### Key Characteristics

1. **Distinct**: No duplicates. {1, 2, 2, 3} = {1, 2, 3}
2. **Unordered**: {1, 2, 3} = {3, 1, 2}
3. **Well-defined**: It must be clear whether an element belongs to the set or not

### Examples

- **Natural numbers**: ℕ = {0, 1, 2, 3, ...}
- **Integers**: ℤ = {..., -2, -1, 0, 1, 2, ...}
- **Real numbers**: ℝ = all decimal numbers
- **Finite set**: A = {a, e, i, o, u} (vowels)

---

## Set Notation

### Listing Elements (Explicit Form)
```
A = {1, 2, 3, 4, 5}
B = {apple, orange, banana}
C = {red, green, blue}
```

### Set Builder Notation (Implicit Form)
```
A = {x | x is a positive integer less than 6}
B = {x ∈ ℕ | x is even}
C = {x ∈ ℝ | x² < 10}
```

Read as: "A is the set of all x such that..."

### Membership
- `x ∈ A` : x is an element of A (x belongs to A)
- `x ∉ A` : x is not an element of A

### Cardinality
- `|A|` : the number of elements in A (cardinality of A)

**Example:**
```
A = {1, 2, 3}
|A| = 3

B = {}
|B| = 0  (empty set)

C = {a, b, c, d, e}
|C| = 5
```

---

## Basic Definitions

### Subset
**A ⊆ B** (A is a subset of B)

Every element of A is also in B.

```
A ⊆ B  ⟺  ∀x: (x ∈ A ⟹ x ∈ B)
```

**Examples:**
- {1, 2} ⊆ {1, 2, 3}  ✓ TRUE
- {1, 4} ⊆ {1, 2, 3}  ✗ FALSE
- A ⊆ A for any set A (reflexive property)
- ∅ ⊆ A for any set A (empty set is subset of everything)

### Proper Subset
**A ⊂ B** (A is a proper subset of B)

A ⊆ B AND A ≠ B (A is strictly smaller than B)

```
A ⊂ B  ⟺  (A ⊆ B  ∧  A ≠ B)
```

**Examples:**
- {1, 2} ⊂ {1, 2, 3}  ✓ TRUE (proper subset)
- {1, 2, 3} ⊂ {1, 2, 3}  ✗ FALSE (equal, not proper)

### Equal Sets
**A = B** (A equals B)

A and B have exactly the same elements.

```
A = B  ⟺  (A ⊆ B  ∧  B ⊆ A)
```

---

## Set Relations

### Disjoint Sets
**A ∩ B = ∅** (A and B are disjoint)

Two sets are disjoint if they have no elements in common.

**Example:**
```
A = {1, 2, 3}
B = {4, 5, 6}
A ∩ B = ∅  → disjoint ✓
```

### Overlapping Sets
Two sets overlap if they share at least one element.

**Example:**
```
A = {1, 2, 3}
B = {3, 4, 5}
A ∩ B = {3}  → overlapping ✓
```

---

## Fundamental Properties

### De Morgan's Laws

For sets A, B, and universal set U:

1. **(A ∪ B)' = A' ∩ B'**
   - The complement of a union equals the intersection of complements

2. **(A ∩ B)' = A' ∪ B'**
   - The complement of an intersection equals the union of complements

### Distributive Laws

1. **A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)**
   - Union distributes over intersection

2. **A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)**
   - Intersection distributes over union

### Commutative Laws
- **A ∪ B = B ∪ A**
- **A ∩ B = B ∩ A**

### Associative Laws
- **(A ∪ B) ∪ C = A ∪ (B ∪ C)**
- **(A ∩ B) ∩ C = A ∩ (B ∩ C)**

### Idempotent Laws
- **A ∪ A = A**
- **A ∩ A = A**

---

## Empty Set & Universal Set

### Empty Set (∅)

The set containing no elements.

```
∅ = {} = {x | x ≠ x}
|∅| = 0
```

**Properties:**
- ∅ ⊆ A for any set A
- ∅ ∪ A = A
- ∅ ∩ A = ∅
- ∅' = U (complement of empty set is universal set)

### Universal Set (U)

The set containing all elements under consideration in a particular context.

**Example:**
If we're working with digits:
```
U = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

If we're working with letters:
```
U = {a, b, c, ..., z}
```

**Properties:**
- A ⊆ U for any set A in the context
- A ∪ U = U
- A ∩ U = A
- A ∪ A' = U
- A ∩ A' = ∅

---

## Key Takeaways

1. **Sets are unordered, distinct collections**
2. **Subset notation is fundamental** (A ⊆ B)
3. **Set operations follow algebraic laws** (commutative, associative, distributive)
4. **The empty set is special** (subset of everything)
5. **Cardinality measures set size** (|A| = number of elements)

---

**Next Steps:**
- Read [OPERATIONS.md](OPERATIONS.md) to learn all set operations
- Read [FUNCTIONS.md](FUNCTIONS.md) to understand functions between sets
- Read [LEARNING_GUIDE.md](LEARNING_GUIDE.md) for exercises
