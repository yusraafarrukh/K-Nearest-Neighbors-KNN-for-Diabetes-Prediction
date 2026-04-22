# K-Nearest Neighbors (KNN) for Diabetes Prediction

## Project Overview

This project implements the **K-Nearest Neighbors (KNN)** algorithm to predict whether a patient has diabetes using the **Pima Indians Diabetes Dataset**.

KNN is a **supervised machine learning algorithm** used for classification tasks. It classifies new data points based on the majority class of their nearest neighbors.

The objective of this project is to assist in the **early detection of diabetes** and support medical decision-making.

---

## Problem Statement

This is a **binary classification problem**:

- **Class 0:** Non-diabetic  
- **Class 1:** Diabetic  

A key challenge in this task is handling medical data with features of different scales, making **feature scaling essential** for accurate distance calculations.

---

## Dataset Information

- **Dataset:** Pima Indians Diabetes Dataset  
- **Source:** Kaggle  
- **Shape:** 768 rows × 9 columns  

### Features

- Pregnancies  
- Glucose  
- Blood Pressure  
- Skin Thickness  
- Insulin  
- BMI  
- Diabetes Pedigree Function  
- Age  

### Target

- **Outcome:** 0 (Non-diabetic), 1 (Diabetic)

---

## Methodology

### 1. Data Preprocessing
- Checked dataset structure and summary statistics  
- No missing values found  
- Applied **StandardScaler** for feature normalization  

### 2. Exploratory Data Analysis (EDA)
- Plotted histograms for all features  
- Observed variation in glucose and insulin levels  

### 3. Model Training
- Split dataset into:
  - **80% Training**
  - **20% Testing**

- Used KNN with:
  - **k = 11**
  - **Euclidean distance metric**

### 4. Model Evaluation
- Evaluated performance using:
  - Confusion Matrix  
  - Accuracy Score  

---

## Results

- **Accuracy:** Approximately **77–80%**

### Interpretation
- The model performs reasonably well in identifying diabetic patients  
- Some misclassification occurs due to overlapping feature values  
- Model performance is sensitive to the choice of **k**

---

## Why KNN?

### Comparison with Other Algorithms

**Logistic Regression**  
- Assumes linear relationships  
- KNN handles non-linear patterns effectively  

**Decision Trees**  
- Easier to interpret but prone to overfitting  
- KNN is simpler but computationally expensive  

**Support Vector Machine (SVM)**  
- Can achieve higher accuracy but requires complex tuning  
- KNN is easier to implement  

---

## Future Improvements

- Perform hyperparameter tuning to find the optimal value of **k**  
- Evaluate using additional metrics:
  - Precision  
  - Recall  
  - F1-score  
- Compare performance with advanced models like:
  - Random Forest  
  - Support Vector Machine (SVM)  

---

## Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  

---

## References

- Pima Indians Diabetes Dataset (Kaggle)  
- Cover, T., & Hart, P. (1967). *Nearest Neighbor Pattern Classification*  
- Scikit-learn Documentation  

---

## Authors

- **Yousra Farrukh (SP24-BAI-057)**  
