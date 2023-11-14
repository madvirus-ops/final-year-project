# import pandas as pd
# import matplotlib.pyplot as plt
# import os

# # Read the CSV file into a Pandas DataFrame
# file_path = "final_data_csv.csv"  # Replace with the actual path to your CSV file
# data = pd.read_csv(file_path)

# # Create the 'plots' directory if it doesn't exist
# os.makedirs("histoc", exist_ok=True)

# # Get unique years in the dataset
# unique_years = data['YEAR'].unique()

# # Create a color map with a unique color for each year
# color_map = plt.cm.get_cmap('tab10', len(unique_years))

# # Iterate through each column and create a histogram for the number of data points against each year
# for column in data.columns:
#     # Replace invalid characters in the column name
#     sanitized_column_name = column.replace(" ", "_").replace("/", "_").replace(",", "").replace("(", "").replace(")", "")

#     plt.figure()
    
#     for i, year in enumerate(unique_years):
#         year_data = data[data['YEAR'] == year]
#         # plt.hist(year, len(year_data), color=color_map(i), label=str(year))
#         plt.hist(year, len(year_data), color=color_map(i), label=str(year), edgecolor='black')

#     plt.xlabel('Year')
#     plt.ylabel('Number of Data Points')
#     plt.title(f'Number of Data Points vs. Year for {column}')
#     plt.legend(title='Year', loc='upper right')

#     # Save the plot with the sanitized column name
#     plt.savefig(f'histoc/{sanitized_column_name}_data_points_vs_year.png')

#     plt.close()  # Close the current figure

# # Optionally, display a message indicating the completion
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Import seaborn for color maps

# Read the Excel file into a Pandas DataFrame
file_path = "lastes_daily_data.xlsx"  # Replace with the actual path to your Excel file
data = pd.read_excel("latest_daily_data.xlsx")

# Get unique years in the dataset
unique_years = data['YEAR'].unique()

# Define a color map with a unique color for each year
color_map = sns.color_palette("husl", len(unique_years))

# Iterate through each column and create a separate plot for each column
for column in data.columns:
    # Replace invalid characters in the column name
    sanitized_column_name = column.replace(" ", "_").replace("/", "_").replace(",", "").replace("(", "").replace(")", "")

    # Create a new figure for each column
    plt.figure(figsize=(15, 5 * len(unique_years)))

    # Iterate through each year and create a subplot for each year
    for i, year in enumerate(unique_years):
        # Filter data for the current year
        data_year = data[data['YEAR'] == year]

        # Plot histogram in the current subplot with a unique color
        plt.subplot(len(unique_years), 1, i + 1)
        plt.hist(data_year[column], bins=20, color=color_map[i], edgecolor='black')
        plt.xlabel('Number of Data Points')
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {column} for Year {year}')

    # Adjust layout and save the plot as an image
    plt.tight_layout()
    plt.savefig(f'histod_subplots/{sanitized_column_name}_data_points_vs_years.png')
    plt.show()

