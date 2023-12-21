import socket

def main():
    # Inisialisasi socket TCP
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind ke alamat dan port tertentu
    server_address = ('localhost', 8000)
    tcp_server_socket.bind(server_address)

    # Listen untuk koneksi masuk
    tcp_server_socket.listen(1)

    print('Server TCP siap menerima koneksi...')

    while True:
        # Terima koneksi dari client
        client_socket, client_address = tcp_server_socket.accept()
        print('Menerima koneksi dari : ', client_address)

        # Kirim pesan balasan ke client
        message = 'Arigatou gozaimasu ! Terhubung dengan server TCP desu !'
        client_socket.send(message.encode('utf-8'))

        # Tutup koneksi dengan client
        client_socket.close()

if __name__ == '__main__':
    main()