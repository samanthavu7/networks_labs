'''
	Simple udp socket server
	rdt3.0 receiver
'''

import socket
import sys
import time
from check import ip_checksum

HOST = ''	
PORT = 8888	

try :
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print 'Socket created'
except socket.error, msg :
	print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
	
print 'Socket bind complete'

N = 4
expectedseqnum = 0
lastseqnum = 100
while 1:
	d = s.recvfrom(1024)
	data = d[0]
	addr = d[1]
	print 'Received message ' + str(data[0]) + ': ' + str(data[1:-2])
	
	if data[-2:] != ip_checksum(data[1:-2]):
		print 'Packet corrupted'
	elif data[0] == str(expectedseqnum): 	
		reply = 'ACK' + str(expectedseqnum)
		s.sendto(reply, addr)
		print 'Sending message ' + str(reply)
		lastseqnum = expectedseqnum
		expectedseqnum = (expectedseqnum + 1) % (N * 2 + 1)
	else: 
		reply = 'ACK' + str(lastseqnum)
		s.sendto(reply, addr)
		print 'Sending message ' + str(reply)

s.close()

