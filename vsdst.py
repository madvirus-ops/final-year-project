import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the Excel file into a Pandas DataFrame
file_path = "latest_daily_data.xlsx"  # Replace with the actual path to your Excel file
data = pd.read_excel(file_path)

# Create the 'vs_dst' directory if it doesn't exist
os.makedirs("vs_dst", exist_ok=True)

# Convert 'Hour' column to numeric and handle non-numeric values
data['DOY'] = pd.to_numeric(data['DOY'], errors='coerce').ffill()

# Ensure 'Hour' column has the same length as other columns
data = data.dropna(subset=['DOY'])

# Get unique years in the dataset
unique_years = data['YEAR'].unique()

# Iterate through each column and create separate plots for each year
for column in data.columns:
    # Replace invalid characters in the column name
    sanitized_column_name = column.replace(" ", "_").replace("/", "_").replace(",", "").replace("(", "").replace(")", "")

    # Create a new figure with subplots
    fig, axs = plt.subplots(len(unique_years), 1, figsize=(10, 5 * len(unique_years)), sharex=True)

    # Plot each column for each year along with corresponding DST data
    for i, year in enumerate(unique_years):
        year_data = data[data['YEAR'] == year]
        axs[i].plot(year_data['DOY'], year_data['Dst-index (nT)'], label=f'DST Index {year}', color='red')
        axs[i].plot(year_data['DOY'], year_data[column], label=str(year))
        axs[i].set_ylabel(f'{column} - {year}')
        axs[i].legend(title='Year', loc='upper right')

    axs[-1].set_xlabel('DOY')
    plt.suptitle(f'DST Index and {column} vs. DOY for Different Years', y=0.92)  # Adjust the title position
    plt.subplots_adjust(hspace=0.5)  # Adjust the vertical space between subplots

    # Save the plot with the sanitized column name
    plt.savefig(f'vs_dst/{sanitized_column_name}_with_DST_Index_vs_Daily_average_subplots.png')

    plt.close()  # Close the current figure

# Optionally, display a message indicating the completion
print("Plots saved to the 'vs_dst' directory.")
