# class hayvon:
#     def __init__(self,ovoz):
#         self.ovoz = ovoz    
#     def ovoz(self):
#         return f"hayvon :"
# class mushuk(hayvon):
#     def __init__(self, ovoz):
#         super().__init__(ovoz)
#     def mushuk_ovoz(self):
#         return f"Mushuk ovozi: {self.ovoz}"
# class Kuchuk(hayvon):
#     def __init__(self, ovoz):
#         super().__init__(ovoz)
#     def Kuchuk_ovozi(self):
#         return f"Kuchuk ovozi: {self.ovoz}"
# mushuk1 = mushuk("miav")
# kuchuk1 = Kuchuk("vov")
# print(mushuk1.mushuk_ovoz())
# print(kuchuk1.Kuchuk_ovozi())

    
# 2-misol

# class transport:
#     def __init__(self,madel):
#         self.madel = madel

#     def tezlik(self):
#         return f"{self.madel} tezligi mator va inson kuchiga bog'liq"

# class avto(transport):
#     def __init__(self, madel,mator):
#         super().__init__(madel)
#         self.mator = mator

#     def tezlik(self):
#         return f"BU avtonabil mator kuchiga qarab tezlashadi, mator kuchi:{self.mator}"

# class velosiped(transport):
#     def __init__(self, madel,inson_kuchi):
#         super().__init__(madel)

#         self.kuch = inson_kuchi

#     def tezlik(self):
#         return f"Velosiped tezligi odam kuchiga qarab o'zgaradi, velosiped tezligi {self.kuch}ga teng"
    
# avto1 = avto("Audi s7","2.8 litr")
# print(avto1.tezlik())
# velo1 = velosiped("T1","Shvas negr")
# print(velo1.tezlik())
        
        
# 3-misol
class meva:
    def __init__(self,nomi,hudud):
        self.nomi = nomi
        self.hudud = hudud
    def color(self):
        return f"Meva turi va {self.hudud} qarab o'zgaradi" 
class olma(meva):
    def __init__(self, nomi, hudud):
        super().__init__(nomi, hudud)
    def color(self):
        return f"{self.nomi} rangi sarg'ish , o'sadigan hudud {self.hudud}"  
class banan(meva):
    def __init__(self, nomi, hudud):
        super().__init__(nomi, hudud)
    def color(self):
        return f"{self.nomi} rangi sariq , o'sadigan hudud {self.hudud}"
olma1 = olma("Karvak olma,", "Kravak")
print(olma1.color())
banan1 = banan("Osiyo banan","Afrika")
print(banan1.color())
