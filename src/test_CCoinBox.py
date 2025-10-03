import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def test_pass(self):
        pass

    def setUp(self):
        coinBox = CCoinBox()

    def test_monnaie(self):
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        self.assertEqual(coinBox.get_vente_permise(), True)

    def test_retourne_monnaie(self):
        coinBox.ajouter_25c()
        piece = coinBox.retourne_monnaie()
        self.assertEqual(coinBox.get_vente_permise(), False)
        self.assertEqual(piece, 1)

    def test_permet_une_double_vente(self):
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.vente()
        self.assertEqual(coinBox.get_vente_permise(), True)

    def test_monnaie_mutant(self):
        coinBox.ajouter_25c()
           self.assertFalse(coinBox.get_vente_permise())
