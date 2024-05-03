def conditional_probability(y, x):
    """Calculate conditional probability P(Y | X)."""
    y = np.array(y, dtype=bool)
    x = np.array(x, dtype=bool)
    return np.mean(y[x]) / np.mean(x) if np.mean(x) > 0 else 0
