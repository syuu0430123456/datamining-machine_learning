a = [45,67,34,87,56,78,91,45,64,86,90,73]
x = 0
for i in a:
    print(i)
for i in a:
    x += i
x = x/len(a)
print("ave=",x)