class Bank_hisobi:

    def __init__(self, i, b = 0):
        self.ism = i
        self.balans = b

    def deposit(self, qosh):
        self.balans += qosh
        print(f"Blans {qosh} ga oshirildi")
        print(f"Balans = {self.balans}")

    def yechib_ol(self, yech):
        if self.balans >= yech:
            self.balans -= yech
            print(f"Blansdan {yech} yechib olindi")
            print(f"Balans = {self.balans}")
        else:
            print("Hisobda yeterli mablag' yo'q. Iltimos hisobingizni toldiring")

    def hisob(self):
        return f"{self.ism} ning hozirgi balansi = {self.balans}"
    
bank = Bank_hisobi("Nozima", 1000)

bank.deposit(1000)
bank.yechib_ol(400)
print(bank.hisob())

    
        





# 4-masala. Bank Hisobi
# BankHisob classi yarating. Atributlari: ism, balans=0.

# deposit(summa) â€“ balansni oshiradi.

# yechib_ol(summa) â€“ balansni kamaytiradi (agar yetarli bo'lsa).

# hisob() â€“ hozirgi balansni qaytaradi.
# Hisob oching, unga 1000 qo'shing, 400 yeching.
# ===============================================