# -*- coding: utf-8 -*-
# RNNs code adapted from the tutorial "Time series forecasting", TensorFlow by Google: https://www.tensorflow.org/tutorials/structured_data/time_series

"""Helper functions to use neural network to predict the future"""
import tensorflow as tf
import numpy as np
import pandas as pd
import gc

def predict_future(dataset, full_pkl_path, run_RNN = False, past_history = 10, verbose = False):
    """Predict missing data in the future using RNNs. The years to predict are all the ones as NaN
    in the dataset.
    Inputs:
        - dataset (pandas dataframe): incomplete dataset with NaN for all the missing years
        - pkl_path (string): path to the pickle containing the complete dataset for the already launched RNN
        - run_RNN (bool, default False): launch all the RNN training and prediction. 
        - past_history (integer, default 10): window dimension to look back in the history
        - verbose (bool, default False): defines if print or not logging messages
    Output:
        - dataset_full (pandas dataframe): complete dataset contatining prediction for the missing years.
    WARNING: Using RNNs requires more than 20 GB of RAM and about 1 hour to run, 
    don't change the flag run_RNN without having this amount of memory/time"""
    
    if run_RNN == False:
        try:
            dataset_full = pd.read_pickle(full_pkl_path)
            return dataset_full
        except:
            print("Wrong path to the complete pickle")
            return dataset
    
    years = dataset.index.values
    first_year = dataset.isna().any(axis=1).idxmax() # Find first null value in the years rows
    last_year_index = len(years) - 1 # last year to predict
    train_index = list(years).index(first_year) - 1 # Index of the last year for which we have information
    dataset_full = dataset.copy()
    
    if verbose:
        print("Prediction started")
    
    for c in dataset.columns.values:
        if verbose:
            print("Predicting {}".format(c))
        country = dataframe[c]
        country = country.values[:train_index + 1] # Train data
        
        # Normalize train data
        country_mean = country.mean()
        country_std = country.std()
        country = (country - country_mean)/country_std
        
        # Predict
        country_full = make_pred(country, past_history, first_year, train_index, last_year_index)
        if verbose:
            print("{} finished".format(c))
        
        # Assing back
        new_country = new_country*country_std + country_mean
        dataset_full[c] = new_country
    
    if verbose:
        print("Prediction finished")
    
    return dataset_full
    

def prepare_data(dataset, start_index, end_index, history_size, target_size = 0):
    """Prepare data for the RNN by windowing and giving a 3D shape.
    Inputs:
        - dataset (numpy array): dataset with already known data
        - start_index (integer): first index to use in dataset for train
        - end_index (integer): last index to use in dataset for train
        - history_size (integer): length of the windows
        - target_size (integer, default 0): how far predict in the future (0 for the next step)"""
    
    data = []
    labels = []
    
    # Setting the index for the windows, with end_index = None we are considering the test set
    start_index = start_index + history_size
    if end_index is None:
        end_index = len(dataset) - target_size
    
    # Building the windows
    for i in range(start_index, end_index):
        indices = range(i-history_size, i)
        
        # Reshape data from (history_size,) to (history_size, 1)
        data.append(np.reshape(dataset[indices], (history_size, 1)))
        labels.append(dataset[i+target_size])
    
    return np.array(data), np.array(labels)


def make_pred(country, past_history, first_year, train_index, last_year_index, verbose = False):
    """Make prediction for a particolar country.
    Inputs:
        - country (numpy array): array containig the already known values for training
        - past_history (integer): window dimension to look back in the history to predict
        - first_year (integer): year from which start to predict (used only for verbose purpose)
        - train_index (integer): index of the last known year
        - last_year_index (integer): index of the last year to predict
        - verbose (bool, default False): defines if print or not logging messages
    Output:
        - country (numpy array): update array with prediction for the new years"""
    
    for i in range(train_index, last_year):
        if verbose:
            print("Predicting year {}..".format(first_year + i - train_index)) 
        
        # Open session for this training
        sess = tf.compat.v1.Session()
        
        # Preparing data
        country_train, y_train = prepare_data(country, 0, i, past_history)
        country_predict, y_predict = prepare_data(italy, i-past_history, None, past_history)
        
        # Constants for batching
        BATCH_SIZE = 256
        BUFFER_SIZE = 10000

        train = tf.data.Dataset.from_tensor_slices((country_train, y_train))
        train = train.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()

        to_pred = tf.data.Dataset.from_tensor_slices((country_predict, y_predict))
        to_pred = to_pred.batch(BATCH_SIZE).repeat()
        
        # Define model
        rnn_model = tf.keras.models.Sequential([
        tf.keras.layers.LSTM(8, input_shape=train.shape[-2:]),
        tf.keras.layers.Dense(1)
        ])

        rnn_model.compile(optimizer='adam', loss='mae')

        EVALUATION_INTERVAL = 200
        EPOCHS = 5

        rnn_model.fit(train, epochs=EPOCHS,
                              steps_per_epoch=EVALUATION_INTERVAL, verbose=0)
        
        # Make predictions
        new_pred = rnn_model.predict(to_pred, steps=1)
        
        # The new prediction is the last element of the new_pred vector (it predict also values we already have)
        country = np.append(country, new_pred[-1])
        
        # Cleaning the memory
        del country_train, y_train, country_predict, y_predict, train, to_pred, rnn_model, new_pred
        gc.collect()
        tf.keras.backend.clear_session()
        sess.close()
        for gcs in range(0, 3):
            gc.collect()
        
        if verbose:
            print("Year {} predicted".format(first_year + i - train_index))
        
    return country