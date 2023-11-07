import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the CSV file into a Pandas DataFrame
file_path = "final_data_csv.csv"  # Replace with the actual path to your CSV file
data = pd.read_csv(file_path)

# Create the 'plots' directory if it doesn't exist
os.makedirs("histod", exist_ok=True)

# Get unique years in the dataset
unique_years = data['YEAR'].unique()

# Create a color map with a unique color for each year
color_map = plt.cm.get_cmap('tab10', len(unique_years))

# Iterate through each column and create a histogram for the number of data points against each year
for column in data.columns:
    # Replace invalid characters in the column name
    sanitized_column_name = column.replace(" ", "_").replace("/", "_").replace(",", "").replace("(", "").replace(")", "")

    plt.figure()
    
    for i, year in enumerate(unique_years):
        year_data = data[data['YEAR'] == year]
        plt.bar(year, len(year_data), color=color_map(i), label=str(year))

    plt.xlabel('Year')
    plt.ylabel('Number of Data Points')
    plt.title(f'Number of Data Points vs. Year for {column}')
    plt.legend(title='Year', loc='upper right')

    # Save the plot with the sanitized column name
    plt.savefig(f'histod/{sanitized_column_name}_data_points_vs_year.png')

    plt.close()  # Close the current figure

# Optionally, display a message indicating the completion
print("Histograms saved to the 'plots' directory.")
