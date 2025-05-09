# Preprocessing Code for Synthetic Storage Dataset

# Step 1: Import Libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Step 2: Load the Dataset
df = pd.read_csv('synthetic_storage_dataset.csv')

# Step 3: Check Basic Info
print("Initial Dataset Info:")
print(df.info())
print("\nSample Data:")
print(df.head())

# Step 4: Handle Missing Values (if any)
# (In synthetic data, there should be none, but safe to check.)
if df.isnull().sum().sum() > 0:
    df = df.dropna()
    print("\nMissing values found and dropped.")

# Step 5: Normalize Numerical Columns
numerical_cols = ['File_Size_MB', 'Last_Accessed_Days_Ago', 'Number_of_Accesses', 'Noise_Level_Percent']

scaler = MinMaxScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

print("\nAfter Normalization:")
print(df[numerical_cols].head())

# Step 6: Encode Categorical Columns
# Encoding 'File_Type' using Label Encoding
encoder = LabelEncoder()
df['File_Type'] = encoder.fit_transform(df['File_Type'])

print("\nAfter Encoding File_Type:")
print(df['File_Type'].unique())

# Step 7: Create Storage Class Labels
# Rule: 
# - If Last Accessed < 90 days AND Number of Accesses > 5 → Short-Term (Label 0)
# - Else → Long-Term (Label 1)

df['Storage_Class'] = df.apply(lambda x: 0 if (x['Last_Accessed_Days_Ago'] < 0.5 and x['Number_of_Accesses'] > 0.5) else 1, axis=1)

print("\nStorage Class Distribution:")
print(df['Storage_Class'].value_counts())

# Step 8: Save the Preprocessed Dataset
df.to_csv('preprocessed_storage_dataset.csv', index=False)

print("\nPreprocessing Complete. Preprocessed file saved as 'preprocessed_storage_dataset.csv'.")