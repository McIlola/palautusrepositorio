from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._kumoa_olio = Kumoa(sovelluslogiikka)
        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka),
            Komento.EROTUS: Erotus(sovelluslogiikka),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka),
            Komento.KUMOA: self._kumoa_olio
        }

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)
    
    def _lue_syote(self):
        try:
            return int(self._syote_kentta.get())
        except ValueError:
            return 0
    
    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita(self._lue_syote())
        if komento != Komento.KUMOA:
            self._kumoa_olio.aseta_edellinen_komento(komento_olio)

        self._kumoa_painike["state"] = constants.NORMAL if self._kumoa_olio._edellinen_komento else constants.DISABLED

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())

class Summa:
    def __init__(self, logiikka):
        self._logiikka = logiikka
        self._edellinen_arvo = 0

    def suorita(self, arvo):
        self._edellinen_arvo = self._logiikka.arvo()
        self._logiikka.plus(arvo)

    def kumoa(self):
        self._logiikka.aseta_arvo(self._edellinen_arvo)

class Erotus:
    def __init__(self, logiikka):
        self._logiikka = logiikka
        self._edellinen_arvo = 0

    def suorita(self, arvo):
        self._edellinen_arvo = self._logiikka.arvo()
        self._logiikka.miinus(arvo)

    def kumoa(self):
        self._logiikka.aseta_arvo(self._edellinen_arvo)

class Nollaus:
    def __init__(self, logiikka):
        self._logiikka = logiikka
        self._edellinen_arvo = 0

    def suorita(self, arvo=None):
        self._edellinen_arvo = self._logiikka.arvo()
        self._logiikka.nollaa()

    def kumoa(self):
        self._logiikka.aseta_arvo(self._edellinen_arvo)

class Kumoa:
    def __init__(self, logiikka):
        self._logiikka = logiikka
        self._edellinen_komento = None
    
    def aseta_edellinen_komento(self, komento):
        self._edellinen_komento = komento
    
    def suorita(self, arvo=None):
        if self._edellinen_komento:
            self._edellinen_komento.kumoa()
            self._edellinen_komento = None