#!/usr/bin/env python   
import socket

connection= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("10.0.2.15",4444))

