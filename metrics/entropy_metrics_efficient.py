def entropy_metrics_efficient(choice, reward, hr_side, stay=None):
    choice = np.array(choice)
    reward = np.array(reward)
    hr_side = np.array(hr_side)

    if stay is None:
        stay = choice[:-1] == choice[1:]
        win = reward[:-1] == 1
        better = choice[:-1] == hr_side[:-1]
    else:
        stay = np.array(stay)
        win = reward == 1
        better = choice == hr_side

    lose = ~win
    worse = ~better
    switch = ~stay

    interactions = {
        'better': better, 'worse': worse, 'switch': switch, 'stay': stay, 'win': win, 'lose': lose,
        'winstay': win & stay, 'winswitch': win & switch,
        'losestay': lose & stay, 'loseswitch': lose & switch,
        'betterstay': better & stay, 'worsestay': worse & stay,
        'betterswitch': better & switch, 'worseswitch': worse & switch,
        'winbetter': win & better, 'winworse': win & worse,
        'losebetter': lose & better, 'loseworse': lose & worse,
        'winbetterstay': win & better & stay, 'winworsestay': win & worse & stay,
        'losebetterstay': lose & better & stay, 'loseworsestay': lose & worse & stay,
        'winbetterswitch': win & better & switch, 'winworseswitch': win & worse & switch,
        'losebetterswitch': lose & better & switch, 'loseworseswitch': lose & worse & switch
    }

    for key, value in interactions.items():
        interactions[key] = np.nanmean(value.astype(float))

    output = {}


    for key in ['better', 'worse', 'win', 'lose']:
        stay_key = key + 'stay'
        switch_key = key + 'switch'
        eods_stay = np.multiply(interactions[stay_key], np.log2(np.divide(interactions[stay_key], interactions[key], where=interactions[key] != 0)))
        eods_switch = np.multiply(interactions[switch_key], np.log2(np.divide(interactions[switch_key], interactions[key], where=interactions[key] != 0)))
        output['EODS_' + key] = -nansum_zero_helper(np.concatenate([eods_stay[eods_stay != 0], eods_switch[eods_switch != 0]]))

    for condition in ['win', 'lose']:
        stay_key = condition + 'stay'
        switch_key = condition + 'switch'
        erds_stay = np.multiply(interactions[stay_key], np.log2(np.divide(interactions[stay_key], interactions[condition], where=interactions[condition] != 0)))
        erds_switch = np.multiply(interactions[switch_key], np.log2(np.divide(interactions[switch_key], interactions[condition], where=interactions[condition] != 0)))
        output['ERDS_' + condition] = -nansum_zero_helper(np.concatenate([erds_stay[erds_stay != 0], erds_switch[erds_switch != 0]]))


    combinations = ['winbetter', 'winworse', 'losebetter', 'loseworse']
    for combination in combinations:
        stay_key = combination + 'stay'
        switch_key = combination + 'switch'
        erods_stay = np.multiply(interactions[stay_key], np.log2(np.divide(interactions[stay_key], interactions[combination], where=interactions[combination] != 0)))
        erods_switch = np.multiply(interactions[switch_key], np.log2(np.divide(interactions[switch_key], interactions[combination], where=interactions[combination] != 0)))
        output['ERODS_' + combination] = -nansum_zero_helper(np.concatenate([erods_stay[erods_stay != 0], erods_switch[erods_switch != 0]]))

    output['ERDS'] = output['ERDS_win'] + output['ERDS_lose']
    output['EODS'] = output['EODS_better'] + output['EODS_worse']
    output['ERODS'] = output['ERODS_winbetter'] + output['ERODS_winworse'] + output['ERODS_losebetter'] + output['ERODS_loseworse']

    return output
