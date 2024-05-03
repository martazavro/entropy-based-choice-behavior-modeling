import matplotlib.pyplot as plt
import seaborn as sns

def plot_deviation(data_plot):
    sns.set(style="whitegrid")

    plt.hist(data_plot.matching_measure_run, bins=30, alpha=0.75, color='skyblue')
    plt.axvline(x=0, color='blue', linestyle='--', linewidth=2, label='Baseline')  # Add a label for the line

    plt.xlabel('Deviation from Matching')
    plt.ylabel('Number of Blocks')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


data_plot = results_all[~results_all['matching_measure'].isna()]
data_plot = data_plot[data_plot['monkey']=='ke']
data_plot = data_plot[data_plot['len']>20]
data_plot.reset_index(inplace=True, drop=True)

plot_deviation(data_plot)
