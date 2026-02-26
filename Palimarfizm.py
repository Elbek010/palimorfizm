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
# class meva:
#     def __init__(self,nomi,hudud):
#         self.nomi = nomi
#         self.hudud = hudud
#     def color(self):
#         return f"Meva turi va {self.hudud} qarab o'zgaradi" 
# class olma(meva):
#     def __init__(self, nomi, hudud):
#         super().__init__(nomi, hudud)
#     def color(self):
#         return f"{self.nomi} rangi sarg'ish , o'sadigan hudud {self.hudud}"  
# class banan(meva):
#     def __init__(self, nomi, hudud):
#         super().__init__(nomi, hudud)
#     def color(self):
#         return f"{self.nomi} rangi sariq , o'sadigan hudud {self.hudud}"
# olma1 = olma("Karvak olma,", "Kravak")
# print(olma1.color())
# banan1 = banan("Osiyo banan","Afrika")
# print(banan1.color())




# 4-misol
# class hodim :
#     def init(self , nomi , ish_haqqi):
#         self.nomi = nomi
#         self.ish_haqqi = ish_haqqi
#     def info(self):
#         print(f"Hodim : {self.nomi} , Ishaqqi : {self.ish_haqqi}")
# class direktor(hodim):
#     def init(self , nomi , ish_haqqi , ):
#         super().init(nomi , ish_haqqi)
#     def info(self):
#         print(f"lavozimi : {self.nomi} , Ishaqqi : {self.ish_haqqi}")
# class oqituvchi(hodim):
#     def info(self):
#         print(f"lavozimi : {self.nomi} , Ishaqqi : {self.ish_haqqi}")
# hodimlar = [direktor("Direktor : Alisher" , 10000000) , oqituvchi("O'qituvchi : Anvar" , 5000000)]
# for hodim in hodimlar :
#     hodim.info()
# 5-misol
# class qurilma :
#     def init(self , nomi , ishlab_chiqaruvchi):
#         self.nomi = nomi
#         self.ishlab_chiqaruvchi = ishlab_chiqaruvchi
#     def info(self):
#         print(f"Qurilma : {self.nomi} , Ishlab chiqaruvchi : {self.ishlab_chiqaruvchi}")
# class telefon(qurilma):
#     def info(self):
#         print(f"Qurilma : {self.nomi} , Ishlab chiqaruvchi : {self.ishlab_chiqaruvchi}")
# class kampyuter(qurilma):
#     def info(self):
#         print(f"Qurilma : {self.nomi} , Ishlab chiqaruvchi : {self.ishlab_chiqaruvchi}")
# qurilmalar = [telefon("Telefon : Iphone" , "Apple") , kampyuter("Kampyuter : Macbook" , "Apple")]
# for qurilma in qurilmalar :
#     qurilma.info()
# 6-misol
# class hayvon :
#     def init(self , nomi , harakat):
#         self.nomi = nomi
#         self.harakat = harakat
#     def info(self):
#         print(f"nomi : {self.nomi} , Harakati : {self.harakat}")
# class qush(hayvon):
#     def info(self):
#         print(f"nomi : {self.nomi} , Harakati : {self.harakat}")
# class baliq(hayvon):
#     def info(self):
#         print(f"nomi : {self.nomi} , Harakati : {self.harakat}")
# hayvonlar = [qush("Qush : Qalampir" , "Uchadi") , baliq("Baliq : Karp" , "Suzadi")]
# for hayvon in hayvonlar :
#     hayvon.info()
# 7-misol
# class auto :
#     def init(self , nomi , tezlik , narxi):
#         self.nomi = nomi
#         self.tezlik = tezlik
#         self.narxi = narxi
#     def info(self):
#         print(f"Avto : {self.nomi} , Tezlik : {self.tezlik} , Narxi : {self.narxi}")
# class malibu(auto):
#     def info(self):
#         print(f"Nomi: {self.nomi} , Tezlik : {self.tezlik} , Narxi : {self.narxi}")
# class nexia(auto):
#     def info(self):
#         print(f"Nomi: {self.nomi} , Tezlik : {self.tezlik} , Narxi : {self.narxi}")
# class cobalt(auto):
#     def info(self):
#         print(f"Nomi: {self.nomi} , Tezlik : {self.tezlik} , Narxi : {self.narxi}")
# avtomobil = [malibu("Malibu" , 220, 1000000) , nexia("Nexia" , 180, 800000) , cobalt("Cobalt" , 190, 900000)]
# for avtomobil in avtomobil :
#     avtomobil.info()
# 8-misol
# class asbob :
#     def init(self , nomi , vazifasi , ovoz):
#         self.nomi = nomi
#         self.vazifasi = vazifasi
#         self.ovoz = ovoz
#     def info(self):
#         print(f"Asbob : {self.nomi} , Vazifasi : {self.vazifasi} , Ovozi : {self.ovoz}")
# class gitara(asbob):
#     def info(self):
#         print(f"Asbob : {self.nomi} , Vazifasi : {self.vazifasi} , Ovozi : {self.ovoz}")    
# class baraban(asbob):
#     def info(self):
#         print(f"Asbob : {self.nomi} , Vazifasi : {self.vazifasi} , Ovozi : {self.ovoz}")
# asboblar = [gitara("Gitara" , "Musiqa asbobi" , "Dun Dun") , baraban("Baraban" , "Musiqa asbobi" , "Dum Dum")]
# for asbob in asboblar : 
#     asbob.info()
# 9-misol
# class oyinchi :
#     def init(self , nomi , sport_turi):
#         self.nomi = nomi
#         self.sport_turi = sport_turi
#     def info(self):
#         print(f"Oyinchi : {self.nomi} , Sport turi : {self.sport_turi}")
# class futbolchi(oyinchi):
#     def info(self):
#         print(f"Oyinchi : {self.nomi} , Sport turi : {self.sport_turi}")
# class basketbolchi(oyinchi):
#     def info(self):
#         print(f"Oyinchi : {self.nomi} , Sport turi : {self.sport_turi}")

