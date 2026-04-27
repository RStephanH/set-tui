# Set Operations Guide

**Complete reference for all set operations implemented in Set-TUI**

## Table of Contents

1. [Basic Operations](#basic-operations)
2. [Advanced Operations](#advanced-operations)
3. [Cardinality](#cardinality)
4. [Set Comprehension](#set-comprehension)
5. [Properties & Laws](#properties--laws)

---

## Basic Operations

In this document, we use the convention **ℕ = {0, 1, 2, 3, ...}**.

### Union (A ∪ B)

**Definition:** The set of all elements that are in A, in B, or in both.

```text
A ∪ B = {x | x ∈ A  OR  x ∈ B}
```

**Example:**
```text
A = {1, 2, 3}
B = {3, 4, 5}
A ∪ B = {1, 2, 3, 4, 5}
```

**Properties:**
- Commutative: A ∪ B = B ∪ A
- Associative: (A ∪ B) ∪ C = A ∪ (B ∪ C)
- Idempotent: A ∪ A = A
- Identity: A ∪ ∅ = A

### Intersection (A ∩ B)

**Definition:** The set of all elements that are in BOTH A and B.

```text
A ∩ B = {x | x ∈ A  AND  x ∈ B}
```

**Example:**
```text
A = {1, 2, 3}
B = {3, 4, 5}
A ∩ B = {3}
```

**Properties:**
- Commutative: A ∩ B = B ∩ A
- Associative: (A ∩ B) ∩ C = A ∩ (B ∩ C)
- Idempotent: A ∩ A = A
- Identity: A ∩ U = A (U = universal set)
- Annihilation: A ∩ ∅ = ∅

**Note on Disjoint Sets:**
```text
If A ∩ B = ∅, then A and B are DISJOINT (no common elements)
```

### Difference (A \ B)

**Definition:** The set of all elements in A that are NOT in B.

```text
A \ B = {x | x ∈ A  AND  x ∉ B}
```

**Example:**
```text
A = {1, 2, 3}
B = {3, 4, 5}
A \ B = {1, 2}
B \ A = {4, 5}
```

**Important:** Difference is NOT commutative!
```text
A \ B ≠ B \ A  (in general)
```

**Properties:**
- A \ A = ∅
- A \ ∅ = A
- ∅ \ A = ∅

### Symmetric Difference (A △ B)

**Definition:** The set of all elements in A or B, but NOT in both.

```text
A △ B = (A \ B) ∪ (B \ A)
      = (A ∪ B) \ (A ∩ B)
```

**Example:**
```text
A = {1, 2, 3}
B = {3, 4, 5}
A △ B = {1, 2, 4, 5}
```

**Properties:**
- Commutative: A △ B = B △ A
- Associative: (A △ B) △ C = A △ (B △ C)
- Identity: A △ ∅ = A

---

## Advanced Operations

### Complement (A' or Ā)

**Definition:** The set of all elements in the universal set U that are NOT in A.

```text
A' = U \ A = {x ∈ U | x ∉ A}
```

**Requires:** A ⊆ U (A must be a subset of the universe)

**Example:**
```text
U = {1, 2, 3, 4, 5}
A = {2, 4}
A' = {1, 3, 5}
```

**Properties:**
- Double complement: (A')' = A
- Complement of universal: U' = ∅
- Complement of empty: ∅' = U
- Union with complement: A ∪ A' = U
- Intersection with complement: A ∩ A' = ∅

**De Morgan's Laws:**
- (A ∪ B)' = A' ∩ B'
- (A ∩ B)' = A' ∪ B'

### Cartesian Product (A × B)

**Definition:** The set of all ordered pairs (a, b) where a ∈ A and b ∈ B.

```text
A × B = {(a, b) | a ∈ A  AND  b ∈ B}
```

**Important:** Order matters!
- (a, b) ≠ (b, a) unless a = b
- A × B ≠ B × A (in general)

**Example:**
```text
A = {1, 2}
B = {a, b}
A × B = {(1,a), (1,b), (2,a), (2,b)}
```

**Cardinality:**
```text
|A × B| = |A| × |B|
```

If |A| = 2 and |B| = 2, then |A × B| = 4

**Properties:**
- A × ∅ = ∅
- ∅ × A = ∅
- Distributive: A × (B ∪ C) = (A × B) ∪ (A × C)

### Power Set (P(A))

**Definition:** The set of ALL subsets of A.

```text
P(A) = {S | S ⊆ A}
```

**Example:**
```text
A = {1, 2}
P(A) = {∅, {1}, {2}, {1,2}}
|P(A)| = 4 = 2²
```

**Cardinality Formula:**
```text
|P(A)| = 2^|A|
```

**Example Cardinalities:**
- |A| = 0  →  |P(A)| = 2⁰ = 1
- |A| = 1  →  |P(A)| = 2¹ = 2
- |A| = 2  →  |P(A)| = 2² = 4
- |A| = 3  →  |P(A)| = 2³ = 8
- |A| = 10 →  |P(A)| = 2¹⁰ = 1024

**⚠️ Warning:** Power sets grow exponentially, making enumeration quickly impractical for moderately large sets (e.g., around |A| ≈ 20 or more).

---

## Cardinality

**Definition:** The cardinality |A| is the number of elements in set A.

```text
|A| = number of elements in A
```

**Examples:**
```text
|{1, 2, 3}| = 3
|{a, b, c, d, e}| = 5
|∅| = 0
```

### Cardinality of Operations

**Union (with overlap):**
```text
|A ∪ B| = |A| + |B| - |A ∩ B|
```

**Intersection:**
```text
|A ∩ B| ≤ min(|A|, |B|)
```

**Difference:**
```text
|A \ B| = |A| - |A ∩ B|
```

**Cartesian Product:**
```text
|A × B| = |A| × |B|
```

**Power Set:**
```text
|P(A)| = 2^|A|
```

---

## Set Comprehension

**Definition:** Building a set by specifying a condition that elements must satisfy.

```text
A = {x ∈ U | P(x)}
```

Read as: "A is the set of all x in U such that P(x) is true"

### Examples

**Even numbers up to 10:**
```text
A = {x ∈ {1,2,...,10} | x is even}
A = {2, 4, 6, 8, 10}
```

**Squares less than 100:**
```text
B = {x ∈ ℕ | x² < 100}
B = {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
```

**Numbers divisible by 3:**
```text
C = {x ∈ {1,...,20} | x % 3 == 0}
C = {3, 6, 9, 12, 15, 18}
```

### Using Set-TUI

In Set-TUI, you can build sets by comprehension with Python expressions:

```python
# Predicate examples:
"x % 2 == 0"           # even numbers
"x > 5 and x < 10"    # 5 < x < 10
"x ** 2 < 50"          # x² < 50
"x % 3 == 0"           # multiples of 3
"abs(x) <= 5"          # |x| ≤ 5
```

---

## Properties & Laws

### Commutative Laws
```text
A ∪ B = B ∪ A
A ∩ B = B ∩ A
A △ B = B △ A
```

### Associative Laws
```text
(A ∪ B) ∪ C = A ∪ (B ∪ C)
(A ∩ B) ∩ C = A ∩ (B ∩ C)
(A △ B) △ C = A △ (B △ C)
```

### Distributive Laws
```text
A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
A × (B ∪ C) = (A × B) ∪ (A × C)
```

### De Morgan's Laws
```text
(A ∪ B)' = A' ∩ B'
(A ∩ B)' = A' ∪ B'
```

### Idempotent Laws
```text
A ∪ A = A
A ∩ A = A
A △ A = ∅
```

### Identity Laws
```text
A ∪ ∅ = A
A ∩ U = A
A △ ∅ = A
```

### Complement Laws
```text
A ∪ A' = U
A ∩ A' = ∅
(A')' = A
U' = ∅
∅' = U
```

---

**Next Steps:**
- Read [FUNCTIONS.md](FUNCTIONS.md) to learn about functions
- Read [LEARNING_GUIDE.md](LEARNING_GUIDE.md) for practice exercises
