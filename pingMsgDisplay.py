#run this on the pi
import I2C_LCD_driver
import socket
import fcntl
import struct
import time
import subprocess
import traceback
import os

#This line opens a log file
#log = open("log.txt", "w")



mylcd = I2C_LCD_driver.lcd()

def get_txt_in_ping():
    #output = subprocess.check_output("hw4_10_21/getIP_withTCPDUMP.sh " + ifname, shell=True)


    with open('temp.txt','r') as myfile:
        TCPString = myfile.read()

    # file = open('temp.txt',mode='r')
    # all_of_it = file.read()
    # file.close()
    if TCPString.find('????') > 1:
        index = TCPString.find('????')
        containsMsg = TCPString[index+2:index+2+16]
        containsMsg = containsMsg.split("??")
        message = containsMsg[1]
    else:
        message = 'Waitng 4 ping...'
    return message


subprocess.call("/home/ssuee/hw4_10_21/getPingData.sh &", shell=True)
time.sleep(0.1)
tempFileModified = os.path.getmtime("/home/ssuee/temp.txt")
prevModified = tempFileModified

for i in range(0,500): #time out after x scans
    time.sleep(0.5)
    tempFileModified = os.path.getmtime("/home/ssuee/temp.txt")

    print('checking for file update')
    if prevModified != tempFileModified:
        print('file update detected')
        try:
            with open('temp.txt','r') as myfile:
                TCPString = myfile.read()
            if TCPString.find('????') > -1:
                print('message detected')
                #time.sleep(3.1)
                mylcd.lcd_write(0x01) # clear screen
                #mylcd.lcd_display_string('eth0, loop ' + str(i), 1)
                mylcd.lcd_display_string(get_txt_in_ping(), 1)

                print('rerunning sh script')
                subprocess.call("/home/ssuee/hw4_10_21/getPingData.sh &", shell=True)
                #tempFileModified = os.path.getmtime("/home/ssuee/temp.txt")
            elif TCPString.find('dead') > -1:
                print('rerunning sh script')
                subprocess.call("/home/ssuee/hw4_10_21/getPingData.sh &", shell=True)
                #tempFileModified = os.path.getmtime("/home/ssuee/temp.txt")
            else:
                print('message not detected')



        #except Exception:
        except Exception as e:
            print("failed to open file")
            # f = open('log.txt', 'w')
            # f.write('An exceptional thing happed - %s' % e)
            # f.close()
            #traceback.print_exc(file=log)
            continue
    prevModified = tempFileModified
