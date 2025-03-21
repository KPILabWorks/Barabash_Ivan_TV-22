import pandas as pd
import numpy as np

num_rows = 1000000

data = {
    'User_ID': [f'U{i}' for i in range(1, num_rows + 1)],
    'Power_W': np.random.randint(100, 1000, num_rows),
    'Temperature_C': np.random.randint(-10, 40, num_rows),
    'Factor': np.random.uniform(0.8, 1.2, num_rows)
}

df = pd.DataFrame(data)

file_name = 'generated_sensor_data.csv'
df.to_csv(file_name, index=False)

print(f"Файл '{file_name}' успішно створено!")