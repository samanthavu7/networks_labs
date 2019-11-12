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

seq_num = '100' # bogus initial value
while 1:
	d = s.recvfrom(1024)
	data = d[0]
	addr = d[1]
	
	if not data: 
		break
	
	prev_sn = seq_num	
	seq_num = data[0]	

	if data[-2:] != ip_checksum(data[1:-2]):
		print 'Packet corrupted' 	
	else:
		reply = 'ACK' + str(seq_num)
		# Add for scenario 3: time.sleep(8)
		s.sendto(reply , addr)

	if seq_num != prev_sn:
		print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()[1:-2]
	else:
		print 'Duplicate detected'
s.close()
