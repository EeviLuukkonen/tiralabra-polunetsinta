import unittest
from dead_end_filling import DeadEndFilling
from labyrintti import Labyrintti

lab =  [['.', '.', '#', '#'],
        ['#', '.', '.', '#'],
        ['#', '#', '.', '.'],
        ['#', '#', '#', '.']]

lab2 = [[".",".",'.','.'],
        ['#','.','#','.'],
        ['.','.','.','#'],
        ['.','#','.','.']]

class TestDeadEndFilling(unittest.TestCase):
    def setUp(self):
        self.def1 = DeadEndFilling(Labyrintti(lab, 4, 4, (0,0), (3,3)))
        self.def2 = DeadEndFilling(Labyrintti(lab2, 4, 4, (0,0), (3,2)))

    def test_polun_pituus_oikein(self):
        self.def1.dead_end_filling()
        path = self.def1.polku_labyrinttiin()

        self.assertEqual(path[0], 6)

    def test_ei_yhtaan_dead_endia(self):
        self.def1.dead_end_filling()
        path = self.def1.polku_labyrinttiin()

        self.assertEqual(path[0], 6)

    def test_algoritmi_tunnistaa_reunat_umpikujiksi(self):
        self.def2.dead_end_filling()

        self.assertEqual(self.def2.labyrintti.labyrintti[3][0], "#")
