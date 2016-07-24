#!/usr/bin/python

import socket
import struct
import sys

if len(sys.argv) != 2:
    print "Usage: " + sys.argv[0] + " [port]"
    sys.exit(1)

DEST_IP = '127.0.0.1'
DEST_PORT = int(sys.argv[1])
MESSAGE = "Hello\n"

def convert(message):
    raw = ''
    raw += struct.pack("<I", len(message))
    raw += message
    return raw


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((DEST_IP, DEST_PORT))
s.send(convert(MESSAGE))

data = s.recv(1024)
s.close()

print "Received data: ", data
