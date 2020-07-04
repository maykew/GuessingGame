import socket
import struct

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
# Campos da mensagem
idSensor = 70000
tpSensor = 50000
vlSensor = -169


#Funcao que recebe uma mensagem e uma conexao como paramentro, e encaminha a mensagem para o cliente
def enviaMensagem(msg, destino):
    msg = msg.encode('UTF-8')       # Codifica a mensagem para UTF-8
    destino.send(msg)     #Envia mensagem ao cliente

#Funcao que recebe uma conexao e fica no aguardo para receber uma mensagem
def recebeMensagem(remetente):
    msg = remetente.recv(1024)		# Le uma mensgem vinda do cliente
    msg = msg.decode('UTF-8')	# Decodifica a mensagem
    return msg

# Funcao de empacotamento e envio de da mensagem
#def mySend (socket, idSensor, tpSensor, vlSensor):
#	msg = struct.pack('!IHh', idSensor, tpSensor, vlSensor) # Empacota a informação
#	print (msg)
#	socket.send (msg)

######### Inicio do programa	
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

try:
    #Recebendo mensagem inicial
    msg = recebeMensagem(tcp)
    print (msg)

except:
    print("\nO jogo foi iniciado antes de você conseguir se conectar, tente novamente")
    tcp.close()

else:
    #Recebendo mensagem da jogada
    msg = recebeMensagem(tcp)

    #Envia mensagem da jogada
    jog = input(msg)
    enviaMensagem(jog, tcp)

    #Recebendo mensagem inicial
    msg = recebeMensagem(tcp)
    result = msg.split(",") 
    print ("\nNumero sorteado:",result[0],"\nPosição final: ", result[1])

    ######### Envia uma mensagem
    #mySend (tcp, idSensor, tpSensor, vlSensor)

    tcp.close()