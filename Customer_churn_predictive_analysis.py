# Import the necessary library
import pandas as pd

# Load the dataset
# Replace 'your_dataset.csv' with the actual file path or dataset name
df = pd.read_csv('customer_churn_data.csv')

# Display the first few rows of the dataset to understand its structure
print("First few rows of the dataset:")
print(df.head())

# Show the column names and number of rows and columns in the dataset
print("\nDataset shape (rows, columns):", df.shape)
print("Column names:", df.columns.tolist())

# Check data types of each column
print("\nData types of each column:")
print(df.dtypes)

# Check for missing values
print("\nCount of missing values in each column:")
print(df.isnull().sum())

# Get basic statistics on numeric columns
print("\nStatistical summary of numeric columns:")
print(df.describe())

# Get a summary of non-numeric columns
print("\nSummary of non-numeric columns:")
print(df.describe(include=['object']))
