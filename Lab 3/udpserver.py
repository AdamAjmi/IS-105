# -*- coding: latin-1 -*-

from socket import *
import lab2

s_port = 50007
s_socket = socket(AF_INET, SOCK_DGRAM)
s_socket.bind(('', s_port))
print 'The server has been set up and is ready to recieve data.'

while 1:
    
    roman_num, c_address = s_socket.recvfrom(4096)
    print 'Roman numeral to be converted: ' + roman_num
    fromRoman = lab2.roman_to_int(roman_num)
    print 'Converted roman numeral to send to client'
    s_socket.sendto(str(fromRoman), c_address)
    
    arab_num, c_address = s_socket.recvfrom(4096)
    fromArab = lab2.int_to_roman(arab_num)
    s_socket.sendto(fromArab, c_address)