import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def compute_metrics(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100 if np.any(y_true) else float('inf')
    r_squared = r2_score(y_true, y_pred)

    return {
        'RMSE': rmse,
        'MAE': mae,
        'MAPE': mape,
        'R-squared': r_squared
    }
