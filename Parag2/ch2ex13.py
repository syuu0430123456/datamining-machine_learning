#実行するときC:\Users\shudai.t\Documents\04Python\datamining\datamining-machine_learning\Parag2の下で実行しないと
#エラーになる
f = open("textfile.txt", "r", encoding="utf-8")
lines = f.readlines()
print("まとめて表示する")
print(lines)
for line in lines:
    line = line.strip()
    print(line)
f.close()