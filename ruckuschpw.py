#!/usr/bin/env python 
import sys
import pexpect
import string
from random import randint

n = 8
PW=''.join(["{}".format(randint(0, 9)) for num in range(0, n)])

PWSTR=("open wpa2 passphrase " + str(PW) + " algorithm AES")


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
