#import pandas as pd
#from mlxtend.preprocessing import TransactionEncoder
#from mlxtend.frequent_patterns import apriori, association_rules
#try:
#    df=pd.read_csv('dataset9.csv',quotechar="",on_bad_lines='warn')

 #   transactions=df['Items'].apply(lambda x: x.split(',')).tolist()

  #  te=TransactionEncoder()
   # te_ary=te.fit(transactions).transform(transactions)
    #df_trans=pd.DataFrame(te_ary, columns=te.columns_)

    #frequent_itemsets=apriori(df_trans, min_support=0.2, use_colnames=True)
   # print("Frequent Itemsets:")
    #print(frequent_itemsets)

#    rules=association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)
 #   print("\nAssociation Rules:")
  #  print(rules)

#except Exception as e:
 #   print(f"An error occurred: {e}")





import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Load dataset with error handling
try:
    # Use on_bad_lines='warn' to skip problematic lines and display a warning
    df = pd.read_csv('dataset9.csv', quotechar='"', on_bad_lines='warn')
   
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

    # Generate association rules
    rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)
    print("\nAssociation Rules:")
    print(rules)

except Exception as e:
    print(f"An error occurred: {e}")
