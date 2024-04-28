def entropy_metrics(choice, reward, hr_side, strr=None):
    """Computes entropy based metrics for given behavioral data."""
    if strr is None:
        strr = [choice[i] == choice[i+1] for i in range(len(choice)-1)]


    choice, reward, hr_side, strr = map(np.array, [choice, reward, hr_side, strr])
    opt = choice == hr_side

    if len(reward) > len(strr):
        reward = reward[:-1]
        opt = opt[:-1]

    rew_and_opt = binary_to_decimal(np.vstack([reward, opt]).T)

    return {
        "ERDS": conditional_entropy(strr, reward, "ERDS", {0: 'lose', 1: 'win'}),
        "EODS": conditional_entropy(strr, opt, "EODS", {0: 'worse', 1: 'better'}),
        "ERODS": conditional_entropy(strr, rew_and_opt, "ERODS", {0: 'loseworse', 1: 'losebetter', 2: 'winworse', 3: 'winbetter'})
    }