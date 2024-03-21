# Project Title: Rice Yield Prediction

## Introduction

Rice yield estimation is a critical aspect of agriculture, influencing food security, economic stability and resource allocation.
This Rice Yield Prediction project aims to develop a predictive model to estimate rice yields based on various factors. The models utilized for this project include Decision Tree Regressor, RandomForestRegressor and Support Vector Machine (SVM). By leveraging these machine learning algorithms, the goal is to enhance the accuracy of rice yield predictions, providing valuable insights for farmers and stakeholders in the agriculture sector.

### Problem Statement

The primary problem at hand is to develop predictive model for rice yield estimation that can provide accurate and timely forecasts, considering diverse geographical, climatic and agronomic factors. Accurate yield estimation is essential for farmers, policymakers, and the agricultural sector. It helps in making informed decisions regarding planting, resource allocation, and food distribution. This project aims to address the challenge of predicting rice crop yields based on multiple factors, including fertilizer usage, seedling quantity, land preparation methods and irrigation techniques.

### Objective:

The primary objective of this project is to create a reliable model that can predict rice yields accurately. This predictive capability can assist farmers in making informed decisions about crop management, resource allocation, and overall planning.

Other objectives include:
-	To collect historical data on rice production.
-	To Train and finetune the selected model.
-   To evaluate performance of the model.
-	To develop a machine learning model to predict rice yields.
-	To perform comparative analysis with other similar existing models.

## Methodology:
### Data Collection:
The dataset used for training and evaluating the models was obtained from Zindi Africa Digital Green Crop Estimate Challenge. It includes various factors that can impact the yield of rice crpos such as irrigation methods, fertilizers used, the quantity of seedlings planted, methods of land preparation and agricultural practices. The target variable is the rice yield, which is the quantity of rice produced per unit area across multiple districts in India.

### Data size
The dataset is divided into two parts: 'Train' and 'Test'. The 'Train' dataset contains the target variable (Yield) and it is used to train the predictive models. The 'Test' dataset resembles the 'Train' dataset but does not include the target variable. 

- Train dataset: 3870 rows and 44 columns
- Test dataset: 1290 rows and 43 columns

#### Data Exploration

The data exploration phase involved several steps, including:

- Identifying unique districts and blocks where agriculture is practiced.
- Analyzing the methods used in land preparation.
- Comparing the Cultivated Land and Crop Cultivated Land variables to understand the disparities in land usage.
- Examining the methods used in harvesting and threshing.

#### Data Cleaning

The data cleaning phase involved checking for duplicate rows in the "ID" column, and it was found that there were no duplicates. Additionally, missing values in the dataset were identified.

### Data Preprocessing:

Prior to model training, the dataset underwent preprocessing steps to handle missing values, normalize numerical features, and encode categorical variables. Feature engineering was also applied to extract relevant information and enhance model performance.

### Models and Approaches

Several models and approaches will be used to predict crop yields:

- **Statistical Models:** These models will use historical data on  yields, weather patterns, soil characteristics, and other relevant factors to make predictions. Time series analysis is an example of a statistical method that will be applied.

- **Machine Learning Models:** Machine learning techniques such as decision trees, random forests and support vector machines will be used to analyze complex interactions between various factors affecting  yields.

## Model Selection:
### Decision Tree Regressor:

The Decision Tree Regressor was chosen for its ability to capture non-linear relationships in the data. This model breaks down the data into a tree-like structure, making it interpretable and suitable for regression tasks.

### RandomForestRegressor:

The RandomForestRegressor was selected to improve predictive accuracy by combining multiple decision trees. This ensemble learning approach helps mitigate overfitting and enhances the model's generalization capabilities.

### Support Vector Machine (SVM):
The Support Vector Machine was incorporated for its effectiveness in handling complex datasets with high dimensionality. SVM aims to find the hyperplane that best separates data points, making it suitable for regression tasks.


### Model Performance Comparison

| Model             | Mean Absolute Error (MAE) | Mean Squared Error (MSE) | R-squared (R²) |
|-------------------|---------------------------|--------------------------|----------------|
| Decision Tree     | 88.72                     | 21341.95                 | 0.849         |
| Random Forest     | 19.575                    | 1690.31                  | 0.984         |
| Support Vector Machine (SVM) |198.927         | 90883.10                 | 0.185         |

In this comparison, the Random Forest model outperformed the other models in terms of MAE, MSE, and R² values. Therefore, it was selected as the model of choice for further yield predictions.

