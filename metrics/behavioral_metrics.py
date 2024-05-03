def behavioral_metrics(choice, reward, hr_side, stay=None):
    choice = np.array(choice)
    reward = np.array(reward)
    hr_side = np.array(hr_side)

    better = choice == hr_side

    if stay is None:
        stay = choice[:-1] == choice[1:]
        rewardR = reward[:-1] == 1
        betterR = better[:-1]
    else:
        stay = np.array(stay)
        rewardR = np.array(reward)
        betterR = np.array(better)

    not_stay = ~stay
    not_better = ~better
    not_betterR = ~betterR
    not_rewardR = ~rewardR

    output = {
        'pbetter': np.mean(better),
        'pstay': np.mean(stay),
        'pwin': np.mean(reward == 1), #here
        'pwinR': np.mean(rewardR),
        'ploseR': 1 - np.mean(rewardR),
        'pbetterR': np.mean(betterR),
        'pworseR': 1 - np.mean(betterR),
        'betterstay': conditional_probability(betterR, stay),
        'worseswitch': conditional_probability(not_betterR, not_stay),
        'winbetter': np.mean(better & (reward == 1)),
        'losebetter': np.mean(better & (reward == 0)),
        'winworse': np.mean(not_better & (reward == 1)),
        'loseworse': np.mean(not_better & (reward == 0)),
        'winstaybetter': conditional_probability(betterR & rewardR, stay),
        'loseswitchbetter': conditional_probability(betterR & not_rewardR, not_stay),
        'winstayworse': conditional_probability(not_betterR & rewardR, stay),
        'loseswitchworse': conditional_probability(not_betterR & not_rewardR, not_stay),
        'winstay': conditional_probability(rewardR, stay),
        'loseswitch': conditional_probability(not_rewardR, not_stay)
    }

    output['delta_winstay_losestay'] = output['winstay'] - conditional_probability(not_rewardR, stay)
    output['choice_fraction'] = np.mean(choice == -1) / np.mean(np.abs(choice) == 1)
    output['reward_fraction'] = np.mean((reward == 1) & (choice == -1)) / np.mean((reward == 1) & np.abs(choice) == 1)
    output['reward_fraction1'] = np.sum((reward == 1) & (choice == -1)) / np.sum(reward == 1)


    output['matching_measure'] = np.sign(output['choice_fraction'] - output['reward_fraction']) * (output['choice_fraction'] - output['reward_fraction']) #here


    output['choice_fraction_run'] = np.mean(better) / (np.mean(better) + np.mean(~better))
    output['reward_fraction_run'] = np.mean(reward == 1 & better) / (np.mean(reward == 1 & better) + np.mean(reward == 1 & ~better))
    output['matching_measure_run'] = output['choice_fraction_run'] - output['reward_fraction_run']
    output['RI'] = output['pstay'] - (output['pbetter'] ** 2 + (1 - output['pbetter']) ** 2)
    output['RI_B'] = np.mean(stay & betterR) - output['pbetter'] ** 2
    output['RI_W'] = np.mean(stay & not_betterR) - (1 - output['pbetter']) ** 2

    return output
