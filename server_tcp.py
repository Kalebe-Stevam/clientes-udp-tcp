import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind(("0.0.0.0", 1234))  # endereço e porta onde vai escutar
    server.listen(5)  # Número de conexões simuntaneas
    print("Listening...")

    # server.accept() dele recebemos um socket para enviar e receber dados do cliente
    client_socket, adress = server.accept()  # esperando conexões e aceitando
    print("Recuved from:" + adress[0])
    while True:
        data = client_socket.recv(1024).decode()
        print(data)
        msg = input("mensagem: ")+"\n"
        client_socket.send(msg.encode())

    server.close()
except Exception as error:
    print("hove um erro:")
    print(error)
    server.close()

