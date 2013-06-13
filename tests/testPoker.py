#coding:utf-8
# Testes automatizados para a classe Poker.
# Autor: Weslley Martins Araujo
# E-mail: weslleyaraujo@inf.ufg.br
# Blog: weslleyaraujo.com


import unittest

class PokerTest(unittest.TestCase):
    from poker import Poker
    p = Poker()

    def test_valor_cartas(self):
        self.assertEquals(self.p.valor_cartas('Kc 9s Ks Kd 9d 3c 6d'.split()), ['K', '9', 'K', 'K', '9', '3', '6'])

    def test_ordenar_cartas(self):
        self.assertEquals(self.p.ordenar_cartas('Kc 9s Ks Kd 9d 3c 6d'), [3, 6, 9, 9, 13, 13, 13])

    def test_naipe_carta(self):
        self.assertEquals(self.p.naipe_carta('Kc 9s Ks Kd 9d 3c 6d'), {'h': [], 's': ['9s', 'Ks'], 'c': ['Kc', '3c'], 'd': ['Kd', '9d', '6d']})

    def test_agrupa_carta(self):
        self.assertEquals(self.p.agrupa_carta('Kc 9s Ks Kd 9d 3c 6d'), {'9': ['9s', '9d'], 'K': ['Kc', 'Ks', 'Kd'], '3': ['3c'], '6': ['6d']})

    def test_isRoyalFlush(self):
        self.assertEquals(self.p.isRoyalFlush('Kc 9s Ks Kd 9d 3c 6d'), False)
        self.assertEquals(self.p.isRoyalFlush('Ks Ts Js As 9d 3c Qs'), True)
        self.assertEquals(self.p.isRoyalFlush('Kd Td Jd Ad Qd'), True)

    def test_isStraightFlush(self):
        self.assertEquals(self.p.isStraightFlush('Kc 9s Ks Kd 9d 3c 6d'), 0)
        self.assertEquals(self.p.isStraightFlush('7c Jc Tc 8c 9c 3c 6d'), 11)

    def test_isFourOfKind(self):
        self.assertEquals(self.p.isFourOfKind('Kc 9s Ks Kd 9d 3c 6d'), 0)
        self.assertEquals(self.p.isFourOfKind('Kc Ks Ks Kd 9d 3c Kh'), 13)

    def test_isFullHouse(self):
        self.assertEquals(self.p.isFullHouse('Kc 9s Ks Kd 9d 3c 6d'), 13)
        self.assertEquals(self.p.isFullHouse('Kc 9s Ks Kd 2d 3c 6d'), 0)

    def test_isFlush(self):
        self.assertEquals(self.p.isFlush('Kc 9s Ks Kd 9d 3c 6d'), 0)
        self.assertEquals(self.p.isFlush('2h 7h Jh Ah 4h 3c 5s'), 14)

    def test_isStraight(self):
        self.assertEquals(self.p.isStraight('Kc 9s Ks Kd 9d 3c 6d'), 0)
        self.assertEquals(self.p.isStraight('3c 5s 4d 6s 7h 3c 6d'), 7)

    def test_isThreeOfKind(self):
        self.assertEquals(self.p.isThreeOfKind('Jc 9s 2s Kd 9d 3c 6d'), 0)
        self.assertEquals(self.p.isThreeOfKind('8c 8s 8h Kd 9d 3c 6d'), 8)

    def test_isTwoPairs(self):
        self.assertEquals(self.p.isTwoPairs('Jc 9s 2s Kd 9d 3c 6d'), 0)
        self.assertEquals(self.p.isTwoPairs('Jc 9s Js Kd 9d 3c 3d'), 11)

    def test_isOnePair(self):
        self.assertEquals(self.p.isOnePair('Jc 7s 2s Kd 9d 3c 6d'), 0)
        self.assertEquals(self.p.isOnePair('7c 7s 2s Kd 9d Kc 6d'), 0)
        self.assertEquals(self.p.isOnePair('3c 7s 2s Kd 9d Kc 6d'), 13)

    def test_whatIsHighCard(self):
        self.assertEquals(self.p.whatIsHighCard('3c 7s 2s 4d 9d Kc 6d'), 13)
        self.assertEquals(self.p.whatIsHighCard('3c 7s 2s 4d 9d 5c 6d'), 9)
        self.assertEquals(self.p.whatIsHighCard('3c 5d'), 5)

suite = unittest.TestLoader().loadTestsFromTestCase(PokerTest)
unittest.TextTestRunner(verbosity=2).run(suite)
