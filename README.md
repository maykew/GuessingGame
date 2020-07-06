<h1 align="center">
    Guessing Game
</h1>

<p align="center">
    <img width="40%" src="https://image.freepik.com/vetores-gratis/bolha-do-discurso-plana-com-pontos-de-interrogacao_23-2148148274.jpg" alt="Guessing Game Image"/>
</p>

<p align="center">
  <a href="#computer-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#dart-objetivos">Objetivos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#boom-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#warning-regras-do-jogo">Regras do Jogo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#mortar_board-como-executar-o-projeto">Como executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#family-como-contribuir">Como contribuir</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-licença">Licença</a>
</p>

_________

### :computer: Projeto

<p align="justify">
Este é um desafio com o intuito de desenvolver uma aplicação distribuída concorrente que simulará um jogo de adivinhação com qualquer número de participantes.
</p>

### :dart: Objetivos

- Familiarizar-se com a programação utilizando a API [socket](https://docs.python.org/3/library/socket.html);<br>
- Ambientar-se na programação com Threads utilizando a API [_thread](https://docs.python.org/3/library/_thread.html).

### :boom: Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org/)

### :warning: Regras do Jogo

Participantes:
- Árbitro do jogo: representado pela aplicação servidora, que atenderá qualquer número de jogadores;
- Jogador: representado por uma instância da aplicação cliente.

Funcionamento:
1. O árbitro do jogo sorteia um número entre 1 e 100 e envia uma mensagem para cada jogador
solicitando um palpite;
2. Os jogadores apresentam as suas opções;
3. O árbitro do jogo calcula as diferenças de forma absoluta entre as opções de cada jogador e o número
sorteado. Vence o jogador com a menor diferença.

### :mortar_board: Como executar o projeto

Em breve 

### :family: Como contribuir

- Faça um fork desse repositório;
- Cria uma branch com a sua feature: `git checkout -b minha-feature`;
- Faça commit das suas alterações: `git commit -m 'feat: Minha nova feature'`;
- Faça push para a sua branch: `git push origin minha-feature`.

Depois que o merge da sua pull request for feito, você pode deletar a sua branch.

### :memo: Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](https://github.com/maykew/GuessingGame/blob/master/LICENSE.md) para mais detalhes.
_________

<h4 align="center"> ♥ by Mayke Willans ♥ </h4>
