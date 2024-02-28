
#Overview
Module contains information about machine learning."""

##Types of Learning
There are three main ways models can learn:

Supervised Learning: Models predict from labeled data (you got both features and labels, X and the Y)
Unsupervised Learning: Models identify patterns autonomously, where you don't have labeled date (you only got features no response variable, only X)
Reinforcement Learning: Algorithms learn via action feedback.


##Categories of Models
Here are most common ML model evaluation metrics per model type:

1. Regression Metrics:

MAE, MSE, RMSE: Measure differences between predicted and actual values.
R-Squared: Indicates variance explained by the model.

2. Classification Metrics:

Accuracy: Percentage of correct predictions.
Precision, Recall, F1-Score: Assess prediction quality.
ROC Curve, AUC: Gauge model's discriminatory power.
Confusion Matrix: Compares actual vs. predicted classifications.

3. Clustering Metrics:

Silhouette Score: Gauges object similarity within clusters.
Davies-Bouldin Index: Assesses cluster separation.


## Simple Linear Regression

Y = B0 + B1*X + ui

Here Y is the dependent variable.
X is the independent variable.
B0 is the intercept and is constant.
ui is the error term, representing the amount of errors the model makes when
predicting.

If multiple terms are added, B1*X1+B2*X2 etc. Then it is multiple linear
regression.


