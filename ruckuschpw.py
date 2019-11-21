#!/usr/bin/env python 
import sys
import pexpect
import string
from random import randint
import email
import smtplib
import ssl

#chooses a random 8 digit number to use as the wifi password
n = 8
PW=''.join(["{}".format(randint(0, 9)) for num in range(0, n)])

PWSTR=("open wpa2 passphrase " + str(PW) + " algorithm AES")

#logs into the Zonedirector and changes the password of the SSID to the random password
child = pexpect.spawn ("ssh <IP address of target>")
child.expect ('Please login:') 
child.sendline ('<Username>') 
child.expect ('Password:') 
child.sendline ('<Password>') 
child.expect ('ruckus>')
child.sendline('enable')
child.expect ('ruckus#')
child.sendline('config')
child.expect('#')
child.sendline('wlan "<SSID>"')
child.expect('#')
child.sendline(PWSTR)
child.expect('#')
child.sendline('exit')
child.expect('#')
child.sendline('exit')
child.expect ('ruckus#')
child.sendline('exit')
#print (child.before) #this object refers to the output of the last child call 
#child.interact() #puts me on the AP CLI 
child.expect(pexpect.EOF, timeout=20)
sys.exit()


#Emails the new password to the specified emails
port = 465  # For SSL
password = str("<Email Password>")
sender_email = "<Email Account""
receiver_email = "<recipent1>","<recipent2>","<recipent3>
message = ("Subject: Guest Wifi Password"+"\n"+"\n"+"\n"+ "The new password for the Guest Wifi netowrk is: "+ str(PW))

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


sys.exit()
