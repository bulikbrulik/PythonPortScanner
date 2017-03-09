import argparse
import socket
import subprocess
import sys
from datetime import datetime

#Start tracking time
startTime = datetime.now()

#Get arguments from command line
parser = argparse.ArgumentParser(description='Scan the specified port(s) of the indicated host(s). Can scan a range of hosts and ports. Can also specify to do UDP scan instead of default TCP')
parser.add_argument('-t', required=True, help='The target host or range of hosts to be scanned.\n May specify range or subnet mask, eg. 192.168.207.2-255 or 192.168.207.0/24)', metavar="Target")
parser.add_argument('-p', required=True, help='The ports or range of ports to be scanned.\n Specify range as such: 100-1000', metavar="Port") 
parser.add_argument('-sU', '--udpscan', action='store_true', help='Enable this for UDP scans. Default is TCP')
args = parser.parse_args()

try:
	#Parse the target argument
	host = args.t
	if "-" in host:
		pieces = host.split("-")
		subPieces = pieces[0].split(".")
		targetStart = int(subPieces[3])
		targetEnd = int(pieces[1])+1
		host = ".".join(subPieces[0:3])
	elif "/" in host:
		targetStart=1
		pieces = host.split("/")
		targetEnd = 2**(32-int(pieces[1]))
		subPieces = pieces[0].split(".")
		host = ".".join(subPieces[0:3])
	else:
		pieces = host.split(".")
		targetStart = int(pieces[3]);
		targetEnd = targetStart + 1;
		host = ".".join(pieces[0:3])
	if targetStart > 255 or targetEnd > 256:
		raise IOError
	#Parse the port argument
	portIn = args.p
	ports = []
	if "-" in portIn:
		ppieces = portIn.split("-")
		portStart = int(ppieces[0])
		portEnd = int(ppieces[1])+1
		for port in range(portStart, portEnd):
			ports.append(int(port))
	elif "," in portIn:
		ppieces = portIn.split(",")
		for p in ppieces:
			ports.append(int(p))
	else:
		ports.append(int(portIn))
		

except ValueError:
	print("ERROR: Invalid character.")
	sys.exit()
except IOError:
	print("ERROR: Host or port is out of range.")
	sys.exit()

print("-" * 60)
print("Scanning...")
print("-" * 60)

#iterate through targets
for target in range(targetStart,targetEnd):
	try:
		remoteServer=host+"."+str(target)
		
		print(remoteServer)
		#iterate through ports		
		for port in ports:
			#if TCP
			if args.udpscan == False:
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.settimeout(0.2)
					s.connect((remoteServer, port))
				except Exception:
					print("\tPort " + str(port) + ":\ttcp\tClosed")
				else:
					print("\tPort " + str(port) + ":\ttcp\tOpen")
				s.close()
			#if UDP			
			else:
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					s.settimeout(1)
					s.sendto("--Some Content to Test--", (remoteServer, port))
					recv, svr = s.recvfrom(1024)
					print("\tPort " + str(port) + ":\tudp\tOpen")
				except Exception as e:
					print(e)
					try: errno, errtxt = e
					except ValueError as w:
						print("\tPort " + str(port) + ":\tudp\tFiltered|Open")
					else:
						print("\tPort " + str(port) + ":\tudp\tClosed")
				s.close()			
		print("\n")

#Catch invalid hosts
	except socket.gaierror:
		print("Hostname '" + remoteServer + "' could not be resolved.")

	#Catch socket errors
	except socket.error:
		print("Could not connect to remote host '" + remoteServer + "'.")

	#Catch user interrupt 
	except KeyboardInterrupt:
		print("Ended by Ctrl+C")
		sys.exit()

#Calculate time to scan
finishTime = datetime.now()
total = finishTime-startTime
print("Scan completed in: " + str(total))

