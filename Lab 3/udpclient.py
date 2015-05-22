# -*- coding: utf-8 -*-

from socket import *
#Tillater oss å lage sockets i python.

s_address = '127.0.0.1'
#Navn på server. 127.0.0.1 = localhost.
s_port = 50007
c_socket = socket(AF_INET, SOCK_DGRAM)
#AF_INET = IPv4 | SOCK_DGRAM = UDP.

while 1:  
#Klienten kjører på udefinert tid fram all kode i 
#while-statement har blitt kjørt.    
    uni_lower = raw_input('Lower-case unicode letter to be capitalized: ')
    c_socket.sendto(uni_lower, (s_address, s_port))
    #Sender variabel til server.
    uni_full, s_address = c_socket.recvfrom(4096)
    #socket for å motta fange opp meldinger fra server.
    print uni_full
    
    roman_num = raw_input('Roman number to be converted to an arabic number:')
    c_socket.sendto(roman_num, (s_address, s_port))
    fromRoman, s_address = c_socket.recvfrom(4096)
    print fromRoman
    
    arab_num = raw_input('Arabic number to be converted to roman:')
    c_socket.sendto(arab_num, (s_address, s_port))
    fromArab, s_address = c_socket.recvfrom(4096)
    print fromArab   
    
    num1 = raw_input('First roman number: ')
    num2 = raw_input('Second roman number: ')
    c_socket.sendto(num1, (s_address, s_port))
    c_socket.sendto(num2, (s_address, s_port))
    added_num, s_address = c_socket.recvfrom(4096)
    print added_num
    
c_socket.close()