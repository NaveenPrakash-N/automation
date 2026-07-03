from io import StringIO
import pandas as pd
import requests

url = 'https://en.wikipedia.org/wiki/List_of_anime_series_by_episode_count'
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
response.raise_for_status()  

tables = pd.read_html(StringIO(response.text))

anime_table = tables[1]
anime_table.rename(columns={'Runtime': 'Duration'}, inplace=True)

print(anime_table.to_string())

# anime_table.to_csv('anime_series_by_episode_count.csv', index=False)
