# -*- coding: utf-8 -*-
import socket # aynı şekilde burada da içeri dahil ediyoruz
client=socket.socket() # bir socket nesnesi oluşturuyoruz
host="localhost" # bağlanacağımız adres
port=9001 # bağlanacağımız kapı



client.connect((host,port)) # bağlantı yapılıyor
print("Bağlantı yapıldı")
client.send("Mesaj: Coderistan was here!".encode()) # mesaj gönderiyoruz
mesaj=client.recv(1024) # geri gelen mesajı okuyoruz
print(mesaj)
client.close() # bağlantıyı kapatıyoruz