import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import os

folderName = input("Urunler foto klasoru icin bir isim verin:")

isdir = os.path.isdir("images/" + folderName)

if isdir:
    print("aynı isimde bir klasör zaten mevcut...")
    quit()
else:
    os.mkdir("images/" + folderName)

#csv çıktısı alma
csv_file =  open("photoList.csv", 'w', encoding="utf-8",newline='')
csv_writer = csv.writer(csv_file, delimiter=",")

#Excel oku ve listeye çevir
data = pd.read_excel (r'yedekparca.xlsx') 

liste = []
for i in range(len(data)) :
    liste.append(data.loc[i, "Ürün/Hizmet Adı"].replace("'","")) 
i = 1
for line in liste:   
    
    try:
        url = 'https://www.google.com/search?q={0}&tbm=isch&tbs=isz:lt,islt:xga'.format(line)
        content = requests.get(url).content
        soup = BeautifulSoup(content,'lxml')
        images = soup.findAll('img',limit=2)

        with open('images/'+ folderName+'/' + str(i) +'.jpg', 'wb') as handle:
            response = requests.get(images[1].get('src'), stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
        row = ["http://teknoatik.com.tr/images/"+ folderName+"/" + str(i) +".jpg"]                                
    except:
        row = []
    
    csv_writer.writerow(row)
    print(f'islem {i}/{len(liste)}...')
    i=i+1
csv_file.close()