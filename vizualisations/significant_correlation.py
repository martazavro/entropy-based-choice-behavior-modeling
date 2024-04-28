import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
import plotly.figure_factory as ff


matrix_labels = [ "P(stay)", "WinStay", "LoseSwitch", "WinWorse", "LoseWorse", "RI", "RI(better)",
    "RI(worse)", "ERDS", "ERDS(win)", "ERDS(lose)", "EODS", "EODS(better)", "EODS(worse)","ERODS",
   "ERODS(win,better)", "ERODS(lose,better)" , "ERODS(win,worse)", "ERODS(lose,worse)" ,"Deviation from matching"]


def plot_significant_correlations(df, method='pearson', significance_level=0.05, agent=''):
    df.columns = matrix_labels
    correlation_matrix = pd.DataFrame(data=np.zeros((df.shape[1], df.shape[1])), columns=df.columns, index=df.columns)
    p_values_matrix = pd.DataFrame(data=np.ones((df.shape[1], df.shape[1])), columns=df.columns, index=df.columns)

    def correlate(col1, col2):
        if method == 'pearson':
            return pearsonr(col1, col2)
        elif method == 'spearman':
            return spearmanr(col1, col2)
        else:
            raise ValueError("Method must be either 'pearson' or 'spearman'.")

    for col1 in df.columns:
        for col2 in df.columns:
            if col1 != col2 and df[col1].dtype.kind in 'bifc' and df[col2].dtype.kind in 'bifc':
                corr, p_value = correlate(df[col1].dropna(), df[col2].dropna())
                correlation_matrix.loc[col1, col2] = corr if p_value < significance_level else np.nan
            else:
                correlation_matrix.loc[col1, col2] = 1.0 if col1 == col2 else np.nan



    mask = np.where(np.isnan(correlation_matrix), True, False)
    annotations = correlation_matrix.round(2).astype(str)
    annotations = np.where(mask, "", annotations) 

    fig = ff.create_annotated_heatmap(
        z=correlation_matrix.to_numpy(),
        x=list(correlation_matrix.columns),
        y=list(correlation_matrix.index),
        annotation_text=annotations,
        colorscale='RdBu',
        reversescale=True,  
        showscale=True
    )

    for i in range(len(fig.layout.annotations)):
        fig.layout.annotations[i].font.size = 8 

    text_color_threshold = 0.5 
    for i, row in enumerate(correlation_matrix.to_numpy()):
        for j, value in enumerate(row):
            if not np.isnan(value):
                font_color = 'white' if abs(value) > text_color_threshold else 'black'
            else:
                font_color = 'black'
            fig.layout.annotations[i * len(row) + j].font.color = font_color


    fig.update_layout(
        title=f'{method.capitalize()} (p < {significance_level}) Agent {agent}',
        xaxis=dict(
            showgrid=False, 
            tickfont=dict(size=10),
            tickangle=-45,

        ),
        yaxis=dict(
            showgrid=False,
            tickfont=dict(size=10),

        ),
        width=800,
        height=600
    )


    fig.show()
