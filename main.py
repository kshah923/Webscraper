# Kevin Shah
# Webscraper Assignment
# March 2021

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url = "http://18.206.38.144:8000/random_company"

count = []
df = pd.DataFrame(count, columns=['Name', 'Purpose'])

if __name__ == "__main__":
    for i in range(50):
        r = requests.get(url=url)
        soup = BeautifulSoup(r.text, features="html.parser")

        x = soup.find('ol')
        text = list(x.stripped_strings)

        name = filter(lambda a: 'Name:' in a, text)
        purpose = filter(lambda a: 'Purpose:' in a, text)
        a = list(name)
        a1 = str(a)[8:-2]
        b = list(purpose)
        b1 = str(b)[11:-2]

        df = df.append({'Name': a1, 'Purpose': b1}, ignore_index=True)
        df.index = np.arange(1, len(df) + 1)

print(df)
# df.to_csv('Webscraper.csv')
