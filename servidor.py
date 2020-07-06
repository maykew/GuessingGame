import socket
import _thread
import random

HOST = ''              # Endereco IP do Servidor
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

#Funcao que abre a conexao com um cliente
def conectado(con, cliente):
    #idSensor, tpSensor, vlSensor = myRecv(con)
    #print (cliente, idSensor, tpSensor, vlSensor)
    print ('Connected by', cliente,'\n\nType 1 to start the game or press ENTER to wait for more players:')
    enviaMensagem("\nHi! Welcome to Guessing Game\nI will raffle a number from 1 to 100 and you will have to guess\n\nPlease wait for the game to start", con)
    _thread.exit()

#Funcao que encerra a conexao com um cliente
def finaliza(con, cliente):
    print ('Finalizing client connection', cliente)
    con.close()

#Funcao que envia mensagem para receber jogada e recebe a jogada
def setJogadas(con, cliente, indice):
    enviaMensagem("\nLet's go, what's your guess: ", con)
    jogada = recebeMensagem(con)
    # Caso a jogada seja valida, é armazenada no dicionario de jogadas
    if jogada.isdigit():
        jogadas[con] = int(jogada)
    #Caso a jogada não seja valida, é adicionada na lista de eliminados
    else:
        jogadas[con] = None
        clientesEliminados.append(indice)
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

#Funcao que gera string para a posicao em ingles
def posicao(num):
    if num == 1:
        return "st"
    elif num == 2:
        return "nd"
    else:
        return "th"



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

clientesEliminados = [] # Lista que armazena indices de clientes com jogadas invalidas
aguardarJog = True  # Variavel para aguardar jogadores

print("\nWaiting for connections...")
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
for i in range(len(clientes)):
    con = clientes[i][0]
    cli = clientes[i][1]
    _thread.start_new_thread(setJogadas, tuple([con, cli, i]))

#Espera todos os jogadores enviarem as jogadas (todas as threads finalizarem)
print ("\nWaiting for hunches...")
while len(jogadas) != len(clientes):
    pass

#Elimina clientes com jogadas invalidas
for indice in clientesEliminados:
    con = clientes[indice][0]
    cli = clientes[indice][1]
    enviaMensagem("-1,0",con)  # Envia ensagem de eliminação
    finaliza(con, cli)  # Finaliza conexao
    clientes.pop(indice)  # Exclui da lista de clientes
    jogadas.pop(con)  # Exclui jogada

#Print para controle do servidor
print("\nNumber drawn: ", numero)

#Print para controle do servidor
print("\nGuesses:")
for cli in clientes:
    print (cli[1],"- ",jogadas[cli[0]])

ordenaLista()

#Print para controle do servidor
print("\nRanking:")
for i in range(len(clientes)):
    cli = clientes[i]
    pos = posicao(i+1)
    print ("%d%s: (%s, %d)  Difference: |%d-%d| = %d" %(i+1, pos, cli[1][0], cli[1][1], numero, jogadas[cli[0]], abs(numero-jogadas[cli[0]])))

resultado()

#Encerra as conexoes
print("\n")
for cli in clientes:
    finaliza(cli[0], cli[1])

# Fecha a conexao
tcp.close()