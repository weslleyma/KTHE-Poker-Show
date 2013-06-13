#coding:utf-8
# Testes automatizados para a classe Baralho.
# Autor: Weslley Martins Araujo
# E-mail: weslleyaraujo@inf.ufg.br
# Blog: weslleyaraujo.com


import unittest

class BaralhoTest(unittest.TestCase):
    from baralho import Baralho, Carta
    baralho = Baralho()

    def testBaralho(self):
        self.assertEquals(len(self.baralho), 52)
        self.assertEquals(len(self.baralho.cartas), 52)
        print self.baralho.cartas

teste = unittest.TestLoader().loadTestsFromTestCase(BaralhoTest)
unittest.TextTestRunner(verbosity=2).run(teste)
