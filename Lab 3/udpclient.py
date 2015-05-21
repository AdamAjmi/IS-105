# -*- coding: latin-1 -*-

from socket import *

s_address = 'localhost'
s_port = 50007
c_socket = socket(AF_INET, SOCK_DGRAM)

while 1:  
    
    roman_num = raw_input('Roman number to be converted to an arabic number:')
    c_socket.sendto(roman_num, (s_address, s_port))
    fromRoman, s_address = c_socket.recvfrom(4096)
    print fromRoman
    
    arab_num = raw_input('Arabic number to be converted to roman:')
    c_socket.sendto(arab_num, (s_address, s_port))
    fromArab, s_address = c_socket.recvfrom(4096)
    print fromArab
    
c_socket.close()