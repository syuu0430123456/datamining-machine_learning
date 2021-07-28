#九九を表示
for i in range(1,10):
    for j in range(1,i+1):
        print("%1dx%1d=%2d " % (i, j, i*j), end = "")
    print()