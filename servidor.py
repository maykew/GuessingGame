import socket
import struct
import _thread
import time
import random

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

# Campos da mensagem
#idSensor = None
#tpSensor = None
#vlSensor = None
#structsize = 8

#-------------- Funcoes --------------

# Funcao de recepcao e desempacotamento da mensagem
#def myRecv (socket):
#	try:	
#		msg = socket.recv(structsize)
#		print (cliente, msg)
#		return struct.unpack('!IHh', msg) # Desempacota a informação
#	except:
#		return None

#Funcao que recebe uma mensagem e uma conexao como paramentro, e encaminha a mensagem para o cliente
def enviaMensagem(msg, destino):
    msg = msg.encode('UTF-8')       # Codifica a mensagem para UTF-8
    destino.send(msg)     #Envia mensagem ao cliente

#Funcao que recebe uma conexao e fica no aguardo para receber uma mensagem
def recebeMensagem(remetente):
    msg = remetente.recv(1024)		# Le uma mensgem vinda do cliente
    msg = msg.decode('UTF-8')	# Decodifica a mensagem
    return msg

#Funcao que abre a conexao com um cliente
def conectado(con, cliente):
    #idSensor, tpSensor, vlSensor = myRecv(con)
    #print (cliente, idSensor, tpSensor, vlSensor)
    print ('Concetado por', cliente,'\n\nDigite 1 para começar o jogo ou ENTER para esperar mais jogadores:')
    enviaMensagem("\nHi! Welcome to Guessing Game\n", con)
    _thread.exit()

#Funcao que encerra a conexao com um cliente
def finaliza(con, cliente):
    print ('Finalizando conexao do cliente', cliente)
    con.close()

#Funcao que envia mensagem para receber jogada e recebe a jogada
def setJogadas(con, cliente):
    enviaMensagem("\nQual a sua jogada: ", con)
    jogada = recebeMensagem(con)
    jogadas[con] = int(jogada)
    _thread.exit()

#Funcao que ordena a lista de clientes com base na diferença entre a jogada e numero sorteado
def ordenaLista():
    troca=True
    aux=0
    while troca:
        troca=False
        for i in range (len(clientes)-1):
            con = clientes[i][0]
            con2 = clientes[i+1][0]
            if abs(jogadas[con]-numero) > abs(jogadas[con2]-numero):
                aux=clientes[i]
                clientes[i]=clientes[i+1]
                clientes[i+1]=aux
                troca=True

#Funcao que envia resultado aos clientes
def resultado():
    for i in range(len(clientes)):
        msg = str(numero)+","+str(i+1)
        enviaMensagem(msg, clientes[i][0])



#-------------- Inicio do programa --------------    

# Cria o socket do servidor
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)  # Forma a tupla de host e porta
tcp.bind(orig)  # Solicita ao S.O. acesso exclusivo a porta
tcp.listen(10)  # Entra no modo de escuta

#Lista de clientes que armazenda conxecao e o cliente em uma tupla
clientes = []

#Dicionario de jogadas onde a chave é a conexao e o valor é a jogada 
jogadas = {}

aguardarJog = True  # Variavel para aguardar jogadores

print("\nAguardando conexões...")
while aguardarJog:
    #Realiza a conexao dos clientes
    con, cliente = tcp.accept()
    clientes.append((con, cliente))
    
    #Inicia uma thread para conectar o cliente
    _thread.start_new_thread(conectado, tuple([con, cliente]))
    
    #Caso o servidor receba o valor de inicio do jogo(1), nao são ouvidas mais conexoes 
    if input() == '1': 
        aguardarJog = False

numero = random.randint(1, 100)  # Armazena numero aleatorio de 1 a 100

#Envia e recebe de jogadas e armazena no dicionario
for cli in clientes:
    _thread.start_new_thread(setJogadas, cli)

#Espera todos os jogadores enviarem as jogadas (todas as threads finalizarem)
print ("\nAguardando jogadas...")
while len(jogadas) != len(clientes):
    loopDeEspera = "Aguardando threads finalizarem"

#Print para controle do servidor
print("\nNumero sorteado: ", numero)

#Print para controle do servidor
print("\nJogadas:")
for cli in clientes:
    print (cli[1],"- ",jogadas[cli[0]])

ordenaLista()

#Print para controle do servidor
print("\nResultado final:")
for i in range(len(clientes)):
    cli = clientes[i]
    print ("%d lugar: (%s, %d)  Diferença: |%d-%d| = %d" %(i+1, cli[1][0], cli[1][1], numero, jogadas[cli[0]], abs(numero-jogadas[cli[0]])))

resultado()

#Encerra as conexoes
print("\n")
for cli in clientes:
    finaliza(cli[0], cli[1])

# Fecha a conexao
tcp.close()