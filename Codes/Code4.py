#Reduce the dataset's dimensions by selecting relevant features or performing dimensionality reduction. 

import pandas as pd

# Load datasets
df1 = pd.read_csv('dataset1.csv')
df2 = pd.read_csv('dataset2.csv')

# Display the original data
print("Original Data Part 1:")
print(df1)
print("\nOriginal Data Part 2:")
print(df2)

# Handling missing values
# Fill missing 'age' and 'income' with the mean of the column
df1['age'].fillna(df1['age'].mean(), inplace=True)
df1['income'].fillna(df1['income'].mean(), inplace=True)

# Fill missing 'gender' with the mode of the column
df1['gender'].fillna(df1['gender'].mode()[0], inplace=True)

# Display cleaned data
print("\nCleaned Data Part 1:")
print(df1)




# Concatenate the datasets
df = pd.concat([df1, df2], ignore_index=True)

# Display integrated data
print("\nIntegrated Data:")
print(df)








from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Select relevant features
features = df[['age', 'income']]

# Perform PCA for dimensionality reduction
pca = PCA(n_components=1)
reduced_data = pca.fit_transform(features)

# Create a DataFrame with the reduced data
df_reduced = pd.DataFrame(reduced_data, columns=['principal_component'])
df_reduced['id'] = df['id']
df_reduced['gender'] = df['gender']

# Display reduced data
print("\nReduced Data:")
print(df_reduced)

# Plot the reduced data
plt.figure(figsize=(8, 6))
plt.scatter(df_reduced['principal_component'], df_reduced['gender'].apply(lambda x: 1 if x == 'Male' else 0), c='blue')
plt.title('Reduced Data')
plt.xlabel('Principal Component')
plt.ylabel('Gender (0=Female, 1=Male)')
plt.show()
