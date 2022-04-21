import requests
from bs4 import BeautifulSoup
import csv

csv_file =  open("sample_file.csv", 'w', encoding="utf-8")
csv_writer = csv.writer(csv_file, delimiter=",")

import os
with open('c:\\temp\search.txt', encoding='utf8') as f:
        contents = f.readlines()    
        liste = contents[0].split(",") 
        i = 1
        for line in liste:   
            url = 'https://www.google.com/search?q={0}&tbm=isch'.format(line)
            content = requests.get(url).content
            soup = BeautifulSoup(content,'lxml')
            images = soup.findAll('img',limit=2)
            print(images[1].get('src'))
            row = [line.encode("utf8"),images[1].get('src')]
            csv_writer.writerow(row)
            print(f'islem {i}/{len(liste)}...')
            i=i+1
            
        
csv_file.close()