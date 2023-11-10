import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the CSV file into a Pandas DataFrame
file_path = "final_data_csv.csv"  # Replace with the actual path to your CSV file
data = pd.read_csv(file_path)

# Create the 'plots' directory if it doesn't exist
os.makedirs("plot_month", exist_ok=True)

# Convert 'Hour' column to numeric and handle non-numeric values
data['Hour'] = pd.to_numeric(data['Hour'], errors='coerce').ffill()

# Ensure 'Hour' column has the same length as other columns
data = data.dropna(subset=['Hour'])

# Extract the month from the 'DOY' column
data['Month'] = pd.to_datetime(data['DOY'], format='%j').dt.month

# Get unique years in the dataset
unique_years = data['YEAR'].unique()

# Create a color map with a unique color for each year
color_map = plt.cm.get_cmap('tab10', len(unique_years))

# Iterate through each column and create a separate plot for each year
for column in data.columns:
    # Replace invalid characters in the column name
    sanitized_column_name = column.replace(" ", "_").replace("/", "_").replace(",", "").replace("(", "").replace(")", "")

    for year in unique_years:
        year_data = data[data['YEAR'] == year]

        # Create a new figure with subplots
        fig, axs = plt.subplots(6, 2, figsize=(15, 20), sharex=True)
        fig.suptitle(f'{column} vs. Hour - Year {year}', y=0.92)  # Adjust the title position

        for i, month in enumerate(range(1, 13)):
            month_data = year_data[year_data['Month'] == month]
            row = i // 2
            col = i % 2
            axs[row, col].plot(month_data['Hour'], month_data[column], label=f'Month {month}', color=color_map(i))
            axs[row, col].set_title(f'Month {month}')
            axs[row, col].set_xlabel('Hour')
            axs[row, col].set_ylabel(column)
            axs[row, col].legend(title='Month', loc='upper right')

        plt.subplots_adjust(hspace=0.5)  # Adjust the vertical space between subplots

        # Save the plot with the sanitized column name and year
        plt.savefig(f'plot_month/{sanitized_column_name}_vs_Hour_Year_{year}_subplots.png')

        plt.close()  # Close the current figure

# Optionally, display a message indicating the completion
print("Plots saved to the 'plot_month' directory.")
