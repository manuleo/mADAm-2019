# import gc
import tensorflow as tf
import numpy as np
import gc
from tqdm.notebook import tqdm

def univariate_data(dataset, start_index, end_index, history_size, target_size):
    data = []
    labels = []

    start_index = start_index + history_size
    if end_index is None:
        end_index = len(dataset) - target_size
    #print(start_index)
    #print(end_index)

    for i in range(start_index, end_index):
        indices = range(i-history_size, i)
        #print(indices)
        # Reshape data from (history_size,) to (history_size, 1)
        data.append(np.reshape(dataset[indices], (history_size, 1)))
        labels.append(dataset[i+target_size])
    return np.array(data), np.array(labels)


def make_pred(italy):
    past_history = 10
    future_target = 0
    TRAIN_SPLIT = 52    
    for i in tqdm(range(TRAIN_SPLIT, 59)):
        
        sess = tf.compat.v1.Session()

        italy_train_uni, italy_y_train_uni = univariate_data(italy, 0, i,
                                                   past_history,
                                                   future_target)
        italy_test_uni, italy_y_test_uni = univariate_data(italy, i-past_history, None,
                                               past_history,
                                               future_target)
        BATCH_SIZE = 256
        BUFFER_SIZE = 10000

        train_univariate = tf.data.Dataset.from_tensor_slices((italy_train_uni, italy_y_train_uni))
        train_univariate = train_univariate.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()

        val_univariate = tf.data.Dataset.from_tensor_slices((italy_test_uni, italy_y_test_uni))
        val_univariate = val_univariate.batch(BATCH_SIZE).repeat()

        simple_lstm_model = tf.keras.models.Sequential([
        tf.keras.layers.LSTM(16, input_shape=italy_train_uni.shape[-2:]),
        tf.keras.layers.Dense(1)
        ])

        simple_lstm_model.compile(optimizer='adam', loss='mae')

        EVALUATION_INTERVAL = 200
        EPOCHS = 5

        simple_lstm_model.fit(train_univariate, epochs=EPOCHS,
                              steps_per_epoch=EVALUATION_INTERVAL, verbose=0)

        y_tes = simple_lstm_model.predict(val_univariate, steps=1)

        italy = np.append(italy, y_tes[-1])
        
        gc.collect()
        del italy_train_uni, italy_y_train_uni, italy_test_uni, italy_y_test_uni, train_univariate, val_univariate, simple_lstm_model, y_tes
        gc.collect()
        
        tf.keras.backend.clear_session()
        sess.close()
        for gcs in range(0, 3):
            gc.collect()
    return italy