# oyinchilar = [futbolchi("Futbolchi : Lionel Messi" , "Futbol") , basketbolchi("Basketbolchi : LeBron James" , "Basketbol")]
# for oyinchi in oyinchilar :
#     oyinchi.info()
# 10-misol
# class raqam :
#     def init(self , qiymat , aniqlik):
#         self.qiymat = qiymat
#         self.aniqlik = aniqlik
#     def info(self):
#         print(f"Raqam : {self.qiymat} , Aniqlik : {self.aniqlik}")
# class juft_son(raqam):
#     def info(self):
#         print(f"Juft son : {self.qiymat} , Aniqlik : {self.aniqlik}")
# class toq_son(raqam):
#     def info(self):
#         print(f"Toq son : {self.qiymat} , Aniqlik : {self.aniqlik}")
# raqamlar = [juft_son(2 , "Juft son") , toq_son(3 , "Toq son")]
# for raqam in raqamlar :
#     raqam.info()
# 11-misol
# class taom :
#     def init(self , nomi , kaloriyasi , tami):
#         self.nomi = nomi
#         self.kaloriyasi = kaloriyasi
#         self.tami = tami
#     def info(self):
#         print(f"Taom : {self.nomi} , Kaloriyasi : {self.kaloriyasi} , Tami : {self.tami}")
# class osh(taom):
#     def info(self):
#         print(f"Taom : {self.nomi} , Kaloriyasi : {self.kaloriyasi} , Tami : {self.tami}")   
# class lagmon(taom):
#     def info(self):
#         print(f"Taom : {self.nomi} , Kaloriyasi : {self.kaloriyasi} , Tami : {self.tami}")
# taomlar = [osh("Osh" , 500 , "Yaxshi") , lagmon("Lag'mon" , 400 , "Zo'r")]
# for taom in taomlar :     
#     taom.info()
# 12-misol
# class qush :
#     def init(self , nomi , harakati , uchish_usuli):
#         self.nomi = nomi
#         self.harakati = harakati
#         self.uchish_usuli = uchish_usuli            
#     def info(self):
#         print(f"Qush : {self.nomi} , Harakati : {self.harakati}")
# class burgut(qush):
#     def info(self):
#         print(f"Qush : {self.nomi}\n, Harakati : {self.harakati}\n, Uchish usuli : {self.uchish_usuli}\n")
# class qaldirgoch(qush):
#     def info(self):
#         print(f"Qush : {self.nomi}\n, Harakati : {self.harakati}\n, Uchish usuli : {self.uchish_usuli}\n")
# qushlar = [burgut("Burgut" , "Uchadi" , "Keng qanotlari bilan uchadi") , qaldirgoch("Qaldirgoch" , "Uchadi" , "Tez uchadi")]
# for qush in qushlar :
#     qush.info() 
# 13-misol
# class odam :
#     def init(self , yosh , ism  , manzil , vazifa):
#         self.yosh = yosh
#         self.ism = ism
#         self.manzil = manzil
#         self.vazifa = vazifa
#     def info(self):
#           print(f"Ismi : {self.ism} , Yoshi : {self.yosh} , Vazifasi : {self.vazifa}")
# class talaba(odam):
#     def info(self):
#         print(f"ismi : {self.ism}\n Yoshi : {self.yosh}\n Yashash manzili : {self.manzil}\n Vazifasi : {self.vazifa}")
# class ishchi(odam):
#     def info(self):
#         print(f"Ismi : {self.ism}\n Yoshi : {self.yosh}\n Yashash manzili : {self.manzil}\n Vazifasi : {self.vazifa}")
# malumot = [talaba("Sulaymon" , 16 , "KHOREZM" , "o'qish") , ishchi("Munisbek" , 16 , "Pitnak" , "ishlash")]
# for odam in malumot :
#     odam.info() 
# 15-misol
# class mashina :
#     def init(self , nomi , tezlik , narxi , yoqilgi_turi):
#         self.nomi = nomi
#         self.tezlik = tezlik
#         self.narxi = narxi
#         self.yoqilgi_turi = yoqilgi_turi
#     def info(self):
#         print(f"Avto : {self.nomi} , Tezlik : {self.tezlik} , Narxi : {self.narxi} , Yoqilgi turi : {self.yoqilgi_turi}")
# class BMW(mashina):
#     def info(self):
#         print(f"Avto : {self.nomi} , Tezlik : {self.tezlik} , Narxi : {self.narxi} , Yoqilgi turi : {self.yoqilgi_turi}")
# class tesla(mashina):
#     def info(self):
#         print(f"Avto : {self.nomi} , Tezlik : {self.tezlik} , Narxi : {self.narxi} , Yoqilgi turi : {self.yoqilgi_turi}")   
# auto = [BMW("BMW" , 250 , 5000000 , "Benzin") , tesla("Tesla" , 300 , 7000000 , "Elektr") ]
# for mashina in auto :
#     mashina.info()
# 16-misol
# class binolar:
#     def init(self , nomi , balandligi , qavat_soni , manzili , xonalar_soni):
#         self.nomi = nomi
#         self.balandligi = balandligi
#         self.qavat_soni = qavat_soni
#         self.manzili = manzili


