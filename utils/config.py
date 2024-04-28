class GRUConfig:
    test_size = 0.2
    gru_units = 50
    epochs = 80
    batch_size = 1

class BiLSTMConfig:
    test_size = 0.2
    lstm_units = 50
    epochs = 80
    batch_size = 32

class CNNConfig:
    test_size = 0.2
    filters = 64
    kernel_size = 2
    pool_size = 2
    epochs = 50
    batch_size = 32
