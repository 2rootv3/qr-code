import qrcode as q
import os
banner='''
 ▄▄▄▄▄▄▄ ▄▄  ▄ ▄▄▄▄▄▄▄ 
 █ ▄▄▄ █ ▄▀▄ █ █ ▄▄▄ █ 
 █ ███ █ █▄▄█  █ ███ █ 
 █▄▄▄▄▄█ ▄ ▄ ▄ █▄▄▄▄▄█ 
 ▄▄▄▄  ▄ ▄▀█▀▀▄  ▄▄▄ ▄ 
 █▄██▄▀▄██▄▀▀ ▄ ▄▀ ▀▄█ 
   ▀▄█▄▄  ▀██▄  █▀▀ ▀▄ 
 ▄▄▄▄▄▄▄ ▀▄▄█▀▄ ▄▄ ▀ ▀ 
 █ ▄▄▄ █  ▄ █▄▀ ▄▄██▄▀ 
 █ ███ █ ██▄▄██ ▄ ▄▄▀  
 █▄▄▄▄▄█ █▄▄ ▀██▄  ▄ ▀ 
                       
                       '''
imageformet=".png"
os.system('clear')
print(banner)
print('Enter your ulr or msg ')
usr=input("=>")
print("Enter yor save file name")
usr2=input("=>")
qur = q.make(usr)
qur.save(usr2+imageformet)
print("The qr code was saved in png format")