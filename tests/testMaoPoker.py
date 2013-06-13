#coding:utf-8
# Testes automatizados para a classe MaoPoker.
# Autor: Weslley Martins Araujo
# E-mail: weslleyaraujo@inf.ufg.br
# Blog: weslleyaraujo.com


import unittest

class MaoPokerTest(unittest.TestCase):
    from maoPoker import MaoPoker
    m = MaoPoker()

    def test_setMao(self):
        self.assertEquals(self.m.setMao('Kc 9s Ks Kd 9d 3c 6d'), True)
        self.assertEquals(self.m.setMao('Kc 9s'), True)
        self.assertEquals(self.m.setMao('Kc 9s Ks Kd 6d 3c 6d'), False)
        self.assertEquals(self.m.setMao('9c 9s Kd 6d 3c 6d'), False)

    def test_MaoPoker(self):
        self.m.inicializaMao()
        self.m.setMao('Kc 9s Ks Kd 9d 3c 6d')
        self.m.setMao('9c Ah Ks Kd 9d 3c 6d')
        self.m.setMao('Ac Qc Ks Kd 9d 3c')
        self.m.setMao('9h 5s')
        self.m.setMao('4d 2d Ks Kd 9d 3c 6d')
        self.m.setMao('7s Ts Ks Kd 9d')
        self.m.avaliarMao()

suite2 = unittest.TestLoader().loadTestsFromTestCase(MaoPokerTest)
unittest.TextTestRunner(verbosity=2).run(suite2)