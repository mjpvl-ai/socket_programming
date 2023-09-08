import socket
import sys


HOST = '127.0.0.1'  # Symbolic name meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()


print('Socket bind complete')

s.listen(10)
print('Socket now listening')

# wait to accept a connection - blocking call
conn, addr = s.accept()

# display client information
print('Connected with ' + addr[0] + ':' + str(addr[1]))


