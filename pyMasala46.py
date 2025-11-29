class Kurs:

    def __init__(self, n, d):
        self.nomi = n
        self.davomiyligi = d
        self.talabalar = []


    def talaba_qoshish(self, ism):
        self.talabalar.append(ism)
        print(f"{ism} qoshildi")


    def talaba_soni(self):
        return self.talabalar
    

kurs = Kurs("Foundation", 4)

kurs.talaba_qoshish("bekzod")
kurs.talaba_qoshish("kamron")
kurs.talaba_qoshish("samandar")

print("talabalar:", kurs.talaba_soni())
        
# 6-masala. O'quv Markazi
# Kurs classi yarating. Atributlari: nomi, davomiylik, talabalar=[]. talabar kurs classsninyaratong atrubbut

# talaba_qoshish(ism) â€“ talaba qo'shadi. talaba_qishishs classni qaytaring talaba qoshadi

# talabalar_soni() â€“ nechta talaba borligini qaytaradi.
# Kurs obyektini yarating, 3 ta talaba qo'shing va umumiy sonini chiqaring.