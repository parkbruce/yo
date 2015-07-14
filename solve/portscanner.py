import sys
import subprocess
import socket

subprocess.call('clear', shell=True)
rmip = input("\t Remote host IP:")
r1 = int(input("\t Start port:\t"))
print("*"*40)
print("\n Scanner is working on ", rmip)
print("*"*40)
