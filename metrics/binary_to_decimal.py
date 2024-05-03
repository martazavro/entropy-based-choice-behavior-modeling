def binary_to_decimal(binary_matrix):
    """Converts a binary matrix to a list of decimal values."""
    return [int(''.join(map(str, row)), 2) for row in binary_matrix]
