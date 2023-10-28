# import pandas as pd

# data = pd.read_csv('fyp/final_data_csv.csv')

# # Convert 'DOY' to integer type
# data['DOY'] = data['DOY'].astype(int)

# # Group by the 'DOY' column and calculate the mean for each group along columns
# daily_average = data.groupby('DOY').mean()

# # Merge the daily averages back to the original data
# result = pd.merge(data, daily_average, how='left', on='DOY', suffixes=('', '_daily_avg'))

# # Print the result
# # print(result)

# # Save the result to Excel
# result.to_excel('result.xlsx', index=False)




# this worked
import pandas as pd

data = pd.read_csv('final_data_csv.csv')

# Convert 'DOY' to integer type
data['DOY'] = data['DOY'].astype(int)

# Group by 'Year' and 'DOY' columns and calculate the mean for each group along columns
yearly_daily_average = data.groupby(['YEAR', 'DOY']).mean()

# Reset the index to make 'Year' and 'DOY' as regular columns
yearly_daily_average.reset_index(inplace=True)

# Print the result
# print(yearly_daily_average)

# Save the result to Excel
yearly_daily_average.to_excel('average_daily.xlsx', index=False)
