# -*- coding: latin-1 -*-

from socket import *
#Tillater oss å lage sockets i python.
s_port = 10044
c_socket = socket(AF_INET, SOCK_DGRAM)
#AF_INET = IPv4 | SOCK_DGRAM = UDP.
c_socket.settimeout(3)
loop = True
while loop:  
#Klienten kjører på udefinert tid fram all kode i 
#while-statement har blitt kjørt.    
        
        print "The server can convert lower-case unicode letters to capitalized unicode letters."
        s_address = 'localhost'
        #Navn på server. 127.0.0.1 = localhost.       
        print 'Type in the lower-case unicode letter you want capitalized:'
        uni_lower = raw_input('> ')
        c_socket.sendto(uni_lower, (s_address, s_port))
        #Sender variabel til server.
        print 'The letter was sent to the server. Waiting for response...'
        uni_full, s_address = c_socket.recvfrom(4096)
        #socket for å kunne motta og fange opp meldinger fra server.
        print uni_full
    
        print "--------------------------------------------------------------------"
        
        print "The server can convert roman numbers into arabic numbers."
        s_address = 'localhost'       
        print 'Type in the roman number you would like to be converted to arabic:'
        roman_num = raw_input('> ')
        c_socket.sendto(roman_num, ((s_address), (s_port)))
        print "The roman number was sent to the server. Waiting for response..."
        fromRoman, s_address = c_socket.recvfrom(4096)
        print fromRoman
        
        print "--------------------------------------------------------------------"
        
        print "It can also convert arabic numbers into roman numbers."
        s_address = 'localhost'       
        print 'Type in the arabic number you would like to be converted to roman:'
        arab_num = raw_input('> ')
        c_socket.sendto(arab_num, ((s_address), (s_port)))
        print "The arabic number was sent to the server. Waiting for response..."
        fromArab, s_address = c_socket.recvfrom(4096)
        print fromArab
        
        print "--------------------------------------------------------------------"

        print "Lastly the server can add two roman numerals together."
        s_address = 'localhost'       
        print 'Type in the first roman number you would like to add: '
        num1 = raw_input('> ')
        print 'Type in the second roman number you would like to add: '
        num2 = raw_input('> ')
        c_socket.sendto(num1, ((s_address), (s_port)))
        c_socket.sendto(num2, ((s_address), (s_port)))
        print 'The numbers were sent to the server. Waiting for response...'
        added_num, s_address = c_socket.recvfrom(4096)
        print "" + num1 + " + " + num2 + " = " + added_num + ""
        
        print "--------------------------------------------------------------------"
        
        print "Succesfully ran all functions. Closing the socket..."
        loop = False
        c_socket.close
 