#         self.xonalar_soni = xonalar_soni
#     def info(self):       
#         print(f"Binolar : {self.nomi} , Balandligi : {self.balandligi} , Qavat soni : {self.qavat_soni} , Manzili : {self.manzili} , Xonalar soni : {self.xonalar_soni}")
# class uy(binolar):
#     def info(self):
#         print(f"Binolar : {self.nomi}\n Balandligi : {self.balandligi}\n Qavat soni : {self.qavat_soni}\n Manzili : {self.manzili}\n Xonalar soni : {self.xonalar_soni}")   
# class maktab(binolar):
#     def info(self):
#         print(f"Binolar : {self.nomi}\n Balandligi : {self.balandligi}\n Qavat soni : {self.qavat_soni}\n Manzili : {self.manzili}\n Xonalar soni : {self.xonalar_soni}")   
# bino = [uy("Uy" , 10 , 2 , "Pitnak" , 5) , maktab("Maktab" , 15 , 3 , "Pitnak" , 20)]
# for binolar in bino :
#     binolar.info()
# 17-misol
# class yozuvchi :
#     def init(self , nomi , asarlari , tugilgan_yili , janri):
#         self.nomi = nomi
#         self.asarlari = asarlari
#         self.tugilgan_yili = tugilgan_yili
#         self.janri = janri
#     def info(self):
#         print(f"Yozuvchi : {self.nomi} , Asarlari : {self.asarlari} , Tugilgan yili : {self.tugilgan_yili} , Janri : {self.janri}")
# class shoyir(yozuvchi):
#     def info(self):
#         print(f"Yozuvchi : {self.nomi} , Asarlari : {self.asarlari} , Tugilgan yili : {self.tugilgan_yili} , Janri : {self.janri}")
# class nasriy_yozuvchi(yozuvchi):
#     def info(self):
#         print(f"Yozuvchi : {self.nomi} , Asarlari : {self.asarlari} , Tugilgan yili : {self.tugilgan_yili} , Janri : {self.janri}")
# yozuvchilar = [shoyir("Shoyir : Alisher Navoiy" , "Asarlar : Xamsa" , 1441 , "Janri : Shoyir") , nasriy_yozuvchi("Nasriy yozuvchi : Abdulla Qodiriy" , "Asarlar : O'tgan kunlar" , 1894 , "Janri : Nasriy yozuvchi")]
# for yozuvchi in yozuvchilar :     
#     yozuvchi.info()
# 18-misol
# class hayvon :
#     def init(self , nomi , harakati , yashash_muhiti , ovoz):
#         self.nomi = nomi
#         self.harakati = harakati
#         self.yashash_muhiti = yashash_muhiti
#         self.ovoz = ovoz
#     def info(self):
#         print(f"Hayvon : {self.nomi}\n Harakati : {self.harakati}\n Yashash muhiti : {self.yashash_muhiti}\n Ovozi : {self.ovoz}")
# class ot(hayvon):
#     def info(self):
#         print(f"Hayvon : {self.nomi}\n Harakati : {self.harakati}\n Yashash muhiti : {self.yashash_muhiti}\n Ovozi : {self.ovoz}")
# class sigir(hayvon):
#     def info(self):
#         print(f"Hayvon : {self.nomi}\n Harakati : {self.harakati}\n Yashash muhiti : {self.yashash_muhiti}\n Ovozi : {self.ovoz}")
# hayvonlar = [ot("Ot" , "Yuguradi" , "Ochiq maydon" , "Nya") , sigir("Sigir" , "Yuguradi" , "Ochiq maydon" , "Muu")]
# for hayvon in hayvonlar :
#     hayvon.info()
# 19-misol
# class transport :
#     def init(self , nomi , tezlik , narxi , turi , sigim):
#         self.nomi = nomi
#         self.tezlik = tezlik
#         self.narxi = narxi
#         self.turi = turi
#         self.sigim = sigim
#     def info(self):
#         print(f"Transport : {self.nomi}\n Tezlik : {self.tezlik}\n Narxi : {self.narxi}\n Turi : {self.turi}\n Sigim : {self.sigim}")
# class samolyot(transport):
#     def info(self):
#         print(f"Transport : {self.nomi}\n Tezlik : {self.tezlik}\n Narxi : {self.narxi}\n Turi : {self.turi}\n Sigim : {self.sigim}")
# class autobus(transport):
#     def info(self):
#         print(f"Transport : {self.nomi}\n Tezlik : {self.tezlik}\n Narxi : {self.narxi}\n Turi : {self.turi}\n Sigim : {self.sigim}")
# transportlar = [samolyot("Samolyot" , 900 , 1000000000 , "Havo transporti" , 300) , autobus("Avtobus" , 80 , 50000000 , "Yol transporti" , 50)]
# for transport in transportlar : 
#     transport.info()    
# 20-misol
# class kampaniya :
#     def init(self , nomi , sohasi , xodimlar_soni , daromadi , ish_turi):
#         self.nomi = nomi
#         self.sohasi = sohasi
#         self.xodimlar_soni = xodimlar_soni
#         self.daromadi = daromadi
#         self.ish_turi = ish_turi
#     def info(self):


