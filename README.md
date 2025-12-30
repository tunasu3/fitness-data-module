# fitness-data-module
“A module to analyze personal fitness data”

Overview
----------------------------------------------------------------------------------------------------------------------------------------------------------------
This project focuses on analyzing self-collected personal fitness data to understand activity patterns, wellness trends, and relationships between physical activity, calorie expenditure, and sleep. The project follows the complete data science workflow, including data collection, exploratory data analysis (EDA), hypothesis testing, and machine learning modeling.

Project Goals
----------------------------------------------------------------------------------------------------------------------------------------------------------------
By tracking daily fitness metrics, this project aims to:

- Understand personal activity patterns

- Identify factors affecting performance and wellness

- Provide insights to improve fitness habits and routines

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Motivation

Personal fitness data is often scattered across multiple applications and devices, making analysis difficult. By centralizing self-collected fitness data and applying data science techniques, this project aims to uncover meaningful trends, correlations, and behavioral patterns. Analyzing personal activity records enables a deeper understanding of daily routines and supports informed decisions toward a healthier lifestyle.

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Dataset

The dataset is self-collected and stored in Excel format. Each row represents one day of activity.

Features

- Date: Date of the record

- Workout Duration: Exercise duration in minutes

- Workout Type: Type of workout (e.g., Cardio, Strength)

- Calories Burned: Estimated calories burned per day

- Sleep Duration: Total hours of sleep

- Sleep Quality: Subjective sleep quality rating

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Data Collection

Data was collected using:

- Wearable devices (calories burned, activity data)

- Manual workout logs (duration and type)

- Sleep tracking applications (sleep duration and quality)

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Data Cleaning and Preprocessing

The following preprocessing steps were applied:

- Conversion of the date column to datetime format

- Verification of missing values

- Encoding of categorical variables (Workout Type, Sleep Quality)

- Feature engineering, including:

      - Workout Day (workout vs. rest day)

      - Weekday information

      - Activity Level (high vs. low activity)

- Detection and examination of outliers

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Exploratory Data Analysis (EDA)

EDA was conducted to identify trends and relationships in the data:

- Descriptive statistics (mean, median, standard deviation)

- Time-series analysis of workout duration, calories burned, and sleep duration

- Correlation analysis among numerical variables

- Visualizations using line plots, scatter plots, boxplots, and heatmaps

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Hypothesis Testing

The following hypotheses were tested using statistical methods:

- H1: Sleep duration is associated with calories burned
Method: Pearson correlation test

- H2: Calories burned differ between workout and non-workout days
Method: Independent two-sample t-test

- H3: Sleep duration differs between workout and non-workout days
Method: Independent two-sample t-test

- H4: Calories burned differ across weekdays
Method: One-way ANOVA

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Machine Learning Methods

Train-Test Split

The dataset was split into 80% training and 20% testing sets for supervised learning tasks.

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Regression

- Model: Linear Regression

- Target Variable: Calories Burned

- Features: Workout Duration, Sleep Duration, Workout Day

- Evaluation Metrics: RMSE, R² Score

The regression model demonstrated that workout duration and sleep duration are strong predictors of daily calorie expenditure.

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Classification

- Model: Logistic Regression

- Target Variable: Activity Level (High / Low Activity)

- Features: Sleep Duration, Calories Burned

- Evaluation Metrics: Accuracy, Precision, Recall, F1-score

Due to the small dataset size, the classification accuracy may be misleading. Since the model was trained on a limited number of samples, the reported performance metrics should be interpreted with caution. This highlights the importance of dataset size and diversity in supervised learning tasks.

To improve robustness, cross-validation can be applied to reduce evaluation bias.

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Clustering

- Model: KMeans

- Features: Workout Duration, Calories Burned, Sleep Duration

- Goal: Identify behavioral patterns such as high-activity and low-activity days

Clustering analysis revealed distinct activity patterns separating workout-intensive days from low-activity or rest days.

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Results Summary

- Workout duration and sleep duration are key factors influencing calorie expenditure

- Machine learning models successfully captured relationships in the fitness data

- Activity patterns differ clearly between high-activity and low-activity days

- Dataset size is a limiting factor for classification performance

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Limitations and Future Work

- Limited dataset size

- Low variability in sleep quality labels

- Future improvements may include:

    - Longer data collection period

    - Additional features such as heart rate and step count

    - Time-series forecasting approaches

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Technologies Used

- Python

- Pandas, NumPy

- Matplotlib, Seaborn

- Scikit-learn

- Jupyter Notebook / Google Colab
