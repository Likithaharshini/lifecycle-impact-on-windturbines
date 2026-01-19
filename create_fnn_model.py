# create_fnn_model.py
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import pickle
import os

# ------------------ Ensure models directory exists ------------------
os.makedirs('models', exist_ok=True)

# ------------------ Example Training Data ------------------
# Replace these with your actual blade dataset
# Features: length, width, weight, circumference
# Labels: Metric1, Metric2, Metric3, Metric4

X = np.random.rand(100, 4)  # 100 samples, 4 features
y = np.random.rand(100, 4)  # 100 samples, 4 output metrics

# ------------------ Create Feedforward Neural Network ------------------
model = Sequential([
    Dense(64, activation='relu', input_shape=(4,)),  # input layer
    Dense(32, activation='relu'),                    # hidden layer
    Dense(4)                                         # output layer (4 metrics)
])

# Compile model
model.compile(optimizer='adam', loss='mse')

# Train model
model.fit(X, y, epochs=100, batch_size=8, verbose=1)

# ------------------ Save Model Using Pickle ------------------
model_path = 'models/assessment_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"FNN model trained and saved at '{model_path}'")