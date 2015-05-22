# -*- coding: latin-1 -*-

from socket import *
#Tillater oss å lage sockets i python.
import romanmodule
#Modul fra lab 2 som gjør at vi kan utføre operasjoner
#med romerske numeraler.

s_port = 10044
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
    print "Lower_case letter '" + uni_lower + "'  recieved from client."
    uni_upper = uni_lower.decode('utf-8').upper()
    uni_full = uni_upper.encode('utf-8')
    print "Letter was converted to '" + uni_full + "'. Sending back to client:"
    s_socket.sendto(uni_full, c_address)
    print "Letter was sent to the client."
    #Sender svar tilbake til klientens addresse.
    print "----------------------------------------------------"
    
    roman_num, c_address = s_socket.recvfrom(4096)
    print "Roman numeral '" + roman_num + "' recieved from client."
    fromRoman = romanmodule.roman_to_int(roman_num)
    print "The numeral was converted to arabic numerals."
    #Bruker importert metode fra romanmodule.
    s_socket.sendto(str(fromRoman), c_address)
    print "The arabic numeral was sent to the client."
    print "----------------------------------------------------"
    
    arab_num, c_address = s_socket.recvfrom(4096)
    print "Arabic numeral '" + arab_num + "' recieved from client."
    arab_num2 = int(arab_num)
    fromArab = romanmodule.int_to_roman(arab_num2)
    print "The numeral was converted to '" + fromArab + "' in roman numerals."
    s_socket.sendto(str(fromArab), c_address)
    print "The roman numeral was sent to the client."
    print "----------------------------------------------------"
    
    num1, c_address = s_socket.recvfrom(4096)
    print "The first roman numeral to be added is '" + num1 + "'"
    num2, c_address = s_socket.recvfrom(4096)
    print "The second roman numeral to be added is '" + num2 + "'"
    added_num = romanmodule.roman_add(num1, num2)
    print "The two numerals were added to a total of '" + added_num + "' in roman numerals."
    s_socket.sendto(str(added_num), c_address)
    print "The combined roman numerals were sent to the client."
    print "----------------------------------------------------"