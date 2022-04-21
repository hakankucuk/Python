# -*- coding: utf-8 -*-
import socket# kütüphanemizi kullanmak üzere içeri aktarıyoruz
 
server=socket.socket() # bir socket nesnesi oluşturuyoruz
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # sokete yeniden bağlanmayı etkinleştiriyoruz
host="localhost" # yerel bilgisayarda çalıştıracağımız için localhost olarak belirliyoruz
port=9001 # bağlantıyı kabul edeceğimiz kapı numarası :)
server.bind((host,port)) # bağlantıyı kuruyoruz
server.listen(1) # 1 misafir dinlemek istediğimizi belirtiyoruz
print("Bağlantı bekleniyor...")
makine,bilgi=server.accept() # burada bir mesaj gönderen bekliyoruz ve bilgileri sol tarafa aktarıyoruz
print("Bir bağlantı kabul edildi".encode())
# bilgi, mesajın geldiği makinenin bilgilerini tutar
# makine değişkeni ise, mesaj gönderen adresi temsil eder. Bunu kullanarak geri mesaj göndeririz
mesaj=makine.recv(1024) # gelen mesajı alıyoruz
print(mesaj)
makine.send("Mesajınız alınmıştır!") # geri mesaj gönderiyoruz
 
# son olarak bağlantıyı kapatalım
server.close()