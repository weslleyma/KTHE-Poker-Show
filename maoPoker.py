#coding:utf-8
# Código em Python para avaliar as mãos de Poker.
# Autor: Weslley Martins Araujo
# E-mail: weslleyaraujo@inf.ufg.br
# Blog: weslleyaraujo.com


from poker import Poker

class MaoPoker(Poker):
    ''' Classe que herda de Poker, e que abstrai mãos (hand) de Poker. '''
    __rank = {'RoyalFlush': 2000,
              'StraightFlush': 1700,
              'FourOfKind': 1500,
              'FullHouse': 1200,
              'Flush': 1000,
              'Straight': 800,
              'ThreeOfKind': 600,
              'TwoPairs': 400,
              'OnePair':200,
              'HighCard': 0}
    __mao = {}
    __pontuacao = {}
    __resultado = {}
    __players = 6
    __contador = 0

    @classmethod
    def inicializaMao(self):
        ''' Inicializa o dicionário que salva as hand. '''
        self.__mao = {}
        self.__contador = 0

    @classmethod
    def setMao(self, var, *args):
        ''' Set no dicionário que salva as hand. '''
        self.__contador += 1
        while True:
            if self.isValid(var):
                self.__mao[self.__contador] = str(var)
                return True
            else:
                self.__contador -= 1
                return False
    @classmethod
    def getMao(self):
        ''' Get no dicionário que salva as hand. Retorna um dicionário. '''
        return self.__mao

    @classmethod
    def getPlayers(self):
        ''' Pegar a quantidade de Players no jogo. Retorna um inteiro. '''
        return self.__players

    @classmethod
    def getResultado(self):
        ''' Pegar o resultado da hand. Retorna um dicionário. '''
        return self.__resultado

    @classmethod
    def isValid(self, var):
        ''' Validar entrada da linha, verificar se tem alguma carta repetida e retorna True or False. '''
        cont = 0
        for v in var.split():
            if var.count(v) > 1:
                cont += 1
                break
        if cont > 0:
            return False
        else:
            return True

    @classmethod
    def avaliarMao(self):
        ''' Avaliar a mao e retornar um dicionário com a pontuação de cada player. '''
        var = self.__mao
        cont = 1
        while cont <= self.__players:
            if super(MaoPoker, self).isRoyalFlush(var[cont]):
                self.__pontuacao[cont] = 2000
            elif super(MaoPoker, self).isStraightFlush(var[cont]) > 0:
                self.__pontuacao[cont] = 1700 + super(MaoPoker, self).isStraightFlush(var[cont])
            elif super(MaoPoker, self).isFourOfKind(var[cont]) > 0:
                self.__pontuacao[cont] = 1500 + super(MaoPoker, self).isFourOfKind(var[cont])
            elif super(MaoPoker, self).isFullHouse(var[cont]) > 0:
                self.__pontuacao[cont] = 1200 + super(MaoPoker, self).isFullHouse(var[cont])
            elif super(MaoPoker, self).isFlush(var[cont]) > 0:
                self.__pontuacao[cont] = 1000 + super(MaoPoker, self).isFlush(var[cont])
            elif super(MaoPoker, self).isStraight(var[cont]) > 0:
                self.__pontuacao[cont] = 800 + super(MaoPoker, self).isStraight(var[cont])
            elif super(MaoPoker, self).isThreeOfKind(var[cont]) > 0:
                self.__pontuacao[cont] = 600 + super(MaoPoker, self).isThreeOfKind(var[cont])
            elif super(MaoPoker, self).isTwoPairs(var[cont]) != 0:
                self.__pontuacao[cont] = 400 + super(MaoPoker, self).isTwoPairs(var[cont])
            elif super(MaoPoker, self).isOnePair(var[cont]) > 0:
                self.__pontuacao[cont] = 200 + super(MaoPoker, self).isOnePair(var[cont])
            else:
                self.__pontuacao[cont] = super(MaoPoker, self).whatIsHighCard(var[cont])
            cont += 1
        self.geraResultado()

    @classmethod
    def determinaGanhador(self, var, *args, **kwargs):
        ''' Avaliar um dicionário e retornar outro com o resultado por ordem decrescente. '''
        from operator import itemgetter
        return sorted(var.items(), key=itemgetter(1), reverse=True)

    @classmethod
    def geraResultado(self):
        ''' Gerar resultado para um dicionário e imprimir os valores. '''
        var = self.__pontuacao
        self.__resultado = {}
        self.__resultado = dict(self.__mao)
        pontuacao = self.determinaGanhador(var)
        for p in range(len(pontuacao)):
            if pontuacao[p][1] == 2000:
                if p == 0: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Royal Flush (WINNER)'
                else: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Royal Flush'
            elif (pontuacao[p][1] >= 1700) and (pontuacao[p][1] < 2000):
                if p == 0: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Straight Flush (WINNER)'
                else: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Straight Flush'
            elif (pontuacao[p][1] >= 1500) and (pontuacao[p][1] < 1700):
                if p == 0: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Four Of a Kind (WINNER)'
                else: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Four Of a Kind'
            elif (pontuacao[p][1] >= 1200) and (pontuacao[p][1] < 1500):
                if p == 0: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Full House (WINNER)'
                else: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Full House'
            elif (pontuacao[p][1] >= 1000) and (pontuacao[p][1] < 1200):
                if p == 0: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Flush (WINNER)'
                else: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Flush'
            elif (pontuacao[p][1] >= 800) and (pontuacao[p][1] < 1000):
                if p == 0: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Straight (WINNER)'
                else: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Straight'
            elif (pontuacao[p][1] >= 600) and (pontuacao[p][1] < 800):
                if p == 0: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Three Of Kind (WINNER)'
                else: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Three Of Kind'
            elif (pontuacao[p][1] >= 400) and (pontuacao[p][1] < 600):
                if p == 0: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Two Pairs (WINNER)'
                else: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   Two Pairs'
            elif (pontuacao[p][1] >= 200) and (pontuacao[p][1] < 400):
                if p == 0: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   One Pair (WINNER)'
                else: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   One Pair'
            elif (pontuacao[p][1] >= 0) and (pontuacao[p][1] < 200):
                if p == 0: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0]) + '   (WINNER)'
                else: self.__resultado[pontuacao[p][0]] = self.__mao.get(pontuacao[p][0])
            else:
                pass
        return self.imprimeResultado()

    @classmethod
    def imprimeResultado(self):
        ''' Imprime o resultado da mão de Poker. '''
        resultado = self.__resultado
        for r in resultado:
            print resultado.get(r)
        return self.inicializaMao()
