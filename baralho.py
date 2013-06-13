#coding:utf-8
# Código em Python para gerar as cartas do Baralho de Poker.
# Autor: Weslley Martins Araujo
# E-mail: weslleyaraujo@inf.ufg.br
# Blog: weslleyaraujo.com


class Carta(object):
    ''' Classe que abstrai as Cartas de Baralho de Poker. '''
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    def __repr__(self):
        return '%s%s' % (self.valor, self.naipe)


class Baralho(object):
    ''' Classe que abstrai um Baralho de Poker. '''
    naipes = 's h d c'.split()
    valores = '2 3 4 5 6 7 8 9 T J Q K A'.split()

    def __init__(self):
        ''' Monta o Baralho, valor/naipe '''
        self.cartas = [Carta(v, n) for n in self.naipes for v in self.valores]

    def __len__(self):
        ''' Mostrar a quantidade de cartas do baralho.'''
        return len(self.cartas)

    def __getitem__(self, pos):
        ''' Mostra a carta numa determinada posição do baralho.'''
        return self.cartas[pos]
