from keras.models import Sequential
from keras.layers import LSTM, Dense
from utils.train_preprocessing import prepare_data
from metrics.get_metrics import get_results
from utils.config import LSTMConfig

def run_lstm_model(data, features, target_column):
    train_X, train_y, test_X, test_y, scaler_y = prepare_data(data, features, target_column, LSTMConfig)

    model = Sequential()
    model.add(LSTM(LSTMConfig.lstm_units, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')

    model.fit(train_X, train_y, epochs=LSTMConfig.epochs, batch_size=LSTMConfig.batch_size,
              validation_data=(test_X, test_y), verbose=2, shuffle=False)

    predicted, test_y_inverse = model.predict(test_X), scaler_y.inverse_transform(test_y)
    metrics = get_results(test_y_inverse, scaler_y.inverse_transform(predicted))

    return metrics
