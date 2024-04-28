def entropy(x):
    x_unique = np.unique(x)
    entropy_sum = 0

    for x_num in range(len(x_unique)):
        x_signal = [y == x_unique[x_num] for y in x]
        prob_x = np.mean(x_signal)
        entropy_sum = nansum_zero_helper([entropy_sum, prob_x * np.log2(prob_x)], axis=None)

    return -entropy_sum