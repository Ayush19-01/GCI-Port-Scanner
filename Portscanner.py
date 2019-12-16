import sys
import os
import socket

ip = input("Enter IP: ")
z=0
try:
    m1= int(input("Enter starting port:"))
    m2=int(input("Enter the last port:"))
    if m2<m1:
        print("please enter a valid range")
    elif m2>m1:
        for i in range(m1,m2+1):
            connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            if connection.connect_ex((ip,i))==0:
                print("Port{",i,"}:Open")
                z+=1
            connection.close()
    print("Scan Complete", z, "port(s) are open.")
except:
    print("Host Ip can't be resloved")

