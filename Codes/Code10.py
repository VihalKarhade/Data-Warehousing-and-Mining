#To implement pattern evaluation methods and evaluate the discovered patterns using support, confidence, and lift metrics. 

import pandas as pd 
from mlxtend.preprocessing import TransactionEncoder 
from mlxtend.frequent_patterns import apriori, association_rules 
# Load dataset 
df = pd.read_csv('dataset10.csv', quotechar='"', on_bad_lines='warn') 
# Pattern Mining using Apriori Algorithm 
# Convert the dataset into a list of transactions 
transactions = df['Items'].apply(lambda x: x.split(',')).tolist() 
# Convert the list of transactions into a format suitable for the Apriori algorithm 
te = TransactionEncoder() 
te_ary = te.fit(transactions).transform(transactions) 
df_trans = pd.DataFrame(te_ary, columns=te.columns_) 
# Apply the Apriori algorithm to find frequent itemsets 
frequent_itemsets = apriori(df_trans, min_support=0.2, use_colnames=True) 
print("Frequent Itemsets:") 
print(frequent_itemsets) 
# Pattern Evaluation 
# Generate association rules with metrics: support, confidence, and lift 
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1) 
# Display the association rules 
print("\nAssociation Rules:") 
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]) 
# Display the rules sorted by lift (or other metric) 
sorted_rules = rules.sort_values(by='lift', ascending=False) 
print("\nAssociation Rules Sorted by Lift:") 
print(sorted_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
