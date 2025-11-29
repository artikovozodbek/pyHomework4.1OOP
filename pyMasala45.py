import math

class Uchburchak:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a + self.b + self.c

    def maydon(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

triangle = Uchburchak(3, 4, 5)
print("Perimetr:", triangle.perimetr())
print("Maydon:", triangle.maydon())

    
    

    
        






#     5-masala. Uchburchak Classi
# Uchburchak classi yarating. Uch tomon: a, b, c.

# perimetr() metod â€“ perimetrni qaytaradi.

# maydon() metod â€“ Heron formulasidan foydalanib maydon hisoblaydi.
# Uchburchak classidan obyekt yarating va uning perimetri va maydonini hisoblang.