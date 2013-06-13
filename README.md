KTHE-Poker-Show
===============

Software para avaliar mãos (hand) de uma rodada de Poker e determinar o vencedor.



.: Descrição
É um software para avaliar mãos (hand) de uma rodada de Poker e determinar o vencedor.

Há algoritmos que avaliam a pontuação de cada Player e gera critérios de desempate, caso ocorra.

No final é mostrado a jogada de cada player e é definido o ganhador (Winner)

O software é feito na linguagem Python, compatível com a versão 2.7.3 ou superior do interpretador.


.: Requisitos:
- Python 2.7.3+
http://www.python.org/getit/


.: Instruções de Execução
Para executar o software, baixe-o, dentro do pacote KataTexasHoldEm, execute o seguinte comando abaixo:
python __init__.py

Depois siga as instruções, digitando valores de entrada para 6 Players, como:

Kc 9s Ks Kd 9d 3c 6d
9c Ah Ks Kd 9d 3c 6d
Ac Qc Ks Kd 9d 3c
9h 5s
4d 2d Ks Kd 9d 3c 6d
7s Ts Ks Kd 9d

Cada linha de entrada deve ser digitada, separando cada carta apenas por espaço.


.: Testes Automatizados
Há alguns testes automatizados via 'unittest', que testa o principal do software. Porém pode ser melhorado, com mais tempo.


.: Documentação
O código é bem fácil de ler e compreender. Todavia foi feito documentação por meio de Docstrings.
Digite help(objeto) e poderá ver a documentação da classe e dos métodos.


.: Dúvidas e sugestões
weslleyaraujo@inf.ufg.br
