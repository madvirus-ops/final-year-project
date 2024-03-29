# # import pandas as pd

# # data = pd.read_csv('fyp/final_data_csv.csv')

# # # Convert 'DOY' to integer type
# # data['DOY'] = data['DOY'].astype(int)

# # # Group by the 'DOY' column and calculate the mean for each group along columns
# # daily_average = data.groupby('DOY').mean()

# # # Merge the daily averages back to the original data
# # result = pd.merge(data, daily_average, how='left', on='DOY', suffixes=('', '_daily_avg'))

# # # Print the result
# # # print(result)

# # # Save the result to Excel
# # result.to_excel('result.xlsx', index=False)




# # this worked
# import pandas as pd

# data = pd.read_csv('final_data_csv.csv')

# # Convert 'DOY' to integer type
# data['DOY'] = data['DOY'].astype(int)

# # Group by 'YEAR' and 'DOY' columns and calculate the mean for each group along columns
# yearly_daily_average = data.groupby(['YEAR', 'DOY']).mean()

# # Reset the index to make 'YEAR' and 'DOY' as regular columns
# yearly_daily_average.reset_index(inplace=True)

# # Print the result
# # print(yearly_daily_average)

# # Save the result to Excel
# yearly_daily_average.to_excel('average_daily.xlsx', index=False)


# promtp = "i want to plot all the other columns againt the hour. excluding the DOY and YEAR. the graph should one and thn they should be lable under that states the year for those data e.g 2019 start here and ends her should have a label below them"

# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd.read_csv('final_data_csv.csv')

# # Exclude 'DOY' column
# numeric_data = data.drop(['DOY'], axis=1)

# # Set a larger figure size
# fig, ax = plt.subplots(figsize=(12, 8))

# # Plot each column against 'Hour' with labels
# for column in numeric_data.columns:
#     ax.plot(numeric_data['Hour'], numeric_data[column], label=column, alpha=0.7)

# # Customize the plot
# ax.set_xlabel('Hour')
# ax.set_ylabel('Value')
# ax.legend(title='Column', bbox_to_anchor=(1, 1), loc='upper left')
# ax.set_title('Hourly Data for Each Column')

# # Adjust layout
# plt.tight_layout()

# # Save the figure with higher resolution
# plt.savefig('hourly_data_plot.png', dpi=300, bbox_inches='tight')

# # Show the plot
# plt.show()

# plt.show()






# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd.read_csv('final_data_csv.csv')

# # Exclude 'DOY' column
# numeric_data = data.drop(['DOY'], axis=1)

# # Set a larger figure size
# fig, ax = plt.subplots(figsize=(12, 8))

# # Define line styles for each column
# line_styles = ['-', '--', '-.', ':', '-', '--', '-.', ':', '-', '--']

# # Plot each column against 'Hour' with labels and line styles
# for column, style in zip(numeric_data.columns, line_styles):
#     ax.plot(numeric_data['Hour'], numeric_data[column], label=column, alpha=0.7, linestyle=style)

# # Customize the plot
# ax.set_xlabel('Hour')
# ax.set_ylabel('Value')
# ax.legend(title='Column', bbox_to_anchor=(1, 1), loc='upper left')
# ax.set_title('Hourly Data for Each Column')

# # Adjust layout
# plt.tight_layout()

# # Save the figure with higher resolution
# plt.savefig('hly_data_plot.png', dpi=300, bbox_inches='tight')

# # Show the plot
# plt.show()

# No need to show the plots here since they are saved individually
# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd.read_csv('final_data_csv.csv')

# Exclude 'DOY' and 'YEAR' columns
# numeric_data = data.drop(['DOY', 'YEAR'], axis=1)

# # Create a folder named "plots" if it doesn't exist
# output_folder = 'plots'
# os.makedirs(output_folder, exist_ok=True)

# # Iterate over each row to create separate plots
# for i, (index, row) in enumerate(numeric_data.iterrows()):
#     fig, ax = plt.subplots(figsize=(10, 6))

#     # Plot the row against 'Hour' with a unique color for each year
#     for year, color in zip(data['YEAR'].unique(), ['red', 'blue', 'green', 'purple']):
#         year_data = data[data['YEAR'] == year]
#         ax.plot(year_data['Hour'], row, label=f'Year {year}', alpha=0.7, color=color)

#     # Customize the plot
#     ax.set_xlabel('Hour')
#     ax.set_ylabel('Value')
#     ax.legend(title='Year', bbox_to_anchor=(1, 1), loc='upper left')
#     ax.set_title(f'Hourly Data for Row {index}')

#     # Save the figure with higher resolution into the "plots" folder
#     output_path = os.path.join(output_folder, f'hourly_data_row_{index}_plot.png')
#     plt.savefig(output_path, dpi=300, bbox_inches='tight')

#     # Close the plot to release memory
#     plt.close()

# No need to show the plots here since they are saved individually

# print(data)
# for row, col in data.items():
#     # plt.plot(row,col)
#     # plt.savefig("plt.png")
#     print(row)

# plt.plot(data[0],data[1])


# import pandas as pd
# import matplotlib.pyplot as plt

# # Read the CSV file into a Pandas DataFrame
# file_path = "final_data_csv.csv"  # Replace with the actual path to your CSV file
# data = pd.read_csv(file_path)
# data = data.drop(columns=['YEAR'])


# # Transpose the DataFrame
# transposed_data = data.set_index('DOY').T

# # Plot each variable against the 'DOY'

# for column in transposed_data.columns:
#     plt.plot(transposed_data[column],transposed_data.index,  label=f'{column}')
#     plt.xlabel('Day of Year (DOY)')
#     plt.ylabel('Values')
#     plt.title('Data vs. DOY')
#     plt.legend()
#     plt.savefig(f'plots/{column}_vs_DOY.png')
#     plt.close()  # Close the current figure to start a new one
# # Optionally, display a message indicating the completion
# print("Plots saved to the 'plots' directory.")





# Create the 'plots' directory if it doesn't exist
# os.makedirs("plots", exist_ok=True)

# # Exclude the 'Year' column if it exists
# if 'Year' in data.columns:
#     data = data.drop(columns=['Year'])

# # Plot each row against the 'DOY' and save to the 'plots' directory
# for index, row in data.iterrows():
#     plt.plot(data['DOY'], row, label=f'Row {index}')

#     plt.xlabel('Day of Year (DOY)')
#     plt.ylabel('Values')
#     plt.title(f'Data vs. DOY - Row {index}')
#     plt.legend()
    
#     # Save each plot with a unique filename
#     plt.savefig(f'plots/row_{index}_vs_DOY.png')
    
#     # Clear the current figure for the next iteration
#     plt.clf()

# # Optionally, display a message indicating the completion
# print("Plots saved to the 'plots' directory.")

# print(data['columns'])


