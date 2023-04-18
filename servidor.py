import socket
from random import sample

def Main():
    host = ""
    port = 12000

    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print("Iniciando o servidor na porta: " + str(port) + " | host: " + host)
    tcp_server.bind((host, port))
    tcp_server.listen(1)

    print("Esperando Cliente...")
    client, end_client = tcp_server.accept()

    (msg_receivedByte, _) = client.recvfrom(1024)

    msg_receivedString = msg_receivedByte.decode()

    ShuffledMsg(msg_receivedString)

    print("Endereço do cliente:", end_client)

    client.send(b"Deu certo!")

    tcp_server.close()

def ShuffledMsg(msg_receivedString):
    shuffled = sample(msg_receivedString, len(msg_receivedString))
    shuffled_msg = "".join(shuffled)
    print("Mensagem emmbaralhada do cliente: " + shuffled_msg)
    
if __name__ == '__main__':
    Main()