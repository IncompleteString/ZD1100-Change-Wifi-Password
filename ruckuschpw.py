#!/usr/bin/env python 

import sys
import pexpect
import string
from random 
import randint
import email
import smtplib
import ssl

#chooses a random 8 digit number to use as the wifi password
print("creating a random 8 digit wifi password")
n = 8 #selects number of digits in random number
PW=''.join(["{}".format(randint(0, 9)) for num in range(0, n)]) #generates a random number of "N" digits




#Varibles for use in logging into and controlling the zonedirector
Target=str("<Target Device IP>")
username=str("<username of zonedirector")
password=str("<password of zonedirector>")
WLAN=str('"<Name of SSID>"') #observe the double quotes, this is necessary if there is a space in your SSID
Command=("open wpa2 passphrase " + str(PW) + " algorithm AES") # command to be passed to the zonedirector

#logs into the Zonedirector and changes the password of the SSID to the random number generated above
print("logging into the zonedirector")
child = pexpect.spawn ("ssh "+Target)
child.expect ('Please login:') 
child.sendline (username) 
child.expect ('Password:') 
child.sendline (password) 
#child.interact() #uncomment this is you want to pass the ssh connection through to your CLI
child.expect ('ruckus>')
child.sendline('enable')
child.expect ('#')
child.sendline('config')
child.expect('#')
child.sendline("wlan "+WLAN)
child.expect('#')
child.sendline(Command)
child.expect('#')
child.sendline('exit')
child.expect('#')
child.sendline('exit')
child.expect ('#')
child.sendline('exit')
print (child.before) #prints the last child call
child.expect(pexpect.EOF, timeout=20)





#Emails the new password to the specified email addresses
print("Emailing password to specified emails")
port = 465  #SSL Port Number
sender_email = "<Email Account>" #email account that will be sending the messages
emailpassword = str("<Email Password>") #Password of the email address sending the messages
receiver_email = "<recipent1>","<recipent2>","<recipent3>" #email addresses that will recieve the message
message = ("Subject: Guest Wifi Password"+"\n"+"\n"+"\n"+ "The new password for the Guest Wifi netowrk is: "+ str(PW)+"\n"+"\n"+"\n"+"Place Holder." +"\n"+"\n"+"\n""Place Holder")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, emailpassword)
    server.sendmail(sender_email, receiver_email, message)


print("Success!")
sys.exit()
