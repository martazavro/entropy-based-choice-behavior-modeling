def nansum_zero_helper(myArr, axis):
    mySum = np.nansum(myArr, axis=axis)
    if isinstance(mySum, np.ndarray):
        mySum[np.all(np.isnan(myArr), axis=1)] = np.nan
    return mySum

def binary_to_decimal(binary_matrix):
    """Converts a binary matrix to a list of decimal values."""
    return [int(''.join(map(str, row)), 2) for row in binary_matrix]

def conditional_probability(y, x):
    """Calculate conditional probability P(Y | X)."""
    y = np.array(y, dtype=bool)
    x = np.array(x, dtype=bool)
    return np.mean(y[x]) / np.mean(x) if np.mean(x) > 0 else 0