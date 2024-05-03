def nansum_zero_helper(myArr, axis=None):
    """Handle the summation while ignoring NaNs and returning NaN where all elements are NaN."""
    myArr = np.asarray(myArr)
    mySum = np.nansum(myArr, axis=axis)
    if isinstance(mySum, np.ndarray) and mySum.size == 0:
        return np.nan
    if isinstance(mySum, np.ndarray):
        all_nan = np.all(np.isnan(myArr), axis=axis)
        if np.any(all_nan):
            mySum[all_nan] = np.nan
    return mySum