#         print(f"Kampaniya : {self.nomi}\n Sohasi : {self.sohasi}\n Xodimlar soni : {self.xodimlar_soni}\n Daromadi : {self.daromadi}\n Ish turi : {self.ish_turi}")
# class IT_kampaniya(kampaniya):
#     def info(self):
#         print(f"Kampaniya : {self.nomi}\n Sohasi : {self.sohasi}\n Xodimlar soni : {self.xodimlar_soni}\n Daromadi : {self.daromadi}\n Ish turi : {self.ish_turi}")
# class qurilish_kampaniya(kampaniya):
#     def info(self):
#         print(f"Kampaniya : {self.nomi}\n Sohasi : {self.sohasi}\n Xodimlar soni : {self.xodimlar_soni}\n Daromadi : {self.daromadi}\n Ish turi : {self.ish_turi}")
# kampaniyalar = [IT_kampaniya("IT kampaniya : Google" , "IT" , 100000 , 1000000000 , "Dasturlash") , qurilish_kampaniya("Qurilish kampaniya : Arxitektura" , "Qurilish" , 50000 , 500000000 , "Qurilish")]
# for kampaniya in kampaniyalar :
#     kampaniya.info()
# 21-misol
class oquvchi :
    def init(self , fan_nomi):
        self.fan = fan_nomi
    def info(self):
        print(f"fan nomi : {self.fan}")       
class matematika(oquvchi):
    def init(self, fan_nomi):
        super().init(fan_nomi)
    def info(self):
        print(f"Fan nomi : {self.fan}")
class ingilistili(oquvchi):
    def info(self):
        print(f"Fan nomi : {self.fan}")
fan = [oquvchi("Geografiya") , matematika("matematika") , ingilistili("Ingilis tili")]
for oquvchi in fan :
    oquvchi.info()


        
    

