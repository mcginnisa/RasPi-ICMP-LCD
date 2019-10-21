#ping messages to the pi with this
#format is python3 sendTextOverPing.py 192.168.1.107 'hello world'

import sys
import subprocess

messageText = sys.argv[2]

messageText = '??' + messageText + '??'

if len(messageText)>16:
    print("16 chars or less!")

    exit()

messageHex = ''

for char in messageText:
    messageHex += hex(ord(char)).replace('0x', '')

subprocess.call("ping" + " -p " + messageHex + " -c " "1 " + sys.argv[1], shell=True)
