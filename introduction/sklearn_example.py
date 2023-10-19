import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os
import time
### See https://scikit-learn.org/stable/getting_started.html

# this function reads in all training data from a given start date to a given end date
# it returns the data in a pandas dataframe
# it removes the TX_DATETIME column because the ai model only works with numbers
def read_transaction_data(DIR_INPUT, BEGIN_DATE, END_DATE):
    
    files = [os.path.join(DIR_INPUT, f) for f in os.listdir(DIR_INPUT) if f>=BEGIN_DATE+'.pkl' and f<=END_DATE+'.pkl']

    frames = []
    for f in files:
        df = pd.read_pickle(f)
        frames.append(df)
        del df
    df_final = pd.concat(frames)
    
    df_final=df_final.sort_values('TRANSACTION_ID')
    df_final.reset_index(drop=True,inplace=True)
    #  Note: -1 are missing values for realpi world data 
    df_final=df_final.replace([-1],0)
    
    #drop the TX_DATETIME column because ai model only works with numbers
    return df_final.drop(["TX_DATETIME"], axis=1)

# Save list of strings to a textfile        
def write_list_to_text_file(filename, input_list):
    try:
        with open(filename, 'w') as file:
            for item in input_list:
                file.write(item + '\n')
        print(f"Successfully wrote {len(input_list)} items to {filename}")
    except IOError as e:
        print(f"Error writing to {filename}: {e}")


start_time = time.time()


filepath = "simulated-training-data-raw"
START_DATE = "2018-04-01" # adjust date here
END_DATE = "2018-04-01" # adjust date here
df = read_transaction_data(filepath, START_DATE, END_DATE)

# Splitting the data into features (X) and the target variable (y).
X = df.drop(['TX_FRAUD', "TX_FRAUD_SCENARIO"], axis=1)  # Features: All columns except the ones containing actual data about fraud
y = df['TX_FRAUD']  # Target variable: 'TX_FRAUD'


clf = RandomForestClassifier()

# Train model
clf.fit(X, y)

end_time = time.time()

print("Training done in ", end_time - start_time, " seconds")

# try model out for other data
df1 = read_transaction_data(filepath, "2018-09-02", "2018-09-02")

predictions = clf.predict(df1.drop(['TX_FRAUD', "TX_FRAUD_SCENARIO"], axis=1))


# count errors
errors = 0
count = 0
output = []

for index, item in enumerate(predictions):
    if item == 1:
        count += 1
        output.append(str(int(df1.iloc[index]["TRANSACTION_ID"])))
        if df1.iloc[index]["TX_FRAUD"] == 0:
            errors += 1
    else:
        if df1.iloc[index]["TX_FRAUD"] == 1:
            errors += 1
        
print("Predicted Frauds: ", count)
print("Actual Frauds: ", df1["TX_FRAUD"].value_counts().get(1, 0))

print("Errors: ", errors)

write_list_to_text_file("output.txt", output)