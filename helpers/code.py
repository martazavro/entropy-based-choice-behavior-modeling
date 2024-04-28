import pandas as pd
df = pd.read_csv('/Users/Marta/Desktop/thesis/code/data_csv/Ha_Guanf_VL06_2015-02-19_003_01-A_spikes_CH007_SE7c_01_output.csv')
df = df.head(int(df['trialNum'].iloc[0]))

merged_columns = ['trialInBlock', 'choiceColor', 'choiceLocation',
                  'choiceMotionDirection', 'reward', 'learningStatus', 'HDtrlnum',
                  'probabilityRewardedChoice', 'probabilityRewardedChoice_unitInfo', 'stimOn',
                  'colorOnset', 'motionOnset', 'choiceEvent', 'saccadeChoice',
                  'reward_signalTime', 'f1On', 'f2On', 'stimOnTime']

columns_to_take_first = ['name', 'iso', 'area', 'trialNum']

merged_values = [df[col].tolist() for col in merged_columns]
new_row = pd.DataFrame({col: [val] for col, val in zip(merged_columns, merged_values)})
first_values_row = pd.DataFrame({col: [df[col].iloc[0]] for col in columns_to_take_first})
final_df = pd.concat([first_values_row, new_row], axis=1)
a = final_df['stimOnTime']
print(a[0])
print(type(a[0][0]))