# PythonPortScanner

This project is a Python Port Scanner created for IT567. 

Flags:
  -t  Target
  -p  Port
  -sU UDP Scan
  -h  Help

By default, the scanner uses TCP to scan. To do a UDP port scan, set the -sU flag when running the command.

To scan multiple targets, enter the range or hosts or the subnet mask. When entering ranges, don't repeat the entire IP of the last host in the range, just the last octet. 
For example: <code>python portScanner.py -t 192.168.185.2-100 -p 80</code>
For entire subnet scan: python portScanner.py -t 192.168.185.0/24 -p 80

To scan multiple ports, enter the range or list of comma seperated ports to scan. 
For example: <code>python portScanner.py -t 192.168.185.20 -p 80-100</code>
Or: <code>python portScanner.py -t 192.168.185.20 -p 22,80,443</code>

To view detailed information, run the command with the --help flag.


