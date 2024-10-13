import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the Excel file into a Pandas DataFrame
file_path = "rhe.xlsx"  # Replace with the actual path to your Excel file
data = pd.read_excel(file_path)

# Create the 'plots' directory if it doesn't exist
os.makedirs("plot_daily_sub2", exist_ok=True)

# Convert 'DOY' column to numeric and handle non-numeric values
data['DOY'] = pd.to_numeric(data['DOY'], errors='coerce').ffill()

# Ensure 'DOY' column has the same length as other columns
data = data.dropna(subset=['DOY'])

# Get unique years in the dataset
unique_years = data['YEAR'].unique()

# Iterate through each column and create individual plots for each year
for column in data.columns:
    if column not in ['DOY', 'YEAR']:  # Skip 'DOY' and 'YEAR' columns themselves
        sanitized_column_name = column.replace(" ", "_").replace("/", "_").replace(",", "").replace("(", "").replace(")", "")

        for year in unique_years:
            # Filter data for the current year
            year_data = data[data['YEAR'] == year]

            # Create a new plot for each year
            plt.figure(figsize=(10, 5))
            plt.plot(year_data['DOY'], year_data[column], label=f'{year}', color='blue')
            plt.ylabel(column)
            plt.xlabel('DOY')
            plt.title(f'{column} vs. DOY for Year {year}')
            plt.legend(loc='upper right')

            # Save the plot with the sanitized column name and year
            plt.savefig(f'plot_daily_sub2/{sanitized_column_name}_vs_Daily_average_{year}.png')

            plt.close()  # Close the plot to free memory

# Optionally, display a message indicating the completion
print("Plots saved to the 'plot_daily_sub' directory.")
