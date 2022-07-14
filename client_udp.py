import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        msg = input("Mensagem: ") + "\n"
        # encode transforma em bytes e decode transforma bytes em str
        client.sendto(msg.encode(), ("192.168.0.108",123))  # arg1 = dados em bytes arg2 = tupla com IP ou DNS e porta
        print("Dados enviados com sucesso!")
        data, sender = client.recvfrom(1024)  # recebendo dados
        print(sender[0] + ": " + data.decode())
        if msg == "sair\n" or data.decode() == "sair\n":
            break
    client.close()
except Exception as error:
    print("Houve um erro!")
    print(error)