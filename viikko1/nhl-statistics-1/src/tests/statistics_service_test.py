import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_alussa_oikeat_pelaajat(self):
        odotetut = ["Semenko", "Lemieux", "Kurri", "Yzerman", "Gretzky"]
        saadut = [pelaaja.name for pelaaja in self.stats._players]
        self.assertAlmostEqual(saadut, odotetut)
    
    def test_haku_toimii(self):
        pelaaja = self.stats.search("Kurri")
        self.assertEqual(pelaaja.name, "Kurri")
        self.assertEqual(pelaaja.team, "EDM")
        self.assertEqual(pelaaja.goals, 37)
        self.assertEqual(pelaaja.assists, 53)
    
    def test_haku_jos_pelaajaa_ei_ole(self):
        pelaaja = self.stats.search("Pelaaja1")
        self.assertIsNone(pelaaja)
    
    def test_joukkuehaku(self):
        joukkue = self.stats.team("EDM")
        odotetut = ["Semenko", "Kurri", "Gretzky"]
        saadut = [pelaaja.name for pelaaja in joukkue]
        self.assertListEqual(saadut, odotetut)
    
    def test_parhaat_pelaajat(self):
        pelaajat = self.stats.top(2)
        odotetut = ["Gretzky", "Lemieux", "Yzerman"]
        saadut = [pelaaja.name for pelaaja in pelaajat]
        self.assertListEqual(saadut, odotetut)
    
    def test_parhaat_pelaajat_piste(self):
        pelaajat = self.stats.top(2, SortBy.POINTS)
        odotetut = ["Gretzky", "Lemieux", "Yzerman"]
        saadut = [pelaaja.name for pelaaja in pelaajat]
        self.assertListEqual(saadut, odotetut)
    
    def test_parhaat_pelaajat_maali(self):
        pelaajat = self.stats.top(2, SortBy.GOALS)
        odotetut = ["Lemieux", "Yzerman", "Kurri"]
        saadut = [pelaaja.name for pelaaja in pelaajat]
        self.assertListEqual(saadut, odotetut)
    
    def test_parhaat_pelaajat_syotto(self):
        pelaajat = self.stats.top(2, SortBy.ASSISTS)
        odotetut = ["Gretzky", "Yzerman", "Lemieux"]
        saadut = [pelaaja.name for pelaaja in pelaajat]
        self.assertListEqual(saadut, odotetut)

    


                            
    