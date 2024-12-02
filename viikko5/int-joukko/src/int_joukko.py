KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti <= 0:
            raise ValueError("Väärä kapasiteetti")
        if not isinstance(kasvatuskoko, int) or kasvatuskoko <= 0:
            raise ValueError("Väärä kasvatuskoko")
        
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        if luku in self.ljono:
            return True
        return False

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.ljono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1
            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.ljono):
                taulukko_old = self.ljono
                self.kopioi_lista(self.ljono, taulukko_old)
                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.ljono)
            return True
        return False

    def poista(self, luku):
        for i in range(self.alkioiden_lkm):
            if luku == self.ljono[i]:
                self.ljono[i] = 0
                for j in range(i, self.alkioiden_lkm - 1):
                    self.ljono[j] = self.ljono[j + 1]
                self.alkioiden_lkm -= 1
                return True
        return False

    def kopioi_lista(self, lista1, lista2):
        for i in range(len(lista1)):
            lista2[i] = lista1[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        uus_lista = IntJoukko()

        for luku in a.to_int_list() + b.to_int_list():
            uus_lista.lisaa(luku)
        return uus_lista

    @staticmethod
    def leikkaus(a, b):
        uus_lista = IntJoukko()
       
        for luku in a.to_int_list():
            if luku in b.to_int_list():
                uus_lista.lisaa(luku)
        return uus_lista

    @staticmethod
    def erotus(a, b):
        uus_lista = IntJoukko()

        for luku in a.to_int_list():
            if luku not in b.to_int_list():
                uus_lista.lisaa(luku)
        return uus_lista

    def __str__(self):
        return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm])) + "}"
