import pandas as pd
import matplotlib.pyplot as plt
import os

raw_data_path = 'exercises/vk1test/data/Acceleration without g 2024-09-08 16-30-53/Raw Data.csv'
raw_data = pd.read_csv(raw_data_path)

folder_path = os.path.dirname(raw_data_path)
new_file_name = 'yhdistetty_data.csv'
new_file_path = os.path.join(folder_path, new_file_name)

raw_data.to_csv(new_file_path, index=False)

df = pd.read_csv(new_file_path)

plt.plot(df['Time (s)'], df['Linear Acceleration x (m/s^2)'], label='x-komponentti', color='r')
plt.plot(df['Time (s)'], df['Linear Acceleration y (m/s^2)'], label='y-komponentti', color='g')
plt.plot(df['Time (s)'], df['Linear Acceleration z (m/s^2)'], label='z-komponentti', color='b')

plt.legend() 
plt.xlabel('Aika (s)')
plt.ylabel('Kiihtyvyys (m/s^2)')
plt.title('Kiihtyvyyden mittaus')
plt.grid(True)

plt.xlim(df['Time (s)'].min(), df['Time (s)'].max())
plt.ylim(df[['Linear Acceleration x (m/s^2)', 'Linear Acceleration y (m/s^2)', 'Linear Acceleration z (m/s^2)']].min().min(),
         df[['Linear Acceleration x (m/s^2)', 'Linear Acceleration y (m/s^2)', 'Linear Acceleration z (m/s^2)']].max().max())

pdf_path = os.path.join(folder_path, 'kuvaaja.pdf')
plt.savefig(pdf_path, format='pdf')
plt.show()

keskiarvo_x = df['Linear Acceleration x (m/s^2)'].mean()
keskiarvo_y = df['Linear Acceleration y (m/s^2)'].mean()
keskiarvo_z = df['Linear Acceleration z (m/s^2)'].mean()

keskihajonta_x = df['Linear Acceleration x (m/s^2)'].std()
keskihajonta_y = df['Linear Acceleration y (m/s^2)'].std()
keskihajonta_z = df['Linear Acceleration z (m/s^2)'].std()

print(f"Keskiarvo (x): {keskiarvo_x}") 
print(f"Keskiarvo (y): {keskiarvo_y}")
print(f"Keskiarvo (z): {keskiarvo_z}")

print(f"Keskihajonta (x): {keskihajonta_x}")
print(f"Keskihajonta (y): {keskihajonta_y}")
print(f"Keskihajonta (z): {keskihajonta_z}")
