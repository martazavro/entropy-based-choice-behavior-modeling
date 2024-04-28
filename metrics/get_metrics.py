def get_results(df):
    result_metrics = []

    for index, row in df.iterrows():
        choice = list(row['choiceColor'])
        reward = list(row['reward'])
        hr_side = list(row['hr_side'])
        stay = None


        metrics_result = {
            'entropy': entropy(choice),
            'entropy_metrics': entropy_metrics(choice, reward, hr_side),
            'entropy_metrics_efficient': entropy_metrics_efficient(choice, reward, hr_side, stay),
            'behavioral_metrics': behavioral_metrics(choice, reward, hr_side, stay)
        }

        result_metrics.append(metrics_result)
    result_metrics_df = pd.DataFrame(result_metrics)

    entropy_metrics_df = pd.DataFrame(result_metrics_df['entropy_metrics'].to_list(), index=result_metrics_df.index)
    entropy_metrics_df = entropy_metrics_df.rename(columns={'ERDS':'ERDS_', 'EODS':'EODS_', 'ERODS': 'ERODS_'})
    behavioral_metrics_df = pd.DataFrame(result_metrics_df['behavioral_metrics'].to_list(), index=result_metrics_df.index)
    entropy_metrics_efficient_df = pd.DataFrame(result_metrics_df['entropy_metrics_efficient'].to_list(), index=result_metrics_df.index)
    results_all = pd.concat([entropy_metrics_df, behavioral_metrics_df, entropy_metrics_efficient_df], axis=1)
    results_all['entropy'] = result_metrics_df['entropy']
    results_all.reset_index(inplace=True, drop=True)
    return results_all