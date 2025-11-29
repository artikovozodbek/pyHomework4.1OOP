class kitob:

    def __init__(self, n, m, s):
        self.nomi = n
        self.muallif = m
        self.sahifa_soni = s

    def qisqacha(self):
         return f"Kitob haqida malumotlar: Kitob nomi: {self.nomi}. Muallifi:{self.muallif}. {self.sahifa_soni} ta sahifa dan iborat."
        
    def katta_kitobmi(self):
        if self.sahifa_soni > 300:
            return True
        else:
            return False

kitob1 = kitob("The subtle art of not giving a fuck", " MARK MANSON", 200)

print(kitob1.qisqacha())
print(kitob1.katta_kitobmi())

# -masala. Kitob Classi
# Kitob classi bo'lsin. Atributlari: nomi, muallif, sahifa_soni.

# qisqacha() metodi kitob haqida qisqa malumot qaytarsin.

# katta_kitobmi() metodi sahifa soni 300 dan ko'p bo'lsa True, bo'lmasa False qaytarsin.
# ======================================================================================