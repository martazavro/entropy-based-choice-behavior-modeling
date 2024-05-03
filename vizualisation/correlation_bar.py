def correlation_bar(data):

    correlations = data.corr()['matching_measure'].drop('matching_measure').sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    plt.axvline(x=0, color='gray', linestyle='--')
    plt.title('Correlation with deviation from matching')
    plt.box(False)
    plt.yticks(range(len(correlations)), correlations.index)


    for idx, (column, correlation) in enumerate(correlations.items()):
        if correlation > 0:
            plt.barh(y=idx, width=correlation, color='skyblue')
        else:
            plt.barh(y=idx, width=correlation, color='coral')

    plt.show()