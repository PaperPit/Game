import pandas as pd
from itertools import chain

# Импортируем модуль pandas
import pandas as pd 
# Создаём объект DataFrame, загружая содержимое файла recipes.json
df = pd.read_json('recipes.json') 

# Выводим на экран первые строки полученного DataFrame
combined_set = set(chain.from_iterable(df['ingredients']))
print(len(combined_set))
#так быстро ?
#a;sdfj
#sadfasd
          