# PythonPortScanner

This project is a Python Port Scanner created for IT567. 

Flags:
  -t  Target<br>
  -p  Port<br>
  -sU UDP Scan<br>
  -h  Help<br>

By default, the scanner uses TCP to scan. To do a UDP port scan, set the -sU flag when running the command.

To scan multiple targets, enter the range or hosts or the subnet mask. When entering ranges, don't repeat the entire IP of the last host in the range, just the last octet.<br> 
For example: <code>python portScanner.py -t 192.168.185.2-100 -p 80</code><br>
For entire subnet scan: <code>python portScanner.py -t 192.168.185.0/24 -p 80</code><br>

To scan multiple ports, enter the range or list of comma seperated ports to scan.<br> 
For example: <code>python portScanner.py -t 192.168.185.20 -p 80-100</code><br>
Or: <code>python portScanner.py -t 192.168.185.20 -p 22,80,443</code><br>

To view detailed information, run the command with the --help flag.


