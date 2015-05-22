# -*- coding: utf-8 -*-

from socket import *
#Tillater oss å lage sockets i python.
import romanmodule
#Modul fra lab 2 som gjør at vi kan utføre operasjoner
#med romerske numeraler.

s_port = 50007
s_socket = socket(AF_INET, SOCK_DGRAM)
#AF_INET = IPv4 | SOCK_DGRAM = UDP
s_socket.bind(('', s_port))
#Knytter s_port til sokkelen slik at all informasjon sendt til porten
#fanges av server.
print 'The server has been initialized and is listening.'


while 1:
#Serveren looper til den stanses manuellt.
    
    uni_lower, c_address = s_socket.recvfrom(4096)
    #Når en melding mottas i socket, legges verdien inn i den første variabelen.
    #Den andre variabelen lagrer sendes addresse slik at en melding
    #kan returneres senere.
    uni_upper = uni_lower.decode('utf-8').upper()
    uni_full = uni_upper.encode('utf-8')
    s_socket.sendto(uni_full, c_address)
    #Sender svar tilbake til klientens addresse.
    
    roman_num, c_address = s_socket.recvfrom(4096)
    fromRoman = romanmodule.roman_to_int(roman_num)
    #Bruker importert metode fra romanmodule.
    s_socket.sendto(str(fromRoman), c_address)
    
    arab_num, c_address = s_socket.recvfrom(4096)
    arab_num2 = int(arab_num)
    fromArab = romanmodule.int_to_roman(arab_num2)
    s_socket.sendto(str(fromArab), c_address)
    
    num1, c_address = s_socket.recvfrom(4096)
    num2, c_address = s_socket.recvfrom(4096)
    added_num = romanmodule.roman_add(num1, num2)
    s_socket.sendto(str(added_num), c_address)
    
