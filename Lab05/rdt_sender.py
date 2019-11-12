'''
        udp socket client
        rdt3.0 sender
'''

import socket  
import sys      #for exit
from check import ip_checksum

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
        print 'Failed to create socket'
        sys.exit()

host = 'localhost';
port = 8888;
seq_num = 0

while(1) :
        
	msg = str(seq_num)
	msg += raw_input('Enter message to send : ')
	# msg += str(ip_checksum(msg[1:]))
	msg += '9'	

        try :  
		s.sendto(msg, (host, port))
		print "Sending msg " + str(seq_num) + "...\n"
		s.settimeout(5)

		try: 		
			d = s.recvfrom(1024)
			reply = d[0]
			addr = d[1]
		except socket.timeout:
			print "timeout! resending...\n"
			s.sendto(msg, (host, port))
			d = s.recvfrom(1024)	
			reply = d[0]
			addr = d[1]	

		print reply
		expected_ACK = 'ACK' + str(seq_num)
		if reply == expected_ACK:
			print 'Correct packet ack received'
			if seq_num == 0:
				seq_num = 1
			else:
				seq_num = 0
		else:
			print 'Incorrect packet ack received'
			break

        except socket.error, msg:
                print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
                sys.exit()                        


