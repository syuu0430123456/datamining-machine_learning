def gouhi(namae, kokugo, sansu, rika, syakai):
    print(namae, ":", end="")
    if kokugo>60:
        print("国語合格, ", end="")
    else:
        print("国語不合格, ", end="")
    if sansu>60:
        print("算数合格, ", end="")
    else:
        print("算数不合格, ", end="")
    if rika>60:
        print("理科合格, ", end="")
    else:
        print("理科不合格, ", end="")
    if syakai>60:
        print("社会合格, ", end="")
    else:
        print("社会不合格, ", end="")
    return

#クラスの定義
class student:
    def __init__(self,namae,kokugo,sansu,rika,syakai):
        self.namae = namae
        self.kokugo = kokugo
        self.sansu = sansu
        self.rika = rika
        self.syakai = syakai
    
    def showdata(self):
        print(self.namae, self.kokugo, self.sansu, self.rika, self.syakai)
        return

    def showave(self):
        ave = (self.kokugo + self.sansu + self.rika + self.syakai)/4.0
        print(self.namae, "ave=", ave)
        return
    def getdata(self):
        return self.namae, self.kokugo, self.sansu, self.rika, self.syakai

seito1 = student("yamada",34 ,56, 87,45)
seito1.showdata()
seito1.showave()
n,k1,k2,k3,k4 = seito1.getdata()
gouhi(n,k1,k2,k3,k4)
seito2 = student("takeda",54 , 98, 82, 92)
seito2.showdata()
seito2.showave()
n,k1,k2,k3,k4 = seito2.getdata()
gouhi(n,k1,k2,k3,k4)