import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the CSV file into a Pandas DataFrame
file_path = "final_data_csv.csv"  # Replace with the actual path to your CSV file
data = pd.read_csv(file_path)

# Create the 'plots' directory if it doesn't exist
os.makedirs("plotsq", exist_ok=True)

# Exclude the 'YEAR' column if it exists
# if 'YEAR' in data.columns:
#     data = data.drop(columns=['YEAR'])

# Convert 'DOY' column to numeric and handle non-numeric values
data['DOY'] = pd.to_numeric(data['DOY'], errors='coerce').ffill()

# Ensure 'DOY' column has the same length as other columns
data = data.dropna(subset=['DOY'])

# Get unique years in the dataset
unique_years = data['YEAR'].unique()

# Create a color map with a unique color for each year
color_map = plt.cm.get_cmap('tab10', len(unique_years))

# Plot each column against the 'DOY' with a different color for each year
for column in data.columns:
    # Replace invalid characters in the column name
    sanitized_column_name = column.replace(" ", "_").replace("/", "_").replace(",", "").replace("(", "").replace(")", "")
    
    # Create a new figure for each plot
    plt.figure()

    for i, year in enumerate(unique_years):
        year_data = data[data['YEAR'] == year]
        plt.plot(year_data['DOY'], year_data[column], label=str(year), color=color_map(i))

    plt.xlabel('Day of Year (DOY)')
    plt.ylabel(column)
    plt.title(f'{column} vs. DOY')
    plt.legend(title='Year', loc='upper right')

    # Save the plot with the sanitized column name
    plt.savefig(f'plotsq/{sanitized_column_name}_vs_DOY.png')

    plt.close()  # Close the current figure

# Optionally, display a message indicating the completion
print("Plots saved to the 'plots' directory.")
