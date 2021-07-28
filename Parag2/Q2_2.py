print("試験の点数を打ち込んでください")
p = int(input())
if 90<=p<=100:
    print("S")
elif 80<=p<90:
    print("A")
elif 70<=p<80:
    print("B")
elif 60<=p<70:
    print("C")
elif 0<=p<60:
    print("D")
else:
    print("0~100の値で打ち込んでください")