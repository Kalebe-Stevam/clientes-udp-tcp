import socket

# arg == argumento
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # arg1 == famylia -> IPV4 ou iIPV6, arg2 == tipo TCP ou UDP
    client.connect(("google.com", 80))  # em uma tupla passe o agr1 onde me conectar, arg2 em qual porta,
    client.send(b"GET / HTTP/1.1\nHost: www.google.com\n\n\n\n")  # enviar resposta, b transforma em bytes
    pacotes_recebidos = client.recv(1024).decode()  # tamanho de bytes que quer receber a resposta
    print(pacotes_recebidos)
except Exception as error:
    print("Ocorreu um erro!")
    print(error)


