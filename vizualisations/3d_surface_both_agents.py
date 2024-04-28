import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D

def normalize_data(data):
    """Normalize data to have a mean of 0 and a standard deviation of 1."""
    return (data - np.mean(data)) / np.std(data)

def remove_outliers_3d(x, y, z, threshold=3):
    """Remove outliers based on the Z-score method for 3D data."""
    points = np.column_stack((x, y, z))
    mean = np.mean(points, axis=0)
    std = np.std(points, axis=0)
    z_scores = np.abs((points - mean) / std)
    filtered_indices = np.all(z_scores < threshold, axis=1)
    return x[filtered_indices], y[filtered_indices], z[filtered_indices]

def overlayed_scatter(ax, x, y, z, point_col, transparency=0.5, x_min=None, y_min=None):
    """Plot scatter points close to the model surface."""
    for i in range(len(x)):
        if x_min is not None and x[i] < x_min:
            continue
        if y_min is not None and y[i] < y_min:
            continue

        if  x[i]<=1 and y[i]<=1 and z[i]<=1:
            ax.scatter(x[i], y[i], z[i], c=point_col, alpha=transparency, s=9)

def plot_combined_metric_surfaces(dataset1, dataset2, name, ymin=0, color1='blue', color2='red'):
    bd_labels = [["winstay", "pwinR", "ERDS_win"], ["loseswitch", "ploseR", "ERDS_lose"],
                 ["betterstay", "pbetterR", "EODS_better"], ["worseswitch", "pworseR", "EODS_worse"],
                 ["winstay", "loseswitch", "ERDS"], ["betterstay", "worseswitch", "EODS"]]

    fig = plt.figure(figsize=(16,16))
    fig.suptitle(f'Relationship between entropy based metrics and behavioral strategies \n trial length >= {name}, y_min={ymin}')

    for i in range(4):
        ax = fig.add_subplot(2, 2, i+1, projection='3d')
        points = np.linspace(0, 1, 50)
        WS, win = np.meshgrid(points, points)
        WS = np.clip(WS, 1e-10, 1 - 1e-10)
        win = np.clip(win, 1e-10, 1 - 1e-10)

        ERDSp = (-win * WS * np.log2(WS) - win * (1 - WS) * np.log2(1 - WS))
        ERDSp = np.nan_to_num(ERDSp)
        ax.plot_surface(WS, win, ERDSp, alpha=0.3, color='pink')

        x1, y1, z1 = np.array(dataset1[bd_labels[i][0]]), np.array(dataset1[bd_labels[i][1]]), np.array(dataset1[bd_labels[i][2]])

        x2, y2, z2 = np.array(dataset2[bd_labels[i][0]]), np.array(dataset2[bd_labels[i][1]]), np.array(dataset2[bd_labels[i][2]])


        overlayed_scatter(ax, x1, y1, z1, color1,   x_min=ymin, y_min=ymin)
        overlayed_scatter(ax, x2, y2, z2, color2,  x_min=ymin, y_min=ymin)

        ax.set_xlabel(bd_labels[i][0])
        ax.set_ylabel(bd_labels[i][1])
        ax.set_zlabel(bd_labels[i][2])
        ax.view_init(elev=30, azim=20)
        ax.dist = 12
        ax.set_xticks([0, 0.5, 1])
        ax.set_yticks([0, 0.5, 1])
        ax.set_zticks([0, 0.5, 1])

    legend_elements = [Line2D([0], [0], marker='o', color='w', label='agent 1',
                              markerfacecolor=color1, markersize=10),
                       Line2D([0], [0], marker='o', color='w', label='agent 2',
                              markerfacecolor=color2, markersize=10)]


    fig.legend(handles=legend_elements, loc='upper right', ncol=2)

    plt.subplots_adjust(wspace=0.001, hspace=0.1)
    plt.savefig(f'/content/drive/MyDrive/thesis/plots_3d_combined/{name}_{ymin}_no_removing.png')
    plt.show()