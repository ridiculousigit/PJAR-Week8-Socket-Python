import socket

def main():
    # Inisialisasi socket UDP
    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Kirim pesan ke server
    server_address = ('localhost', 9000)
    message = 'Konnichiwa ! Kore wa UDP client kara no messeji desu.'
    udp_client_socket.sendto(message.encode('utf-8'), server_address)

    # Terima pesan balasan dari server
    response, server_address = udp_client_socket.recvfrom(1024)
    print('Pesan balasan dari server : ', response.decode('utf-8'))

    # Tutup koneksi dengan server
    udp_client_socket.close()

if __name__ == '__main__':
    main()