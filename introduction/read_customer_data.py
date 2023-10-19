import os
import pandas as pd

def read_customer_data(filepath):
    df_final = pd.read_pickle(filepath)

    
    df_final=df_final.sort_values('CUSTOMER_ID')
    df_final.reset_index(drop=True,inplace=True)
    #  Note: -1 are missing values for realpi world data 
    df_final=df_final.replace([-1],0)
    
    return df_final

#example how to use the read customer data function
filepath = "training-data/customer.pkl" 
frame = read_customer_data(filepath)
print(frame.columns)

#print the first line of the dataframe line by line
for value in frame.iloc[0]:
    print(value)