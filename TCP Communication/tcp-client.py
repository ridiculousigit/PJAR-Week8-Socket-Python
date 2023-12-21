import socket

def main():
    # Inisialisasi socket TCP
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Koneksi ke server TCP
    server_address = ('localhost', 8000)
    tcp_client_socket.connect(server_address)

    # Terima pesan dari server
    message = tcp_client_socket.recv(1024).decode('utf-8')
    print('Pesan dari server : ', message)

    # Tutup koneksi dengan server
    tcp_client_socket.close()

if __name__ == '__main__':
    main()