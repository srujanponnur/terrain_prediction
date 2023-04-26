# Terrain_prediction

This Project aims to train a deep learning model for predicting various terrains using the gyroscope and accelerometer data.

## Here is a brief description of the data

* _x files contain the xyz accelerometers and xyz gyroscope measurements from the lower limb  
* _x_time" files contain the time stamps for the accelerometer and gyroscope measurements. The units are in seconds and the sampling rate is 40 Hz
* "_y" files contain the labels. (0) indicates standing or walking in solid ground, (1) indicates going down the stairs, (2) indicates going up the stairs, and (3) indicates walking on grass.
* "_y_time" files contain the time stamps for the labels. The units are in seconds and the sampling rates is 10 Hz.

## The data set is imbalanced, the steps that were taken to handle the imbalance

* Validation set was created with the same distribution as that of train data in order to better represent the test data.
* Loss function includes the weights that compensates the imbalance distribution present in the dataset
* When doing data augmentation, you can make sure your training data is balanced by getting more replications (with some deformation / noise) for those classes that have fewer samples.
* You can also apply a subsampling approach when creating your batches which includes all the data for the smaller datasets but selects a smaller proportion from the classes with most instances (in order to keep the number per class about the same)

## Future Steps

* Data Augmentation techniques to balance the training dataset either by introducing some deformation / noise.

## Environment

* Python v3.9.7

* ### Steps to run the code

  * python -m venv /path/to/env
  * source env/bin/activate
  * Set up the enviroment using the requirements.txt (python -m pip install -r requirements.txt)
  * Run the baseline.ipyb file to train and evaluate the classical machine learning model
  * Run the CNN_window.ipynb to visualize, plot the data distributions and train CNN, LSTM, BiLSTM Model using Pytorch
  * Run the terrain_prediction_tf.ipynb notebook to train, visualize and evaluate the model using tensorflow