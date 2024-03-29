"""

for hourly plot

"""



import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the Excel file into a Pandas DataFrame
file_path = "lastes_daily_data.xlsx"  # Replace with the actual path to your Excel file
data = pd.read_excel("latest_hourly_data.xlsx")

# Create the 'plots' directory if it doesn't exist
os.makedirs("plot_hour_sub", exist_ok=True)

# Convert 'Hour' column to numeric and handle non-numeric values
data['DOY'] = pd.to_numeric(data['DOY'], errors='coerce').ffill()

# Ensure 'Hour' column has the same length as other columns
data = data.dropna(subset=['DOY'])

# Get unique years in the dataset
unique_years = data['YEAR'].unique()

# Create a color map with a unique color for each year
color_map = plt.cm.get_cmap('tab10', len(unique_years))

# Iterate through each column and create subplots for each year
for column in data.columns:
    # Replace invalid characters in the column name
    sanitized_column_name = column.replace(" ", "_").replace("/", "_").replace(",", "").replace("(", "").replace(")", "")

    # Create a new figure with subplots
    fig, axs = plt.subplots(len(unique_years), 1, figsize=(10, 5 * len(unique_years)), sharex=True)

    for i, year in enumerate(unique_years):
        year_data = data[data['YEAR'] == year]
        axs[i].plot(year_data['DOY'], year_data[column], label=str(year), color=color_map(i))
        axs[i].set_ylabel(column)

    axs[-1].set_xlabel('DOY')
    axs[-1].legend(title='Year', loc='upper left', bbox_to_anchor=(1, 1))  # Place legend outside the plot
    plt.suptitle(f'{column} vs. DOY', y=0.92)  # Adjust the title position
    plt.subplots_adjust(hspace=0.5)  # Adjust the vertical space between subplots

    # Save the plot with the sanitized column name
    plt.savefig(f'plot_hour_sub/{sanitized_column_name}_vs_Hour_average_subplots.png')

    plt.close()  # Close the current figure

# Optionally, display a message indicating the completion
print("Plots saved to the 'plot_hour_sub' directory.")
