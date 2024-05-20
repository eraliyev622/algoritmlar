class Hisob:
    def __init__(self,balans):
        self .__balans=balans
    def balansni_ol(self):
        return self.__balans 
    def deposit(self,miqdor):
        self .miqdor=miqdor
        if self.miqdor>0:
            return self.miqdor+self.__balans
        else:
            return("siz musbat son kiritishingiz kere")
    def yechb_ol(self ,miqdor):
            self .miqdor=miqdor
            if self.miqdor>0:
              if self.miqdor<=self.__balans:
                  self.__balans-=miqdor   
# Obyekt yaratish
hisob = Hisob(1000)
print("Dastlabki balans:", hisob.balansni_ol())

# Depozit qilish
hisob.deposit(500)
print("Depozitdan so'nggi balans:", hisob.balansni_ol())

# Yechib olish
hisob.yechb_ol(300)
print("Yechib olingandan so'nggi balans:", hisob.balansni_ol())

# Yechib olish (yetarli mablag' yo'q)
hisob.yechb_ol(1500)
print("Yechib olish urinishidan so'nggi balans:", hisob.balansni_ol())


