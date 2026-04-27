# Guide des Opérations sur les Ensembles

**Référence complète de toutes les opérations sur les ensembles implémentées dans Set-TUI**

## Table des matières

1. [Opérations de base](#opérations-de-base)
2. [Opérations avancées](#opérations-avancées)
3. [Cardinalité](#cardinalité)
4. [Compréhension d'ensembles](#compréhension-densembles)
5. [Propriétés et lois](#propriétés-et-lois)

---

## Opérations de base

Dans ce document, nous utilisons la convention **ℕ = {0, 1, 2, 3, ...}**.

### Union (A ∪ B)

**Définition:** L'ensemble de tous les éléments qui sont dans A, dans B, ou dans les deux.

```text
A ∪ B = {x | x ∈ A  OU  x ∈ B}
```

**Exemple:**
```text
A = {1, 2, 3}
B = {3, 4, 5}
A ∪ B = {1, 2, 3, 4, 5}
```

**Propriétés:**
- Commutative: A ∪ B = B ∪ A
- Associative: (A ∪ B) ∪ C = A ∪ (B ∪ C)
- Idempotente: A ∪ A = A
- Identité: A ∪ ∅ = A

### Intersection (A ∩ B)

**Définition:** L'ensemble de tous les éléments qui sont dans A ET dans B.

```text
A ∩ B = {x | x ∈ A  ET  x ∈ B}
```

**Exemple:**
```text
A = {1, 2, 3}
B = {3, 4, 5}
A ∩ B = {3}
```

**Propriétés:**
- Commutative: A ∩ B = B ∩ A
- Associative: (A ∩ B) ∩ C = A ∩ (B ∩ C)
- Idempotente: A ∩ A = A
- Identité: A ∩ U = A (U = ensemble universel)
- Annihilation: A ∩ ∅ = ∅

**Remarque sur les ensembles disjoints:**
```text
Si A ∩ B = ∅, alors A et B sont DISJOINTS (aucun élément commun)
```

### Différence (A \ B)

**Définition:** L'ensemble de tous les éléments de A qui ne sont PAS dans B.

```text
A \ B = {x | x ∈ A  ET  x ∉ B}
```

**Exemple:**
```text
A = {1, 2, 3}
B = {3, 4, 5}
A \ B = {1, 2}
B \ A = {4, 5}
```

**Important:** La différence n'est PAS commutative!
```text
A \ B ≠ B \ A  (en général)
```

**Propriétés:**
- A \ A = ∅
- A \ ∅ = A
- ∅ \ A = ∅

### Différence symétrique (A △ B)

**Définition:** L'ensemble de tous les éléments dans A ou B, mais PAS dans les deux.

```text
A △ B = (A \ B) ∪ (B \ A)
      = (A ∪ B) \ (A ∩ B)
```

**Exemple:**
```text
A = {1, 2, 3}
B = {3, 4, 5}
A △ B = {1, 2, 4, 5}
```

**Propriétés:**
- Commutative: A △ B = B △ A
- Associative: (A △ B) △ C = A △ (B △ C)
- Identité: A △ ∅ = A

---

## Opérations avancées

### Complémentaire (A' ou Ā)

**Définition:** L'ensemble de tous les éléments de l'ensemble universel U qui ne sont PAS dans A.

```text
A' = U \ A = {x ∈ U | x ∉ A}
```

**Requiert:** A ⊆ U (A doit être un sous-ensemble de l'univers)

**Exemple:**
```text
U = {1, 2, 3, 4, 5}
A = {2, 4}
A' = {1, 3, 5}
```

**Propriétés:**
- Double complémentaire: (A')' = A
- Complémentaire de l'universel: U' = ∅
- Complémentaire du vide: ∅' = U
- Union avec complémentaire: A ∪ A' = U
- Intersection avec complémentaire: A ∩ A' = ∅

**Lois de De Morgan:**
- (A ∪ B)' = A' ∩ B'
- (A ∩ B)' = A' ∪ B'

### Produit cartésien (A × B)

**Définition:** L'ensemble de toutes les paires ordonnées (a, b) où a ∈ A et b ∈ B.

```text
A × B = {(a, b) | a ∈ A  ET  b ∈ B}
```

**Important:** L'ordre compte!
- (a, b) ≠ (b, a) sauf si a = b
- A × B ≠ B × A (en général)

**Exemple:**
```text
A = {1, 2}
B = {a, b}
A × B = {(1,a), (1,b), (2,a), (2,b)}
```

**Cardinalité:**
```text
|A × B| = |A| × |B|
```

Si |A| = 2 et |B| = 2, alors |A × B| = 4

**Propriétés:**
- A × ∅ = ∅
- ∅ × A = ∅
- Distributive: A × (B ∪ C) = (A × B) ∪ (A × C)

### Ensemble des parties (P(A))

**Définition:** L'ensemble de TOUS les sous-ensembles de A.

```text
P(A) = {S | S ⊆ A}
```

**Exemple:**
```text
A = {1, 2}
P(A) = {∅, {1}, {2}, {1,2}}
|P(A)| = 4 = 2²
```

**Formule de cardinalité:**
```text
|P(A)| = 2^|A|
```

**Exemples de cardinalités:**
- |A| = 0  →  |P(A)| = 2⁰ = 1
- |A| = 1  →  |P(A)| = 2¹ = 2
- |A| = 2  →  |P(A)| = 2² = 4
- |A| = 3  →  |P(A)| = 2³ = 8
- |A| = 10 →  |P(A)| = 2¹⁰ = 1024

**⚠️ Attention:** Les ensembles des parties croissent exponentiellement, ce qui rend leur énumération rapidement peu pratique pour des ensembles de taille modérée (par exemple autour de |A| ≈ 20 ou plus).

---

## Cardinalité

**Définition:** La cardinalité |A| est le nombre d'éléments dans l'ensemble A.

```text
|A| = nombre d'éléments de A
```

**Exemples:**
```text
|{1, 2, 3}| = 3
|{a, b, c, d, e}| = 5
|∅| = 0
```

### Cardinalité des opérations

**Union (avec chevauchement):**
```text
|A ∪ B| = |A| + |B| - |A ∩ B|
```

**Intersection:**
```text
|A ∩ B| ≤ min(|A|, |B|)
```

**Différence:**
```text
|A \ B| = |A| - |A ∩ B|
```

**Produit cartésien:**
```text
|A × B| = |A| × |B|
```

**Ensemble des parties:**
```text
|P(A)| = 2^|A|
```

---

## Compréhension d'ensembles

**Définition:** Construire un ensemble en spécifiant une condition que les éléments doivent satisfaire.

```text
A = {x ∈ U | P(x)}
```

Lire comme: "A est l'ensemble de tous les x dans U tels que P(x) soit vrai"

### Exemples

**Nombres pairs jusqu'à 10:**
```text
A = {x ∈ {1,2,...,10} | x est pair}
A = {2, 4, 6, 8, 10}
```

**Carrés inférieurs à 100:**
```text
B = {x ∈ ℕ | x² < 100}
B = {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
```

**Nombres divisibles par 3:**
```text
C = {x ∈ {1,...,20} | x % 3 == 0}
C = {3, 6, 9, 12, 15, 18}
```

### Utilisation dans Set-TUI

Dans Set-TUI, vous pouvez construire des ensembles par compréhension avec des expressions Python:

```python
# Exemples de prédicats:
"x % 2 == 0"           # nombres pairs
"x > 5 and x < 10"    # 5 < x < 10
"x ** 2 < 50"          # x² < 50
"x % 3 == 0"           # multiples de 3
"abs(x) <= 5"          # |x| ≤ 5
```

---

## Propriétés et lois

### Lois commutatives
```text
A ∪ B = B ∪ A
A ∩ B = B ∩ A
A △ B = B △ A
```

### Lois associatives
```text
(A ∪ B) ∪ C = A ∪ (B ∪ C)
(A ∩ B) ∩ C = A ∩ (B ∩ C)
(A △ B) △ C = A △ (B △ C)
```

### Lois distributives
```text
A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
A × (B ∪ C) = (A × B) ∪ (A × C)
```

### Lois de De Morgan
```text
(A ∪ B)' = A' ∩ B'
(A ∩ B)' = A' ∪ B'
```

### Lois idempotentes
```text
A ∪ A = A
A ∩ A = A
A △ A = ∅
```

### Lois d'identité
```text
A ∪ ∅ = A
A ∩ U = A
A △ ∅ = A
```

### Lois du complémentaire
```text
A ∪ A' = U
A ∩ A' = ∅
(A')' = A
U' = ∅
∅' = U
```

---

**Prochaines étapes:**
- Lisez [FUNCTIONS.md](FUNCTIONS.md) pour apprendre les fonctions
- Lisez [LEARNING_GUIDE.md](LEARNING_GUIDE.md) pour les exercices pratiques
