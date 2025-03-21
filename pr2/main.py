import pandas as pd
import time

file_path = 'pr2/music_sentiment_dataset.csv'
df = pd.read_csv(file_path)

# Випадковий User_ID для пошуку
search_user = 'U573'

# Пошук без індексу 
start_time = time.time()
result_no_index = df[df['User_ID'] == search_user]
no_index_time = time.time() - start_time

# Пошук із set_index() 
df_indexed = df.set_index('User_ID')

start_time = time.time()
result_with_index = df_indexed.loc[search_user]
with_index_time = time.time() - start_time

print("Результат без індексу:\n", result_no_index)
print("Час без індексу: {:.6f} секунд".format(no_index_time))

print("\nРезультат з індексом:\n", result_with_index)
print("Час з індексом: {:.6f} секунд".format(with_index_time))

# set_index() вийшов набагато швидшим