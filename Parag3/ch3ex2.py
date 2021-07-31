#クラスの定義と利用

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

#インスタンス生成
seito1 = student("yamada",34 ,56, 87,45)
seito1.showdata()
seito1.showave()
seito2 = student("takeda",54 , 98, 82, 92)
seito2.showdata()
seito2.showave()