def plot_correlation(df, method='pearson'):
    correlation_matrix = df.corr(method=method)
    correlation_matrix
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 6})
    plt.title(f'Correlation Matrix - {method}  small dataset')
    plt.show()