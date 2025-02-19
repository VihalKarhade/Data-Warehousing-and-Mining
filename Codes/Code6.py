#To design, create, and populate a data warehouse using sample data from multiple sources in Google Firestore. 

#First, install the required libraries.

#pip install pandas google-cloud-firestore


#Set up Firebase Firestore:
#Go to the Firebase console: https://console.firebase.google.com/
#Create a new project.
#Enable Firestore in the project.
#Set up authentication and get your service account key (JSON file). Save this file as serviceAccountKey.json.
#Create CSV files for regional sales data. 

#Follow this steps for Google Firebase Account:
#Step 1: Search on Google "Firebase"
#Step 2: Click on "Firebase Console"
#Step 3: Click on "Create a Project"
#Step 4:  "Enter your Project Name"
#Step 5: Go to Left Panel and Click on "Firestore Database"
#Step 6: "Create Database"
#Step 7: Go to "Project Overview Setting" -> "Project Setting" -> "Service Accounts"
#Step 8:  Click on "Generate Private Key"







import pandas as pd
from google.cloud import firestore

# Initialize Firestore DB
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "serviceAccountKey.json"
db = firestore.Client()

# Extract data from CSV files
df_region1 = pd.read_csv('region1_sales.csv')
df_region2 = pd.read_csv('region2_sales.csv')

# Transform data: Standardize column names and data types if necessary
df_region1['Region'] = 'Region1'
df_region2['Region'] = 'Region2'

# Load data into Firestore
def load_data_to_firestore(df, collection_name):
    for _, row in df.iterrows():
        doc_ref = db.collection(collection_name).document(str(row['OrderID']))
        doc_ref.set(row.to_dict())

load_data_to_firestore(df_region1, 'sales')
load_data_to_firestore(df_region2, 'sales')

# Verify the data loading
sales_ref = db.collection('sales')
docs = sales_ref.stream()

print("Data in Firestore:")
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
