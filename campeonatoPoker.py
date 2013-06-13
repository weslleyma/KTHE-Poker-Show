#coding:utf-8
# Código em Python para criar o campeonato de Poker.
# Autor: Weslley Martins Araujo
# E-mail: weslleyaraujo@inf.ufg.br
# Blog: weslleyaraujo.com


from maoPoker import MaoPoker

class PokerChampionship(MaoPoker):
    ''' Classe que herda de MaoPoker, e que abstrai um Campeonato de Poker. '''
    __campeonato = {}
    __rodada = 0

    @classmethod
    def __init__(self):
        ''' Método para inicializar a classe. Médodo Inicializador, similar ao método Construtor de Java. '''
        self.inicializaCampeonato()
        self.__rodada = 0

    @classmethod
    def inicializaCampeonato(self):
        ''' Método para inicializar o campeonato de Poker. '''
        self.__campeonato = {}

    @classmethod
    def menu(self):
        ''' Método com menu e retorna um inteiro. '''
        print ' '
        print 'DIGITE: '
        print '1 - Para avaliar uma rodada.'
        print '2 - Para mostrar as rodadas anteriores.'
        print '0 - Para SAIR.'
        acao = raw_input()
        return int(acao)

    @classmethod
    def incrementaRodada(self):
        ''' Método para incrementar a rodada do Poker. '''
        self.__rodada += 1

    @classmethod
    def runCampeonato(self):
        ''' Método rodar o campeonato de Poker. '''
        while True:
            opcao = self.menu()
            if opcao == 1:
                self.incrementaRodada()
                self.lerRodada()
                self.setCampeonato()
            elif opcao == 2:
                self.imprimeCampeonato()
            elif opcao == 0:
                break
            else:
                return self.runCampeonato()

    @classmethod
    def setCampeonato(self):
        ''' Método popular o dicionário do campeonato de Poker. '''
        self.__campeonato[self.__rodada] = super(PokerChampionship, self).getResultado()

    @classmethod
    def imprimeCampeonato(self):
        ''' Método que imprime o histórico do campeonato de Poker. '''
        campeonato = self.__campeonato
        for camp in campeonato:
            print 'Rodada ' + str(camp) + ' do Campeonato'
            for c in campeonato.get(camp):
                print campeonato.get(camp).get(c)
            print '----------------------------------------------------'

    @classmethod
    def lerRodada(self):
        ''' Método para ler uma rodada com N Players e já avaliar. '''
        cont = 0
        while cont < MaoPoker.getPlayers():
            cont += 1
            linha = raw_input('Digite a mão do Player %s: ' % cont)
            if self.isValid(linha):
                self.setMao(linha)
            else:
                cont -= 1
        super(PokerChampionship, self).avaliarMao()
