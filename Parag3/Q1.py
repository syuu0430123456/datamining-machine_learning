def check_grade(point,grade):
    s = "0~100の値で打ち込んでください"
    if 90<=p<=100:
        s = "S"
    elif 80<=p<90:
        s = "A"
    elif 70<=p<80:
        s = "B"
    elif 60<=p<70:
        s = "C"
    elif 0<=p<60:
        s = "D"

#関数呼び出し
print("試験の点数を打ち込んでください")
p = int(input())
chcek = check_grade(p)
print(check)
