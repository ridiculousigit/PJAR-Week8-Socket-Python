# PJAR-Week8-Socket-Python

This repository contains Python programs developed for the eighth week of the Networking Programming course at the Informatics Program, Faculty of Industrial Technology, Gunadarma University, under the guidance of **Ary Bima Kurniawan, S.T., M.T.**.

## Programs

### TCP Communication

- **tcp-server.py:** Establishes a TCP server that listens for incoming connections on a specified address and port. Sends a confirmation message to the client upon connection and closes the connection.

- **tcp-client.py:** Serves as the TCP client, connecting to the TCP server and receiving a message. The received message confirms the successful connection.

### UDP Communication

- **udp-server.py:** Binds to a specified address and port, ready to receive messages from clients. Prints the client's address and message contents upon receiving a message, then sends a confirmation message back to the client.

- **udp-client.py:** Sends a message to the UDP server and waits for a response. The received response confirms the successful communication with the server.

## Usage

To run the programs:

1. **For TCP Communication:**
   - Execute `tcp-server.py` in one terminal to start the TCP server.
   - In another terminal, execute `tcp-client.py` to connect to the server and receive a message.

2. **For UDP Communication:**
   - Execute `udp-server.py` in one terminal to start the UDP server.
   - In another terminal, execute `udp-client.py` to send a message to the server and receive a confirmation.

## Reference

These programs were developed with reference to the book "Python Network Programming Cookbook" by Kathiravelu, P., & Sarker, M. F. (2017), particularly Chapter 1, pages 36-42.

## Additional Resources

- [Python Socket Documentation](https://docs.python.org/3/library/socket.html)
- [Petanikode Tutorial: Python Dasar - Sockets](https://www.petanikode.com/python-socket/) (Accessed on May 25, 2023)