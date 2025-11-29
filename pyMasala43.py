class avtomobil:

    def __init__(self, m , y, t):
        self.model = m
        self.yil = y
        self.tezlik = t
        

    def tezlashtir(self):
        self.tezlik += 10
        print("Tezlik +10 ga oshirildi")
        print(self.tezlik)

    def sekinlashtir(self):
         self.tezlik -= 10
         print("Tezlik -10 ga kamaytirildi")
         print(self.tezlik)

    def info(self):
        print(f"Avtomobil modeli: {self.model}. Yili: {self.yil}. Tezligi: {self.tezlik}")


avtomobil2 = avtomobil("Mers", 2027, 250)


avtomobil2.tezlashtir()
avtomobil2.tezlashtir()
avtomobil2.tezlashtir()
avtomobil2.sekinlashtir()
avtomobil2.info()



# 3-masala. Avtomobil
# Avtomobil classi tuzing. Atributlari: model, yil, tezlik.

# tezlashtir() â€“ tezlikni +10 oshiradi.

# sekinlashtir() â€“ tezlikni -10 kamaytiradi.

# info() â€“ avtomobil model, yil va tezligini chiqaradi.
# Avtomobilni 3 marta tezlashtiring, keyin 1 marta sekinlashtiring.