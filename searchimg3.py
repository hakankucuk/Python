import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import os

folderName = input("Urunler fotu klasoru icin bir isim verin:")

isdir = os.path.isdir("images/" + folderName)

if isdir:
    print("aynı isimde bir klasör zaten mevcut...")
    quit()
else:
    os.mkdir("images/" + folderName)

#csv çıktısı alma
csv_file =  open("photoList.csv", 'w', encoding="utf-8")
csv_writer = csv.writer(csv_file, delimiter=",")

#Excel oku ve listeye çevir
data = pd.read_excel (r'yedekparca.xlsx') 

liste = []
for i in range(len(data)) :
    liste.append(data.loc[i, "Ürün/Hizmet Adı"].replace("'","")) 

sayac = 1
for line in liste:
    try:

        url = 'https://www.google.com/search?q={0}&tbm=isch'.format(line)
        content = requests.get(url).content
        soup = BeautifulSoup(content,'lxml')
        images = soup.findAll('img',limit=2)

        print(images.)

        row = [line.encode("utf8"),images[1].get('src')]
    except:
        row=[]

    csv_writer.writerow(row)
    print(f'Yapilan islem << {line} >> {sayac}/{len(liste)}...')
    sayac=sayac+1         
        
csv_file.close()