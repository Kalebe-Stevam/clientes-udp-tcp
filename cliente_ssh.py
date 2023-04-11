

import paramiko


host = "192.168.0.108"
user = "kali"
senha = "kali"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=senha)  # se conecta

while True:
    stdin, stdout, stderr = (client.exec_command(input("Comando: ")))  
    for i in stdout:
        print(i.strip())

    erros = stderr.readlines()
    if erros:
        print(erros)
