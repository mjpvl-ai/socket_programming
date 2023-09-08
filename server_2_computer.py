import socket
import os
import sys
import stun


nat_type, external_ip, external_port = stun.get_ip_info()#stun_host='stunserver.org')
print(nat_type, external_ip, external_port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "192.168.207.76"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

import socket

def main():
  # Create a socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Bind the socket to a port
  host = "127.0.0.1"  # The IP address of the server
  port = 8080  # The port number of the server
  sock.bind((host, port))

  # Listen for connections
  sock.listen(5)

  # Accept a connection
  client_socket, address = sock.accept()

  # Receive data from the client
  data = client_socket.recv(1024)

  # Send data back to the client
  client_socket.sendall(data)

  # Close the sockets
  client_socket.close()
  sock.close()

if __name__ == "__main__":
  main()
