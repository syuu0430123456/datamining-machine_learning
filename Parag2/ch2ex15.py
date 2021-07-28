#ファイルへ入力
f = open("newdata.txt","w",encoding="utf-8")
a = [45,67,34,87,56,78,91,45,64,86,90,73]
for i in a:
    print("点数 = ", i)
    f.write("点数 =" + str(i) + "\n")
f.close()