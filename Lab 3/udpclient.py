from socket import *

s_address = '127.0.0.1'
s_port = 50007
c_socket = socket(AF_INET, SOCK_DGRAM)

message_lower = raw_input('Type in a lower-case message to be converted to upper-case:')
c_socket.sendto(message_lower,(s_address, s_port))
uppercase_message, s_address = c_socket.recvfrom(4096)
print uppercase_message

ct_socket.close()