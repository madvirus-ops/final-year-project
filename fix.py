import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the CSV file into a Pandas DataFrame
file_path = "final_data_csv.csv"  # Replace with the actual path to your CSV file
data = pd.read_csv(file_path)

# Create the 'plots' directory if it doesn't exist
os.makedirs("plots", exist_ok=True)

# Exclude the 'YEAR' column if it exists
if 'YEAR' in data.columns:
    data = data.drop(columns=['YEAR'])

# Convert 'DOY' column to numeric and handle non-numeric values
data['DOY'] = pd.to_numeric(data['DOY'], errors='coerce').ffill()

# Ensure 'DOY' column has the same length as other columns
data = data.dropna(subset=['DOY'])

# Plot each column against the 'DOY' and save to the 'plots' directory
for column in data.columns:
    # Replace invalid characters in the column name
    sanitized_column_name = column.replace(" ", "_").replace("/", "_").replace(",", "").replace("(", "").replace(")", "")
    
    plt.plot(data['DOY'], data[column])
    plt.xlabel('Day of Year (DOY)')
    plt.ylabel(column)
    plt.title(f'{column} vs. DOY')
    
    # Save the plot with the sanitized column name
    plt.savefig(f'plots/{sanitized_column_name}_vs_DOY.png')
    
    plt.close()  # Close the current figure


# Optionally, display a message indicating the completion
print("Plots saved to the 'plots' directory.")
