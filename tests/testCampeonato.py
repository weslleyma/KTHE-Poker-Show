#coding:utf-8
# Testes automatizados para a classe PokerChampionship.
# Autor: Weslley Martins Araujo
# E-mail: weslleyaraujo@inf.ufg.br
# Blog: weslleyaraujo.com


import unittest

class PokerChampionshipTest(unittest.TestCase):
    from campeonatoPoker import PokerChampionship
    campeonato = PokerChampionship()

    def test_runCampeonato(self):
        self.campeonato.inicializaMao()
        self.campeonato.setMao('Kc 9s Ks Kd 9d 3c 6d')
        self.campeonato.setMao('9c Ah Ks Kd 9d 3c 6d')
        self.campeonato.setMao('Ac Qc Ks Kd 9d 3c')
        self.campeonato.setMao('9h 5s')
        self.campeonato.setMao('4d 2d Ks Kd 9d 3c 6d')
        self.campeonato.setMao('7s Ts Ks Kd 9d')
        self.campeonato.incrementaRodada()
        self.campeonato.avaliarMao()
        self.campeonato.setCampeonato()
        self.campeonato.imprimeCampeonato()
        ### rodada 2
        self.campeonato.inicializaMao()
        self.campeonato.setMao('Th 2d 4h Kd 9d 3c 6d')
        self.campeonato.setMao('Ah 2d Kh Kd 9d 3c 6d')
        self.campeonato.setMao('Jh 2d 7h Kd 9d 3c 6d')
        self.campeonato.setMao('Kh 2d 9h Kd 9d 3c 6d')
        self.campeonato.setMao('5h 2d 2h Kd 9d 3c 6d')
        self.campeonato.setMao('Qh 2d 3h Kd 9d 3c 6d')
        self.campeonato.incrementaRodada()
        self.campeonato.avaliarMao()
        self.campeonato.setCampeonato()
        self.campeonato.imprimeCampeonato()

suite3 = unittest.TestLoader().loadTestsFromTestCase(PokerChampionshipTest)
unittest.TextTestRunner(verbosity=2).run(suite3)