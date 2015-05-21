from socket import *

s_port = 50007
s_socket = socket(AF_INET, SOCK_DGRAM)
s_socket.bind(('', s_port))
print 'The server has been set up and is ready to recieve data.'

while 1:
    message, c_address = s_socket.recvfrom(4096)
    print 'Server recieved message from client.'
    uppercase_message = message.upper()
    s_socket.sendto(uppercase_message, c_address)
    print 'Message was sent back to client.'