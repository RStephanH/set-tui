# Fondements de la Théorie des Ensembles

**Un guide complet des fondations mathématiques de Set-TUI**

## Table des matières

1. [Qu'est-ce qu'un ensemble?](#quest-ce-quun-ensemble)
2. [Notation des ensembles](#notation-des-ensembles)
3. [Définitions de base](#définitions-de-base)
4. [Relations entre ensembles](#relations-entre-ensembles)
5. [Propriétés fondamentales](#propriétés-fondamentales)
6. [Ensemble vide et ensemble universel](#ensemble-vide-et-ensemble-universel)

---

## Qu'est-ce qu'un ensemble?

Un **ensemble** est une collection bien définie d'objets distincts (appelés **éléments** ou **membres**).

### Caractéristiques clés

1. **Distincts**: Pas de doublons. {1, 2, 2, 3} = {1, 2, 3}
2. **Non ordonnés**: {1, 2, 3} = {3, 1, 2}
3. **Bien défini**: Il doit être clair si un élément appartient à l'ensemble ou non

### Exemples

- **Nombres naturels**: ℕ = {0, 1, 2, 3, ...}
- **Nombres entiers**: ℤ = {..., -2, -1, 0, 1, 2, ...}
- **Nombres réels**: ℝ = tous les nombres décimaux
- **Ensemble fini**: A = {a, e, i, o, u} (voyelles)

---

## Notation des ensembles

### Énumération des éléments (Forme explicite)
```
A = {1, 2, 3, 4, 5}
B = {pomme, orange, banane}
C = {rouge, vert, bleu}
```

### Notation en compréhension (Forme implicite)
```
A = {x | x est un entier positif inférieur à 6}
B = {x ∈ ℕ | x est pair}
C = {x ∈ ℝ | x² < 10}
```

Lire comme: "A est l'ensemble de tous les x tels que..."

### Appartenance
- `x ∈ A` : x est un élément de A (x appartient à A)
- `x ∉ A` : x n'est pas un élément de A

### Cardinalité
- `|A|` : le nombre d'éléments de A (cardinalité de A)

**Exemple:**
```
A = {1, 2, 3}
|A| = 3

B = {}
|B| = 0  (ensemble vide)

C = {a, b, c, d, e}
|C| = 5
```

---

## Définitions de base

### Sous-ensemble
**A ⊆ B** (A est un sous-ensemble de B)

Tout élément de A est aussi dans B.

```
A ⊆ B  ⟺  ∀x: (x ∈ A ⟹ x ∈ B)
```

**Exemples:**
- {1, 2} ⊆ {1, 2, 3}  ✓ VRAI
- {1, 4} ⊆ {1, 2, 3}  ✗ FAUX
- A ⊆ A pour n'importe quel ensemble A (propriété réflexive)
- ∅ ⊆ A pour n'importe quel ensemble A (ensemble vide est sous-ensemble de tout)

### Sous-ensemble strict
**A ⊂ B** (A est un sous-ensemble strict de B)

A ⊆ B ET A ≠ B (A est strictement plus petit que B)

```
A ⊂ B  ⟺  (A ⊆ B  ∧  A ≠ B)
```

**Exemples:**
- {1, 2} ⊂ {1, 2, 3}  ✓ VRAI (sous-ensemble strict)
- {1, 2, 3} ⊂ {1, 2, 3}  ✗ FAUX (égal, pas strict)

### Ensembles égaux
**A = B** (A égale B)

A et B ont exactement les mêmes éléments.

```
A = B  ⟺  (A ⊆ B  ∧  B ⊆ A)
```

---

## Relations entre ensembles

### Ensembles disjoints
**A ∩ B = ∅** (A et B sont disjoints)

Deux ensembles sont disjoints s'ils n'ont aucun élément en commun.

**Exemple:**
```
A = {1, 2, 3}
B = {4, 5, 6}
A ∩ B = ∅  → disjoints ✓
```

### Ensembles qui se chevauchent
Deux ensembles se chevauchent s'ils partagent au moins un élément.

**Exemple:**
```
A = {1, 2, 3}
B = {3, 4, 5}
A ∩ B = {3}  → chevauchement ✓
```

---

## Propriétés fondamentales

### Lois de De Morgan

Pour les ensembles A, B et l'ensemble universel U:

1. **(A ∪ B)' = A' ∩ B'**
   - Le complémentaire d'une union égale l'intersection des complémentaires

2. **(A ∩ B)' = A' ∪ B'**
   - Le complémentaire d'une intersection égale l'union des complémentaires

### Lois distributives

1. **A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)**
   - L'union se distribue sur l'intersection

2. **A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)**
   - L'intersection se distribue sur l'union

### Lois commutatives
- **A ∪ B = B ∪ A**
- **A ∩ B = B ∩ A**

### Lois associatives
- **(A ∪ B) ∪ C = A ∪ (B ∪ C)**
- **(A ∩ B) ∩ C = A ∩ (B ∩ C)**

### Lois idempotentes
- **A ∪ A = A**
- **A ∩ A = A**

---

## Ensemble vide et ensemble universel

### Ensemble vide (∅)

L'ensemble ne contenant aucun élément.

```
∅ = {} = {x | x ≠ x}
|∅| = 0
```

**Propriétés:**
- ∅ ⊆ A pour n'importe quel ensemble A
- ∅ ∪ A = A
- ∅ ∩ A = ∅
- ∅' = U (le complémentaire de l'ensemble vide est l'ensemble universel)

### Ensemble universel (U)

L'ensemble contenant tous les éléments considérés dans un contexte particulier.

**Exemple:**
Si nous travaillons avec les chiffres:
```
U = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

Si nous travaillons avec les lettres:
```
U = {a, b, c, ..., z}
```

**Propriétés:**
- A ⊆ U pour n'importe quel ensemble A dans le contexte
- A ∪ U = U
- A ∩ U = A
- A ∪ A' = U
- A ∩ A' = ∅

---

## Points clés à retenir

1. **Les ensembles sont des collections non ordonnées et distinctes**
2. **La notation de sous-ensemble est fondamentale** (A ⊆ B)
3. **Les opérations sur les ensembles suivent des lois algébriques** (commutative, associative, distributive)
4. **L'ensemble vide est spécial** (sous-ensemble de tout)
5. **La cardinalité mesure la taille de l'ensemble** (|A| = nombre d'éléments)

---

**Prochaines étapes:**
- Lisez [OPERATIONS.md](OPERATIONS.md) pour apprendre toutes les opérations sur les ensembles
- Lisez [FUNCTIONS.md](FUNCTIONS.md) pour comprendre les fonctions entre ensembles
- Lisez [LEARNING_GUIDE.md](LEARNING_GUIDE.md) pour les exercices
