class Kitob:
    def __init__(self, n, m):
        self.nomi = n
        self.muallif = m


class Kutubxona:
    def __init__(self):
        self.kitoblar = []     

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)
        print(f"'{kitob.nomi}' kitobi qo'shildi.")

    def qidirish(self, nom):
        for k in self.kitoblar:
            if k.nomi == nom:
                return f"Topildi: {k.nomi} — {k.muallif}"
        return "Bunday kitob topilmadi."



k1 = Kitob("Alkimyogar", "Paulo Coelho")
k2 = Kitob("1984", "George Orwell")
k3 = Kitob("Sariq devni minib", "Xudoyberdi To'xtaboyev")

kutubxona = Kutubxona()

kutubxona.kitob_qoshish(k1)
kutubxona.kitob_qoshish(k2)
kutubxona.kitob_qoshish(k3)

print(kutubxona.qidirish("1984"))      
print(kutubxona.qidirish("Harry Potter")) 