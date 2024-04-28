def conditional_entropy(y, x, metric_name, decomp_map=None):
    y_unique = np.unique(y)
    x_unique = np.unique(x)

    if decomp_map is not None:
        decompose_flag = True
    else:
        decompose_flag = False

    if decompose_flag:
        decomp_vals = list(decomp_map.values())
        for decomp_val in decomp_vals:
            locals()[f'{metric_name}_{decomp_val}'] = np.nan

    x_entropies_storage = [np.nan]

    for x_val in x_unique:
        x_entropy = 0

        x_signal = [y == x_val for y in x]
        prob_x = np.mean(x_signal)

        for y_val in y_unique:
            y_signal = [x == y_val for x in y]
            prob_x_given_y = conditional_probability(y_signal, x_signal)
            x_entropy += nansum_zero_helper([prob_x_given_y * prob_x * np.log2(prob_x_given_y)], axis=None)

        if decompose_flag:
            locals()[f'{metric_name}_{decomp_map[x_val]}'] = -x_entropy

        x_entropies_storage.append(-x_entropy)

    locals()[metric_name] = nansum_zero_helper(x_entropies_storage, axis=None)

    if decompose_flag:
        return locals()
    else:
        return locals()[metric_name]