# AIML Lab Experiment 4,5,6

This Repository contain Lab Experiment of Elements of AI/Ml Lab 

# Experiment-4 Overview :

"This Python program uses Pandas to efficiently import and export datasets, providing detailed insights including the number of rows and columns, dataset size, first five rows, missing value count, as well as the sum, average, minimum, and maximum values of numerical columns."

The Output of the Experiment-4 is provided in the word file  Output_Exp_4,5,6.docx

# Experiment -5 Overview: 

Perform exploratory data analysis on the dataset imported in Lab 4 using Python, uncovering key patterns, trends, and summary statistics.

Fig_1, Fig_2, Fig_3 and Fig_4 are the Output related to the experiment-5 

# Experiment-6 Overview:
Implement data preprocessing techniques to handle missing values and outliers on the dataset imported in Lab 4 or any other dataset.

Fig_5 is the Output related to the Experiment-6


# Customer churn Predictive Analysis 

This code performs a comprehensive exploratory data analysis (EDA) and data cleaning on a customer churn dataset to ensure data quality and suitability for analysis. Key steps include:

1.Data Loading and Initial Overview: The dataset is loaded, and its structure, data types, and missing values are inspected to understand the initial data quality.

2.Handling Missing Values:
   - Columns with over 50% missing values are dropped to retain only meaningful data.
   - Numeric columns are filled with the median, and categorical columns with the mode to preserve data integrity.

3.Outlier Detection and Management:
   - Outliers in numeric columns are detected using the Interquartile Range (IQR) method.
   - Outliers are either capped to specified limits or removed based on the analysis need, ensuring more robust data distribution.

4.Statistical Summaries and Visualizations:
   - Summary statistics for numeric and categorical columns reveal key insights.
   - Data patterns and correlations are visualized with heatmaps, distribution plots, and boxplots, highlighting relationships between features and the target variable (churn).

**Objective**: By addressing missing values and outliers, this process provides a cleaner dataset, reducing skewness and enhancing model performance in downstream analyses. This structured EDA and data preprocessing pipeline ensures a high-quality dataset for predictive modeling and analysis.


**Output of Predictive analysis of customer churn.docx** contain the results of the analysis 

Fig_6,Fig_7,Fig_8,Fig_9,Fig_10,Fig_11,Fig_12 are the output related to the customer_churn_EDA.py

Fig_13,Fig_14,Fig_15,Fig_16 are the output related to the customer_churn_handling_missing_values_outliers.py