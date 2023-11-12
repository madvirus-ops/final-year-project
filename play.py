import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_data_graph(file_name: str, file_type: str, output_name: str):
    try:
        os.makedirs("akawu", exist_ok=True)
        data = pd.read_excel(file_name)

        # Convert 'Time' column to string
        data['Time'] = data['Time'].astype(str)

        plt.figure(figsize=(10, 6))  # Adjust the size as needed

        x = data['Time']
        y = data['Magnetic Field Strength']

        plt.plot(x, y, label=file_type)
        plt.xlabel("Time (min)")
        plt.ylabel("Magnetic Field Strength")
        plt.suptitle(f'Magnetic Field Strength vs Time {file_type}')

        plt.xticks(rotation=45)  # Rotate x-axis labels

        plt.savefig(f"akawu/{output_name}")
        plt.close()

        print("Plotted and saved")
        return True

    except Exception as e:
        print(str(e))
        return False

    
plot_data_graph("akawu/day1_near_330kv.xlsx","Near 330kv Day 1","near_330kv_day1.png")
plot_data_graph("akawu/day2_near_330kv.xlsx","Near 330kv Day 2","near_330kv_day2.png")
plot_data_graph("akawu/day1_near_fm_hostel.xlsx","Near Female Hostel Day 1","near_fm_hostel_day1.png")
plot_data_graph("akawu/day2_near_fm_hostel.xlsx","Near Female Hostel Day 2","near_fm_hostel_day2.png")