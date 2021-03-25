# import os
# import random


# #ZAD1
# with open("Zadanie1.txt", "w") as funkcja:
#     for i in range(10):
#         funkcja.write(str(random.randint(0, 30) * 2))
#         funkcja.write('\n')



# #ZAD2
# with open("Zadanie1.txt", 'r') as funkcja:
#     print(funkcja.read())



#ZAD3

# with open("pliktekstowy.txt", "w+") as funkcja:
#     funkcja.write("Dzisiaj będzie\n bardzo ładna\n pogoda")
#     funkcja.seek(0)
#     for line in funkcja:
#         print(line)


#ZAD4
# class NaZakupy:
#
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = int(ilosc)
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = float(cena_jed)
#
#
#     def wyswietl_produkt(self):
#         print("Nazwa:", self.nazwa_produktu, sep=' ')
#         print("Ilosc:", self.ilosc, sep=' ')
#         print("Miara:", self.jednostka_miary, sep=' ')
#         print("Koszt za", self.jednostka_miary, "=", self.cena_jed, sep=' ')
#
#     def ile_produktu(self):
#
#             print("Całkowita ilość produktu wynosi", self.ilosc, self.jednostka_miary, sep=' ')
#
#
#     def ile_kosztuje(self, wybrana_ilosc):
#         print(wybrana_ilosc, self.jednostka_miary, "kosztuje", self.cena_jed * wybrana_ilosc, sep=' ')
#
# produkt = NaZakupy("Sok", 2, "szt", 2.99)
#
# produkt.wyswietl_produkt()
#
# produkt.ile_produktu()
#
# produkt.ile_kosztuje(3)