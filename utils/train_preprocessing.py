import numpy as np
from sklearn.preprocessing import MinMaxScaler

def prepare_data(data, features, target_column, config, model_type='rnn'):
    scaler_x = MinMaxScaler(feature_range=(0, 1))
    scaler_y = MinMaxScaler(feature_range=(0, 1))

    data_features = scaler_x.fit_transform(data[features])
    data_target = scaler_y.fit_transform(data[target_column].values.reshape(-1, 1))

    if model_type == 'cnn':
        # Reshape data for CNN [samples, features, time steps]
        data_features = np.reshape(data_features, (data_features.shape[0], data_features.shape[1], 1))
    else:
        # Reshape data for RNN [samples, time steps, features]
        data_features = np.reshape(data_features, (data_features.shape[0], 1, data_features.shape[1]))

    split_index = int((1 - config.test_size) * len(data_features))
    train_X = data_features[:split_index]
    train_y = data_target[:split_index]
    test_X = data_features[split_index:]
    test_y = data_target[split_index:]

    return train_X, train_y, test_X, test_y, scaler_y
