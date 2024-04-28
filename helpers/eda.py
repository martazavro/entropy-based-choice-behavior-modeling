import pandas as pd

def load_data(filepath):
    """Load JSON data into a DataFrame."""
    return pd.read_json(filepath)

def preprocess_data(df):
    """Perform initial preprocessing and data checking."""
    # Extracting specific patterns from 'name' column and assigning new columns
    df['channel'] = df['name'].str.extract(r'CH(\d+)_')
    df['vl'] = df['name'].str.extract(r'VL(.*?)_')
    df['monkey'] = df['name'].str.extract(r'^(.*?)_VL')
    df[['date', 'number', 'unit']] = df['name'].str.extract(r'(\d{4}-\d{2}-\d{2})_(.*?)\-A_spikes.*?(SE.*)$')
    
    # Filtering out rows where 'name' does not contain 'A_spikes'
    df = df[~df['name'].str.contains('A_spikes')]
    
    # Convert 'learningStatus' to integer and remove empty values
    df['learningStatus'] = df['learningStatus'].apply(lambda x: [int(val) for val in x if val])
    return df

def explore_data(df):
    """Perform data exploration and transformations."""
    print(df.head())
    print("Data Shape:", df.shape)
    print("Unique Monkeys:", df.monkey.unique())
    print("Unique Channels:", df.channel.unique())
    print("Unique VLs:", df.vl.unique())
    
    # Check and print the first few rows of specific selections
    selected = df[(df['monkey'] == 'ha') & (df['vl'] == '05a') & (df['date'] == '2014-09-24') & (df['number'] == '100_01')]
    print(selected.head())
    
    # Handling and exploring nested list columns
    df_exploded = df.apply(lambda col: col.explode() if col.apply(type).eq(list).any() else col)
    df_exploded.reset_index(drop=True, inplace=True)
    print(df_exploded.head())

def aggregate_data(df):
    """Aggregate data based on certain columns."""
    agg_dict = {
        'monkey': 'first',
        'vl': 'first',
        'date': 'first',
        'number': 'first',
        'trialInBlock': list,
        'choiceColor': list,
        'choiceLocation': list,
        'choiceMotionDirection': list,
        'reward': list,
        'learningStatus': list,
        'probabilityRewardedChoice_unitInfo': list
    }
    result_df = df.groupby('HDtrlnum').agg(agg_dict).reset_index()
    return result_df

def main():
    df = load_data('/content/full_dataset.json')
    df_preprocessed = preprocess_data(df)
    explore_data(df_preprocessed)
    result_df = aggregate_data(df_preprocessed)
    print("Aggregated Data:")
    print(result_df)

if __name__ == "__main__":
    main()
