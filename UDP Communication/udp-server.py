import socket

def main():
    # Inisialisasi socket UDP
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind ke alamat dan port tertentu
    server_address = ('localhost', 9000)
    udp_server_socket.bind(server_address)

    print('Server UDP siap menerima koneksi...')

    while True:
        # Terima pesan dari client
        message, client_address = udp_server_socket.recvfrom(1024)
        print('Menerima pesan dari : ', client_address)
        print('Isi pesan : ', message.decode('utf-8'))

        # Kirim pesan balasan ke client
        response = 'Pesan diterima di server UDP ! Arigatou gozaimasu !'
        udp_server_socket.sendto(response.encode('utf-8'), client_address)

if __name__ == '__main__':
    main()