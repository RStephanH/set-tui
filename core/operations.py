def union(A, B):
    return A | B


def intersection(A, B):
    return A & B


def difference(A, B):
    """Left difference"""
    return A - B


def sym_difference(A, B):
    """Symmetric difference"""
    return A ^ B


def cardinality(A):
    return len(A)


def cartesian_product(A, B):
    return {(a, b) for a in A for b in B}
