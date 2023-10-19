import pandas as pd
import matplotlib.pyplot as plt

def read_terminal_data():
    filepath = "training-data/terminal.pkl" 
    df_final = pd.read_pickle(filepath)

    
    df_final=df_final.sort_values('TERMINAL_ID')
    df_final.reset_index(drop=True,inplace=True)
    #  Note: -1 are missing values for realpi world data 
    df_final=df_final.replace([-1],0)
    return df_final

def read_customer_data():
    filepath = "training-data/customer.pkl" 
    df_final = pd.read_pickle(filepath)
    
    df_final=df_final.sort_values('CUSTOMER_ID')
    df_final.reset_index(drop=True,inplace=True)
    #  Note: -1 are missing values for realpi world data 
    df_final=df_final.replace([-1],0)
    return df_final


terminal_profiles_table = read_terminal_data()
customer_profiles_table = read_customer_data()


terminals_available_to_customer_fig, ax = plt.subplots(figsize=(5,5))
number_of_terminals_to_print = 10

# Plot locations of terminals
ax.scatter(terminal_profiles_table.x_terminal_id.values[0:number_of_terminals_to_print], 
           terminal_profiles_table.y_terminal_id.values[0:number_of_terminals_to_print], 
           color='blue', label = 'Locations of terminals')

# Plot location of the last customer
customer_id=4
ax.scatter(customer_profiles_table.iloc[customer_id].x_customer_id, 
           customer_profiles_table.iloc[customer_id].y_customer_id, 
           color='red',label="Location of last customer")

ax.legend(loc = 'upper left', bbox_to_anchor=(1.05, 1))

# Plot the region within a radius of 50 of the last customer
circ = plt.Circle((customer_profiles_table.iloc[customer_id].x_customer_id,
                   customer_profiles_table.iloc[customer_id].y_customer_id), radius=50, color='g', alpha=0.2)
ax.add_patch(circ)

fontsize=15

ax.set_title("Green circle: \n Terminals within a radius of 50 \n of the last customer")
ax.set_xlim([0, 100])
ax.set_ylim([0, 100])
    
ax.set_xlabel('x_terminal_id', fontsize=fontsize)
ax.set_ylabel('y_terminal_id', fontsize=fontsize)

plt.show()