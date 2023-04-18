import socket

def Main():
    ip_server = "127.0.0.1"
    port = 12000

    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    dest = (ip_server, port)
    print("Conectando no servidor...")
    tcp_client.connect(dest)

    try:
        print("Digite algo: ")
        msg = input()
        tcp_client.sendall(msg.encode("utf-8"))

        data = tcp_client.recv(1024)
        print("Recebido: " + data.decode())
    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print("Fechando conexao..")
        tcp_client.close()


if __name__ == '__main__':
    Main()