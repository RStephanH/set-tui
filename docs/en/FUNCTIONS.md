# Functions & Applications

**Understanding functions as mathematical relations and their properties**

## Table of Contents

1. [What is a Function?](#what-is-a-function)
2. [Function Notation](#function-notation)
3. [Domain, Codomain, and Image](#domain-codomain-and-image)
4. [Function Properties](#function-properties)
5. [Special Functions](#special-functions)

---

## What is a Function?

A **function** (or **application**) f: A → B is a rule that assigns to each element x in A exactly ONE element f(x) in B.

### Key Requirements

1. **Every element in A must map to something** (total function)
2. **Each element in A maps to exactly ONE element in B** (well-defined)
3. **No element in A maps to multiple elements in B**

### Notation

```text
f: A → B
x ↦ f(x)
```

Read as: "f is a function from A to B that sends x to f(x)"

### Representation

Functions can be represented as:

**Ordered pairs:**
```text
f = {(1, 2), (2, 4), (3, 6), (4, 8)}
```

**Table:**
```text
x  | 1  2  3  4
f(x)| 2  4  6  8
```

**Formula:**
```text
f(x) = 2x
```

**Machine analogy:**
```text
Input (x) → [f] → Output (f(x))
```

---

## Function Notation

### Domain & Codomain

```text
f: A → B
```

- **A** = **Domain** (set of all possible inputs)
- **B** = **Codomain** (set where outputs are supposed to come from)
- **f(x)** = the output when input is x

### Examples

**Linear function:**
```text
f: ℝ → ℝ
f(x) = 2x + 1
```

**Squaring function:**
```text
f: ℤ → ℤ
f(x) = x²
```

**Modulo function:**
```text
f: ℤ → {0, 1, 2}
f(x) = x mod 3
```

---

## Domain, Codomain, and Image

### Domain (A)

The set of all possible inputs.

```text
f: A → B
Domain of f = A
```

All elements must have a function value assigned.

### Codomain (B)

The set where outputs are supposed to come from (declared in the function definition).

```text
f: A → B
Codomain of f = B
```

Not all elements of B need to be reached!

### Image (Range)

The set of all actual output values (elements of B that ARE reached).

```text
Image(f) = f(A) = {f(x) | x ∈ A}
```

**Important:** Image(f) ⊆ Codomain(f)

### Example

```text
f: {1, 2, 3} → {1, 4, 9, 16, 25}
f(x) = x²

Domain = {1, 2, 3}
Codomain = {1, 4, 9, 16, 25}
Image = {1, 4, 9}  ← only these are actually reached

Notice: Image ⊂ Codomain (proper subset!)
```

---

## Function Properties

### Injectivity (One-to-One)

**Definition:** A function is **injective** if different inputs always produce different outputs.

```text
f is injective  ⟺  f(x₁) = f(x₂) ⟹ x₁ = x₂

Or equivalently:  x₁ ≠ x₂ ⟹ f(x₁) ≠ f(x₂)
```

**Intuition:** No two elements map to the same output.

**Examples:**

✓ **Injective:**
```text
f: ℝ → ℝ,  f(x) = 2x + 1
If f(x₁) = f(x₂), then 2x₁ + 1 = 2x₂ + 1, so x₁ = x₂
```

✗ **Not injective:**
```text
f: ℝ → ℝ,  f(x) = x²
f(-2) = 4 and f(2) = 4, but -2 ≠ 2
Two different inputs give the same output!
```

### Surjectivity (Onto)

**Definition:** A function is **surjective** if every element in the codomain is reached by at least one input.

```text
f is surjective  ⟺  f(A) = B
                 ⟺  ∀y ∈ B, ∃x ∈ A: f(x) = y
```

**Intuition:** No element in the codomain is "missed."

**Examples:**

✓ **Surjective:**
```text
f: ℤ → {0, 1, 2},  f(x) = x mod 3
Every element {0, 1, 2} is reached:
  f(0) = 0, f(1) = 1, f(2) = 2
```

✗ **Not surjective:**
```text
f: {1, 2, 3} → {1, 4, 9, 16, 25},  f(x) = x²
Image = {1, 4, 9}
Elements 16 and 25 are never reached!
```

### Bijectivity (One-to-One and Onto)

**Definition:** A function is **bijective** if it is both injective AND surjective.

```text
f is bijective  ⟺  f is injective AND f is surjective
```

**Intuition:** A perfect pairing between domain and codomain. Every input maps to a unique output, and every output comes from exactly one input.

**Important consequence:**
```text
If f: A → B is bijective, then |A| = |B|
```

**Example:**

✓ **Bijective:**
```text
f: {1, 2, 3} → {a, b, c}
f(1) = a
f(2) = b
f(3) = c

This is bijective: perfect one-to-one correspondence
```

✓ **Bijective:**
```text
f: ℝ → ℝ,  f(x) = 2x + 1
- Injective: f(x₁) = f(x₂) ⟹ x₁ = x₂ ✓
- Surjective: for any y, we can find x = (y-1)/2 ✓
```

### Summary Table

| Property | Meaning | Example |
|----------|---------|---------|
| **Injective** | Different inputs → different outputs | f(x) = 2x |
| **Surjective** | Every codomain element is reached | f: ℤ → {0,1,2}, f(x)=x%3 |
| **Bijective** | Both injective and surjective | f(x) = 2x + 1 on ℝ → ℝ |

---

## Special Functions

### Identity Function

```text
f: A → A
f(x) = x

Every element maps to itself.
```

**Properties:**
- Always injective
- Always surjective
- Always bijective

### Constant Function

```text
f: A → B
f(x) = c  (for some fixed c ∈ B)

Every element maps to the same output.
```

**Example:**
```text
f: {1, 2, 3} → {5}
f(x) = 5
```

**Properties:**
- Injective only if |A| ≤ 1
- Surjective only if |B| = 1
- Never bijective if |A| > 1

### Composition of Functions

```text
f: A → B
g: B → C
g ∘ f: A → C

(g ∘ f)(x) = g(f(x))
```

Read as: "g circle f" or "g after f"

**Example:**
```text
f: ℝ → ℝ,  f(x) = x + 1
g: ℝ → ℝ,  g(x) = x²

(g ∘ f)(x) = g(f(x)) = g(x+1) = (x+1)²

For x = 2:
f(2) = 3
g(3) = 9
(g ∘ f)(2) = 9 ✓
```

### Inverse Function

A function f has an **inverse** f⁻¹: B → A if and only if f is **bijective**.

```text
f: A → B is bijective
⟹ ∃ f⁻¹: B → A such that:
  f⁻¹(f(x)) = x  for all x ∈ A
  f(f⁻¹(y)) = y  for all y ∈ B
```

**Example:**
```text
f: ℝ → ℝ,  f(x) = 2x + 1
f⁻¹: ℝ → ℝ,  f⁻¹(y) = (y - 1)/2

Check:
f⁻¹(f(3)) = f⁻¹(7) = (7-1)/2 = 3 ✓
f(f⁻¹(5)) = f(2) = 5 ✓
```

---

## Image & Preimage

### Direct Image (Image of a Set)

For S ⊆ A, the **direct image** f(S) is the set of all outputs when inputs come from S.

```text
f(S) = {f(x) | x ∈ S}
```

**Example:**
```text
f: ℝ → ℝ,  f(x) = x²
S = {-2, -1, 0, 1, 2}

f(S) = {0, 1, 4}
Note: f(-2) = f(2) = 4, so 4 appears only once in f(S)
```

### Inverse Image (Preimage)

For T ⊆ B, the **inverse image** (or **preimage**) f⁻¹(T) is the set of all inputs that map to elements in T.

```text
f⁻¹(T) = {x ∈ A | f(x) ∈ T}
```

**Important:** f⁻¹(T) is a SET, not necessarily a function!

**Example:**
```text
f: ℝ → ℝ,  f(x) = x²
T = {4}

f⁻¹({4}) = {-2, 2}
Note: Two different inputs both map to 4!
```

---

## Function Counting

### Number of Functions

The number of different functions from A to B is:

```text
|functions from A to B| = |B|^|A|
```

**Example:**
```text
A = {1, 2},  B = {a, b, c}
Number of functions = 3² = 9

The 9 functions are:
f₁(1)=a, f₁(2)=a
f₂(1)=a, f₂(2)=b
f₃(1)=a, f₃(2)=c
f₄(1)=b, f₄(2)=a
f₅(1)=b, f₅(2)=b
f₆(1)=b, f₆(2)=c
f₇(1)=c, f₇(2)=a
f₈(1)=c, f₈(2)=b
f₉(1)=c, f₉(2)=c
```

### Number of Injective Functions

The number of injective functions from A to B is:

```text
|injective functions| = |B| × (|B|-1) × (|B|-2) × ... × (|B|-|A|+1)
                      = P(|B|, |A|)  (permutation)
```

**Requirement:** |A| ≤ |B|

### Number of Bijective Functions

The number of bijective functions from A to B is:

```text
|bijective functions| = |A|!   (factorial)
```

**Requirement:** |A| = |B|

**Example:**
```text
A = {1, 2, 3},  B = {a, b, c}
Number of bijections = 3! = 6
```

---

**Next Steps:**
- Read [OPERATIONS.md](OPERATIONS.md) for set operation details
- Read [LEARNING_GUIDE.md](LEARNING_GUIDE.md) for practice problems
