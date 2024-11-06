# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('customer_churn_data.csv')

# Display initial data structure and info
print("Initial Data Overview:")
print(df.info())
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# 1. Handling Missing Values

# Drop columns with a large number of missing values, if any
# Here, it's assumed that if any column has more than 50% missing values, we drop it
threshold = len(df) * 0.5
df = df.dropna(thresh=threshold, axis=1)

# Filling missing values for numeric columns with median (better for skewed distributions)
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_columns:
    df[col].fillna(df[col].median(), inplace=True)

# Filling missing values for categorical columns with mode (most frequent value)
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Verify missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 2. Detecting and Managing Outliers

# Using IQR (Interquartile Range) method to detect and handle outliers in numeric columns
for col in numeric_columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Outliers below the lower bound or above the upper bound
    outliers = (df[col] < lower_bound) | (df[col] > upper_bound)

    # Option 1: Cap outliers to the lower and upper bounds
    df.loc[df[col] < lower_bound, col] = lower_bound
    df.loc[df[col] > upper_bound, col] = upper_bound

    # Option 2: Remove outlier rows (optional)
    # df = df[~outliers]

# Verify the cleaned data
print("\nData Overview After Cleaning:")
print(df.describe())

# Visualize the cleaned data for outlier confirmation
for col in numeric_columns:
    plt.figure(figsize=(6, 4))
    sns.boxplot(y=df[col])
    plt.title(f'Boxplot of {col} (After Outlier Management)')
    plt.show()
