# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns  # Import seaborn for color maps
# import os

# # Read the Excel file into a Pandas DataFrame
# file_path = "lastes_daily_data.xlsx"  # Replace with the actual path to your Excel file
# data = pd.read_excel("latest_daily_data.xlsx")

# # Get unique years in the dataset
# unique_years = data['YEAR'].unique()
# os.makedirs("count_vs_year", exist_ok=True)

# # Define a color map with a unique color for each year
# color_map = sns.color_palette("husl", len(unique_years))

# # Iterate through each column and create a separate plot for the count of data points against the year
# for column in data.columns:
#     # Replace invalid characters in the column name
#     sanitized_column_name = column.replace(" ", "_").replace("/", "_").replace(",", "").replace("(", "").replace(")", "")

#     # Create a new figure for each column
#     plt.figure(figsize=(10, 6))

#     # Count the data points for each year
#     data_counts = data.groupby(['YEAR', column]).size().unstack(fill_value=0).sum(axis=1)

#     # Plot the bar plot with a unique color for each year
#     plt.bar(data_counts.index, data_counts.values, color=color_map, width=0.8)
#     plt.xlabel('Year')
#     plt.ylabel('Number of Data Points')
#     plt.title(f'Number of Data Points for {column} Against Year')
#     plt.xticks(rotation=45)
#     plt.tight_layout()

#     # Save the plot as an image
#     plt.savefig(f'count_vs_year/{sanitized_column_name}_data_points_vs_year.png')
#     plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Import seaborn for color maps
import os

# Read the Excel file into a Pandas DataFrame
file_path = "lastes_daily_data.xlsx"  # Replace with the actual path to your Excel file
data = pd.read_excel("latest_daily_data.xlsx")

# Get unique years in the dataset
unique_years = data['YEAR'].unique()
os.makedirs("count_vs_year_histogram", exist_ok=True)

# Define a color map with a unique color for each year
color_map = sns.color_palette("husl", len(unique_years))

# Iterate through each column and create a separate histogram for the count of data points against the year
for column in data.columns:
    # Replace invalid characters in the column name
    sanitized_column_name = column.replace(" ", "_").replace("/", "_").replace(",", "").replace("(", "").replace(")", "")

    # Create a new figure for each column
    plt.figure(figsize=(10, 6))

    # Count the data points for each year
    data_counts = data.groupby(['YEAR', column]).size().unstack(fill_value=0).sum(axis=1)

    # Plot the histogram with a unique color for each bar
    plt.hist(unique_years, data_counts, color="black", edgecolor='black', alpha=0.7)
    plt.xlabel('Year')
    plt.ylabel('Number of Data Points')
    plt.title(f'Histogram of Data Points for {column} Against Year')
    plt.xticks(unique_years)
    plt.tight_layout()

    # Save the plot as an image
    plt.savefig(f'count_vs_year_histogram/{sanitized_column_name}_data_points_vs_year.png')
    plt.show()

