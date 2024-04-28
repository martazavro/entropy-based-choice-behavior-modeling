from scipy import stats
def distr(column):

    W, p_value = stats.shapiro(data[column])

    sns.set_style('whitegrid')

    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], bins=20, kde=True, color='skyblue', alpha=0.7)
    plt.title(f'{column}   W: {round(W, 5)}, P: {round(p_value, 5)}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

    plt.show()


def plot_all_distributions(data, columns):
    sns.set_style('whitegrid')
    plt.figure(figsize=(10, 6))

    for column in columns:
        sns.kdeplot(data[column], label=column, fill=True)

    plt.title('Distribution')
    plt.legend()
    plt.xlabel('Value')
    plt.ylabel('Density')

    plt.show()
