# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('customer_churn_data.csv')

# Display the first few rows to understand the structure
print(df.head())

# 1. Statistical Summaries

# Basic statistics for numeric columns
print("\nStatistical summary of numeric columns:")
print(df.describe())

# Check for skewness and kurtosis in numerical columns (only numeric columns)
numeric_columns = df.select_dtypes(include=['number'])

print("\nSkewness of numeric columns:")
print(numeric_columns.skew())
print("\nKurtosis of numeric columns:")
print(numeric_columns.kurtosis())

# Summary for categorical columns
print("\nSummary of categorical columns:")
print(df.describe(include=['object']))

# Count unique values in each column to understand cardinality
print("\nUnique values per column:")
print(df.nunique())

# 2. Checking Churn Distribution

# Plot churn distribution to see class imbalance
plt.figure(figsize=(6, 4))
sns.countplot(x='Churn', data=df)
plt.title('Distribution of Churn')
plt.show()

# 3. Visualizing Relationships and Patterns

# Correlation heatmap for numeric variables
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_columns.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Numeric Features')
plt.show()

# Distribution plots for continuous variables
for column in numeric_columns.columns:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

# 4. Analyzing Churn with Categorical Variables

# Churn distribution by categorical features
categorical_columns = df.select_dtypes(include=['object']).columns

for column in categorical_columns:
    if column != 'Churn':  # Skip the target variable itself
        plt.figure(figsize=(8, 4))
        sns.countplot(x=column, hue='Churn', data=df)
        plt.title(f'Churn by {column}')
        plt.legend(title='Churn')
        plt.xticks(rotation=45)
        plt.show()

# 5. Examining Continuous Features in Relation to Churn

# Boxplots for continuous features to observe distribution by Churn
for column in numeric_columns.columns:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x='Churn', y=column, data=df)
    plt.title(f'{column} by Churn')
    plt.show()

# 6. Spotting Outliers

# Using boxplots to identify potential outliers in numeric features
for column in numeric_columns.columns:
    plt.figure(figsize=(6, 4))
    sns.boxplot(y=df[column])
    plt.title(f'Boxplot of {column} (Outlier Detection)')
    plt.show()
