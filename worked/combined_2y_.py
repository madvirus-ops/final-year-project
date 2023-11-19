import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the Excel file into a Pandas DataFrame
file_path = "lastes_daily_data.xlsx"  # Replace with the actual path to your Excel file
data = pd.read_excel("latest_daily_data.xlsx")

# Separate 2019 and non-2019 data
data_2019 = data[data['YEAR'] == 2019]
data_not_2019 = data[data['YEAR'] != 2019]

# Concatenate 2019 data to the front of 2020 data
data_combined = pd.concat([data_2019, data_not_2019], ignore_index=True)

# Create the 'plot_hourplaying' directory if it doesn't exist
os.makedirs("plot_seperate", exist_ok=True)

# Convert 'Hour' column to numeric and handle non-numeric values
data_combined['DOY'] = pd.to_numeric(data_combined['DOY'], errors='coerce').ffill()

# Ensure 'Hour' column has the same length as other columns
data_combined = data_combined.dropna(subset=['DOY'])

# Get unique years in the dataset
unique_years = data_combined['YEAR'].unique()

# Create a color map with a unique color for each year
color_map = plt.cm.get_cmap('tab10', len(unique_years))

# Iterate through each column and create subplots for each year
for column in data_combined.columns:
    # Replace invalid characters in the column name
    sanitized_column_name = column.replace(" ", "_").replace("/", "_").replace(",", "").replace("(", "").replace(")", "")

    # Create a new figure with subplots for each column
    fig, axs = plt.subplots(len(unique_years), 1, figsize=(10, 5 * len(unique_years)), sharex=True)

    # Plot data for the first two years on the same subplot
    for i, year in enumerate(unique_years[:2]):
        year_data = data_combined[data_combined['YEAR'] == year]
        axs[0].plot(year_data['DOY'], year_data[column], label=str(year), color=color_map(i))
    axs[0].set_ylabel(column)

    # Plot data for subsequent years on new subplots
    for i, year in enumerate(unique_years[2:]):
        year_data = data_combined[data_combined['YEAR'] == year]
        axs[i + 1].plot(year_data['DOY'], year_data[column], label=str(year), color=color_map(i + 2))
        axs[i + 1].set_ylabel(column)

    axs[-1].set_xlabel('DOY')

    # Add legends for all subplots
    for ax in axs:
        ax.legend(title='Year', loc='upper left', bbox_to_anchor=(1, 1))  # Place legend outside the plot

    plt.suptitle(f'{column} vs. DOY', y=0.92)  # Adjust the title position
    plt.subplots_adjust(hspace=0.5)  # Adjust the vertical space between subplots

    # Save the plot with the sanitized column name
    plt.savefig(f'plot_seperate/{sanitized_column_name}_vs_Hour_average_subplots.png')
    plt.close()  # Close the current figure

# Optionally, display a message indicating the completion
print("Plots saved to the 'plot_hourplaying' directory.")