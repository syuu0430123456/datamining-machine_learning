#modulenの利用
import ch3ex3module

seito1 = ch3ex3module.student("yamada",34 ,56, 87,45)
seito1.showdata()
seito1.showave()
n,k1,k2,k3,k4 = seito1.getdata()
ch3ex3module.gouhi(n,k1,k2,k3,k4)
seito2 = ch3ex3module.student("takeda",54 ,98,82,92)
seito2.showdata()
seito2.showave()
n,k1,k2,k3,k4 = seito2.getdata()
ch3ex3module.gouhi(n,k1,k2,k3,k4)