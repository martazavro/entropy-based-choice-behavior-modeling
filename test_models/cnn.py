from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense
from utils.train_preprocessing import prepare_data
from metrics.get_metrics import get_results
from utils.config import CNNConfig

def run_cnn_model(data, features, target_column):

    train_X, train_y, test_X, test_y, scaler_y = prepare_data(data, features, target_column, CNNConfig, model_type='cnn')

    model = Sequential()
    model.add(Conv1D(filters=CNNConfig.filters, kernel_size=CNNConfig.kernel_size, activation='relu', input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(MaxPooling1D(pool_size=CNNConfig.pool_size))
    model.add(Flatten())
    model.add(Dense(50, activation='relu')) 
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')

    model.fit(train_X, train_y, epochs=CNNConfig.epochs, batch_size=CNNConfig.batch_size,
              validation_data=(test_X, test_y), verbose=2, shuffle=False)

    predicted, test_y_inverse = model.predict(test_X), scaler_y.inverse_transform(test_y)
    metrics = get_results(test_y_inverse, scaler_y.inverse_transform(predicted))

    return metrics
