'''
        udp socket client
        rdt3.0 sender
'''

import socket  
import sys      #for exit
from check import ip_checksum
import threading

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
        print 'Failed to create socket'
        sys.exit()

host = 'localhost';
port = 8888;

def recv_thread(basie):
	d = s.recvfrom(1024)
	reply = d[0]

	while reply[3] != str(base % (2 * N + 1)):	
		d = s.recvfrom(1024)
		reply = d[0]		
	
	print "Receiving msg " + str(reply)

TIMEOUT = 2
N = 4
base = 0
nextseqnum = 0
index = 0
messages = ['Hello', 'my', 'name', 'is', 'Billy', 'Bob', 'Joe', 'James', 'Amanda', 'Katie', 'Eric', 'Kim', 'Bradley', 'yee', 'haw']

# main function
while 1:
	if index >= base and index < base + N and index < len(messages):
#		if(base == nextseqnum):
#			msg0 = str(nextseqnum) + messages[index] + str(ip_checksum(messages[index]))
#			msg1 = str(nextseqnum + 1) + messages[index + 1] + str(ip_checksum(messages[index + 1]))
#			msg2 = str(nextseqnum + 2) + messages[index + 2] + str(ip_checksum(messages[index + 2]))
#			msg3 = str(nextseqnum + 3) + messages[index + 3] + str(ip_checksum(messages[index + 3]))
			
#			s.sendto(msg0, (host, port))
#			s.sendto(msg1, (host, port))
#			s.sendto(msg2, (host, port))
#			s.sendto(msg3, (host, port))

#			print "Sending msg " + str(msg0[0]) + ": " + str(msg0[1:-2])
#			print "Sending msg " + str(msg1[0]) + ": " + str(msg1[1:-2])
#			print "Sending msg " + str(msg2[0]) + ": " + str(msg2[1:-2])
#			print "Sending msg " + str(msg3[0]) + ": " + str(msg3[1:-2])

			#if index == 2:
			#	msg = str(nextseqnum) + messages[index] + str(99)

#			x = threading.Thread(target = recv_thread, args=(base,))
#			x.start()
#			x.join(TIMEOUT)

#			while x.isAlive():
#                        	s.sendto(msg0, (host, port))
#	                        s.sendto(msg1, (host, port))
#        	                s.sendto(msg2, (host, port))
#                	        s.sendto(msg3, (host, port))

#                        	print "Resending msg " + str(msg0[0]) + ": " + str(msg0[1:-2])
#	                        print "Resending msg " + str(msg1[0]) + ": " + str(msg1[1:-2])
#        	                print "Resending msg " + str(msg2[0]) + ": " + str(msg2[1:-2])
#                	        print "Resending msg " + str(msg3[0]) + ": " + str(msg3[1:-2])

#				x = threading.Thread(target = recv_thread, args=(base,))
#				x.start()
#				x.join(TIMEOUT)	

#			index = index + 4
#                	nextseqnum = index % (N * 2 + 1)
#              	 	base = base +1

		msg = str(nextseqnum) + messages[index] + str(ip_checksum(messages[index]))
		s.sendto(msg, (host, port))
                print "Sending msg " + str(msg[0]) + ": " + str(msg[1:-2])

		x = threading.Thread(target = recv_thread, args=(base,))
                x.start()
                x.join(TIMEOUT)

                while x.isAlive():
			for r in range(base, base + 3):
				msg = str(r % (N * 2 + 1)) + messages[r] + str(ip_checksum(messages[r]))
                       		s.sendto(msg, (host, port))
                       		print "Sending msg " + str(msg[0]) + ": " + str(msg[1:-2]) 

			x = threading.Thread(target = recv_thread, args=(base,))
                        x.start()
       	                x.join(TIMEOUT)

		index = index + 1
                nextseqnum = index % (N * 2 + 1)
                base = base + 1
              
s.close()
