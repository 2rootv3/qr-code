from termcolor import colored
import qrcode as q
import os
banner=colored('''
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
                       
                       ''','green')
imageformet=".png"
os.system('clear')
print(banner)
print(colored('Enter your ulr or msg ','yellow'))
usr=input(colored("=>",'red'))
print(colored("Enter yor save file name",'yellow'))
usr2=input(colored("=>",'red'))
qur = q.make(usr)
qur.save(usr2+imageformet)
print(colored("The qr code was saved in png format",'yellow'))
