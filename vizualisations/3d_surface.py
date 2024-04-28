import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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



def overlayed_scatter(ax, x, y, z, point_col, model_z, threshold, transparency=0.5, x_min=None, y_min=None):
    """Plot scatter points close to the model surface."""
    for i in range(len(x)):
        if x_min is not None and x[i] < x_min:
            continue
        if y_min is not None and y[i] < y_min:
            continue


        model_value = model_z(x[i], y[i])
        if model_value is not None and abs(z[i] - model_value) <= threshold:
            ax.scatter(x[i], y[i], z[i], c=point_col, alpha=transparency, s=5)


def model_z(x, y):
    """Calculate the model's Z value for given x, y."""
    eps = 1e-10  
    x = np.clip(x, eps, 1-eps)
    y = np.clip(y, eps, 1-eps)
    return (-y * x * np.log2(x) - y * (1 - x) * np.log2(1 - x))

def plot_combined_metric_surfaces(output1, point_col1, threshold, name, ymin=0):

    bd_labels = [["winstay", "pwinR", "ERDS_win"], ["loseswitch", "ploseR", "ERDS_lose"],
                 ["betterstay", "pbetterR", "EODS_better"], ["worseswitch", "pworseR", "EODS_worse"],
                 ["winstay", "loseswitch", "ERDS"], ["betterstay", "worseswitch", "EODS"]]

    fig = plt.figure(figsize=(18, 12))
    fig.suptitle(f' data = {name},  threshold = {threshold}, y_min = {ymin}')
    for i in range(4):
        ax = fig.add_subplot(2, 2, i+1, projection='3d')
        points = np.linspace(0, 1, 50)
        WS, win = np.meshgrid(points, points)
        WS = np.clip(WS, 1e-10, 1 - 1e-10)
        win = np.clip(win, 1e-10, 1 - 1e-10)

        ERDSp = (-win * WS * np.log2(WS) - win * (1 - WS) * np.log2(1 - WS))
        ERDSp = np.nan_to_num(ERDSp)
        surf = ax.plot_surface(WS, win, ERDSp, alpha=0.5)

        x, y, z = remove_outliers_3d(np.array(output1[bd_labels[i][0]]),
                                     np.array(output1[bd_labels[i][1]]),
                                     np.array(output1[bd_labels[i][2]]), threshold=3)

        overlayed_scatter(ax, x, y, z, point_col1, model_z, threshold, x_min=0.0, y_min=ymin)

        ax.set_xlabel(bd_labels[i][0])
        ax.set_ylabel(bd_labels[i][1])
        ax.set_zlabel(bd_labels[i][2])
        ax.view_init(elev=30, azim=20)
        ax.set_xticks([0, 0.5, 1])
        ax.set_yticks([0, 0.5, 1])
        ax.set_zticks([0, 0.5, 1])

    plt.show()
