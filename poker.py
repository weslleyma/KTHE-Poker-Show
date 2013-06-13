#coding:utf-8
# Código em Python com as regras do Poker.
# Autor: Weslley Martins Araujo
# E-mail: weslleyaraujo@inf.ufg.br
# Blog: weslleyaraujo.com


class Poker(object):
    ''' Classe que abstrai as regras do Poker por meio de diversos médodos. '''
    __valor_rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    @classmethod
    def valor_cartas(self, var, *args, **kwargs):
        ''' Mostra o valor de cada carta, dada uma lista. Retorna uma lista com o valor de cada carta. '''
        tmp = []
        for v in var:
            v = list(v)[0]
            tmp.append(v)
        return tmp

    @classmethod
    def ordenar_cartas(self, var, *args, **kwargs):
        ''' Ordena as cartas de em uma lista, retornando uma lista ordenada com o valor correspondente.'''
        cartas_ordenadas = []
        valor_cartas = self.valor_cartas(var)
        for valor in valor_cartas:
            for rank in self.__valor_rank:
                if valor == rank:
                    tmp = int(self.__valor_rank.get(rank))
                    cartas_ordenadas.append(tmp)
        return sorted(cartas_ordenadas)

    @classmethod
    def naipe_carta(self, var, *args, **kwargs):
        ''' Separa as cartas por naipe e retorna um dicionário, com o índice sendo o naipe e o valor sendo uma lista com as cartas.'''
        s = []
        h = []
        d = []
        c = []
        for v in var.split():
            if v[1] == 's': s.append(v)
            elif v[1] == 'h': h.append(v)
            elif v[1] == 'd': d.append(v)
            elif v[1] == 'c': c.append(v)
            else: pass
        naipe = {'s': s, 'h': h, 'd': d, 'c': c}
        return naipe

    @classmethod
    def agrupa_carta(self, var, *args, **kwargs):
        ''' Agrupa as cartas por valor e retorna um dicionário, com o índice sendo o quantidade e o valor sendo uma lista com as cartas.'''
        var1 = []
        var2 = []
        var3 = []
        var4 = []
        var5 = []
        var6 = []
        var7 = []
        lista = var.split()
        cont = 0
        for li in lista:
            if cont == 0:
                var1.append(li)
                cont += 1
                continue
            if list(li)[0] == list(var1[0])[0]:
                var1.append(li)
                continue
            elif len(var2) == 0:
                var2.append(li)
                continue
            elif list(li)[0] == list(var2[0])[0]:
                var2.append(li)
                continue
            elif len(var3) == 0:
                var3.append(li)
                continue
            elif list(li)[0] == list(var3[0])[0]:
                var3.append(li)
                continue
            elif len(var4) == 0:
                var4.append(li)
                continue
            elif list(li)[0] == list(var4[0])[0]:
                var4.append(li)
                continue
            elif len(var5) == 0:
                var5.append(li)
                continue
            elif list(li)[0] == list(var5[0])[0]:
                var5.append(li)
                continue
            elif len(var6) == 0:
                var6.append(li)
                continue
            elif list(li)[0] == list(var6[0])[0]:
                var6.append(li)
                continue
            elif len(var7) == 0:
                var7.append(li)
                continue
            elif list(li)[0] == list(var7[0])[0]:
                var7.append(li)
                continue
            else:
                pass
        tmp = {}
        if len(var1) > 0:
            tmp[var1[0][0]] = var1
        if len(var2) > 0:
            tmp[var2[0][0]] = var2
        if len(var3) > 0:
            tmp[var3[0][0]] = var3
        if len(var4) > 0:
            tmp[var4[0][0]] = var4
        if len(var5) > 0:
            tmp[var5[0][0]] = var5
        if len(var6) > 0:
            tmp[var6[0][0]] = var6
        if len(var7) > 0:
            tmp[var7[0][0]] = var7
        return tmp

    @classmethod
    def isRoyalFlush(self, var, *args, **kwargs):
        ''' Verifica se é Royal Flush e retorna True or False.'''
        mesmo_naipe = 5
        lista = ['A', 'K', 'Q', 'J', 'T']
        var = self.naipe_carta(var)
        s = var.get('s')
        h = var.get('h')
        d = var.get('d')
        c = var.get('c')
        if len(s) >= mesmo_naipe:
            for cada in s:
                if lista.count(cada[0]):
                    lista.remove(cada[0])
        if len(h) >= mesmo_naipe:
            for cada in h:
                if lista.count(cada[0]):
                    lista.remove(cada[0])
        if len(d) >= mesmo_naipe:
            for cada in d:
                if lista.count(cada[0]):
                    lista.remove(cada[0])
        if len(c) >= mesmo_naipe:
            for cada in c:
                if lista.count(cada[0]):
                    lista.remove(cada[0])
        if len(lista) == 0:
            return True
        else:
            return False

    @classmethod
    def isStraightFlush(self, var, *args, **kwargs):
        ''' Verifica se é Straight Flush e retorna a maior carta da sequência caso seja verdadeiro, ou 0 caso não seja.'''
        mesmo_naipe = 5
        var = self.naipe_carta(var)
        s = var.get('s')
        h = var.get('h')
        d = var.get('d')
        c = var.get('c')
        cont = prox = sequencia = 1
        maior_carta = 0
        if len(s) >= mesmo_naipe:
            linha = self.ordenar_cartas(s)
            menor_carta = linha[0]
            maior_carta = linha[len(linha)-1]
            while cont < len(linha):
                if menor_carta+prox == linha[cont] and linha[cont] != 14:
                    sequencia += 1
                    menor_carta = linha[cont]
                else:
                    if sequencia >= mesmo_naipe:
                        pass
                    else:
                        sequencia = 1
                        menor_carta = linha[cont]
                cont += 1
        if len(h) >= mesmo_naipe:
            linha = self.ordenar_cartas(h)
            menor_carta = linha[0]
            maior_carta = linha[len(linha)-1]
            while cont < len(linha):
                if menor_carta+prox == linha[cont] and linha[cont] != 14:
                    sequencia += 1
                    menor_carta = linha[cont]
                else:
                    if sequencia >= mesmo_naipe:
                        pass
                    else:
                        sequencia = 1
                        menor_carta = linha[cont]
                cont += 1
        if len(d) >= mesmo_naipe:
            linha = self.ordenar_cartas(d)
            menor_carta = linha[0]
            maior_carta = linha[len(linha)-1]
            while cont < len(linha):
                if menor_carta+prox == linha[cont] and linha[cont] != 14:
                    sequencia += 1
                    menor_carta = linha[cont]
                else:
                    if sequencia >= mesmo_naipe:
                        pass
                    else:
                        sequencia = 1
                        menor_carta = linha[cont]
                cont += 1
        if len(c) >= mesmo_naipe:
            linha = self.ordenar_cartas(c)
            menor_carta = linha[0]
            maior_carta = linha[len(linha)-1]
            while cont < len(linha):
                if menor_carta+prox == linha[cont] and linha[cont] != 14:
                    sequencia += 1
                    menor_carta = linha[cont]
                else:
                    if sequencia >= mesmo_naipe:
                        pass
                    else:
                        sequencia = 1
                        menor_carta = linha[cont]
                cont += 1
        if sequencia == 5:
            return maior_carta
        else:
            return 0

    @classmethod
    def isFourOfKind(self, var, *args, **kwargs):
        ''' Verifica se é Four of Kind e retorna a maior quadra caso seja verdadeiro, ou 0 caso não seja.'''
        cartas = 4
        mao = var.split()
        for m in mao:
            if var.count(list(m)[0]) >= cartas:
                tmp = self.ordenar_cartas(m)
                return tmp[0]
            else:
                return 0

    @classmethod
    def isFullHouse(self, var, *args, **kwargs):
        ''' Verifica se é Full House e retorna o valor da trinca. Caso contrário retorna 0.'''
        trinca = 3
        par = 2
        mao = self.agrupa_carta(var)
        cont = 0
        tmp = []
        for m in mao:
            if len(mao[m]) == trinca:
                tmp.append(self.ordenar_cartas(m))
                cont += 3
                continue
            elif len(mao[m]) == par:
                cont += 2
                continue
        if cont >= 5:
            return tmp[0][0]
        else:
            return 0

    @classmethod
    def isFlush(self, var, *args, **kwargs):
        ''' Verifica se é Flush e retorna a maior carta da sequência caso seja verdadeiro, ou 0 caso não seja.'''
        mesmo_naipe = 5
        var = self.naipe_carta(var)
        s = var.get('s')
        h = var.get('h')
        d = var.get('d')
        c = var.get('c')
        cont = prox = nao_sequencia = 1
        maior_carta = 0
        if len(s) >= mesmo_naipe:
            linha = self.ordenar_cartas(s)
            menor_carta = linha[0]
            maior_carta = linha[len(linha)-1]
            while cont < len(linha):
                if menor_carta+prox != linha[cont]:
                    nao_sequencia += 1
                    menor_carta = linha[cont]
                else:
                    sequencia = 1
                    menor_carta = linha[cont]
                cont += 1
        if len(h) >= mesmo_naipe:
            linha = self.ordenar_cartas(h)
            menor_carta = linha[0]
            maior_carta = linha[len(linha)-1]
            while cont < len(linha):
                if menor_carta+prox != linha[cont]:
                    nao_sequencia += 1
                    menor_carta = linha[cont]
                else:
                    sequencia = 1
                    menor_carta = linha[cont]
                cont += 1
        if len(d) >= mesmo_naipe:
            linha = self.ordenar_cartas(d)
            menor_carta = linha[0]
            maior_carta = linha[len(linha)-1]
            while cont < len(linha):
                if menor_carta+prox != linha[cont]:
                    nao_sequencia += 1
                    menor_carta = linha[cont]
                else:
                    sequencia = 1
                    menor_carta = linha[cont]
                cont += 1
        if len(c) >= mesmo_naipe:
            linha = self.ordenar_cartas(c)
            menor_carta = linha[0]
            maior_carta = linha[len(linha)-1]
            while cont < len(linha):
                if menor_carta+prox != linha[cont]:
                    nao_sequencia += 1
                    menor_carta = linha[cont]
                else:
                    sequencia = 1
                    menor_carta = linha[cont]
                cont += 1
        if nao_sequencia == 5:
            return maior_carta
        else:
            return 0

    @classmethod
    def isStraight(self, var, *args, **kwargs):
        ''' Verifica se é Straight e retorna a maior carta da sequência caso seja verdadeiro, ou 0 caso não seja.'''
        cartas = 5
        var = var.split()
        cont = prox = sequencia = 1
        if len(var) >= cartas:
            linha = self.ordenar_cartas(var)
            menor_carta = linha[0]
            while cont < len(linha):
                if menor_carta+prox == linha[cont] or menor_carta == linha[cont]:
                    sequencia += 1
                    menor_carta = linha[cont]
                    maior_carta_sequencia = linha[cont]
                else:
                    if sequencia >= cartas:
                        pass
                    else:
                        sequencia = 1
                        menor_carta = linha[cont]
                cont += 1
        if sequencia >= cartas:
            return maior_carta_sequencia
        else:
            return 0

    @classmethod
    def isThreeOfKind(self, var, *args, **kwargs):
        ''' Verifica se é Three of a Kind e retorna o valor da maior trinca. Caso contrário retorna 0.'''
        trinca = 3
        mao = self.agrupa_carta(var)
        cont = 0
        tmp = {}
        for m in mao:
            if len(mao[m]) == trinca:
                tmp[trinca]=m
                cont += 3
        maior_trinca = 0
        for t in tmp:
            if t > maior_trinca:
                maior_trinca = tmp[t][0]
        if cont >= trinca:
            return int(maior_trinca)
        else:
            return 0

    @classmethod
    def isTwoPairs(self, var, *args, **kwargs):
        ''' Verifica se é Two Pairs e retorna uma lista com os pares. Caso contrário retorna 0.'''
        par = 2
        mao = self.agrupa_carta(var)
        cont = 0
        tmp = []
        for m in mao:
            if len(mao[m]) == par:
                tmp.append(mao[m][0])
                cont += 2
        if cont >= 4:
            tmp = self.ordenar_cartas(tmp)
            return tmp[len(tmp)-1]
        else:
            return 0

    @classmethod
    def isOnePair(self, var, *args, **kwargs):
        ''' Verifica se é One Pair e retorna o maior par. Caso contrário retorna 0.'''
        par = 2
        mao = self.agrupa_carta(var)
        cont = 0
        tmp = []
        for m in mao:
            if len(mao[m]) == par:
                tmp.append(mao[m][0])
                cont += 2
        if cont == par:
            tmp = self.ordenar_cartas(tmp)
            return tmp[0]
        else:
            return 0

    @classmethod
    def whatIsHighCard(self, var, *args, **kwargs):
        ''' Verifica qual é a HighCard e retorna a maior.'''
        mao = self.ordenar_cartas(var)
        return mao[len(mao)-1]

