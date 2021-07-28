#解けてない


f = open("mathscore.txt", "r", encoding="utf-8")
lines = f.readlines()
for line in lines:
    line = line.strip()
    line = line.strip(" ")
    print(line)
f.close