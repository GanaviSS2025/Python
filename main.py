import pandas as pd
import matplotlib.pyplot as plt

# Load files
csv_df = pd.read_csv('data.csv')
excel_df = pd.read_excel('data.xlsx')
json_df = pd.read_json('data.json')

# Clean data
csv_df.dropna(inplace=True)
excel_df.dropna(inplace=True)
json_df.dropna(inplace=True)

csv_df.reset_index(drop=True, inplace=True)
excel_df.reset_index(drop=True, inplace=True)
json_df.reset_index(drop=True, inplace=True)

# Merge
merged_df = pd.concat([csv_df, excel_df, json_df], ignore_index=True)

# Summary
print("Summary Statistics:")
print(merged_df.describe(include='all'))

# Chart
if 'lotsize' in merged_df.columns and 'tradedlots' in merged_df.columns:
    merged_df[['lotsize', 'tradedlots']].dropna().plot(kind='bar')
    plt.title("Lotsize vs Traded Lots")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.show()
else:
    print("No numeric columns found for plotting.")
