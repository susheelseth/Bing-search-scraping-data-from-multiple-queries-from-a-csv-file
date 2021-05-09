from bs4 import BeautifulSoup
import requests
import lxml
import csv
import pandas as pd

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

keywords = pd.read_csv('D:\\xampp\\htdocs\\Python\\Test\\duck\\input.csv', header=0, index_col=None)

df = pd.DataFrame(columns=['keyword', 'url'])

for keyword in keywords['keywords']:
    print(keyword)
    response = requests.get("https://www.bing.com/search?form=QBRE&q="  + keyword, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    for j in soup.select('.b_algo h2 a', limit=1):
        link = j['href']
        print(link)
    df = df.append({'keyword': keyword, 'url': link}, ignore_index=True)        

df.to_csv(r'D:\\xampp\\htdocs\\Python\\Test\\duck\\final_dataset.csv', index=False)

input(" press close to exit ")