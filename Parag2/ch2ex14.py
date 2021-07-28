f = open("scoredata.txt", "r", encoding="utf-8")
lines = f.readlines()
s = 0
for line in lines:
    p = int(line.strip())
    print(p)
    s += p
l = len(lines)
print("人数 = ",l)
print(s/l)
f.close()

f.close()