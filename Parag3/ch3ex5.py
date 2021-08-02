#SciPyの使い方
from scipy import integrate

#積分関数
def func(x):
    y = 4.0/(1+x*x)
    return y

#積分範囲[0,1]
result, err = integrate.quad(func,0,1)
print("積分結果=", result)
print("誤差=", err)
