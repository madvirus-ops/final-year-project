"""

for hourly plot

"""


import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the Excel file into a Pandas DataFrame
file_path = "average_daily.xlsx"  # Replace with the actual path to your Excel file
data = pd.read_excel(file_path)

# Create the 'plot_month' directory if it doesn't exist
os.makedirs("plot_month_subplots", exist_ok=True)

# Extract the month from the 'DOY' column
data['Month'] = pd.to_datetime(data['DOY'], format='%j').dt.month

# Get unique years in the dataset
unique_years = data['YEAR'].unique()

# Create a color map with a unique color for each year
color_map = plt.cm.get_cmap('tab10', len(unique_years))

# Plot average values for each month against the year in subplots
for column in data.columns:
    if column not in ['YEAR', 'DOY', 'Month']:
        # Replace invalid characters in the column name
        sanitized_column_name = column.replace(" ", "_").replace("/", "_").replace(",", "").replace("(", "").replace(")", "")

        # Determine the number of rows and columns for subplots
        num_years = len(unique_years)
        num_rows = num_years // 2 + num_years % 2  # Adjust for odd number of years
        num_cols = 2

        # Create a new figure with subplots for each year arranged side by side and then down
        fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(12, 4 * num_rows), sharex=True, sharey=True)

        for i, year in enumerate(unique_years):
            row = i // num_cols
            col = i % num_cols
            year_data = data[data['YEAR'] == year]
            avg_monthly_values = year_data.groupby('Month')[column].mean()
            axes[row, col].plot(avg_monthly_values.index, avg_monthly_values.values, label=str(year), color=color_map(i))
            axes[row, col].set_title(f'Average {column} vs. Month - {year}')
            axes[row, col].legend(loc='upper right')

        # Remove empty subplots
        for i in range(num_years, num_rows * num_cols):
            fig.delaxes(axes.flatten()[i])

        fig.suptitle(f'Average {column} vs. Month')
        fig.tight_layout(rect=[0, 0, 1, 0.95])

        # Save the plot with the sanitized column name
        plt.savefig(f'plot_month_subplots/{sanitized_column_name}_vs_Month_subplots.png')

        plt.close()  # Close the current figure

# Optionally, display a message indicating the completion
print("Subplots saved to the 'plot_month_subplots' directory.")
