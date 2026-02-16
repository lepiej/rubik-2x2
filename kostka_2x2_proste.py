#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
KOSTKA RUBIKA 2x2

WYMAGANIA:
1. Zapamiętanie stanu ścianek - każda ściana to tablica 2x2 z literami kolorów
2. Wyświetlanie - widok pseudo-3D i siatka rozłożona
3. Wszystkie 12 ruchów - U/U', D/D', R/R', L/L', F/F', B/B'
4. Rotacja całej kostki - x, y, z (obrócenie wokół osi)
5. Mieszanie - losowe ruchy
"""

import random

class Kostka:
    def __init__(self):
        # WYMAGANIE 1: Zapamiętanie stanu ścianek kostki
        # Każda ściana to tablica 2x2 z literami reprezentującymi kolory
        # B=Biały, Z=Żółty, P=Pomarańczowy, C=Czerwony, ZI=Zielony, N=Niebieski
        self.gora = [["B", "B"], ["B", "B"]]
        self.dol = [["Z", "Z"], ["Z", "Z"]]
        self.lewa = [["P", "P"], ["P", "P"]]
        self.prawa = [["C", "C"], ["C", "C"]]
        self.przod = [["ZI", "ZI"], ["ZI", "ZI"]]
        self.tyl = [["N", "N"], ["N", "N"]]
    
    def obrot_90(self, sciana):
        """Obraca ścianę o 90 stopni"""
        s = [wiersz[:] for wiersz in sciana]
        sciana[0][0] = s[1][0]
        sciana[0][1] = s[0][0]
        sciana[1][1] = s[0][1]
        sciana[1][0] = s[1][1]
    
    def ruch_U(self):
        self.obrot_90(self.gora)
        t = [self.przod[0][0], self.przod[0][1]]
        self.przod[0] = [self.prawa[0][0], self.prawa[0][1]]
        self.prawa[0] = [self.tyl[0][0], self.tyl[0][1]]
        self.tyl[0] = [self.lewa[0][0], self.lewa[0][1]]
        self.lewa[0] = t
    
    def ruch_D(self):
        self.obrot_90(self.dol)
        t = [self.przod[1][0], self.przod[1][1]]
        self.przod[1] = [self.lewa[1][0], self.lewa[1][1]]
        self.lewa[1] = [self.tyl[1][0], self.tyl[1][1]]
        self.tyl[1] = [self.prawa[1][0], self.prawa[1][1]]
        self.prawa[1] = t
    
    def ruch_R(self):
        self.obrot_90(self.prawa)
        t = [self.przod[0][1], self.przod[1][1]]
        self.przod[0][1] = self.dol[0][1]
        self.przod[1][1] = self.dol[1][1]
        self.dol[0][1] = self.tyl[1][0]
        self.dol[1][1] = self.tyl[0][0]
        self.tyl[1][0] = self.gora[0][1]
        self.tyl[0][0] = self.gora[1][1]
        self.gora[0][1] = t[0]
        self.gora[1][1] = t[1]
    
    def ruch_L(self):
        self.obrot_90(self.lewa)
        t = [self.przod[0][0], self.przod[1][0]]
        self.przod[0][0] = self.gora[0][0]
        self.przod[1][0] = self.gora[1][0]
        self.gora[0][0] = self.tyl[1][1]
        self.gora[1][0] = self.tyl[0][1]
        self.tyl[0][1] = self.dol[1][0]
        self.tyl[1][1] = self.dol[0][0]
        self.dol[0][0] = t[0]
        self.dol[1][0] = t[1]
    
    def ruch_F(self):
        self.obrot_90(self.przod)
        t = [self.gora[1][0], self.gora[1][1]]
        self.gora[1][0] = self.lewa[1][1]
        self.gora[1][1] = self.lewa[0][1]
        self.lewa[0][1] = self.dol[0][0]
        self.lewa[1][1] = self.dol[0][1]
        self.dol[0][0] = self.prawa[1][0]
        self.dol[0][1] = self.prawa[0][0]
        self.prawa[0][0] = t[0]
        self.prawa[1][0] = t[1]
    
    def ruch_B(self):
        self.obrot_90(self.tyl)
        t = [self.gora[0][0], self.gora[0][1]]
        self.gora[0][0] = self.prawa[0][1]
        self.gora[0][1] = self.prawa[1][1]
        self.prawa[0][1] = self.dol[1][1]
        self.prawa[1][1] = self.dol[1][0]
        self.dol[1][1] = self.lewa[1][0]
        self.dol[1][0] = self.lewa[0][0]
        self.lewa[0][0] = t[0]
        self.lewa[1][0] = t[1]
    
    def ruch_x(self):
        # WYMAGANIE 4: Rotacja całej kostki wokół osi R-L (obrót X)
        # Obrót całej kostki tak, jakbyśmy obracali prawą ścianę
        self.ruch_R()
        self.przod, self.gora, self.tyl, self.dol = self.dol, self.przod, self.gora, self.tyl
    
    def ruch_y(self):
        # WYMAGANIE 4: Rotacja całej kostki wokół osi U-D (obrót Y)
        # Obrót całej kostki jak górna ściana
        self.ruch_U()
        self.przod, self.lewa, self.tyl, self.prawa = self.prawa, self.przod, self.lewa, self.tyl
    
    def ruch_z(self):
        # WYMAGANIE 4: Rotacja całej kostki wokół osi F-B (obrót Z)
        # Obrót całej kostki jak przednia ściana
        self.ruch_F()
        self.gora, self.prawa, self.dol, self.lewa = self.lewa, self.gora, self.prawa, self.dol
    
    def wykonaj(self, ruch):
        # WYMAGANIE 3: Obsługa wszystkich 12 ruchów + rotacje całej kostki
        ruchy = {
            # Ruchy jednoteczne (6 w prawo, 6 w lewo)
            "U": self.ruch_U, "U'": lambda: [self.ruch_U() for _ in range(3)],
            "D": self.ruch_D, "D'": lambda: [self.ruch_D() for _ in range(3)],
            "R": self.ruch_R, "R'": lambda: [self.ruch_R() for _ in range(3)],
            "L": self.ruch_L, "L'": lambda: [self.ruch_L() for _ in range(3)],
            "F": self.ruch_F, "F'": lambda: [self.ruch_F() for _ in range(3)],
            "B": self.ruch_B, "B'": lambda: [self.ruch_B() for _ in range(3)],
            # Rotacje całej kostki
            "x": self.ruch_x, "x'": lambda: [self.ruch_x() for _ in range(3)],
            "y": self.ruch_y, "y'": lambda: [self.ruch_y() for _ in range(3)],
            "z": self.ruch_z, "z'": lambda: [self.ruch_z() for _ in range(3)],
        }
        if ruch in ruchy:
            ruchy[ruch]()
    
    def siatka(self):
        # WYMAGANIE 2: Wyświetlanie kostki jako siatka rozłożona
        print()
        print(f"     {self.gora[0][0]} {self.gora[0][1]}")
        print(f"     {self.gora[1][0]} {self.gora[1][1]}")
        print()
        for i in range(2):
            print(f"{self.lewa[i][0]} {self.lewa[i][1]} {self.przod[i][0]} {self.przod[i][1]} {self.prawa[i][0]} {self.prawa[i][1]} {self.tyl[i][0]} {self.tyl[i][1]}")
        print()
        print(f"     {self.dol[0][0]} {self.dol[0][1]}")
        print(f"     {self.dol[1][0]} {self.dol[1][1]}")
        print()
    
    def wyswietl(self):
        # WYMAGANIE 2: Wyświetlanie kostki w widoku pseudo-3D
        print()
        print(f"      {self.gora[0][0]} {self.gora[0][1]}")
        print(f"      {self.gora[1][0]} {self.gora[1][1]}")
        print()
        for i in range(2):
            print(f"  {self.lewa[i][0]} {self.lewa[i][1]}  {self.przod[i][0]} {self.przod[i][1]}  {self.prawa[i][0]} {self.prawa[i][1]}")
        print()
        print(f"      {self.dol[0][0]} {self.dol[0][1]}")
        print(f"      {self.dol[1][0]} {self.dol[1][1]}")
        print()
    
    def mieszaj(self, ile=20):
        # WYMAGANIE 5: Funkcja mieszająca wykonująca losowe ruchy
        ruchy = ["U", "U'", "D", "D'", "R", "R'", "L", "L'", "F", "F'", "B", "B'"]
        for _ in range(ile):
            self.wykonaj(random.choice(ruchy))


# PROGRAM
if __name__ == "__main__":
    kostka = Kostka()
    
    while True:
        kostka.wyswietl()
        print("Ruchy: U D R L F B (dodaj ' dla lewego obrotu)")
        print("Rotacje: x y z (obrót całej kostki)")
        print("S - siatka | M - mieszaj | C - reset | Q - wyjście")
        
        cmd = input("> ").strip().upper()
        
        # Obsługa ruchów (12 ruchów + rotacje całej kostki)
        if cmd in ["U", "U'", "D", "D'", "R", "R'", "L", "L'", "F", "F'", "B", "B'",
                   "X", "X'", "Y", "Y'", "Z", "Z'"]:
            kostka.wykonaj(cmd.lower())
        elif cmd == "S":
            kostka.siatka()
        elif cmd == "M":
            kostka.mieszaj()
            print("Kostka pomieszana!")
        elif cmd == "C":
            kostka = Kostka()
            print("Reset!")
        elif cmd == "Q":
            break
        else:
            print("Nieznane polecenie!")
