import os
import pandas as pd

input_folder = '/Users/Marta/Desktop/thesis/code/data_csv'
output_folder = '/Users/Marta/Desktop/thesis/code/'

merged_columns = ['trialInBlock', 'choiceColor', 'choiceLocation',
                  'choiceMotionDirection', 'reward', 'learningStatus', 'HDtrlnum',
                  'probabilityRewardedChoice', 'probabilityRewardedChoice_unitInfo', 'stimOn',
                  'colorOnset', 'motionOnset', 'choiceEvent', 'saccadeChoice',
                  'reward_signalTime', 'f1On', 'f2On', 'stimOnTime']

columns_to_take_first = ['name', 'iso', 'area', 'trialNum']

csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
merged_df = pd.DataFrame()

for csv_file in csv_files:
    df = pd.read_csv(os.path.join(input_folder, csv_file))
    df = df.head(int(df['trialNum'].iloc[0]))
    merged_values = [df[col].tolist() for col in merged_columns]
    new_row = pd.DataFrame({col: [val] for col, val in zip(merged_columns, merged_values)})
    first_values_row = pd.DataFrame({col: [df[col].iloc[0]] for col in columns_to_take_first})
    final_df = pd.concat([first_values_row, new_row], axis=1)
    merged_df = pd.concat([merged_df, final_df], ignore_index=True)

json_data = merged_df.to_json(orient='records')
with open('full_dataset.json', 'w') as json_file:
    json_file.write(json_data)
