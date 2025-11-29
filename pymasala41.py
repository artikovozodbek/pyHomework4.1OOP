class student:

    def __init__(self, i, f, y, b):
        self.ism = i
        self.familiya = f
        self.yonalish = y
        self.bosqich = b

    def check_exam(self, ball):
        if ball >= 70:
            self.bosqich += 1
            print("Siz imtihondan o'ttingiz, Bosqich 1 balga oshirildi")
            print(f"Ism-Familiya: {self.ism} {self.familiya}, Yo'nalish:{self.yonalish} Bosqich: {self.bosqich}.")
        else:
            print("Imtihondan o'tmadingiz ")


student1 = student("Bekzod", " Baratov", "IT", 3)

student1.check_exam(90)