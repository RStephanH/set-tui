# Fonctions et Applications

**Comprendre les fonctions comme des relations mathématiques et leurs propriétés**

## Table des matières

1. [Qu'est-ce qu'une fonction?](#quest-ce-quune-fonction)
2. [Notation des fonctions](#notation-des-fonctions)
3. [Domaine, codomaine et image](#domaine-codomaine-et-image)
4. [Propriétés des fonctions](#propriétés-des-fonctions)
5. [Fonctions spéciales](#fonctions-spéciales)

---

## Qu'est-ce qu'une fonction?

Une **fonction** (ou **application**) f: A → B est une règle qui associe à chaque élément x dans A exactement UN élément f(x) dans B.

### Conditions clés

1. **Chaque élément de A doit être associé à quelque chose** (fonction totale)
2. **Chaque élément de A est associé à exactement UN élément de B** (bien définie)
3. **Aucun élément de A n'est associé à plusieurs éléments de B**

### Notation

```
f: A → B
x ↦ f(x)
```

Lire comme: "f est une fonction de A vers B qui envoie x à f(x)"

### Représentation

Les fonctions peuvent être représentées comme:

**Paires ordonnées:**
```
f = {(1, 2), (2, 4), (3, 6), (4, 8)}
```

**Tableau:**
```
x  | 1  2  3  4
f(x)| 2  4  6  8
```

**Formule:**
```
f(x) = 2x
```

**Analogie de machine:**
```
Entrée (x) → [f] → Sortie (f(x))
```

---

## Notation des fonctions

### Domaine et codomaine

```
f: A → B
```

- **A** = **Domaine** (ensemble de toutes les entrées possibles)
- **B** = **Codomaine** (ensemble où les sorties sont censées venir)
- **f(x)** = la sortie quand l'entrée est x

### Exemples

**Fonction linéaire:**
```
f: ℝ → ℝ
f(x) = 2x + 1
```

**Fonction carrée:**
```
f: ℤ → ℤ
f(x) = x²
```

**Fonction modulo:**
```
f: ℤ → {0, 1, 2}
f(x) = x mod 3
```

---

## Domaine, codomaine et image

### Domaine (A)

L'ensemble de toutes les entrées possibles.

```
f: A → B
Domaine de f = A
```

Tous les éléments doivent avoir une valeur de fonction assignée.

### Codomaine (B)

L'ensemble où les sorties sont censées venir (déclaré dans la définition de la fonction).

```
f: A → B
Codomaine de f = B
```

Pas tous les éléments de B ont besoin d'être atteints!

### Image (Ensemble image)

L'ensemble de toutes les valeurs de sortie réelles (éléments de B qui SONT atteints).

```
Image(f) = f(A) = {f(x) | x ∈ A}
```

**Important:** Image(f) ⊆ Codomaine(f)

### Exemple

```
f: {1, 2, 3} → {1, 4, 9, 16, 25}
f(x) = x²

Domaine = {1, 2, 3}
Codomaine = {1, 4, 9, 16, 25}
Image = {1, 4, 9}  ← seulement ceux-ci sont réellement atteints

Remarque: Image ⊂ Codomaine (sous-ensemble strict!)
```

---

## Propriétés des fonctions

### Injectivité (One-to-One)

**Définition:** Une fonction est **injective** si des entrées différentes produisent toujours des sorties différentes.

```
f est injective  ⟺  f(x₁) = f(x₂) ⟹ x₁ = x₂

Ou équivalemment:  x₁ ≠ x₂ ⟹ f(x₁) ≠ f(x₂)
```

**Intuition:** Aucun deux éléments ne sont associés à la même sortie.

**Exemples:**

✓ **Injective:**
```
f: ℝ → ℝ,  f(x) = 2x + 1
Si f(x₁) = f(x₂), alors 2x₁ + 1 = 2x₂ + 1, donc x₁ = x₂
```

✗ **Non injective:**
```
f: ℝ → ℝ,  f(x) = x²
f(-2) = 4 et f(2) = 4, mais -2 ≠ 2
Deux entrées différentes donnent la même sortie!
```

### Surjectivité (Onto)

**Définition:** Une fonction est **surjective** si chaque élément du codomaine est atteint par au moins une entrée.

```
f est surjective  ⟺  f(A) = B
                  ⟺  ∀y ∈ B, ∃x ∈ A: f(x) = y
```

**Intuition:** Aucun élément du codomaine n'est "manqué."

**Exemples:**

✓ **Surjective:**
```
f: ℤ → {0, 1, 2},  f(x) = x mod 3
Chaque élément {0, 1, 2} est atteint:
  f(0) = 0, f(1) = 1, f(2) = 2
```

✗ **Non surjective:**
```
f: {1, 2, 3} → {1, 4, 9, 16, 25},  f(x) = x²
Image = {1, 4, 9}
Les éléments 16 et 25 ne sont jamais atteints!
```

### Bijectivité (One-to-One and Onto)

**Définition:** Une fonction est **bijective** si elle est à la fois injective ET surjective.

```
f est bijective  ⟺  f est injective ET f est surjective
```

**Intuition:** Un appariement parfait entre le domaine et le codomaine. Chaque entrée est associée à une sortie unique, et chaque sortie vient d'exactement une entrée.

**Conséquence importante:**
```
Si f: A → B est bijective, alors |A| = |B|
```

**Exemple:**

✓ **Bijective:**
```
f: {1, 2, 3} → {a, b, c}
f(1) = a
f(2) = b
f(3) = c

C'est bijective: correspondance parfaite one-to-one
```

✓ **Bijective:**
```
f: ℝ → ℝ,  f(x) = 2x + 1
- Injective: f(x₁) = f(x₂) ⟹ x₁ = x₂ ✓
- Surjective: pour n'importe quel y, nous pouvons trouver x = (y-1)/2 ✓
```

### Tableau récapitulatif

| Propriété | Signification | Exemple |
|-----------|--------------|---------|
| **Injective** | Entrées différentes → sorties différentes | f(x) = 2x |
| **Surjective** | Chaque élément du codomaine est atteint | f: ℤ → {0,1,2}, f(x)=x%3 |
| **Bijective** | À la fois injective et surjective | f(x) = 2x + 1 sur ℝ → ℝ |

---

## Fonctions spéciales

### Fonction identité

```
f: A → A
f(x) = x

Chaque élément est associé à lui-même.
```

**Propriétés:**
- Toujours injective
- Toujours surjective
- Toujours bijective

### Fonction constante

```
f: A → B
f(x) = c  (pour un c ∈ B fixé)

Chaque élément est associé à la même sortie.
```

**Exemple:**
```
f: {1, 2, 3} → {5}
f(x) = 5
```

**Propriétés:**
- Injective seulement si |A| ≤ 1
- Surjective seulement si |B| = 1
- Jamais bijective si |A| > 1

### Composition de fonctions

```
f: A → B
g: B → C
g ∘ f: A → C

(g ∘ f)(x) = g(f(x))
```

Lire comme: "g rond f" ou "g après f"

**Exemple:**
```
f: ℝ → ℝ,  f(x) = x + 1
g: ℝ → ℝ,  g(x) = x²

(g ∘ f)(x) = g(f(x)) = g(x+1) = (x+1)²

Pour x = 2:
f(2) = 3
g(3) = 9
(g ∘ f)(2) = 9 ✓
```

### Fonction inverse

Une fonction f a une **inverse** f⁻¹: B → A si et seulement si f est **bijective**.

```
f: A → B est bijective
⟹ ∃ f⁻¹: B → A telle que:
  f⁻¹(f(x)) = x  pour tous x ∈ A
  f(f⁻¹(y)) = y  pour tous y ∈ B
```

**Exemple:**
```
f: ℝ → ℝ,  f(x) = 2x + 1
f⁻¹: ℝ → ℝ,  f⁻¹(y) = (y - 1)/2

Vérification:
f⁻¹(f(3)) = f⁻¹(7) = (7-1)/2 = 3 ✓
f(f⁻¹(5)) = f(2) = 5 ✓
```

---

## Image et préimage

### Image directe (Image d'un ensemble)

Pour S ⊆ A, l'**image directe** f(S) est l'ensemble de toutes les sorties quand les entrées viennent de S.

```
f(S) = {f(x) | x ∈ S}
```

**Exemple:**
```
f: ℝ → ℝ,  f(x) = x²
S = {-2, -1, 0, 1, 2}

f(S) = {0, 1, 4}
Remarque: f(-2) = f(2) = 4, donc 4 n'apparaît qu'une fois dans f(S)
```

### Image inverse (Préimage)

Pour T ⊆ B, l'**image inverse** (ou **préimage**) f⁻¹(T) est l'ensemble de toutes les entrées qui sont associées à des éléments dans T.

```
f⁻¹(T) = {x ∈ A | f(x) ∈ T}
```

**Important:** f⁻¹(T) est un ENSEMBLE, pas nécessairement une fonction!

**Exemple:**
```
f: ℝ → ℝ,  f(x) = x²
T = {4}

f⁻¹({4}) = {-2, 2}
Remarque: Deux entrées différentes sont associées à 4!
```

---

## Comptage de fonctions

### Nombre de fonctions

Le nombre de fonctions différentes de A vers B est:

```
|fonctions de A vers B| = |B|^|A|
```

**Exemple:**
```
A = {1, 2},  B = {a, b, c}
Nombre de fonctions = 3² = 9

Les 9 fonctions sont:
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

### Nombre de fonctions injectives

Le nombre de fonctions injectives de A vers B est:

```
|fonctions injectives| = |B| × (|B|-1) × (|B|-2) × ... × (|B|-|A|+1)
                       = P(|B|, |A|)  (permutation)
```

**Requiert:** |A| ≤ |B|

### Nombre de fonctions bijectives

Le nombre de fonctions bijectives de A vers B est:

```
|fonctions bijectives| = |A|!   (factorielle)
```

**Requiert:** |A| = |B|

**Exemple:**
```
A = {1, 2, 3},  B = {a, b, c}
Nombre de bijections = 3! = 6
```

---

**Prochaines étapes:**
- Lisez [OPERATIONS.md](OPERATIONS.md) pour les détails des opérations sur les ensembles
- Lisez [LEARNING_GUIDE.md](LEARNING_GUIDE.md) pour les problèmes pratiques
