import socket

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

#-------------- Funcoes --------------

#Funcao que recebe uma mensagem e uma conexao como paramentro, e encaminha a mensagem para o cliente
def enviaMensagem(msg, destino):
    msg = msg.encode('UTF-8')       # Codifica a mensagem para UTF-8
    destino.send(msg)     #Envia mensagem ao cliente

#Funcao que recebe uma conexao e fica no aguardo para receber uma mensagem
def recebeMensagem(remetente):
    msg = remetente.recv(1024)		# Le uma mensgem vinda do cliente
    msg = msg.decode('UTF-8')	# Decodifica a mensagem
    return msg



#-------------- Inicio do programa --------------

# Cria o socket do cliente
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)  # Forma a tupla de host(ip), porta
tcp.connect(dest)  # Estabelece a conexao

# Tenta se conectar ao servidor
try:
    #Recebendo mensagem inicial
    msg = recebeMensagem(tcp)
    print (msg)

# Caso não consiga se conectar é obtido um erro
except:
    print("\nThe game started before you were able to connect, try again")
    tcp.close()

#Caso consiga se conectar, o programa segue normalmente
else:
    #Recebendo mensagem da jogada
    msg = recebeMensagem(tcp)

    #Envia mensagem da jogada
    jog = input(msg)
    enviaMensagem(jog, tcp)

    #Recebendo mensagem de resultado
    msg = recebeMensagem(tcp)
    result = msg.split(",")
    if int(result[0]) < 0:
        print("\nInvalid choice, you were eliminated!")
    else:
        print ("\nNumber drawn:",result[0],"\nFinal position in the ranking:", result[1])

    tcp.close()  # Fecha a conexao com o servidor