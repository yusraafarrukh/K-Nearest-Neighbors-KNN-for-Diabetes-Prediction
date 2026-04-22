# import joblib
# import json
# import pandas as pd

# # Load model
# model = joblib.load("knn_model.pkl")
# print("Model loaded successfully!")

# # Load feature names
# with open("feature_names.json") as f:
#     features = json.load(f)
# print("Features:", features)

# # Example input (must match feature order!)
# sample = [5, 166, 72, 19, 175, 25.8, 0.587, 51]

# # Put into a dataframe with correct column names
# sample_df = pd.DataFrame([sample], columns=features)

# # Predict
# prediction = model.predict(sample_df)

# print("Prediction (0 = no diabetes, 1 = diabetes):", prediction[0])



import os
import joblib
import json
import numpy as np

# ==============================
# Get base directory (important)
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==============================
# Load model
# ==============================
model_path = os.path.join(BASE_DIR, "..", "models", "knn_model.pkl")
model = joblib.load(model_path)
print("Model loaded successfully!")

# ==============================
# Load feature names
# ==============================
feature_path = os.path.join(BASE_DIR, "..", "config", "feature_names.json")

with open(feature_path) as f:
    features = json.load(f)

print("Features:", features)

# ==============================
# Take user input
# ==============================
print("\nPlease enter values for the following features:")

values = []
for feature in features:
    while True:
        try:
            val = float(input(f"{feature}: "))
            values.append(val)
            break
        except ValueError:
            print("Please enter a valid number.")

# ==============================
# Convert input to numpy array
# ==============================
sample = np.array([values])

# ==============================
# Make prediction
# ==============================
prediction = model.predict(sample)

# ==============================
# Output result
# ==============================
if prediction[0] == 1:
    print("\nResult: The patient is likely DIABETIC.")
else:
    print("\nResult: The patient is likely NOT DIABETIC.")