#%% DOWNLOAD DATA
import yfinance as yf
keys = ['GOOG','IBM','MSFT']

for key in keys:
    df = yf.download(key, start='2023-01-05', end='2024-01-05')   
    df.to_csv(f'./data/{key}.csv')
#%%
#%%
import csv
def read_write_csv(input_file, output_file): 
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)  # Reading CSV content

    # Calculate 'Change' column
    for row in data:
        row['Change'] = (float(row['Close']) - float(row['Open'])) / float(row['Open'])

    # Append'Change' column
    fieldnames = reader.fieldnames + ['Change']

    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  
        writer.writerows(data)  

    print(f"CSV data from '{input_file}' processed with 'Change' column and written to '{output_file}'.")



keys = ['GOOG','IBM','MSFT']

for key in keys:
    input_csv_file = f'./data/{key}.csv'  # Replace with your input file name
    output_csv_file = f'./data/{key}_final.csv'  # Replace with your output file name

    read_write_csv(input_csv_file, output_csv_file)


# %%
