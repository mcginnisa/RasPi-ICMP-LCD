#!/bin/python3
import sys, subprocess
text = sys.argv[2]
target = sys.argv[1]
text = '??' + text + '??'
if len(text)>16:
    print("Text too long!")
    exit()
enctext = r''.join( hex(ord(c)).split("x")[1] for c in text )
subprocess.check_output(["ping", "-p", enctext, "-c", "1", target])
